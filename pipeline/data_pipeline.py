import sys
import pandas as pd

month = sys.argv[1]

df = pd.DataFrame({'day': [1,2]})

df['month'] = month

df.to_parquet('/app/test/test.parquet')