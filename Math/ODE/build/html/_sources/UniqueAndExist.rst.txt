
.. _toc-unique-and-exist:

解的存在与唯一性
===================

柯西 (Cauchy, 1789-1857) 在 19 世纪初提出了初值问题解的存在与唯一性定理（因此初值问题也成为柯西问题），而此后 1876 年李普希兹 (Lipschitz, 1832-1903) 减弱了该条件．在 1893 年，皮卡 (Picard, 1856-1941) 对李普希兹条件下的定理给出了新证明，也使 Picard 定理成为解的存在性判定的一般方法．而解的存在性定理由佩阿诺 (Peano, 1858-1932) 给出，他指明了一个在更一般条件下判定初值问题的解的存在性（不顾及唯一性）的条件．

除了解的存在与唯一性，本章介绍初值问题的基本知识，因此也包括解的延伸、初值扰动的问题．


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

    那么我们称函数 :math:`f(\bx)` 是在 :math:`\bx_0` 处 **局部 Lipschitz** (locally Lipschitz) 的．如果对区域 :math:`D` 内任意一点 :math:`\bx_0` 都有上式成立，那么我们称函数是在区域 :math:`D` 上局部 Lipschitz 的．
    
    特别地，在微分方程的研究中，如果不特别指明 :math:`\bx_0` 的值，那么 :math:`\bx_0` 均指原点．

    以上定义中，满足不等式的能够取到的最小常数 :math:`L`，称为 **Lipschitz 常数** (Lipschitz constant)．


此外，我们指出无须使用上述定义的、常用的判断方法：

1. 如果函数 :math:`f: \uR^n\to\uR^n` 在区域 :math:`D` 上存在连续的偏导数，那么它是局部 Lipschitz 的．如果区域 :math:`D` 还是有界且闭（称为 **紧** [#uae1]_ ）的，那么函数在该紧区域上满足全局 Lipschitz 的条件，即：

    .. math::

        |f(\bx_1) - f(\bx_2)| \leq L |\bx_1 - \bx_2|, \quad \forall \bx_1, \bx_2\in D\subseteq \uR^n

2. 如果函数存在连续的偏导数，且存在 :math:`L\geq 0` 使得 :math:`|\partial f_i/\partial x_j|` 对所有 :math:`\bx\in\uR^n` 与 :math:`1\leq i, j\leq n` 均成立，那么函数 :math:`f` 是全局 Lipschitz 的． 


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


Picard-Lindelöff 定理
----------------------------

Picard-Lindelöff 定理（或称 Picard 存在性定理、Cauchy-Lipschitz 定理），在微分方程中的研究中也通常简称为 Picard 定理，描述了解的唯一性条件．

.. admonition:: Picard-Lindelöff 定理
   :class: def

    对于初值问题：

    .. math::

        \begin{cases}
        \frac{\ud \bx}{\ud t} = f(t, \bx) \\
        \bx(0) = \bx_0
        \end{cases}

    Picard 定理有如下内容：
    
    1. 如果 :math:`f(t, \bx)` 对 :math:`\bx` 是全局 Lipschitz 的，那么初值问题的解 :math:`\bx(t)` 在 :math:`t\in\uR` 上是唯一的．

    2. 如果 :math:`f(\bx)` 对 :math:`\bx` 是（原点处）局部 Lipschitz 的 （且 Lipschitz 常数与 :math:`t` 无关），那么存在 :math:`T>0` 与一个在 :math:`[-T, T]` 上的唯一解 :math:`\bx: [-T,T]\to \uR^n` ．其中，:math:`T` 的值通常取决于 :math:`\bx_0`．

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

Peano 定理描述了解的存在判定条件，其证明不在此叙述．

.. admonition:: Peano 定理
   :class: def

   如果初值问题 :math:`\bx_t = f(t, \bx), \bx(0) = \bx_0` 中的函数 :math:`f` 在区域 :math:`D` 上是连续的，那么初值问题在区域 :math:`D` 对应的 :math:`t` 所在闭区间上至少存在一个解．

如果初值问题对任意 :math:`t\in\uR` 与初值 :math:`x_0\in\uR^n` 均存在解，那么称该微分方程定义了一个全流 (complete flow)；如果只对 :math:`t\geq 0` 时存在解，那么称其定义了一个半流 (semiflow)．


解的延伸与最大存在区间
-------------------------

解的延伸 (extension of solutions) 也是重要的内容．对于定义在区域 :math:`D` 上的函数 :math:`f`，初值问题的解在区域 :math:`D` 内是存在的．而该解如何延伸到区域外则需要以下定理：

.. admonition:: 解的延伸定理
   :class: def

    设 :math:`P` 为区域 :math:`G` 内任意一点，并设 :math:`\Gamma` 为一条标量微分方程 :math:`x_t = f(t,x)` 的积分曲线，则 :math:`\Gamma` 将在区域 :math:`G` 内延伸到边界．

    换言之，对任何 *有界闭区域* :math:`G_1` （:math:`P\in G_1\subset G`），积分曲线都将延伸到 :math:`G_1` 之外．

下面介绍最大存在区间的概念：

.. admonition:: 简化定义：最大存在区间

    解 :math:`x(t), \, t\in J` 中定义的 :math:`x` 最大能够取到的区间 :math:`J = (T_-, T_+)` 称为 **最大存在区间** （maximal interval of existence），其中 :math:`-\infty\leq T_- < 0 < T_+ \leq \infty`．


解的延伸判断
^^^^^^^^^^^^^^^^

解的延伸判断主要用两种方法：

1. 利用局部 Lipschitz 及最大存在区间单侧有限来判断：

    如果函数 :math:`f` 是局部 Lipschitz 的，且微分方程的解的最大存在区间 :math:`(T_-, T_+)` 至少单侧有限的（即 :math:`-\infty<T_-` 或 :math:`T_+<\infty`），那么解 :math:`\bx(t)` 在最大存在区间上必能趋向无穷，即相应有：

    .. math::

        T_+ < \infty \implies \lim_{t\to\infty} |\bx(t)|\to\infty 

        T_- > -\infty \implies \lim_{t\to-\infty} |\bx(t)|\to\infty

2. 利用解的延伸定理的一个推论来判断：

    .. admonition:: 推论：解的延伸定理
       :class: def

        设函数 :math:`f(x,y)` 在区域 :math:`G` 连续且对 :math:`y` 局部 Lipschitz，那么微分方程经过 :math:`G` 内任一点 :math:`P` 存在唯一的积分曲线 :math:`\Gamma` ，且 :math:`\Gamma` 在 :math:`G` 延伸到边界．

下面来看一个例子：

.. admonition:: 例子：解的延伸判定
   :class: eg

    对于 Hamiltonian 系统（参考 :ref:`toc-hamiltonian` 一节）： :math:`H(q_1,q_2,p_1,p_2) = q_1^8 + q_2^{10} + p_1^6 + p_2^{12}` ，其微分式：

    .. math::

        \begin{cases}
        q_i &= \frac{\partial H}{\partial p_i} \\
        p_i &= -\frac{\partial H}{\partial q_i}
        \end{cases}

    判断该动力系统的解的延伸性．

    **解：** 在此 Hamiltonian 系统中，轨线只能出现在 :math:`H=C` 这个 :math:`\uR^4` 上的有界区域内．因此，该方程的解是有界的，并对 :math:`t\in\uR` 都存在．


初值扰动对解的影响*
----------------------

先介绍一个引理：

.. admonition:: 引理：Grönwall–Bellman 不等式
   :class: def

    设 :math:`\psi: [0,\infty) \to \uR` 是一个满足下式的连续函数：

    .. math::

        \psi(t) \leq \psi_0 + M\int^t_0 \psi(s)\ud s
    
    对 :math:`t\geq 0` 恒成立，其中 :math:`\psi_0, M` 均为常数．那么，我们有下式对 :math:`t\geq 0` 恒成立：

    .. math::

        \psi (t) \leq \psi_0 \ue^{Mt} 

    **证明：** 令 :math:`g(t) = \psi_0 + M\int^t_0 \psi(s)\ud s` ，那么有 :math:`\psi\leq g` ．对 :math:`g` 微分，得到： :math:`g_t = M\psi \leq Mg` ，并推知 :math:`\left(\ue^{-Mt}g\right)_t \leq 0` ．由此，我们知道 :math:`\ue^{-Mt}g` 随 :math:`t` 是单调不增的，也就有 :math:`\ue^{-Mt}g(t) \leq \ue^{0}g(0) = \psi_0` ，因此 :math:`g(t)\leq \psi_0 \ue^{Mt}` ．又由 :math:`\psi\leq g` ，证毕．

再介绍如下定理：

.. admonition:: 定理

    设紧集 :math:`E\subset \uR^n` 上的函数 :math:`f: E\to \uR^n` 是在 :math:`E` 上 Lipschitz 的，且有 Lipschitz 常数 :math:`M` ．如果 :math:`x, y: I\subset \uR \to \uR^n` 分别是初值问题 :math:`IVP(f, x_0)` 与 :math:`IVP(f, y_0)` 在包含 :math:`t=0` 的公有域 :math:`I` 上的解，那么有：

    .. math::

        |x(t) - y(t)| \leq |x_0 - y_0|\ue^{|M|t}.

    对任意 :math:`t\in I` 均成立．

    **证明：** 将微分方程改写为 :math:`x(t) = x_0+\int_0^t f(x(s)) \ud s, y(t) = y_0+\int_0^t f(y(s)) \ud s` ，那么相减有：

    .. math::

        x(t) - y(t) &= (x_0 - y_0) + \int_0^t [f(x(s)) - f(y(s))]\ud s

        |x(t) - y(t)| &\leq |x_0 - y_0| + |\int_0^t [f(x(s)) - f(y(s))]\ud s|

        &\leq |x_0 - y_0| + M\int_0^t |x(s) - y(s)|\ud s \quad \textrm{(Lipschitz)}

    根据 Grönwall–Bellman 不等式，令 :math:`\psi(t) = |x(t) - y(t)|` ，那么对 :math:`t\geq 0`：

    .. math::

        |x(t) - y(t)| \leq |x_0 - y_0|\ue^{Mt}

    用 :math:`-t` 代替以上证明中的 :math:`t` 即可证明 :math:`t\in I` 的情形．

以上定理说明了，如果微分方程的两个初值有较小的差异，那么它们的解在某个时间尺度内也会相距较近．

.. rubric:: 注释

.. [#uae1] 有界 (bounded) 且闭 (close) 的也称为紧 (compact) 的．例如，我们常把有界闭集称为紧集．

