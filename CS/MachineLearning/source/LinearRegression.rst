线性回归
==========

本章介绍线性回归的内容．

**线性回归（Linear regression）** 是最基础的机器学习模型．在机器学习中，线性回归的模型可以用下式描述：

.. math::

   y' = w_1x_1 + w_2x_2 + \cdots + w_nx_n + b

其中，模型左侧的 :math:`y'` 表示待预测的标签，各 :math:`w_i` 表示特征 :math:`x_i` 的权重，而 :math:`b` 表示截距．要利用线性回归模型对给定的特征 :math:`\boldsymbol{x}=\{c_1, c_2, \ldots, c_n\}` 进行推断，只须将它们代入等式右侧即可．


误差
--------

评价线性回归模型的一个标准是 **误差（error）** ．

最广为使用的线性回归误差函数是平方误差（L2 误差）函数，也就是诸位读者应当学习过的最小二乘法：

.. math::
   
   MSE = \frac{1}{|D|}\sum_{(x_i,y_i)\in D} (y_i - y'_i)^2

其中集合 :math:`D` 表示样本数据集，:math:`|D|` 表示该集的样本数量．每个样本用 :math:`(x, y)` 的形式表示，标签的预测值则用 :math:`y'` 表示．


示例
--------

一个线性回归的示范．

.. ipython:: python
   
   from sklearn import datasets, linear_model
   
   # To be continued
