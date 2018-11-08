平衡点的稳定性
=================

虽然前文已介绍过，但此处仍简单叙述平衡点的定义：

.. admonition:: 定义：动力系统的平衡点

    对动力系统 :math:`\bx(t) = f(\bx)`，我们称其流 :math:`\varphi_t(\bx)` 的不动点 :math:`\varphi_t(\eqbx) = \eqbx` 为动力系统的 **平衡点** (equilibrium)，并一般记作 :math:`\eqbx` ．

流如果满足上式，那么如果初值设为流的不动点 :math:`\bx_0 = \eqbx`，我们总有 :math:`\bx(t) = \eqbx` 成立．从几何上解释，在平衡点处粒子运动的速度为 :math:`f(\eqbx) = 0`，因此粒子如果到达该点就不会离开，即平衡．


稳定性引言
-------------

平衡点的稳定性是一个很自然的描述；例如，把小球放置在弧顶与弧底都是平衡的，但前者只要放置时稍稍偏离正顶点，小球就会移动．这是一种“不稳定”的平衡．

在微分方程中，**平衡点的稳定性描述的不是粒子位于平衡点处是否稳定，而是粒子位于平衡点附近时，能否被平衡点吸引** ．如果在平衡点附近的解会逃逸，那么平衡点称为 **不稳定** (unstable) 的就像小球放置在稍偏离弧顶的位置；否则，称平衡点为 **稳定** (stable) 的，就像小球绕着弧底的光滑侧壁作圆圈运动，既不远离也不靠近．此外，稳定之中还有一种特别情形，即解被逐渐吸引，此时称为 **渐进稳定** (asymptotically stable)，就像小球放置在稍偏离弧底的位置．

以上小球的例子是不严谨的，只是提供了一个粗浅的、生活化的启发．比如小球放置在偏离弧底的位置，那么它会周而复始地作摆动；这与微分方程上平衡点的意义不严格对等（到达平衡点时速度为零）．下面我们来介绍稳定性．


Lyapunov 稳定性
---------------------

如无特殊说明，本笔记中提到的稳定均指李雅普诺夫 (Lyapunov) 稳定．

.. admonition:: 定义：Lyapunov 稳定

    动力系统 :math:`\bx(t) = f(\bx)` 及其平衡点 :math:`\eqbx` 如果满足对 :math:`\eqbx` 附近的任意邻域 :math:`U`，均存在一个 :math:`\eqbx` 附近的邻域 :math:`V` ，使得只要 :math:`\bx\in V` 均有 :math:`\varphi_t(\bx)\in U` 对 :math:`t\neq 0` 成立，那么称该平衡点是 **Lyapunov 稳定** (Lyapunov stable) 的，或 Lyapunov 意义下稳定，也简称为稳定．

    如果平衡点 :math:`\eqbx` 不是 Lyapunov 稳定的，则称它是 **Lyapunov 不稳定** (Lyapunov unstable) 的．

上述定义有如下等价的 :math:`\varepsilon-\delta` 表述：

.. admonition:: 定义：Lyapunov 稳定的 ε-𝛿 表述

    对任意 :math:`\varepsilon>0` ，存在 :math:`\delta>0` 使得

    .. math::

        |\eqbx_0 - \eqbx| < \delta \implies | \varphi_t(\eqbx_0) - \eqbx |
    
    对任意 :math:`t\geq 0` 恒成立，那么称平衡点 :math:`\eqbx` 是 Lyapunov 稳定的．

从几何意义上说，平衡点的稳定是指如果粒子的初始位置距离平衡点 :math:`\eqbx` 足够近，此后它的运动轨迹也会一直保持与平衡点较近的一个距离．

下面给出渐进稳定的定义：

.. admonition:: 定义： Lyapunov 渐进稳定
   :class: def

    动力系统的平衡点 :math:`\eqbx` 如果满足以下：

    (1) 它是 Lyapunov 稳定的；
    (2) 存在  :math:`\eqbx` 的邻域 :math:`U`，使得对任意 :math:`\bx\in U` ，均有 :math:`\lim_{t\to\infty}\varphi_t(x) \to \eqbx` 成立． 

    那么称平衡点 :math:`\eqbx` 是 **Lyapunov 渐进稳定** (Lyapunov asymptotically stable) 的，简称渐进稳定的．


线性化系统与双曲平衡点
-------------------------

考虑标量动力系统，我们将动力系统右侧的函数 :math:`f(x)` 在平衡点附近作 Talyor 展开，得到：

.. math::

    f(x) = f(\bar{x} + y) = f(\bar{x}) + f'(\bar{x})y + r(y)

其中高阶微分项省略．注意到 :math:`f(\eqbx) = 0` ，在代入 :math:`y=x - \bar{x}` 后只剩下动力系统的线性形式： :math:`y_t = f'(\eqbx)y`．这个过程称为在 :math:`\bar{x}` 处的 **线性化** (linearization)． 

高维系统 :math:`\bx_t = f(\bx)` 的线性化需要计算 Jacobi 矩阵，即线性化为：

.. math::

    \frac{\ud }{\ud t} \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix}
    = A(x_1,x_,2\ldots,x_n) \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix}
    = \begin{pmatrix}
    \frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} & \cdots & \frac{\partial f_1}{\partial x_n} \\
    \frac{\partial f_2}{\partial x_1} & \frac{\partial f_2}{\partial x_2} & \cdots & \frac{\partial f_2}{\partial x_n} \\
    \vdots & \vdots &  & \vdots \\
    \frac{\partial f_n}{\partial x_1} & \frac{\partial f_n}{\partial x_2} & \cdots & \frac{\partial f_n}{\partial x_n} 
    \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix}



线性稳定性
^^^^^^^^^^^^^^

标量系统的 **线性稳定性** (linearly stability) 判断：

1. 如果 :math:`f'(\bar{x}) < 0` ，那么线性渐进稳定；
2. 如果 :math:`f'(\bar{x}) = 0` ，那么线性稳定；
3. 如果 :math:`f'(\bar{x}) > 0` ，那么线性不稳定．

对于高维系统的线性稳定性，若其线性化后在平衡点处得到常矩阵 :math:`x_t = \bA x` ，那么：

1. 如果 :math:`\bA` 的所有特征根的实部都为负，那么线性渐进稳定；
2. 如果 :math:`\bA` 的所有特征根的实部都非正，且实部为零的特征根对应的 Jordan 块是一阶的，那么线性稳定；
3. 如果 :math:`\bA` 的存在实部为正的特征根，或存在实部为零但其 Jordan 块高于一阶，那么线性不稳定．


平衡点的双曲性
^^^^^^^^^^^^^^^^^^

对于标量动力系统 :math:`x_t = f(x)` ，如果 :math:`f'(\bar{x})\neq 0` ，那么称平衡点是 **双曲** (hyperbolic) 的，或称为双曲型平衡点．

扩展到高维的情况，对于向量值动力系统的线性化形式 :math:`x_t = \bA x` ，即要求矩阵 :math:`\bA` 的所有特征根的实部均非零．

下面介绍一个由线性化系统反推原系统平衡点稳定性的结论：

.. admonition:: 线性稳定性与原稳定性的联系
   :class: def

    对于标量动力系统，如果平衡点 :math:`\bar{x}` 是双曲的，那么线性系统在  :math:`\bar{x}` 处稳定就等价于原系统渐进稳定．

    对于高维动力系统及其线性化后的 :math:`x_t = \bA x` ，如果平衡点 :math:`\eqbx` 是双曲的，那么线性系统渐进稳定等价于原系统渐进稳定、线性系统不稳定等价于原系统不稳定．


如果平衡点不是双曲的，那么不能由线性系统的稳定性推断原系统的稳定性．例如：

.. admonition:: 例子：非双曲型的平衡点
   :class: eg

    以下标量动力系统均满足 :math:`f'(\bar{x}) = 0` ，即非双曲型平衡点．

    .. math::

        (1)\quad x_t = x^3; 
        (2)\quad x_t = -x^3;
        (3)\quad x_t = x^2;
        (4)\quad x_t = x^4\sin \frac{1}{x}.
    
    以上四个动力系统线性化后均为非双曲的（也均线性稳定），而原系统的平衡性依次为：(1) 不稳定；(2) 渐进稳定；(3) 不稳定； (4) 稳定．请读者自行验证．


拓扑共轭与稳定流形*
^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: 定义：拓扑共轭
   :class: def

    动力系统如果存在同胚 (homeomorphism, 本身与逆均是连续映射的映射) :math:`h: U\to V` 使得 :math:`\varphi_t(\bx)\in U \iff \psi_t(h(\bx))\in V` 与 :math:`h\circ \varphi_t = \psi_t \circ h` ，那么称系统是 **拓扑共轭** (topological conjugate) 的．

拓扑共轭指出了在某些条件下，线性化后的系统与原系统在平衡点处的相似性，即以下定理：

.. admonition:: Hartman-Grobman 定理
   :class: def

    如果 :math:`\eqbx` 是自治系统 :math:`\bx_t = f(\bx)` 的双曲平衡点，那么在 :math:`\eqbx` 附近存在一个邻域，使得 :math:`\bx_t = f(\bx)` 与 :math:`\boldsymbol{y}_t = \mathrm{D}f(\xi)\boldsymbol{y}` 拓扑共轭．

为了指明两种系统在平衡点处稳定性的联系，我们介绍稳定流形与不稳定流形．**稳定流形** (stable manifold) :math:`W^\mathrm{s}` 是指所有正向趋向平衡点的流组成的集合，而 **不稳定流形** (unstable manifold) :math:`W^\mathrm{u}` 是指所有负向趋向平衡点的流组成的集合，即：

.. math::

    W^\mathrm{s} &= \{ \bx\in \uR^n \,:\, \varphi_t(\bx) \to \eqbx \textrm{ as } t\to \infty \},

    W^\mathrm{u} &= \{ \bx\in \uR^n \,:\, \varphi_t(\bx) \to \eqbx \textrm{ as } t\to -\infty \}




高维动力系统的稳定性
--------------------------

动力系统的不变集*
^^^^^^^^^^^^^^^^^^^^^

为了引入子空间的内容，在此介绍不变集的概念．

如果集合中的任意元素经过某种变换后，仍然属于该集合，那么这个集合称为 **不变集** (invariant set)．动力系统的研究中，不变集是值：

.. admonition:: 定义：动力系统的不变集
   :class: def

    在动力系统 :math:`\bx(t) = f(\bx)` 中，如果集合 :math:`\Lambda\subset\uR^n` 满足任意 :math:`x_0\in \Lambda` 均使得过此点的流 :math:`\varphi_t(\bx_0)` 在任意 :math:`t\in\uR` 时也都位于集合中 :math:`\varphi_t(\bx_0)` ，那么称集合 :math:`\Lambda` 为动力系统的一个不变集．

一个最简单的不变集是动力系统中一个平衡点：:math:`\Lambda = \{\eqbx\}`．此外的例子还包括周期轨线对应的流、Lorenz 吸引子．无需强调，:math:`\uR^n` 是动力系统的一个平凡的不变集．


自治线性系统与稳定性子空间
^^^^^^^^^^^^^^^^^^^^^^^^^^^

对于定常自治系统 :math:`\bx_t = \bA t, \quad \bx(0)=\bx_0` ，我们解出 :math:`x(t) = \ue^{t\bA} \bx_0` [#s1]_ ．如果 :math:`\bx_0  = \sum_{j=1}^n c_j \br_j` （其中 :math:`\br_j` 是 :math:`\bA` 的特征值 :math:`\lambda_j` 对应的特征向量），那么：

.. math::

    x(t) = \ue^{t\bA} = \sum_{j=1}^n c_j\ue^{t\bA}\br_j = \sum_{j=1}^n \ue^{t\lambda_j}c_j\br_j

我们定义特征向量可以写成复数形式 :math:`\br_j = \boldsymbol{u}_j \pm i \boldsymbol{v}_j` ，那么，我们在此给出子三个稳定线性子空间 (subspace) 的定义：

.. admonition:: 定义：稳定性子空间
   :class: def

    对于自治系统 :math:`\bx_t = \bA t, \quad \bx(0)=\bx_0` 及其平衡点原点，以下定义了三个稳定性子空间： 稳定子空间 :math:`\mathrm{E}^\mathrm{s}` 、中心子空间 :math:`E^\mathrm{sc}` 与不稳定子空间 :math:`E^\mathrm{u}` ： 
    
    .. math::

        E^\mathrm{s} = \span \{ \boldsymbol{u}_j, \boldsymbol{v_j} \,:\, \mathrm{Re}(\lambda_j) < 0 \} 

        E^\mathrm{c} = \span \{ \boldsymbol{u}_j, \boldsymbol{v_j} \,:\, \mathrm{Re}(\lambda_j) = 0 \} 

        E^\mathrm{u} = \span \{ \boldsymbol{u}_j, \boldsymbol{v_j} \,:\, \mathrm{Re}(\lambda_j) > 0 \} 

一些其他的性质：

1. 全空间 :math:`\uR^n` 是以上三个稳定性子空间的一个唯一组合 :math:`\uR^n = E^\mathrm{s} \oplus E^\mathrm{c} \oplus E^\mathrm{u}` ．

2. 如果 :math:`\bA` 非奇异 (nonsingular, 即可逆)，那么 :math:`x=0` 是唯一的平衡点．

3. 三个稳定性子空间均是原方程的不变子空间． 


非自治线性系统与基解矩阵
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

本小节考虑非定常齐次系统： :math:`\bx_t = A(t) \bx, \quad \bx(t) = \bx_0` ，其中矩阵值函数 :math:`A: \uR\to\uR^{n\times n}` 是连续的．

设基 :math:`\boldsymbol{e}_j` 是除第 :math:`j` 位为 1 外其余 :math:`n-1` 位均为 0 的向量，而 :math:`\bx_j(t)` 是初值问题 :math:`\ud \bx_j/\ud t = A(t) \bx_j, \quad \bx_j(t_0) = \boldsymbol{e}_j` 的解．那么，称它们依次为各列组成的矩阵 :math:`\bPhi(t, t_0)=[\bx_1(t), \bx_2(t), \ldots, \bx_n(t)]` 为系统的 **基解矩阵** (fundamental matrix) ． 

设初值 :math:`\bx_0` 可由基 :math:`\boldsymbol{e}_j` 表示如下： :math:`\bx_0 = \sum_{j=1}^n c_j\boldsymbol{e}_j = [c_1, c_2, \ldots, c_n]` ，因此，系统的解也可以表示为：

.. math::

    \bx(t) = \sum_{j=1}^n c_j\bx_j(t) = [\bx_1(t), \bx_2(t), \ldots, \bx_n(t)]\bx_0


基解矩阵的性质：

1. 基解矩阵可代入微分方程中，可令等式相等：

    .. math::

        \frac{\ud}{\ud t}\bPhi(t, t_0) = [(\bx_1)_t, (\bx_2)_t, \ldots, (\bx_n)_t] = A(t)[\bx_1(t), \bx_2(t), \ldots, \bx_n(t)]
        = A(t)\bPhi(t, t_0)

2. 加法群的性质：

    .. math::

        \bPhi(t ,s)\bPhi(s, r) = \bPhi(t, r)
    
    特别地，我们有： :math:`\bPhi(s, t) = \bPhi^{-1}(t, s)`，以及 :math:`\bPhi(t_0, t_0) = \bI` ．


非齐次线性系统与 Duhamel's 原理
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

考虑非齐次线性系统 :math:`\bx_t = A(t)\bx + \boldsymbol{g}(t), \quad \bx(t_0)=\bx_0` ，现在我们讨论它与其次线性系统初值问题（即 :math:`\boldsymbol{g}(t)\equiv 0` ）的解的联系．

.. admonition:: 引理

    如果可微的矩阵值函数 :math:`A(t)` 是可逆的，那么 :math:`\frac{\ud}{\ud t}A^{-1}(t) = - A^{-1}\frac{\ud A}{\ud t}A^{-1}` ．

    **证明：** 由 :math:`\frac{\ud}{\ud t} \bI = \frac{\ud}{\ud t}\left[ A(t)A^{-1}(t) \right] = 0` 得：

    .. math::

        \frac{\ud}{\ud t}\left[ A(t)A^{-1}(t) \right] = \frac{\ud A}{\ud t}A^{-1} + A\frac{\ud A^{-1}}{\ud t}, 

    证毕．

.. admonition:: 定理：Duhamel's Principle
   :class: def

    若齐次线性系统可解，那么对应的非齐次线性系统也可解．

    **证明：** 设 :math:`\bx(t)` 是非齐次线性系统的解，并让 :math:`\boldsymbol{y}(t) = \Phi^{-1}(t,t_0)\bx(t)` ，那么：

    .. math::

        \boldsymbol{y}_t &= \frac{\ud}{\ud t} \Phi^{-1}(t,t_0)\bx(t)

        &= -\frac{\ud}{\ud t}(\Phi^{-1}(t, t_0))\bx(t) + \Phi^{-1}(t, t_0)\frac{\ud}{\ud t}\bx(t)

        &= -\left(\Phi^{-1}(t, t_0)\frac{\ud}{\ud t}\Phi(t, t_0)\Phi^{-1}(t, t_0)\right)\bx(t) + \Phi^{-1}(t, t_0)(A(\bx) + \boldsymbol{g}(t)) 

        &= -\left(\Phi^{-1}(t, t_0)A(t)\Phi(t, t_0)\Phi^{-1}(t, t_0)\right)\bx(t) + \Phi^{-1}(t, t_0)A(\bx) + \Phi^{-1}(t, t_0)\boldsymbol{g}(t)

        &= \Phi^{-1}(t, t_0)\boldsymbol{g}(t)

        \therefore \boldsymbol{y}(t) &= \boldsymbol{y}_0 + \int_0^t \Phi^{-1}(s, t_0)\boldsymbol{g}(s) \ud s
    
    其中 :math:`\boldsymbol{y}_0 = \boldsymbol{y}(t_0) = \boldsymbol{x}_0` ．因而：

    .. math::

        \boldsymbol{x}(t) &= \Phi(t, t_0)\boldsymbol{y}(t) = \Phi(t, t_0)\boldsymbol{x}_0 + \Phi(t, t_0)\int_0^t \Phi(t_0, s)\boldsymbol{g}(s) \ud s

        &= \Phi(t, t_0)\boldsymbol{x}_0 + \int_0^t \Phi(t, s)\boldsymbol{g}(s) \ud s. 

.. rubric:: 注释

.. [#s1] 关于矩阵参与的指数运算 :math:`\ue^{t\bA}` ，如有疑问，请参考附录内容．

