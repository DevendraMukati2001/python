import pandas as pd
L={'h':'a','a':'h','d':'j'}
S=pd.DataFrame(L,index = [1,2,3,4,5,6])
print(S)

print(S[S['d']=='j'])