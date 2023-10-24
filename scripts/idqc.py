import pandas as pd
import os
import re
import glob
import tabulate

### Check quality og sequence id (AMD_ID)

files = os.path.join("/mnt/data/bioinfoteam/Betty/malaria/tes_2021/mal_SRA_testdata","*.fastq")                                               # join the path of dir and extension of file
print(files)
my_file = [f for f in glob.glob(files)]                                                                      # use glob functio to list the files
            
clean_filenames = [doc_name.split("/")[-1].split("_")[0] for doc_name in my_file]                             
Sample_file = pd.DataFrame(clean_filenames, columns=["AMD_ID"])                                               # add column name to data frame called AMD_ID
Sample_file = Sample_file.drop_duplicates()                                                                   # drop duplicates from list
print(Sample_file)
## Creat a empty list for AMD_IDs 

Sample_no_match = []        # All the Ids with no match will be saved in list
Sample_with_match = []      # all the ID which has length  20 will be saved in list
 
## First part is to check if Sample ID has length 20 or not

Sample_name = Sample_file.rename(columns={'Sample':"Sample_ID", 'AMD_ID': "Sample_ID",'AMD ID (Pooled)': "Sample_ID", 'Document Name': "Sample_ID"})      # rename column name to Sample_ID as differant files migth have diffenrt column name.
  
SampleID_df = Sample_name[['Sample_ID']]                       # creat a dataframe using the column Sample_ID 

#remove US conrtols to avoid any errors in sample ID

SampleID_df = SampleID_df[SampleID_df['Sample_ID'].str.contains("USxxxx") == False]


for rows in SampleID_df.index:                                 # run a for loop on each rows
    
    sample_name =SampleID_df['Sample_ID'][rows].split('/n')    # split rows by newline
    for each_ID in sample_name:
        if len(each_ID) == 20 :                                # if length is 20, save the samples in Sample_with_match list
            Sample_with_match.append(each_ID) 
        else: 
            Sample_no_match.append(each_ID)                    # if length is not 20 then save the results in Sample_no_match list. 
            print(each_ID,"has length", int(len(each_ID)))     # print the sample ID with its length if less than 20


## 2nd part is to check all ID with length 20, if it matches with AMD ID information regular expression as shown in discription at begining.

for each_file  in Sample_with_match:                                     # Run a for loop for each file in Sample_with_match list
    
    AMD_ID =('([0-9]{2})([A-Zx]{2})([A-Za-z]{2})([0-9x]{2})([A-Zx]{1})([0-9]{3})(([0-9]{1})|([p]{1}))(([0-9]{2})|([Pf]{2}))([A-Zx]{1})([0-9x]{3})([0-9]{1})')
             
                                                                         # split AMD ID by its information using regular expression
   
    AMD_group = re.match(AMD_ID,each_file)                               # match each ID with pattern
    
    if AMD_group is None :                                               # if match does not found
            
        Sample_no_match.append(each_file)                                # append the ID to list
        print(each_file, "is not maching with ID")
        
    else:
       
        pass                                                             # if ID match with regex, pass
#print(Sample_with_match)


## lastly, print All the IDs without match so that user can review them and make a corrction before further processing.
print(len(Sample_no_match), "out of", len(SampleID_df),"samples did not match with AMD_ID")         # print the total number of samples that did not match 


if len(Sample_no_match) == 0:
        print("you are good to proceed with analysis: All the samples pass through QC test")
else :
    print("\nHere is the list of samples that did not match")
    
ID_No_match = "\n".join ([str(ID) for ID in Sample_no_match if len(Sample_no_match) != 0 ])         #  print the list of IDs that did not match 
print(ID_No_match)


# This part of code runs through the samples_no_match list and creats a table with key. Then user can identyfy where the key does not match visually from the table.

data_regex_QC = []                               

#Sample_no_match = ["17GNDo00F0001PfF1291", "17GNDo00F0001PfF129","17GNDo00F0001PfF12911",'17GNDo00F0001PfF1','17GNDo0F0001PfF1291', "NF54","NTC-DFR", "NTC-DHFR" ]

# Loop through the Sample id with no match list, split the ID by key using regex and creat dictionary .

for id in Sample_no_match:
    if len(id) >= 15:
        match = re.match(r"(?P<year>\w{2})(?P<country>\w{2})(?P<Site>\w{2})(?P<Treatment_Day>\w{2})(?P<Treatment>\w{1})(?P<ID>\w{4})(?P<Genus_Pooled>\w{,2})(?P<Type>\w{,1})(?P<GenemarkerCode>\w{,3})(?P<Repeat>\w{0,})", id)
        dic = match.groupdict()
        Dict_QC_re ={"name": id,"length_of_sample_ID" : len(id)}              # append the two keys to dict for Sample name and its length
        Dict_QC_re.update(dic)                                                # update a dict with new key value pair i.e name and length
        data_regex_QC.append(Dict_QC_re)     
    elif len(id) < 15:
        Dict_QC_re ={"name": id,"length_of_sample_ID" : len(id)}              # append the two keys to dict for Sample name and its length
        data_regex_QC.append(Dict_QC_re)     
                                   
        
if len(data_regex_QC) != 0:                                            # If length of list is not 0; 
    header = data_regex_QC[0].keys()                                   # header = keys of dict
    rows = [x.values() for x in data_regex_QC]                         # rows will be value of dict
    print (tabulate.tabulate(rows, header, tablefmt="grid"))           # use tabulate module to creat a table   

else:
    print('\n',"All the samples are matching with AMD_ID","\n", "No errors found in samples")        # If all the IDs matched with AMD id no table will be created. 
     
