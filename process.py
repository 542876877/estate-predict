from sklearn import linear_model
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

input_file = "res_utf8.csv"
df = pd.read_csv(input_file)
feature_cols = ['R1','R2','Area','Dir','Des','Ele','Tag1','Tag2','Tag3']
X = df[feature_cols]
y = df['Price']

testdata = {'R1' : [3],
	'R2' : [1],
	'Area' : [100],
	'Dir' : [5],
	'Des' : [0],
	'Ele' : [1],
	'Tag1' : [160],
	'Tag2' : [100],
	'Tag3' : [20]}
t = pd.DataFrame(testdata, columns=feature_cols)

# ---- use train_test_split ----
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
linreg = LinearRegression()
linreg.fit(X_train, y_train)
LinearRegression(copy_X = True, fit_intercept = True, normalize = True)
print (linreg.coef_)
print (linreg.predict(t))


# # ---- use cross_validation ----
from sklearn.cross_validation import cross_val_predict
lr = linear_model.LinearRegression()
# cross_val_predict returns an array of the same size as `y` where each entry
# is a prediction obtained by cross validated:
predicted = cross_val_predict(lr, X, y, cv=10)
# from sklearn.externals import joblib
# joblib.dump(lr,"./lr_machine.pkl")
# lr=joblib.load("./lr_machine.pkl")
# lr.fit(X, y)
# LinearRegression(copy_X = True, fit_intercept = True, normalize = True)
# print (lr.coef_)
# print (lr.predict(t))

plt.scatter(predicted,y,s=2)
plt.plot(y, y, 'ro')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=2)
plt.xlabel('Predicted')
plt.ylabel('Measured')
plt.show()
