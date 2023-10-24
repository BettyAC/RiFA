import pandas as pd

# Read data from the source CSV file
df_source = pd.read_csv('E:/sample_name.csv')

# Read data from the destination CSV file
df_destination = pd.read_csv('E:/alex_5genes_ann1.csv')

# Specify the search string and the target column to update
search_string = '#CHROM'
target_column = 'CHROM'
#matching_index=df.index[df['CHROM'].str.contains(search_string)].tolist()
# Iterate through the source column and update the destination column where there is a match
for value in enumerate(df_source['name']):
    m_idx=(df_destination['CHROM']==search_string).idxmax()
    if search_string in df_destination.at[m_idx,target_column]:
        df_destination.at[m_idx,target_column] = value

# Save the updated data to a new CSV file
df_destination.to_csv('E:/alex_5genes_ann_final5.csv', index=False)

#print(df_destination)
