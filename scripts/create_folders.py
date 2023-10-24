import sys
import os

prefix =sys.argv[1]
for i in {bam,vcf,adjvcf,ann}:
	folder_name=f"/mnt/data/bioinfoteam/Betty/malpipeline/results/{prefix}_{i}"
	os.makedirs(folder_name, exist_ok=True)
