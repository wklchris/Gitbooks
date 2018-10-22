示例
===========

本章用于测试 Sphinx 对 reST 各语法功能的显示效果，主要测试内容是数学公式．


数学公式
-----------

常规数学符号：

.. math::

   \left(\frac{x}{y}\in\mathbb{R} \quad \sqrt[3]{x} \quad \int_0^1 x^2_0\ud{} x_0\right)

   \sin x \quad \cos x \quad \tan x \quad \cot x \quad \log x \quad \lg x

   \ln x \quad \lim_{i\to\infty} \quad \max_{x^2+y^2=1}\{x,y\} \quad \binom{n}{k}

   \sum_{i=1}^n a_i \neq \prod_{\substack{0<j<n<m \\ j\in\mathbb{N}}}^m b_j

字体：

.. math::

   \boldsymbol{A} \textrm{ is a matrix}

多行对齐：

.. math::
   :label: eq1

   y &= (a+b)^2 = (a+b)\times (a+b) \\
     &= a^2 + 2ab + b^2

微积分：

.. math::   

   \dot{x}(t) = x'(t) \quad \iint_D f(x) \quad \frac{\partial F}{\partial x} \quad
   \left.\frac{\sin x}{|x|}\right|_{x\in\mathring{U}}


堆叠：

.. math:: 

   \underbrace{a_1 + a_2 + \cdots + a_n}_{n} \quad \overbrace{x\cdot y\cdot z}^{3}

   \vec{a} \quad \overrightarrow{PQ} \quad a\xleftarrow[high]{low} b


矩阵

.. math:: 

   \boldsymbol{A} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \quad
   \det(\boldsymbol{B}) = \begin{vmatrix} 1 & 0 \\ 0 & 1 \end{vmatrix}


在此引用公式1：:eq:`eq1` 是一个多行对齐公式．


推断：（加载了 `extarrows` 包）

.. math::
   
   \alpha \implies \beta

   \gamma \iff \delta

   y\xLongrightarrow{\triangle} x + \varphi


警告
--------

Admonition 指令测试：

.. attention::
   
   Attention.

.. caution::
   
   Caution.
   
.. danger::
   
   Danger.
   
.. error::
   
   Error.
   
.. hint::
   
   Hint.

.. important::
   
   Important.
   
.. note::

   note
   
.. tip::
   
   Tip.
   
.. warning::
   
   Warning. 


测试结束．
