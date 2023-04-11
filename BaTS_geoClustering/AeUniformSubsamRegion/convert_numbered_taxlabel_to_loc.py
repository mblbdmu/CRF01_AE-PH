#!/home/fgmp/miniconda3/bin/python3
'''Swap numbered taxonomic labels from tip names to location, to 
prepare PST treefile for BaTS.
'''

import pandas as pd

# Read numbered taxon labels and 'header_to_islandgrp_dedup_nonan.tsv'
# and 'header_to_region_dedup_nonan.tsv' references.
labels_to_swap = pd.read_csv("numbered_tax_labels_to_swap.tsv", sep="\t", names=["numbers","labels"])
island_data = pd.read_csv("ph_only_monoclade.fixnam.loc_island.tsv", sep="\t", header=0)
region_data = pd.read_csv("ph_only_monoclade.fixnam.loc_region.tsv", sep="\t", header=0)

# Swap each of the 222 labels to location, while keeping numbering.
merged_labels_with_locs = labels_to_swap.merge(island_data, how="left", left_on="labels", right_on="New FASTA header")
merged_labels_with_locs = merged_labels_with_locs.merge(region_data, how="left", left_on="labels", right_on="New FASTA header")
merged_labels_with_locs = merged_labels_with_locs.loc[:,["numbers","labels","island.group","region"]]
labels_to_islandgrp = merged_labels_with_locs.loc[:,["numbers","island.group"]]
labels_to_region = merged_labels_with_locs.loc[:,["numbers","region"]]

# Write to file
labels_to_islandgrp.to_csv("numbers_to_islandgrp.tsv", sep=" ", index=False, header=False)
labels_to_region.to_csv("numbers_to_region.tsv", sep=" ", index=False, header=False)
