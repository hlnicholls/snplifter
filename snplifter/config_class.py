import os

class Config:
    """
    Configuration class for SNP liftover.
    """
    def __init__(self, input_dir, output_dir, phenotype_names, chain_file, liftover_direction):
        """
        Initializes a new instance of the Config class.

        Parameters:
            input_dir (str): Path to the directory containing input files.
            output_dir (str): Path to the directory where output files should be saved.
            phenotype_names (list): A list of phenotype names to be processed.
            chain_file (str): Path to the chain file for liftover.
            liftover_direction (str): Direction of liftover ('38to37' or '37to38').
        """
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.phenotype_names = phenotype_names
        self.chain_file = chain_file
        self.liftover_direction = liftover_direction

        os.makedirs(self.output_dir, exist_ok=True)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='SNPlifter Configuration Test')
    parser.add_argument('--input_dir', type=str, required=True)
    parser.add_argument('--output_dir', type=str, required=True)
    parser.add_argument('--phenotype_names', type=str, required=False, default='')
    parser.add_argument('--chain_file', type=str, required=True)
    parser.add_argument('--liftover_direction', type=str, required=True, choices=['38to37', '37to38'])
    
    args = parser.parse_args()

    phenotype_names = args.phenotype_names.split(',') if args.phenotype_names else []
    cfg = Config(args.input_dir, args.output_dir, phenotype_names, args.chain_file, args.liftover_direction)

    print(f"Configuration loaded:\nInput Directory: {cfg.input_dir}\nOutput Directory: {cfg.output_dir}\nPhenotype Names: {cfg.phenotype_names}\nChain File: {cfg.chain_file}\nLiftover Direction: {cfg.liftover_direction}")
