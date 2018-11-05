
.. _toc-unique-and-exist:

解的存在与唯一性
===================

柯西 (Cauchy, 1789-1857) 在 19 世纪初提出了初值问题解的存在与唯一性定理（因此初值问题也成为柯西问题），而此后 1876 年李普希兹 (Lipschitz, 1832-1903) 减弱了该条件．在 1893 年，皮卡 (Picard, 1856-1941) 对李普希兹条件下的定理给出了新证明，也使 Picard 定理成为解的存在性判定的一般方法．而解的存在性定理由佩阿诺 (Peano, 1858-1932) 给出，他指明了一个在更一般条件下判定初值问题的解的存在性（不顾及唯一性）的条件．

除了解的存在与唯一性，本章还将对解的延伸进行探讨．


Lipschitz 条件
-------------------

为了介绍 Picard 定理，我们需要先理解 Lipschitz 条件的概念．

.. admonition:: 定义：Lipschitz 连续
   :class: def

    对于函数 :math:`f: \uR^n \to \uR^n` ，如果存在常数 :math:`L>0` 使得

    .. math::

        |f(\bx_1) - f(\bx_2)| \leq L |\bx_1 - \bx_2|, \quad \forall \bx_1, \bx_2\in D\subseteq \uR^n

    那么我们称函数 :math:`f(\bx)` 在该区域上是 **Lipschitz 连续** (Lipschitz continuous) 的，或简称为在区域 :math:`D` 上是 Lipschitz 的．也可以称 :math:`f(\bx)` 是区域 :math:`D` 上的一个 Lipschitz 函数．
    
    特别地，如果区域 :math:`D=\uR^n`，那么我们称函数 :math:`f(\bx)` 是 **全局 Lipschitz** (globally Lipschitz) 的；如果区域 :math:`D` 是某点 :math:`\bx_0\in\uR^n` 附近一个半径为 :math:`r>0` 的球，即：

    .. math::

        |f(\bx_1) - f(\bx_2)| \leq L |\bx_1 - \bx_2|, \quad \forall |\bx_1-\bx_0|, |\bx_2-\bx_0|\leq r

    那么我们称函数 :math:`f(\bx)` 是在 :math:`\bx_0` 处 **局部 Lipschitz** (locally Lipschitz) 的．特别地，在微分方程的研究中，如果不特别指明 :math:`\bx_0` 的值，那么 :math:`\bx_0` 均指原点．

    以上定义中，满足不等式的能够取到的最小常数 :math:`L`，称为 **Lipschitz 常数** (Lipschitz constant)．


此外，我们指出无须使用上述定义的、常用的判断方法：

1. 如果函数 :math:`f: \uR^n\to\uR^n` 连续可微，那么它是局部 Lipschitz 的．
2. 如果函数满足上一条，且存在 :math:`L\geq 0` 使得 :math:`|\partial f_i/\partial x_j|` 对所有 :math:`\bx\in\uR^n` 与 :math:`1\leq i, j\leq n` 均成立，那么函数 :math:`f` 是全局 Lipschitz 的． 


下面举三个定义在 :math:`\uR` 上的例子，学习如何用以上定义判断函数是否是 Lipschitz 的：

.. admonition:: 例子：Lipschitz 判定
   :class: eg

    判断以下函数是否是（原点附近的） Lipschitz 函数．

    .. math::

        (1) f(x) = \sqrt{1+x^2}; \quad
        (2) g(x) = x^2; \quad
        (3) h(x) = \sqrt{|x|}.

    **解：** 对于函数 (1)，我们有：

    .. math::

        |f(x)-f(y)| = |\sqrt{1+x^2} - \sqrt{1+y^2}| 
        = \left| \frac{x+y}{\sqrt{1+x^2} + \sqrt{1+y^2}} \right|\cdot |x-y|
        \leq |x-y|
    
    因此函数 :math:`f(x)` 是 Lipschitz 的．
    
    对于函数 (2)，在原点附近的半径 :math:`r` 内，有：

    .. math::

        |g(x) - g(y)| = |x+y||x-y| \leq 2r|x-y|
    
    上式对 :math:`|x|, |y|\leq r` 成立，因此 :math:`g(x)` 在 :math:`(0,0)` 处是局部 Lipschitz 的．

    对于函数 (3)，我们有：

    .. math::

        \frac{|h(x) - h(0)|}{|x - 0|} = \frac{1}{\sqrt{|x|}} \to\infty \textrm{ as } x\to\infty

    因此， :math:`h(x)` 在 :math:`(0,0)` 附近不是局部 Lipschitz 的；它自然也不是全局 Lipschitz 的．


Picard 定理
-----------------

.. admonition:: Picard-Lindeloff 定理
   :class: def

    对于初值问题：

    .. math::

        \begin{cases}
        \frac{\ud \bx}{\ud t} = f(t, \bx) \\
        \bx(0) = \bx_0
        \end{cases}

    Picard 定理有如下内容：
    
    1. 如果 :math:`f(t, \bx)` 对 :math:`\bx` 是全局 Lipschitz 的，那么初值问题的解 :math:`\bx(t)` 在 :math:`t\in\uR` 上是唯一的．

    2. 如果 :math:`f(\bx)` 对 :math:`\bx` 是（原点处）局部 Lipschitz 的，那么存在 :math:`T>0` 与一个在 :math:`[-T, T]` 上的唯一解 :math:`\bx: [-T,T]\to \uR^n` ．其中，:math:`T` 的值通常取决于 :math:`\bx_0`．

在增广空间，解如果唯一，即表示过区域内每一点有且仅有一条积分曲线．


Picard 迭代
^^^^^^^^^^^^^^^^^^

**Picard 迭代** (Picard iteration) 是证明 Picard 定理中使用的方法．

对于初值问题 :math:`y_x = f(x,y),\, y(0)=y_0`，这等价于求解 :math:`y(x) = y_0 + \int_{x_0}^x f(s,y(x))\ud s`． 因此，我们可以用迭代法：

.. math::

    y_{n+1}(x) = y_0 + \int_{x_0}^x f(s, y_n(x))\ud s

后续定理的证明利用 Lipschitz 条件与数列的一致收敛可证．如果函数是局部 Lipschitz 的，那么 :math:`y_n(x)` 会在一个充分小的区间内 :math:`[-X, X]` 一致收敛到初值问题的解 :math:`y(x)` ．

.. admonition:: 例子：Picard 迭代
   :class: eg

    求初值问题 :math:`x_t = x,\quad x(0)=1` 的 Picard 迭代，并判断它是否收敛．

    **解：** 该初值问题的积分形式：

    .. math::

        x(t) = 1 + \int_0^t x(s) \ud s

    迭代：

    .. math::

        x_0 &= 1,

        x_1 &= 1 + \int_0^t x_0(s) \ud s = 1 + t,

        x_2 &= 1 + \int_0^t x_1(s) \ud s = 1 + \int_0^t (1+s) \ud s = 1 + t + \frac{t^2}{2}

    以下由归纳法得 :math:`x_n = \sum_{k=0}^n \frac{t^k}{k!}` 对任意 :math:`n\in \mathbb{N}` 成立；而上式显然是指数函数 :math:`\ue^t` 的 Taylor 展开．这个数列向 :math:`\ue^t` 逐点（并在紧集上一致地）收敛．


Peano 定理
------------

Peano 定理如下，其证明不在此叙述．

.. admonition:: Peano 定理
   :class: def

   如果初值问题 :math:`\bx_t = f(t, \bx), \bx(0) = \bx_0` 中的函数 :math:`f` 在区域 :math:`D` 上是连续的，那么初值问题在区域 :math:`D` 对应的 :math:`t` 所在闭区间上至少存在一个解．



解的延伸
------------

解的延伸 (extension of solutions) 也是重要的内容．

.. admonition:: 解的延伸定理
   :class: def

    设 :math:`P` 为区域 :math:`G` 内任意一点，并设 :math:`\Gamma` 为一条标量微分方程 :math:`y_x = f(x,y)` 的积分曲线，则 :math:`\Gamma` 将在区域 :math:`G` 内延伸到边界．解 :math:`y(x)` 存在的区间 :math:`x\in J` 称为 **最大存在区间** ．

    换言之，对任何有界闭区域 :math:`G_1` （:math:`P\in G_1\subset G`），积分曲线都将延伸到 :math:`G_1` 之外．

上述定理并不是常用的形式，我们更常使用的是它的一个推论：

.. admonition:: 推论：解的延伸定理
   :class: def

    设函数 :math:`f(x,y)` 在区域 :math:`G` 连续且对 :math:`y` 局部 Lipschitz，那么微分方程经过 :math:`G` 内任一点 :math:`P` 存在唯一的积分曲线 :math:`\Gamma` ，且 :math:`\Gamma` 在 :math:`G` 延伸到边界．

