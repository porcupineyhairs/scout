# clinvar Variant sheet
CLINVAR_HEADER = {
    "local_id": "##Local ID",
    "linking_id": "Linking ID",
    "gene_symbol": "Gene symbol",
    "ref_seq": "Reference sequence",
    "hgvs": "HGVS",
    "chromosome": "Chromosome",
    "start": "Start",
    "stop": "Stop",
    "ref": "Reference allele",
    "alt": "Alternate allele",
    "var_type": "Variant type",
    "ncopy": "Copy number",
    "ref_copy": "Reference copy number",
    "breakpoint1": "Breakpoint 1",
    "breakpoint2": "Breakpoint 2",
    "outer_start": "Outer start",
    "inner_start": "Inner start",
    "inner_stop": "Inner stop",
    "outer_stop": "Outer stop",
    "variations_ids": "Variation identifiers",
    "condition_id_type": "Condition ID type",  # default = 'HPO'
    "condition_id_value": "Condition ID value",
    "condition_comment": "Condition comment",
    "clinsig": "Clinical significance",
    "clinsig_comment": "Comment on clinical significance",
    "last_evaluated": "Date last evaluated",
    "variant_comment": "Comment on variant",
    "assertion_method": "Assertion method",
    "assertion_method_cit": "Assertion method citation",
    "inheritance_mode": "Mode of inheritance",
    "clinsig_cit": "Clinical significance citations",
    "clinsig_comment": "Comment on clinical significance",
    "drug_response": "Drug response condition",
    "funct_conseq": "Functional consequence",
    "funct_conseq_comment": "Comment on functional consequence",
}

# clinvar CaseData sheet
CASEDATA_HEADER = {
    "linking_id": "Linking ID",
    "individual_id": "Individual ID",
    "collection_method": "Collection method",  # default = 'clinical testing'
    "allele_origin": "Allele origin",
    "is_affected": "Affected status",
    "sv_analysis_method": "Structural variant method/analysis type",
    "clin_features": "Clinical features",
    "tissue": "Tissue",
    "sex": "Sex",
    "age": "Age",
    "ethnicity": "Population Group/Ethnicity",
    "fam_history": "Family history",
    "is_proband": "Proband",
    "is_secondary_finding": "Secondary finding",
    "is_mosaic": "Mosaicism",
    "zygosity": "Zygosity",
    "co_occurr_gene": "Co-occurrences, same gene",
    "co_occurr_other": "Co-occurrence, other genes",
    "platform_type": "Platform type",
    "platform_name": "Platform name",
    "method": "Method",
    "method_purpose": "Method purpose",
    "method_cit": "Method citations",
    "testing_lab": "Testing laboratory",
    "reported_at": "Date variant was reported to submitter",
}
# silence fields in ClinVar CSV output if other fields exist to avoid validation error - the latter are preferred
CLINVAR_SILENCE_IF_EXISTS = {"chromosome": "hgvs", "start": "hgvs", "stop": "hgvs"}

CLNSIG_TERMS = {
    "affects",
    "benign",
    "benign/likely_benign",
    "conflicting_interpretations_of_pathogenicity",
    "likely_benign",
    "likely_pathogenic",
    "pathogenic",
    "pathogenic/likely_pathogenic",
    "uncertain_significance",
    "affects",
    "association",
    "drug_response",
    "other",
    "protective",
    "risk_factor",
    "association",
    "association_not_found",
    "drug_response",
    "not_provided",
    "other",
    "protective",
    "risk_factor",
}

REVSTAT_TERMS = {
    "conflicting_interpretations",
    "multiple_submitters",
    "no_conflicts",
    "single_submitter",
    "criteria_provided",
    "no_assertion_criteria_provided",
    "no_assertion_provided",
    "practice_guideline",
    "reviewed_by_expert_panel",
}

# Models of inheritance are defined here:
# https://ftp.ncbi.nlm.nih.gov/pub/GTR/standard_terms/Mode_of_inheritance.txt
CLINVAR_INHERITANCE_MODELS = [
    "Autosomal dominant inheritance",
    "Autosomal dominant inheritance with maternal imprinting",
    "Autosomal dominant inheritance with paternal imprinting",
    "Autosomal recessive inheritance",
    "Autosomal unknown",
    "Codominant",
    "Genetic anticipation",
    "Mitochondrial inheritance",
    "Multifactorial inheritance",
    "Oligogenic inheritance",
    "Other",
    "Sex-limited autosomal dominant",
    "Somatic mutation",
    "Sporadic",
    "Unknown mechanism",
    "X-linked dominant inheritance",
    "X-linked inheritance",
    "X-linked recessive inheritance",
    "Y-linked inheritance",
]
