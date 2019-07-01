线性回归
==========

本章介绍线性回归的内容．

**线性回归（Linear regression）** 是最基础的机器学习模型．在机器学习中，一个含有 :math:`p` 个自变量的线性回归的真实模型可以用下式描述：

.. math::

   y = b_1 x_1 + b_2 x_2 + \cdots + b_p x_p + b_0 + \epsilon

其中，模型左侧的 :math:`y'` 表示待预测的标签，各 :math:`b_i` 表示特征 :math:`x_i` 的权重，而 :math:`b_0` 表示截距，最后误差项 :math:`\epsilon` 服从标准差为 0 的某个正态分布： :math:`\epsilon \sim N(0,\sigma)`．

拟合值记作 :math:`\hat{y}` ，即我们通过回归得到的模型是：

.. math::
   
   \hat{y} = \hat{b}_1 x_1 + \hat{b}_2 x_2 + \cdots + \hat{b}_p x_p + \hat{b}_0


简单线性回归
---------------

只有一个自变量 :math:`x` 的线性回归模型，我们称为 **简单线性回归（Simple linear regression）** 。

线性回归实质是一种简单的最优化求解，即求得线性系数 :math:`b_1` 与截距 :math:`b_0` 的估计，使得估计模型与数据集的差别最小。在一般情况下，这个“差别”是通过二次垂直距离定义的，也就是我们通称的最小二乘：

.. math::
   
   Q(b_0, b_1) &= \sum_{i=1}^n \left(y_i - (b_0 + b_1 x_i)\right)

   (\hat{b}_0, \hat{b}_1) &= \argmin_{b_0, b_1} Q(b_0, b_1)

其中，:math:`n` 是样本数据集的大小。从数学上由偏导数容易证明，函数 :math:`Q(b_0, b_1)` 总是在以下取值时达到最小值：

.. math::

   \hat{b}_1 = \frac{\sum_{i=1}^n (x_i-\bar{x})(y_i - \bar{y})}{\sum_{i=1}^n (x_i-\bar{x})^2}, \quad \hat{b}_0 = \bar{y} - \hat{b_1}\bar{x}

其中， :math:`\bar{x}=\frac{1}{n}\sum_{i=1}^n x_i` 与 :math:`\bar{y}=\frac{1}{n}\sum_{i=1}^n y_i` 分别是样本均值。

由此我们得到了线性回归模型，并可以通过该模型求得 **拟合值（Fitted values）** :math:`\hat{y}_i\ (i=1, 2, \ldots, n)`：

.. math::

   \hat{y_i} = \hat{b}_0 + \hat{b}_1 x_i

我们利用 Python 生成一个数据集，并实现一个简单线性回归：

.. literalinclude:: _static/simple_linear_regression.py
   :language: python

下图展示了该简单线性回归的结果：

.. plot:: _static/simple_linear_regression.py
   :align: center
   

残差
^^^^^^^^^^^

观测值 :math:`y_i` 与拟合值 :math:`\hat{y}_i` 之间的差值，称为 **残差（Residuals）** ，记作：

.. math::

   e_i = y_i - \hat{y}_i = (y_i - \bar{y}) - \hat{b}_1 (x_i - \bar{x})

残差 :math:`e_i` 实质上是真实误差项 :math:`\epsilon_i = y_i - (b_0 + b_1 x_i)` 的一个估计。残差有容易证得的三个性质：

.. math::

   \sum_{i=1}^n e_i = 0, \qquad \sum_{i=1}^n x_i e_i = 0, \qquad \sum_{i=1}^n \hat{y}_i e_i = 0.

