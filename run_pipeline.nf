nextflow.enable.dsl=2

params.input_dir = "$baseDir/example/input/"
params.output_dir = "$baseDir/example/output/"
params.chain_file = "/Users/hannah/Documents/GitHub/snplifter/snplifter/data/chain_files/references_grch38_to_grch37.over.chain.gz"
params.liftover_direction = '38to37'
params.phenotype_names = 'LVM'

process runLiftover {
    script:
    """
    snplifter \
        --input_dir ${params.input_dir} \
        --output_dir ${params.output_dir} \
        --chain_file ${params.chain_file} \
        --liftover_direction ${params.liftover_direction} \
        --phenotype_names ${params.phenotype_names}
    """
}

workflow {
    runLiftover()
}
