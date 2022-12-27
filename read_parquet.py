import pandas as pd
data = pd.read_parquet('part-00000-e26211cd-dff6-4c8b-a134-d3c386ec37df-c000.snappy.parquet', engine='fastparquet')
print(data)