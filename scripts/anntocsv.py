import csv
import sys

# Define the input SnpEff annotation file and the output CSV file
input_snpeff_file = sys.argv[1]
output_csv_file = sys.argv[2]

# Create a list to store extracted information
extracted_info = []

# Initialize variables to store sample name
sample_name = None

# Open the SnpEff annotation file for reading
with open(input_snpeff_file, 'r') as snpeff_file:
    for line in snpeff_file:
        if line.startswith("#CHROM"):
            # Extract the sample name from the header
            header_fields = line.strip().split('\t')
            sample_name = header_fields[9]  # Assuming the sample name is in the 10th column
        if line.startswith("#"):
            continue  # Skip comment lines

        # Split the line into fields
        fields = line.strip().split('\t')

        # Extract relevant fields
        chrom = fields[0]
        pos = fields[1]
        ref = fields[3]
        alt = fields[4]
        qual = fields[5]

        # Extract the INFO field
        info_field = fields[7]

        # Split the INFO field into key-value pairs
        info_pairs = info_field.split(';')

        # Initialize variables to store CDS.pos, AA.pos, and DP
        cds_pos = aa_pos = dp = "N/A"

        # Extract CDS.pos, AA.pos, and DP from the INFO field
        for info_pair in info_pairs:
            if info_pair.startswith("ANN="):
                # Assume ANN field contains multiple annotations separated by ","
                ann_parts = info_pair[4:].split(',')
                for part in ann_parts:
                    ann_info = part.split('|')
                    if len(ann_info) >= 11:
                        cds_pos = ann_info[9]
                        aa_pos = ann_info[10]
                        break  # Stop after the first valid annotation
            elif info_pair.startswith("DP="):
                dp = info_pair[3:]

        extracted_info.append((sample_name, chrom, pos, ref, alt, qual, dp, cds_pos, aa_pos))

# Write the extracted information to a CSV file
with open(output_csv_file, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Sample', 'CHROM', 'POS', 'REF', 'ALT', 'QUAL', 'DP', 'CDS.pos', 'AA.pos'])  # Write header
    csv_writer.writerows(extracted_info)

print(f"Extraction complete. The CSV file '{output_csv_file}' has been created.")
