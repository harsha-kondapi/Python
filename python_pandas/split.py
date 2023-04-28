import pandas as pd

chunk_size = 500000
batch_no = 1

for chunk in pd.read_csv('~/Downloads/bfsdependencies.csv',chunksize=chunk_size):
    chunk.to_csv('bfsdependencies' + str(batch_no) + '.csv',index=False)
    batch_no +=1
    