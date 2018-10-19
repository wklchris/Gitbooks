基本概念
========

本章介绍微分方程的基础内容．


微分方程的基本定义
--------------------------

.. _def-ode:

.. rubric:: 定义：常微分方程

对于自变量 :math:`x`、未知一元函数 :math:`y=y(x)`、该未知函数的一阶到 :math:`n` 阶导数与一个已知函数 :math:`F` 的方程：

    .. math::
       :label: ode

       F(x,y,y',\ldots,y^{(n)}) = 0

    就叫做 **常微分方程** [#ode]_ (ordinary differential equations, ODE)．
    

如果未知函数 :math:`y` 是多元函数，那么拥有类似形式的含偏导数的方程叫 **偏微分方程** (partial differential equations, PDE)；偏微分方程的内容不在本手册的讨论范畴．



阶与线性的概念
^^^^^^^^^^^^^^^^^^^

常微分方程式 :eq:`ode` 中出现的最高阶的 :math:`y` 的导数的阶数，称为该微分方程的 **阶** (order)．


.. rubric:: 例子

以下均为常微分方程：

   .. math::

      (1) \; \frac{\ud y}{\ud x} + xy = 0; \quad 
      (2) \; x_t = \sin x + t; \quad
      (3) \; y''' + yy' = x.

其中， :math:`y` 对 :math:`x` 的一阶导数，我们通常记成 :math:`\frac{\ud y}{\ud x}` 或 :math:`y_x`；如果自变量没有歧义，也可以记成上例中 (3) 的形式，即 :math:`y'`．对于 :math:`y` 的 :math:`n` 阶导数，我们通常记为 :math:`\frac{\ud^{n} y}{\ud x^n}` 或者 :math:`y^{(n)}`；如果 :math:`n` 较小，也可以参照上例 (3) 中三阶导数的记法．

式 :eq:`ode` 中，如果右侧的函数 :math:`F` 对未知函数 :math:`y` 与其各阶导数而言是一次的，则称式 :eq:`ode` 为 **线性常微分方程** (linear ODE)；否则，称其为 **非线性常微分方程** (nonlinear ODE)．

通过阶给方程分类，上例中的 (1) 与 (2) 是一阶微分方程，而 (3) 是三阶微分方程．通过线性与否分类，上例中的 (1) 是线性微分方程，而 (2) 与 (3) 是非线性微分方程．更详细的叙述是将两者结合，例如：例中 (1) 是一阶线性常微分方程．


微分方程的解
-------------------

下面定义微分方程的解：

.. _def-solution:

.. rubric:: 定义：微分方程的解

设函数 :math:`y=\varphi(x)` 在区间 :math:`J` 上连续且有 :math:`n` 阶的导数．如果该函数 :math:`y=\varphi(x)` 及其各阶导数代入方程 :eq:`ode` 后，得到一个关于 :math:`x` 的恒等式，即

    .. math::
       
       F(x,\varphi(x),\varphi'(x),\ldots,\varphi^{(n)}(x)) = 0

    对一切 :math:`x\in J` 都成立，则称 :math:`y=\varphi(x)` 为微分方程 :eq:`ode` 在区间 :math:`J` 上的一个 **解** (solution)．


例如，我们容易验证，:math:`y=\ue^x` 是微分方程 :math:`y_x = y` 的一个解．我们还发现，对于任意常数 :math:`C`，函数 :math:`y=C\ue^x` 都是该方程的解．


通解、特解与初值问题
^^^^^^^^^^^^^^^^^^^^^^

.. _def-general-solution:

.. rubric:: 定义：通解、特解

若 :math:`n` 阶微分方程 :eq:`ode` 的解

    .. math::

       y = \varphi(x,C_1,C_2,\ldots,C_n)

    包含 :math:`n` 个独立 [#indep]_ 的任意常数 :math:`C_1, C_2, \ldots, C_n`，则称该解为方程的 **通解** (general solution)；如果方程的解 :math:`y=\varphi(x)` 不含任意常数，则称该解为方程的 **特解** (particular solution)．

显然，如果得到了通解，又能将其所有的任意常数确定下来，通解就会变成特解．在上例的微分方程中 :math:`y=\ue^x`，:math:`y=C\ue^x` 就是它的通解．至于特解，一个典型的例子是初值问题：

.. rubric:: 定义：初值问题

对 :math:`n` 阶微分方程 :eq:`ode`，其对应的 **初值问题** (initial value problem, IVP) 是指：

    .. math::

       \begin{cases}
       y^{(n)} &= F(x,\varphi(x),\varphi'(x),\ldots,\varphi^{(n-1)}(x)) \\
       y(x_0)  &= y_0, y'(x_0) = y'_0, \ldots, y^{(n-1)} = y^{(n)}_0
       \end{cases}

    其中 :math:`x_0` 是自变量所确定的初值，而 :math:`y_0,y'_0,\ldots,y^{(n-1)}_0` 是未知函数 :math:`y` 及其相应导数所确定的初值．相应地，这些初值组成的上述条件称为 **初值条件** (initial value condition)．

例如，如果已知微分方程 :math:`y_x = y` 及其在 :math:`x=0` 处的初值条件 :math:`y(0)=1` ，那么它们就组成了一个初值问题，其解为 :math:`y=\ue^t`．该解是该方程的特解．至于求解微分方程的方法与解的唯一性讨论，我们在下文讨论．


微分方程及其解的几何意义
-------------------------



.. rubric:: 注释

.. [#ode] 方便起见，本手册下文中将常微分方程称微分方程或方程．
.. [#indep] 此处的“独立”是指它们的 Jacobi 行列式非零：
   
   .. math::
      
      \frac{D[\varphi, \varphi', \ldots, \varphi^{(n)}]}{D[C_1,C_2,\ldots,C_n]} =
      \begin{vmatrix}
      \frac{\partial \varphi}{\partial C_1} & \frac{\partial \varphi}{\partial C_2} & \cdots & \frac{\partial \varphi}{\partial C_n} \\[8pt]
      \frac{\partial \varphi'}{\partial C_1} & \frac{\partial \varphi'}{\partial C_2} & \cdots & \frac{\partial \varphi'}{\partial C_n} \\[8pt]
      \vdots & \vdots & & \vdots \\[8pt]
      \frac{\partial \varphi^{(n)}}{\partial C_1} & \frac{\partial \varphi^{(n)}}{\partial C_2} & \cdots & \frac{\partial \varphi^{(n)}}{\partial C_n} \\
      \end{vmatrix} \neq 0.
