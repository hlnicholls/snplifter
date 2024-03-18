from snplifter.config_class import Config
from snplifter.modules.liftover.liftover import LiftOver
import argparse

def run_liftover():
    parser = argparse.ArgumentParser(description='SNPlifter: A tool for SNP liftover operations.')
    parser.add_argument('--input_dir', required=True, help='Directory containing input data files for liftover.')
    parser.add_argument('--output_dir', required=True, help='Directory where liftover output will be saved.')
    parser.add_argument('--chain_file', required=True, help='Path to the chain file for liftover.')
    parser.add_argument('--liftover_direction', required=True, choices=['38to37', '37to38'], help='Direction of liftover (38to37 or 37to38).')
    parser.add_argument('--phenotype_names', help='Comma-separated list of phenotype names to process. If not provided, all files in the input directory will be processed.')

    args = parser.parse_args()

    phenotype_names = args.phenotype_names.split(',') if args.phenotype_names else None

    config = Config(args.input_dir, args.output_dir, phenotype_names, args.chain_file, args.liftover_direction)

    liftover = LiftOver(config.chain_file, config.input_dir, config.output_dir, config.liftover_direction, config.phenotype_names)
    
    liftover.perform_liftover_for_phenotypes()

    print("Liftover operation completed successfully.")

if __name__ == '__main__':
    run_liftover()
