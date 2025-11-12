from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd

data = [['milk', 'bread'], ['milk', 'butter'], ['bread', 'butter']]
df = pd.DataFrame(TransactionEncoder().fit(data).transform(data), columns=['bread', 'butter', 'milk'])

f = apriori(df, min_support=0.5, use_colnames=True)
print(f)
