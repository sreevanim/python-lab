from collections import Counter
data={'item1':45.50,'ittem2':35,'item3':41.30,'item4':55,'item5':24}
k=Counter(data)
p=k.most_common(3)
print("the top 3 items are:,p)
