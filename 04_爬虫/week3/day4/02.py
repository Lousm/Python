import pandas as pd

detail = pd.read_excel('meal_order_detail.xlsx')
a = list(detail.columns)
for i in a:
    print(detail[i].describe())
    if detail[i].describe().loc['count'] == 0:
        detail.drop(labels=i, axis=1, inplace=True)
    try:
        if detail[i].describe().loc['std'] == 0:
            detail.drop(labels=i, axis=1, inplace=True)
    except:
        print('std不存在')
print(detail.shape)
