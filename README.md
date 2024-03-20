
# SNP liftover tool 
- Python tool for efficiently performing liftover of SNPs.
- Tested with python version 3.9

## Installation 

- Change to directory of repo
- Install via setup.py:

``` pip install -e .```


## Example run

- Only input requirement is that the phenotype name is the summary statistic filename prefix.

```
snplifter --input_dir ./example/input/ --output_dir ./example/output/ --chain_file ./data/references_grch38_to_grch37.over.chain.gz   --liftover_direction 38to37 --phenotype_names LVM
```


```
usage: snplifter [-h] --input_dir INPUT_DIR --output_dir OUTPUT_DIR --chain_file CHAIN_FILE --liftover_direction {38to37,37to38}
                 [--phenotype_names PHENOTYPE_NAMES]

SNPlifter: A tool for SNP liftover operations.

options:
  -h, --help            show this help message and exit
  --input_dir INPUT_DIR
                        Directory containing input data files for liftover.
  --output_dir OUTPUT_DIR
                        Directory where liftover output will be saved.
  --chain_file CHAIN_FILE
                        Path to the chain file for liftover.
  --liftover_direction {38to37,37to38}
                        Direction of liftover (38to37 or 37to38).
  --phenotype_names PHENOTYPE_NAMES
                        Comma-separated list of phenotype names to process.
```


### Running with Nextflow (as a test example only)

```
nextflow run run_pipeline.nf
```