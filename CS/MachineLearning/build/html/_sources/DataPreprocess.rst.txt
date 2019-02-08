数据预处理
==============

本章介绍数据预处理的内容。下例命令被提前运行：

.. ipython:: python

   import numpy as np
   import pandas as pd


补全缺失数据
-----------------

缺失数据在不同数据集中可能有不同的标识方式，常见的列出如下。我个人倾向于使用 na，或者 N/A。个人不建议使用字符串“NaN”，因为这将与 pandas 默认的数字类型的 np.nan 混淆。

* 未填写内容，或空格
* N/A（或者 NA，na 等）
* ？（即问号符）
* 0，或所在特征（列）不可能取到的值（比如年龄属性中的负数）

scikit-learn.impute 模块提供了：

* 一个简单的缺失值估计器 `SimpleImputer <https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html>`_ ，由用户指定估计策略。对于字符串类型的特征，可以用 **众数**  `most_frequent` 或 **指定值**  `constant` 来估计；对于数值类型的特征，除了上述两种策略外，还可以用 **均值**  `mean` 或者 **中位数**  `median` 来估计。
* 一个标记各元素是否为缺失值的标记器 `MissingIndicator <https://scikit-learn.org/stable/modules/generated/sklearn.impute.MissingIndicator.html>`_ ，所有缺失位置会被标记为 True。注意：没有缺失值的特征（列）会被剔除。


例1：用本特征的均值补全
^^^^^^^^^^^^^^^^^^^^^^^^^^

方法 `fit_transform` 将本特征的数据用来拟合策略（本例中，即计算对应列除缺失值外的数据的均值）。例如对特征 x1 ，缺失值被估计为 :math:`(0+1+5)/3=2` 。本例中，所有 np.nan 被视为缺失值。

.. ipython:: python
   
   from sklearn.impute import SimpleImputer
   data = pd.DataFrame({"y": ["A", "B", "B", "N/A"], 
                    "x1": [0, 1, np.nan, 5],
                    "x2": [5, np.nan, 1, 9]})
   data.head()

   imp_mean = SimpleImputer(missing_values=np.nan, strategy='mean')
   data_na_mean = data.loc[:, ["x1", "x2"]].values
   imp_mean.fit_transform(data_na_mean)

例2：用外部数据的众数补全
^^^^^^^^^^^^^^^^^^^^^^^^^^

用外部数据进行拟合（方法 `fit` ），再应用于当前数据集（方法 `transform`）。特征 y 中所有的“N/A”被补全为“D”，因为在外部数据中“D”的出现的频数与“E”同为最高，且排序在“E"之前。

.. ipython:: python

   imp_freq = SimpleImputer(missing_values="N/A", strategy='most_frequent')
   fit_data = pd.DataFrame(["E", "D", "D", "E"], dtype="category")
   imp_freq.fit(fit_data)
   imp_freq.transform(data.y.values.reshape(-1, 1))

需要注意的是，如果只应用到一列（或一行）数据，请记得使用 `reshape(-1,1)` （或 `reshape(1,-1)` ）命令。

例3：用给定常数补全
^^^^^^^^^^^^^^^^^^^^^^

这是最简单的一种补全方式，方法上使用 `fit_transform` 即可。下例的所有缺失值被补全为 :math:`-1` 。

.. ipython:: python

   imp_constant = SimpleImputer(missing_values=np.nan, strategy='constant', fill_value=-1)
   imp_constant.fit_transform(data.x1.values.reshape(-1, 1))


数据类型处理
--------------------------

确认各特征的数据类型，例如是数字或是字符串。数据读取后请进行数据类型的检查。

此外，我们一般尽可能地使用数字来表示数据。比如性别男或女，可以处理为 0 或 1 来表示。如果你使用过 R 语言，那你应当对这样的 factor 类型处理不陌生。


拆分训练集与测试集
------------------------------------

将数据集随机打乱，然后抽取一定比例(一般70%～80%)作为训练集，剩下的作为测试集。


特征缩放
-----------------

许多模型使用欧几里德距离作为一个重要的度量方式，这就导致多特征量模型中，特征的不同数值尺度会影响模型结果。为避免这一点，标准化是一种常用的预处理方法。
