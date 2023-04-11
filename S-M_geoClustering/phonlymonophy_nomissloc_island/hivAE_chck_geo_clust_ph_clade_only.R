library(treeio)
library(ggimage)
library(ggtree)
library(slatkin.maddison)

# Set path. Import tree files & location data.
setwd("C:/Users/Guest1/fgmp_working_dir/projects/HIVcrf01ae_molclock_reruns/6.phonlymonocompleteloc_subsamalt_geoclustSM/phonlymonophy_nomissloc_island")
fast_tree_file <- "ph_only_monoclade.fixnam.fasttre.nexus"
fasttre <- read.nexus(fast_tree_file)
fasttre <- midpoint(fasttre)
geo_data <- read.delim("ph_only_monoclade.fixnam.loc.tsv")

# Visualize trees.
fasttre_geo <- ggtree(fasttre, right=FALSE) %<+% geo_data
fasttre_geo2 <- fasttre_geo + geom_tippoint(aes(color=island.group))

# Perform SM test on trees
run_sm(fasttre, geo_data, "island.group", rep=999)

# Renname tree tips with names with location.
# Dataframe for renaming must have replacements for at least all tips in tree.
new_tips <- read.delim("fasttre_alltips_replacements_regions.txt")
fasttre_newtips <- rename_taxa(fasttre, new_tips, New.FASTA.header, newheader)

# Export annotated tree object to tree file with location data.
write.tree(fasttre_newtips, "beastsubsam_region_tips_loc.nwk")
