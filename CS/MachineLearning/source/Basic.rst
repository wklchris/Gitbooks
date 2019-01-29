基础
===============

本章是快速引言，以及介绍机器学习的基本概念．

本书通篇可能使用 scikit-learn 与 TensorFlow，在此先行加载某些库：

.. ipython:: python

   import numpy as np
   import matplotlib.pyplot as plt


为什么要学习机器学习
---------------------

机器学习的优势：

*  **提供了一种可缩短编程时间的方法** ：比起纯粹的、从零开始用人脑思索方法，成熟的机器学习解决方案允许用输入样本的简单方式快速地获得一个可靠方案．例如对于语法纠错，可以通过输入样本的方式解决．
*  **更灵活的自定义** ：传统编程需要很长时间的类似工作来适配一个新场景，但对于机器学习来说这往往只意味着采集一组新数据．例如，增加语法纠错程序所支持的语言．
* **帮助解决难以用人脑确定方法的问题**：人类的一些解决方法是内化在大脑中的，不一定能详尽地阐述其中的原理；机器学习却可以帮助解决这一类问题．例如，人脸识别．


机器学习使用中常遇到的问题：

* 训练集太小
* 训练集代表性欠缺
* 训练集质量低（错误值与噪声）
* 无关特征
* 过拟合或欠拟合


基础概念
----------------------

介绍机器学习的几个概念：

* **标签（Label）** ：即需要预测的变量．一般用 :math:`y` 表示．有时也翻译成“标记”．
* **特征（Feature）** ：即输入变量，通常描述拥有的数据．一般用 :math:`\boldsymbol{x} = \{x_1, x_2, \ldots, x_n\}` 表示．这里的 :math:`n` 表示 **维数（dimensionality）** ．有时也采用“属性（attribute）”的称呼．
* **观测（Observation）** ：一般地，数据集的每一行都是一个观测．；而每一列会对应一个特征（除了标签列）．
* **样例（Example）** ：指数据的一个集合．有时也译作“样本” [#f1]_ 或“示例”，或通称为“数据集”．

  * **有标签样例（labeled example）** ：指带有标签的样例，形如 :math:`\{\boldsymbol{x}, y\}`，用于训练模型．有时也会人为将其划分为用于训练的训练集（training set）与验证预测的测试集（testing set）．
  * **无标签样例（unlabeled example）** ：指仅有特性、没有标签的样例，形如 :math:`\{\boldsymbol{x}, ?\}`，用于预测．

* **模型（Model）** ：指样例与预测结果 :math:`y'` 之间建立的关系．它取决于通过机器学习方法求得的参数． 

  * **训练（training）** ：创建或学习模型，得出标签与样本之间的关系．
  * **推断（inference）** ：将训练得到的模型应用于无标签样本．用于


根据标签的情况，预测模型分为两大类：

* **回归（Regression）** 模型：预测连续值．比如：用户点击广告的概率是多少．
* **分类（Classification）** 模型：预测离散值．比如：给出的邮件是否是垃圾邮件．


监督与无监督学习
------------------

机器学习有多种分类方式，而最常被讨论的是按照人类监督程度划分．

* **监督式学习（Supervised Learning）** 是机器学习的基本框架，其训练集包含标签．主要方法包括：

  * K近邻算法（K-nearest neighbors, kNN）
  * 线性回归（Linear Regression）
  * 逻辑回归（Logistic Regression）
  * 支持向量机（Support Vector Machine, SVM）
  * 决策树和随机森林（Decision Tree & Random Forest）
  * 神经网络（Neural Network）：常被提及的 **深度学习（Deep Learning）** 属于这一分类．

* **无监督学习（Unsupervised Learning）** 的训练数据集不含标签．主要包含：

  * 聚类（Clustering）：K均值聚类（K-means clustering）、层次聚类（Hierarchical clustering, HC）
  * 降维（Dimensionality Reduction）：较著名的有主成分分析（Principle components analysis, PCA）、核方法（kernel method）．

半监督学习不在此介绍．还有一个类别称为 **强化学习（Reinforcement Learning）**，其特征是让学习主体（agent）自行决策，然后根据决策引发的结果，对不同情形下的决策策略进行学习和优化．

.. rubric:: 注释

.. [#f1] 严格地说，Example 这一词不应翻译为“样本”，因为这可能与 Sample 产生混淆．不过，从中文的角度，“样本”这个词既可以表示从全体中选取的一个数据集（即英文的 example），也可以表示抽取的一条或多条数据（即 sample）．本文中将使用“样例”作为翻译．