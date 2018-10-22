基本概念
========

本章介绍微分方程的基础内容．


微分方程的基本定义
--------------------------

.. _def-ode:

.. admonition:: 定义：常微分方程
   :class: def

    对于自变量 :math:`x`、未知一元函数 :math:`y=y(x)`、该未知函数的一阶到 :math:`n` 阶导数与一个已知函数 :math:`F` 的方程：

    .. math::
       :label: ode

       F(x,y,y',\ldots,y^{(n)}) = 0

    就叫做 **常微分方程** [#ode]_ (ordinary differential equation, ODE)．
    

如果未知函数 :math:`y` 是多元函数，那么拥有类似形式的含偏导数的方程叫 **偏微分方程** (partial differential equation, PDE)；偏微分方程的内容不在本手册的讨论范畴．



阶与线性的概念
^^^^^^^^^^^^^^^^^^^

常微分方程式 :eq:`ode` 中出现的最高阶的 :math:`y` 的导数的阶数，称为该微分方程的 **阶** (order)．


.. admonition:: 例子：常微分方程
   :class: eg

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

.. admonition:: 定义：微分方程的解
   :class: def

    设函数 :math:`y=\varphi(x)` 在区间 :math:`J` 上连续且有 :math:`n` 阶的导数．如果该函数 :math:`y=\varphi(x)` 及其各阶导数代入方程 :eq:`ode` 后，得到一个关于 :math:`x` 的恒等式，即

    .. math::
       
       F(x,\varphi(x),\varphi'(x),\ldots,\varphi^{(n)}(x)) = 0

    对一切 :math:`x\in J` 都成立，则称 :math:`y=\varphi(x)` 为微分方程 :eq:`ode` 在区间 :math:`J` 上的一个 **解** (solution)．


例如，我们容易验证，:math:`y=\ue^x` 是微分方程 :math:`y_x = y` 的一个解．我们还发现，对于任意常数 :math:`C`，函数 :math:`y=C\ue^x` 都是该方程的解．


通解、特解与初值问题
^^^^^^^^^^^^^^^^^^^^^^

.. _def-general-solution:

.. admonition:: 定义：通解、特解
   :class: def

    若 :math:`n` 阶微分方程 :eq:`ode` 的解

    .. math::

       y = \varphi(x,C_1,C_2,\ldots,C_n)

    包含 :math:`n` 个独立 [#indep]_ 的任意常数 :math:`C_1, C_2, \ldots, C_n`，则称该解为方程的 **通解** (general solution)；如果方程的解 :math:`y=\varphi(x)` 不含任意常数，则称该解为方程的 **特解** (particular solution)．

显然，如果得到了通解，又能将其所有的任意常数确定下来，通解就会变成特解．在上例的微分方程中 :math:`y=\ue^x`，:math:`y=C\ue^x` 就是它的通解．至于特解，一个典型的例子是初值问题：

.. admonition:: 定义：初值问题
   :class: def

    对 :math:`n` 阶微分方程 :eq:`ode`，其对应的 **初值问题** (initial value problem, IVP) 是指：

    .. math::

       \begin{cases}
       y^{(n)} &= F(x,\varphi(x),\varphi'(x),\ldots,\varphi^{(n-1)}(x)) \\
       y(x_0)  &= y_0, y'(x_0) = y'_0, \ldots, y^{(n-1)} = y^{(n)}_0
       \end{cases}

    其中 :math:`x_0` 是自变量所确定的初值，而 :math:`y_0,y'_0,\ldots,y^{(n-1)}_0` 是未知函数 :math:`y` 及其相应导数所确定的初值．相应地，这些初值组成的上述条件称为 **初值条件** (initial value condition)．

例如，如果已知微分方程 :math:`y_x = y` 及其在 :math:`x=0` 处的初值条件 :math:`y(0)=1` ，那么它们就组成了一个初值问题，其解为 :math:`y=\ue^t`．该解是该方程的特解．至于求解微分方程的方法与解的唯一性，我们在下文讨论．


微分方程及其解的几何意义
-------------------------

从最简单的一阶微分方程开始，我们来简要阐述微分方程及其解的几何意义．

.. admonition:: 定义：积分曲线
   :class: def

    对于一阶的标量（scalar）微分方程

    .. math::
       :label: geometry-ode

       \frac{\ud y}{\ud x} = f(x,y)
    
    其中函数 :math:`f: \uR^2 \to \uR` 是平面区域 :math:`G` 内的连续函数．如果该方程在区间 :math:`I` 上存在解 :math:`y=\varphi(x), \ x\in I`，那么该解 :math:`y=\varphi(x)` 在 :math:`(x,y)` 平面上的图形是一条光滑的曲线 :math:`\Gamma`．该曲线称为微分方程 :eq:`geometry-ode` 的 **积分曲线** (integral curve)．


积分曲线与方向场
^^^^^^^^^^^^^^^^^^^^^

结合导数的定义，我们知道对于积分曲线 :math:`\Gamma` 上任意一点 :math:`(x_0,y_0)` 处的切线斜率即为 :math:`\varphi'(x_0)=f(x_),\varphi(x_0))`．由此可知：即使我们不能直接求得曲线 :math:`\Gamma`，我们也可以写出该曲线在其上任意一点处的切线方程．

在区域 :math:`G` 内的每个点 :math:`P(x,y)`，我们均可用上述方法确定积分曲线（若存在）在该点的切线方向．在点 :math:`P` 处画出一个极短的线段，用以标明曲线 :math:`\Gamma` 在该点处的切线斜率方向，这样的线段称为微分方程在点 :math:`P` 处的 **线素**；区域 :math:`G` 与其上全体线素，称为微分方程的 **方向场** (direction field)，也称 **线素场** (slope field)．在绘制方向场时，通常用等式 :math:`f(x,y)=k` 来绘制由常数 :math:`k` 确定的曲线 :math:`L_k`，称为方向场的 **等倾线** (isocline)．绘制的例子见 :ref:`subsec-direction-field` 一节．

显然，方程的任何积分曲线 :math:`\Gamma` 与它的线素场吻合；反之，如果区域 :math:`G` 上存在一条光滑的曲线

.. math::
   
    \Delta: y = \varphi(x), \ x\in J

与方向场吻合，那么 :math:`\Delta` 是方程 :eq:`geometry-ode` 的一条积分曲线．


.. _subsec-direction-field:

方向场的绘制
^^^^^^^^^^^^^^^^

上文叙述了如何使用线素和等倾线来绘制方向场．但有一点尚需说明：微分方程 :eq:`geometry-ode` 右侧的函数 :math:`f(x,y)` 有时或许是未定式，这是绘制时可能遇到的特殊情况．例如，微分方程通常的对称形式：

.. math::

    P(x,y)\ud x + Q(x,y)\ud y = 0


容易看出，如果在点 :math:`(x_0,y_0)` 附近绘制该微分方程的线素，有三种可能：

1. 如果 :math:`Q(x_0,y_0)\neq 0`，那么可以利用 :math:`\ud y/\ud x = -P(x_0,y_0)/Q(x_0,y_0)` 来绘制；
#. 如果 :math:`P(x_0,y_0)\neq 0`，那么可以利用 :math:`\ud x/\ud y = -Q(x_0,y_0)/P(x_0,y_0)` 来绘制；
#. 如果 :math:`P(x_0,y_0)=Q(x_0,y_0)`，那么 :math:`\ud y/\ud x` 与 :math:`\ud x/\ud y` 在点 :math:`(x_0,y_0)` 处均是未定式，该点的线素没有意义．这时，我们把 :math:`(x_0,y_0)` 称为 **奇异点** (singularity, or singular point)．

.. admonition:: 例子：方向场的绘制
   :class: eg

    绘制下述微分方程的方向场：

    .. math::
      
       \frac{\ud y}{\ud x} = \frac{y}{x}.
    
    易知，原点是奇异点．对于平面上的其他点，我们可以用等倾线 :math:`\frac{y}{x}=k` 来帮助绘制．该式说明线素斜率为 :math:`k` 的点，是由直线 :math:`y=kx` 组成的．由所有任意实数 :math:`k` 组成的直线簇 :math:`y=kx`，就构成了该微分方程的方向场（或称确定了微分方程的积分曲线）．绘制的方向场如下图：
    
    .. plot:: _static/img/direction-field.py
       :align: center

    其实，直线 :math:`y=kx` 上任取一点，我们能确定的是其与原点连线的斜率为 :math:`k`，即 :math:`\arctan \frac{y}{x}=k`；也可以用任意常数 :math:`C` 表述，即该微分方程的积分曲线为 :math:`\arctan \frac{y}{x}=C`．

    可以验证，对原微分方程的变式 :math:`y\ud x - x\ud y = 0` 积分后便得 :math:`\arctan \frac{y}{x}=C`．


方向场对求解微分方程的意义
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

通过方向场的绘制，我们可以大致把握积分曲线的形状．如果取点足够密，那么方向场就能较清楚地展示积分曲线的近似图．这在无法或不必求精确解时，给出了一种近似解的求得方式．

即使我们求得了微分方程的精确解，有时我们仍需借助方向场（或某些特定点附近的线素）来解决问题．


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
