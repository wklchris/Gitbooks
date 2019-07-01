import numpy as np
from sklearn import linear_model
from matplotlib import pyplot as plt

# Generating Dataset
b0, b1 = 3, 1
n = 50
x = np.linspace(0, 5, n).reshape(-1, 1)  # 1 column data
np.random.seed(123)
epsilon = np.random.normal(0, .5, n).reshape(-1, 1)
y = b0 + b1 * x + epsilon

# Regression
regr = linear_model.LinearRegression()
regr.fit(x, y)
yhat = regr.predict(x)

# Plotting
plt.plot(x, y, 'o', label='True data')
plt.plot(x, yhat, label='Fitted line')
plt.legend()
plt.title('LR model: $\hat{{y}}$ = {:.2f} + {:.2f}$x$'.format(regr.intercept_[0], regr.coef_[0][0]))
plt.show()
