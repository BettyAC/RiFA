#!/usr/bin/env python

import argparse
import sys

#complement = {"A": "T", "T": "A", "G": "C", "C": "G","AT":"TA","TA":"AT", "TCA": "AGT", "TGA": "ACT","TCAG": "AGTC","CCT":"GGA","CGTCA":"GCAGT","CCTGCT":"GGACGA","TTGAAAGAAGCAA":"AACTTTCTTCGTT","TCATACGTCATA":"AGTATGCAGTAT","AGTTCCACCAATGT":"TCAAGGTGGTTACA", "TCATAC": "AGTATG", "TCTGGG":"AGACCC", "TCTGGGAAC":"AGACCCTTG", "TCAGATTCCC": "AGTCTAAGGG","TAAAAAAAAA": "ATTTTTTTTT", "TAAAAAAAAAA": "ATTTTTTTTTT", "TAAAAAAAAA": "ATTTTTTTTT", "CATAATAATAATAATAATAAT": "GTATTATTATTATTATTATTA","TTGCTGTTACCACCAGATTCCCG":"AACGACAATGGTGGTCTAAGGGC","CATAATAATAATAATAATAATAAT": "GTATTATTATTATTATTATTATTA","CATAATAATAATAATAATAATAATAAT":"GTATTATTATTATTATTATTATTATTA", "TTGCTGTTACCACCAGATTCCC":"AACGACAATGGTGGTCTAAGGG", "TTCCC":"AAGGG", "TG":"AC", "TGA":"ACT" , "TCATACGTCATAG":"AGTATGCAGTATC", "TCATACGTCATAGA":"AGTATGCAGTATCT", "ATTTTTTTTTTT":"TAAAAAAAAAAA", "ATTTTTTTTTT":"TAAAAAAAAAA", "ATTTTTTTTT":"TAAAAAAAAA","CTGGGAACTAAT":"GACCCTTGATTA", "TAAAAAAAAA,TAAAAAAAAAAA":"ATTTTTTTTT,ATTTTTTTTTTT","CATAATAATAATAATAATAATAAT,CATAATAATAATAATAAT":"GTATTATTATTATTATTATTATTA,GTATTATTATTATTATTA","TAAGAGACA":"ATTCTCTGT","TCC":"AGG","CC":"GG","TAAGATGG":"ATTCTACC","CCCAG":"GGGTC","CGGGAACTAATA":"GCCCTTGATTAT","TCATACGTCA":"AGTATGCAGT","TAAAGATG":"ATTTCTAC","TCCCTA":"AGGGAT","CATAATAATAATAAT":"GTATTATTATTATTA","TCATACGTCAGA":"AGTATGCAGTCT","CATAATAATAATAAT,CATAATAATAATAATAATAATAAT":"GTATTATTATTATTA,GTATTATTATTATTATTATTATTA","TTGCTGTTACCACCAGATTCCCGA":"AACGACAATGGTGGTCTAAGGGCT","CATAATAATAATAAT":"GTATTATTATTATTA","TCATACGTCATA,TTGCTGTTACCACCAGATTCCC":"AGTATGCAGTAT,AACGACAATGGTGGTCTAAGGG","CATACGT":"GTATGCA","TAGAGCC":"ATCTCGG","TCCACCAGA":"AGGTGGTCT","TGGG":"ACCC","CCAAGC":"GGTTCG","CGGACCAG":"GCCTGGTC","CCCAGCCAG":"GGGTCGGTC","CGTCA,CATACGT":"GCAGT,GTATGCA", "GGGCCCAT":"CCCGGGTA" }

def complement_sequence(sequence):
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
    complemented_sequence = ""
    for nucleotide in sequence:
        complemented_sequence += complement.get(nucleotide, nucleotide)

    return complemented_sequence

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_vcf", type=argparse.FileType())
    parser.add_argument("output_vcf", nargs='?', type=argparse.FileType("w"), default=sys.stdout)
    args = parser.parse_args()
    for line in args.input_vcf:
        if line.startswith("#"):
            print(line, end="", file=args.output_vcf)
        else:
            fields = line.rstrip().split("\t")
            pos = int(fields[1])
            if fields[0] == "13":
                # for K13
                fields[1] = str(1726998 - pos)
                fields[3] = complement_sequence(fields[3])
                fields[4] = complement_sequence(fields[4])
            elif fields[0] == "5":
                # for PfMDR1
                fields[1] = str(957889 + pos)
            elif fields[0] == "4":
                # for DHFR
                fields[1] = str(748087 + pos)
            elif fields[0] == "8":
                # for DHPS
                fields[1] = str(548199 + pos)
            elif fields[0] == "7":
                # for pfCRT
                fields[1] = str(403221 + pos)
            print("\t".join(fields), file=args.output_vcf)
