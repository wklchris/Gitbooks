.. Sphinx documentation master file, created by
   sphinx-quickstart on Mon Oct 15 13:34:24 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

《常微分方程笔记》前言
==================================

本书是我学习常微分方程（ODE）的笔记，主要阅读的书籍列出如下（以第一本为主）：

* *丁同仁，李承治．《常微分方程教程》第二版．高等教育出版社．*\ 这本书主讲常微分方程，附带一部分动力系统的内容．本书语言精炼而不失清晰，例子尚算精心，建议初学者阅读．
* *Gerald Teschl．Ordinary Differential Equations and Dynamical Systems．American Mathematical Society．*\ 这本书侧重于动力系统和混沌研究，建议有基础的读者阅读．此书的\ `作者主页 <https://www.mat.univie.ac.at/~gerald/ftp/book-ode/>`__\ 提供了本书的免费的英文版、中文版（《常微分方程与动力系统》机械工业出版社）两版pdf（内部稿）供下载．

阅读本书需要的知识：

* 基础数学知识
* 高等数学内容：极限、函数的导数和连续、基础微积分（阅读常微分部分需要）；多元函数微分，基础牛顿物理学（阅读动力系统部分需要）．
* 线性代数内容：行列式、特征值（阅读常微分部分需要）；子空间（阅读动力系统部分需要）．

以下是全文目录：

.. toctree::
   :maxdepth: 3
   :caption: 第一部分：常微分方程
   :numbered:

   Basic
   MethodForSolving


.. toctree::
   :maxdepth: 3
   :caption: 第二部分：动力系统
   :numbered:

   DS-basic
   DS-solution
   DS-stability
   DS-plane


鸣谢
-------

感谢我本科时的常微分方程授课教授永利，及研究生时的动力系统授课教授 Hunter．微分方程的世界由他们带领我进入．


.. 自定义的链接

.. _Gitbook: https://www.gitbook.com/
.. _`reST 笔记`: https://wklchris.github.io/Gitbooks/CS/reStructuredText/publish/
.. _Sphinx: http://www.sphinx-doc.org
