#from cProfile import label
import numpy as np
import feature_extraction
import pickle
import os
import pandas as pd
from sklearn import svm
import numpy as np
from sklearn.model_selection import train_test_split

#print(pd.__version__)
with open('./data.pickle','rb') as f:
    results = pickle.load(f)

labels = []
for result in results:
    #print(result.shape)
    num_res,_ = result.shape
    if num_res >6000:
        label = [0 for _ in range(num_res)]
    else:
        label = [1 for _ in range(num_res)]
    labels.extend(label)

labels = np.array(labels)



results_merged = results[0]
for i in range(1,len(results)):
    results_merged = pd.concat([results_merged,results[i]])
#print(results_merged)


results_merged.drop(['src_ip','dst_ip','src_port','dst_port','protocol','timestamp'],axis=1,inplace=True)
#print(results_merged)


results_np = results_merged.values
#print(results_np)


results_np_norm = results_np / (results_np.max(axis=0)+1e8) #无标签
#print(results_np_norm)

# svm
# prepare data
train_data,test_data,train_label,test_label=train_test_split(results_np_norm,labels,random_state=1,train_size=0.85,test_size=0.15)
# svm classifier
classifier = svm.SVC(C=0.5,kernel='rbf',gamma='auto',decision_function_shape='ovr')
classifier.fit(train_data,train_label.ravel())

#test results
print("train set:", classifier.score(train_data,train_label))
print("test set:", classifier.score(test_data,test_label))