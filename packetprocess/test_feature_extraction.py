import pickle
import os
#import Feature.feature_extraction
import feature_extraction
import pandas as pd
print(pd.__version__)

pcappath = 'APT'
results = []
for s in os.listdir(pcappath):
    s=os.path.join(pcappath,s)
    try:
        result = feature_extraction.feature_extraction(s)
    except Exception:
        continue
    results.append(result)
#print(result)
with open("./data.pickle","wb") as f:
    pickle.dump(results,f,pickle.HIGHEST_PROTOCOL)

with open('./data.pickle','rb') as f:
    data=pickle.load(f)
results = data

