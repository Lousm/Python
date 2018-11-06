from sklearn.datasets import load_boston
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# 加载数据
boston = load_boston()
###data 数据
###target  标签
# 特征名称 feature_names
# 描述信息DESCR

y = boston['target']
print(y)
names = boston['feature_names']
print(names)
X = boston['data']
print(X)

###导入到Excel
outputfile = r'boston.xlsx'
df = pd.DataFrame(X, index=range(len(y)), columns=names)
pf = pd.DataFrame(y, index=range(len(y)), columns=['outcome'])
pdf = df.join(pf, how='outer')
pdf.to_excel(outputfile)
