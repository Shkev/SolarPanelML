from sklearn import tree
features = [[68,1], [66, 1], [61, 1], [61, 1], [61, 2], [61, 2], [64, 1], [64, 1], [64, 1], [66, 0], [61, 0], [64, 1], [66, 2], [72, 2], [73, 2], [70, 1], [57, 0], [61, 1], [59, 0], [63, 1], [60.8, 1], [76, 1]]
# 0 = cloudy/rainy, 1 = partly cloudy, 2 = sunny
labels = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1]
# 0 = under 35 kwh, 1 = over 35kwh
x = features
y = labels
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)
A = clf.predict([[64, 1]])
if A == 1:
	print('Over 35Kwh')
else:
	print('Under 35Kwh')
