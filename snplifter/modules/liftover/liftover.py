import os
import hail as hl
import argparse
import glob

class LiftOver:
    def __init__(self, chain_file, input_dir, output_dir, liftover_direction, phenotypes=None):
        self.chain_file = chain_file
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.liftover_direction = liftover_direction
        self.phenotypes = phenotypes if phenotypes is not None else []
        
        # Initialize Hail and add liftover chain
        self._init_hail()
        self._add_liftover_chain()

    def _init_hail(self):
        hl.stop()
        hl.init()

    def _add_liftover_chain(self):
        if self.liftover_direction == '38to37':
            rg_source = hl.get_reference("GRCh38")
            rg_target = hl.get_reference("GRCh37")
        else:
            rg_source = hl.get_reference("GRCh37")
            rg_target = hl.get_reference("GRCh38")
        
        rg_source.add_liftover(self.chain_file, rg_target)

    def _liftover_file(self, gwas_file, phenotype):
        ht = hl.import_table(gwas_file, impute=True)  # Using impute=True to guess the types of the fields

        # Standardize chromosome column name
        chrom_col = next((col for col in ht.row if col.lower() in ['chromosome', 'chr', 'chrom']), None)
        if chrom_col is not None:
            ht = ht.rename({chrom_col: 'CHROM'})
        
        # Standardize SNP column name
        snp_col = next((col for col in ht.row if col.lower() in ['snp', 'id', 'variant']), None)
        if snp_col is not None:
            ht = ht.rename({snp_col: 'SNP'})

        pos_col = next((col for col in ht.row if col.lower() in ['genpos', 'BP', 'pos', 'position']), None)
        if pos_col is not None:
            ht = ht.rename({pos_col: 'POS'})

        # Add 'chr' prefix if missing and standardize chromosome representation
        ht = ht.annotate(CHROM=hl.str(ht['CHROM']))
        ht = ht.annotate(CHROM=hl.if_else(hl.literal('chr').contains(ht['CHROM']), ht['CHROM'], hl.literal('chr') + ht['CHROM']))
        
        # Determine source and target genomes based on liftover direction
        source_genome = 'GRCh38' if self.liftover_direction == '38to37' else 'GRCh37'
        target_genome = 'GRCh37' if self.liftover_direction == '38to37' else 'GRCh38'
        
        # Annotate table with source and target loci for liftover
        print('Performing liftover...')
        ht = ht.annotate(locus_source=hl.parse_locus(ht['CHROM'] + ":" + hl.str(ht.POS), reference_genome=source_genome))
        ht = ht.annotate(locus_target=hl.liftover(ht.locus_source, target_genome, include_strand=False))
        
        # Remove 'chr' prefix for standardized CHROM value after liftover
        ht = ht.annotate(CHROM=ht['CHROM'].replace('chr',''))
        
        # Define the output file suffix based on the liftover direction
        suffix = '_38_37.txt' if self.liftover_direction == '38to37' else '_37_38.txt'
        output_file = os.path.join(self.output_dir, f'{phenotype}_GWAS{suffix}')
        ht.export(output_file, delimiter='\t')
    
    def perform_liftover_for_phenotypes(self):
        for phenotype in self.phenotypes:
            pattern = os.path.join(self.input_dir, f'{phenotype}*.txt')
            matching_files = glob.glob(pattern)
            for gwas_file in matching_files:
                self._liftover_file(gwas_file, phenotype)


def main():
    parser = argparse.ArgumentParser(description="Liftover Tool for GWAS Data")
    parser.add_argument('--input_dir', type=str, required=True, help='Directory containing input data files for liftover')
    parser.add_argument('--output_dir', type=str, required=True, help='Directory where liftover output will be saved')
    parser.add_argument('--chain_file', type=str, required=True, help='Path to the chain file for liftover')
    parser.add_argument('--liftover_direction', type=str, required=True, choices=['38to37', '37to38'], help='Direction of liftover (38to37 or 37to38)')
    parser.add_argument('--phenotype_names', type=str, help='Comma-separated list of phenotype names to process, if applicable')

    args = parser.parse_args()
    phenotype_names = args.phenotype_names.split(',') if args.phenotype_names else []

    liftover_processor = LiftOver(chain_file=args.chain_file, input_dir=args.input_dir, output_dir=args.output_dir, liftover_direction=args.liftover_direction, phenotypes=phenotype_names)
    liftover_processor.perform_liftover_for_phenotypes()

    print("Liftover Process Completed Successfully.")

if __name__ == '__main__':
    main()
