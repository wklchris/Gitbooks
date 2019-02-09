数据预处理
==============

本章介绍数据预处理的内容。下例命令被提前运行：

.. ipython:: python

   import numpy as np
   import pandas as pd
   import sklearn.preprocessing as skp  # Personal preferred alias


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

此外，我们一般尽可能地使用数字来表示数据。比如性别男或女，可以编码为 0 或 1。如果你使用过 R 语言，那你应当对这样的 factor 类型处理不陌生。

scikit-learn.preprocessing 提供了：

* 序数编码器 `OrdinalEncoder <https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html>`_ 。将类别特征中每个出现过的值，设为一个单独的整数编码。序数分配将按照字符串的排序先后进行。
* 独热编码器 `OneHotEncoder <https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html>`_ 。该编码器会将一个特征拆分为多个：每个新的特征会把某一个值指定为 1，其余值都赋 0。


例1：序数编码 OrdinalEncoder
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

本例将两个特征（列）的编码方式混写在一个编码器中，用户也可以拆分开来分别处理。编码器在应用到多列上似乎还存在困难，我通常选择结合循环语句、 `data.loc[:, i]` 以及 `reshape(-1, 1)` 来应对。

OrdinalEncoder 在语法上与缺失值估计器 SimpleImputer 十分近似，也是先 fit 再 transform。下面是一个利用外部数据进行编码的例子：

.. ipython:: python

   data = pd.DataFrame({"x1": list("ABBCACAB"), 
                     "x2": [5,6,7,8] * 2})
   data

   enc_ordinal = skp.OrdinalEncoder()
   enc_ordinal.fit([["A", 5], ["C", 6], ["B", 7], ["A", 8]])
   enc_ordinal.transform(data.values)

更通常的做法是基于自特征的编码，即 `fit_transform` 方法：

.. ipython:: python

   enc_ordinal = skp.OrdinalEncoder()
   enc_ordinal.fit_transform(data.values)

对于已知编码结果的情况，可以利用 fit 过后的编码器进行反向解码，推出原有的类别字符串：

.. ipython:: python

   enc_ordinal.inverse_transform([[0, 0], [1, 1]])


例2：独热编码 OneHotEncoder
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

该编码器在使用时，请记住附加 `toarray` 方法。下例使用了 `fit_transform` 方法，用户也可以拆分使用 fit 与 transform。此外，与序数编码器一样，独热编码器支持 `inverse_transform` 方法进行回溯。

下例中使用了 `get_feature_names` 的 `input_features` 参数来命令编码结果的各特征（列）。

.. ipython:: python

   data = pd.DataFrame([["A", "X"], ["A", "Y"], ["B", "Y"]], columns=["x", "y"])
   data

   enc_onehot = skp.OneHotEncoder()
   enc_data = enc_onehot.fit_transform(data).toarray()
   enc_data_index = enc_onehot.get_feature_names(input_features=data.columns)
   data_encoded = pd.DataFrame(enc_data, columns=enc_data_index)
   data_encoded

独热编码器在创建时可以使用一个特殊参数 `handle_unknown='ignore'` 来忽略拟合数据中不存在的值。比如下例的第一特征只使用了“C”来拟合，因此原数据集中的“A”与“B”都被编码为0。此外，编码后的数据也不含“x_A”与“x_B”这两列。

.. ipython:: python

   enc_onehot = skp.OneHotEncoder(handle_unknown='ignore')
   enc_onehot.fit([["C", "X"], ["C", "Y"]])
   pd.DataFrame(enc_onehot.transform(data).toarray(),
               columns=enc_onehot.get_feature_names())

拆分训练集与测试集
------------------------------------

将数据集随机打乱，然后抽取一定比例（一般70%～80%）作为训练集，剩下的作为测试集。

sklearn.model_selection 提供了易用的 `train_test_split <https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html>`_ 来划分训练集与测试集。该方法可以接受多个 np.array 作为输入。参数 `test_size` 是测试集的比重（默认 0.25）， `random_state` 是随机数种子。

一个标准的划分例子如下：

.. ipython:: python

   # Example from scikit-learn 0.20.0 official user guide
   from sklearn.model_selection import train_test_split
   X, y = np.arange(10).reshape((5, 2)).astype(np.float64), range(5)
   X

   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
   X_train
   X_test
   y_train
   y_test


特征缩放：标准化与归一化
------------------------

许多模型使用欧几里德距离作为一个重要的度量方式，这就导致多特征量模型中，特征的不同数值尺度会影响模型结果。为避免这一点，常用的 **标准化（standardization）** 手段, 即 `scale` 命令，通过平移移除了均值（将均值变换为0），并线性缩放将标准差变换为1：

.. math::

   X' = \frac{X - \mu}{\sigma}

上式中的 :math:`\mu` 与 :math:`\sigma` 无法求得时，使用样本均值与样本标准差代替。

而 **归一化（normalization）** 是指将数据缩放到一个给定的区间内（通常是 :math:`[0,1]` 或者 :math:`[-1, 1]`）。以通常所指的最值归一化（归一化到 :math:`[0,1]` ）为例：

.. math::
   
   X' = \frac{X - \min\{X\}}{\max\{X\} - \min\{X\}}

关于特征缩放概念的误解，尤其是 standardization 与 normalization 的混淆，一直都非常严重。 **标准化的含义是唯一的** ；而归一化除了上述的最值归一化外，还有其他的形式，例如均值归一化 :math:`(x-\bar{x})/(\max\{x\}-\min\{x\})` ，单位长归一化 [#f1]_ :math:`x/\| x\|` （即 `skp.normalize`）。

sklearn.preprocessing 提供了以下线性缩放器：

* 标准化 scale / StandardScaler：scale 通过线性变换各个特征，使它们均具有均值为 0、标准差为 1 的特性。而 StandardScaler 默认的参数 `with_mean=True, with_std=True` 也表示平移中心到0、缩放标准差为1，因此默认参数下它与标准化缩放效果相同。
* 归一化 minmax_scale / MinMaxScaler：`MinMaxScaler(feature_range=(0,1))` 默认将各列 **缩放并充满** 到 :math:`[0,1]` 区间，也被称为最值归一化（Min-max normalization）。
* 乘法缩放器 maxabs_scale / MaxAbsScaler： `MaxAbsScaler()` 将各列乘以系数，使结果落在 :math:`[-1, 1]` 的范围内（但不一定充满这个区间）。该方法不平移数据。
* 鲁棒缩放器 robust_scale / RobustScaler：该缩放器会剔除两端的值（默认的 `quantile_range=(25.0, 75.0)` ，即剔除25氛围以下与75分位以上），然后对剩余值执行类似 `MinMaxScaler(-0.5, 0.5)` 的操作。

非线性的缩放器也有不少，这里不一一介绍了。读者可以参考官方 `Nonlinear Transformation <https://scikit-learn.org/stable/modules/preprocessing.html#non-linear-transformation>`_ 这一小节的内容。


例1：标准化
^^^^^^^^^^^^^^^

以下是 scale 的例子：

.. ipython:: python

   data = pd.DataFrame({"x1": [0.0, 1, 2], "y": [-2, 0.0, 1]})
   data_scaled = skp.scale(data)
   data_scaled
   data_scaled.mean(), data_scaled.std()


以下是 StandardScaler 的例子，它较 scale 的优点在于可以将指定的变换应用到另一个数据上：

.. ipython:: python

   st_scaler = skp.StandardScaler().fit(X_train)
   X_train_stscaled = st_scaler.transform(X_train)
   X_train_stscaled.mean(), X_train_stscaled.std()
   X_test_stscaled = st_scaler.transform(X_test)
   X_test_stscaled.mean(), X_test_stscaled.std()


例2：归一化
^^^^^^^^^^^^^^^

范围缩放的缺点在于对异常值比较敏感。

.. ipython:: python
   
   # Max-min normalization
   skp.MinMaxScaler(feature_range=(-1, 1)).fit_transform(data)
   skp.minmax_scale(data, feature_range=(-1, 1))

   # Scaling to unit length normalization (default by row)
   skp.normalize(data, axis=0)


例3：乘法缩放
^^^^^^^^^^^^^^^

本例与归一化例中的 MinMaxScaler 缩放到同样的区间，读者可以比较两者结果的区别。

.. ipython:: python

   skp.MaxAbsScaler().fit_transform(data)
   skp.maxabs_scale(data)


例4：鲁棒缩放
^^^^^^^^^^^^^^^^

鲁棒缩放并不是把所有值都缩放到对应的 25-75 分位之间，它仍然保留了离群值。因此，实际上缩放后的范围可能比预期的更大一些。

.. ipython:: python

   rb_scaler = skp.RobustScaler(quantile_range=(25.0, 75.0))
   rb_scaler.fit_transform(data)
   rb_scaler.scale_, rb_scaler.center_
   # Alternative
   skp.robust_scale(data, quantile_range=(25.0, 75.0))

.. rubric:: 注释

.. [#f1] 单位长归一化的英文是 Scaling to Unit Length，是否应被翻译成“归一化”尚无考证。笔者倾向于对除了标准化之外的其他特征缩放都采用“归一化”的称呼，因此此处权宜这样书写。
