import pkg_resources


###### Files ######

# Gene sources:
hgnc_file = 'resources/hgnc_complete_set.txt.gz'
exac_file = 'resources/forweb_cleaned_exac_r03_march16_z_data_pLI.txt.gz'
transcripts37_file = 'resources/ensembl_transcripts_37.txt.gz'

# OMIM resources:
mim_titles_file = 'resources/mimTitles.txt.gz'
mim2gene_file = 'resources/mim2gene.txt.gz'
genemap2_file = 'resources/genemap2.txt.gz'
morbidmap_file = 'resources/morbidmap.txt.gz'

# Hpo resources
hpogenes_file = 'resources/ALL_SOURCES_ALL_FREQUENCIES_genes_to_phenotype.txt.gz'
hpoterms_file = 'resources/ALL_SOURCES_ALL_FREQUENCIES_phenotype_to_genes.txt.gz'
hpodisease_file = 'resources/diseases_to_genes.txt.gz'

###### Paths ######

# Gene paths
hgnc_path = pkg_resources.resource_filename('scout', hgnc_file)
exac_path = pkg_resources.resource_filename('scout', exac_file)
transcripts37_path = pkg_resources.resource_filename('scout', transcripts37_file)

# OMIM paths
mimtitles_path = pkg_resources.resource_filename('scout', mim_titles_file)
mim2gene_path = pkg_resources.resource_filename('scout', mim2gene_file)
genemap2_path = pkg_resources.resource_filename('scout', genemap2_file)
morbidmap_path = pkg_resources.resource_filename('scout', morbidmap_file)

# Hpo paths
hpogenes_path = pkg_resources.resource_filename('scout', hpogenes_file)
hpoterms_path = pkg_resources.resource_filename('scout', hpoterms_file)
hpodisease_path = pkg_resources.resource_filename('scout', hpodisease_file)
