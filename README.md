# RiFA-Resistance in Falciparum Amplicon
RiFA, Resistance in Falciparum Amplicon, identifies mutations within the main drug resistance genes (crt, mdr1, k13, dhfr, dhps and cytob) and produces results in the form of structured summary
# Background
Malaria continues to be a huge public health challenge specially in low-income resource limited countries. The emergence and spread of drug resistant P. falciparum is creating an additional burden by reducing the efficacy of available anti-malarial drugs. Next generation sequencing is now becoming an important tool in Malaria drug resistance surveillance and efficacy studies and facilitates the detection of existing and emerging mutations associated with drug resistance. Once such approach is targeted amplicon sequencing which is now widely used to identify resistance conferring mutations for different genes. 

Though huge number of sequences has been generated from various surveillance and efficacy studies, there are challenges in the bioinformatics analysis to properly identify already known and especially novel mutation that may relate to drug resistance. To address this issue, we have developed a computational pipeline that can identify already known and other mutations that might have potential to be drug resistance markers from targeted amplicon sequences of P. falciparum.
# Pipeline Overview
The proposed pipeline was developed using the snake make workflow engine and is available on Conda package manger. It integrates various bioinformatics tools from quality checking to annotation of variants and statistical summaries and visualization of results.

![rifa](https://github.com/BettyAC/RiFA/assets/28188254/8e2632d1-fd3f-4304-ab8e-c95aa20ee655)

# Usage
1. Clone this Github repository to your local machine

```bash
git clone https://github.com/BettyAC/rifa.git
```
2. Example fastq files:
 #There are sample data in the example folder 
 #change directory into the repository folder, create a directory to save the fastq files
```bash
cd malpipeline/; sudo mkdir data/fastq; cd data/fastq/
```
 #Copy the example data or your fastq files to the fastq folder 
```bash
sudo cp data/example/* data/fastq
```
 #change back to main `malpipeline` directory
```bash
cd ../../
```
3. Create and activate conda environment
The conda package manager has to be installed then run the below to source all dependencies into a new environment:
```bash
conda env create -f envs/rifa.yml
conda activate rifa
```
4. Run the pipeline pipeline in Snakemake
```bash
snakemake
```
Running the pipeline on a SLURM cluster is under implementation
