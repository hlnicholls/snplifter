import argparse
from snplifter.config_class import Config #Config placehodler incase of future methods additions
from snplifter.modules.liftover.liftover import LiftOver

def main():
    parser = argparse.ArgumentParser(description='SNPlifter: SNP liftover tool for converting SNP coordinates between genome builds.')
    parser.add_argument('--mode', type=str, required=True, choices=['snplifter'], help='Operation mode: snplifter')
    parser.add_argument('--input_dir', type=str, required=True, help='Directory containing input files')
    parser.add_argument('--output_dir', type=str, required=True, help='Directory where output files will be saved')
    parser.add_argument('--phenotype_names', type=str, help='Comma-separated list of phenotype names to process')
    parser.add_argument('--chain_file', type=str, required=True, help='Path to the chain file for liftover (required for liftover mode)')
    parser.add_argument('--liftover_direction', type=str, required=True, choices=['38to37', '37to38'], help='Direction of liftover (38to37 or 37to38)')

    args = parser.parse_args()

    if args.phenotype_names:
        phenotype_names = args.phenotype_names.split(',')
    else:
        phenotype_names = []

    if args.mode == 'snplift':
        liftover_processor = LiftOver(args.chain_file, args.input_dir, args.output_dir, args.liftover_direction, phenotype_names)
        liftover_processor.perform_liftover_for_phenotypes()
        print("Liftover Completed Successfully.")
    
    else:
        print('Only snplift mode is supported at the moment.')

if __name__ == "__main__":
    main()
