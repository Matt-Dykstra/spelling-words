import pandas as pd
df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vS_DoOFxsg8AAC90Q2MmtownxaJIY110XjL1GuXRpxcdOIs202TApb8c2aOmnW_tRzahNozxTcAZbdL/pub?gid=1269470926&single=true&output=csv')
print(df['Words'].sample(n=15, axis=0))