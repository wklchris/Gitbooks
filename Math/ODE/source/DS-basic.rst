动力系统基础
=================

从此处，开始本笔记的第二部分，主要讲述动力系统的内容．


动力系统引言
-----------------

在此不讨论动力系统是否有严格数学意义上的定义．用描述性定义叙述，**动力系统** (dynamic system) 就是点 :math:`\bx` 与其允许运动的空间 :math:`X` 组成的随时间 :math:`t` 变化的系统．结合本笔记第一部分微分方程的概念，任何 **自治** (autonomous) 微分方程

.. math::
   :label: ds-def
   
   \frac{\ud \bx}{\ud t} = \boldsymbol{v}(\bx)

都可以视作一个动力系统．值得注意的是，此处用数学黑体 :math:`\bx` 表示质点的位置是一个 :math:`n` 维向量，且上式右侧的速度函数 :math:`\boldsymbol{v}` 是一个向量值函数．

在现实世界的例子中，质点位置用三维向量标定，即 :math:`n=3`；质点运动的空间通常可以定义为整个三维空间，即 :math:`X=\uR^3`．那么，微分方程 :eq:`ds-def` 可以写作：

.. math::
   
   \frac{\ud }{\ud t}\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} v_1(x) \\ v_2(y) \\ v_3(z) \end{pmatrix}

质点运动空间可以是任何合理的流形；关于流形的概念，请参考选读的 :ref:`toc-manifold` 一节．


连续动力系统
^^^^^^^^^^^^^^^^^

本笔记中主要讨论的动力系统都是连续的情形．更通常地，考虑 :math:`n` 维的一阶自治系统：

.. math::
    
    \frac{\ud \bx}{\ud t} = \boldsymbol{f}(\bx), \quad \bx(t): I\subseteq\uR \to \uR^n

若无特殊说明，其具有 :math:`t=t_0` 时刻的初值条件：

.. math::

    \bx(t_0) = \bx_0

该微分方程与初值条件构成的初值问题的解：:math:`\bx(t) = \varphi(t, t_0, x_0)` （有时也简记为 :math:`\varphi_t(x_0)`，原因见 :ref:`toc-ds-properties` 一节的性质 1） ，实质上也是吻合方向场的积分曲线；而不含初值条件的微分方程（或对应的方向场）的一族解（或吻合的积分曲线），称为 **流** (flow)，或称流图 (flow map)．从几何意义上解释，该初值问题的流描述了质点在 :math:`t_0` 时刻经过坐标 :math:`\bx_0` 的运动．


离散动力系统*
^^^^^^^^^^^^^^^^

离散动力系统不是本笔记的重点，在此只做简要介绍．

为与连续动力系统区分，我们用大写 :math:`\boldsymbol{F}` 来表示动力系统右侧的函数：

.. math::

    \bx_{n+1} = \boldsymbol{F}(\bx_n), \quad \boldsymbol{F}: X\to X

此时，动力系统的质点轨迹是一系列离散的点．如果 :math:`\boldsymbol{F}` 可逆，我们可以由后续的点倒推之前的点位置．


.. _toc-ds-properties:

动力系统的基本性质
^^^^^^^^^^^^^^^^^^^^^

下面给出动力系统 :eq:`ds-def` 的几个基本性质：

1. **积分曲线平移不变性** ：系统的积分曲线在增广相空间中沿 :math:`t` 轴平移后，仍然是该系统的积分曲线．这一点由自治系统的平移性可以获知：若 :math:`\bx=\varphi(t)` 是自治系统的一个解，那么对任意常数 :math:`C` 都有 :math:`\bx=\varphi(t+C)` 也是该自治系统的解．

    由此性质可知，自治微分方程的解 :math:`\varphi(t,t_0,x_0)` 的一个平移 :math:`\varphi(t-t_0,0,x_0)` 也是原方程的解；又知它们满足同样的初值条件，因此它们恒等．因此在解族中只需考虑初始时刻 :math:`t_0=0` 的解，通常可简记为 :math:`\varphi_t(\bx_0)` [#f1]_ 或者 :math:`\varphi(t, \bx_0)`：

    .. math::

        \varphi_t(\bx_0) = \varphi(t, \bx_0) \overset{\textrm{def}}{=} \varphi(t, 0, \bx_0)

#. **过相空间每一点轨线的唯一性** ：轨线的存在性显然．唯一性证明如下：

    假设相空间的点 :math:`\bx` 附近有两条轨线段 :math:`\ell_1,\ell_2` 均通过该点，那么必有两条不同的积分曲线段 :math:`\Gamma_1,\Gamma_2` (它们可以属于同一条积分曲线)在相空间中的投影分别是 :math:`\ell_1,\ell_2`．设这两条积分曲线段上分别在时刻 :math:`t_1,t_2` 的位置投影到相空间为 :math:`\bx`，将 :math:`\Gamma_1` 平移 :math:`t_2-t_1` 后得到新的积分曲线 :math:`\Gamma_3`，它与 :math:`\Gamma_2` 相交．由解的唯一性，:math:`\Gamma_3` 与 :math:`\Gamma_2` 重合．因此，它们在相空间点 :math:`\bx` 附近有相同的投影，这进一步推出 :math:`\Gamma_1` 与 :math:`\Gamma_2` 在相空间此点附近有相同的投影，这与假设相悖．唯一性证毕．

#. **加法群的性质** ：动力系统的解 :math:`\varphi(t, \bx_0)` 满足

    .. math::
    
        \varphi(t_2, \varphi(t_1, \bx_0)) = \varphi(t_1+t_2, \bx_0)

    或用集合的语言描述，单参数变换集合 :math:`S = \{ \varphi_t \,|\, t\in\uR \}` 是一个复合运算下的加法群，即：

    .. math::

        \varphi_s\circ \varphi_t = \varphi_{s+t}

    其中 :math:`\circ` 是复合运算符，上式亦即： :math:`\varphi_s(\varphi_t(\bx)) = \varphi_{s+t}(\bx),\ \bx\in\uR^n`．

    该性质的等价的几何意义描述是：在相空间中，如果从 :math:`\bx_0` 出发的运动经过 :math:`t_1` 时间到达 :math:`\bx_1=\varphi(t_1, \bx_0)`，此后再经过 :math:`t_2` 时间又到达 :math:`\bx_2=\varphi(t_2, \bx_1)`．那么，从 :math:`\bx_0` 出发的运动经过 :math:`t_1+t_2` 时间也到达 :math:`\bx_2`．

    该性质由性质 1 容易证得：:math:`\varphi(t+t_1,\bx_0)` 是系统的解，它与另一个解 :math:`\varphi(t,\varphi(t_1,\bx_0))` 在 :math:`t=0` 处的初值均为 :math:`\varphi(t_1,\bx_0)`，因此它们恒等．将恒等式两侧的 :math:`t` 取特殊值 :math:`t_2`，即可证得性质 3.


动力系统的简化手段
^^^^^^^^^^^^^^^^^^^^^

动力系统通常的简化目的有以下两个，一般都通过引入新的变量来实现．

1. **将高阶微分方程变换为一阶微分方程**
#. **将非自治方程变换为自治方程**

.. admonition:: 例子：动力系统的简化
   :class: eg

    (1) 将非自治系统 :math:`x_t=f(x,t)` 变换为自治系统．

    引入变量 :math:`s=t`，那么：:math:`\begin{cases} x_t &= f(x,s) \\ s_t &= 1 \end{cases}`．

    (2) 将二阶、非自治方程 :math:`x_{tt} + (1+\epsilon\cos t)x = 0` 变换为一阶自治的（:math:`\epsilon` 为常数）．

    引入变量 :math:`y=x_t, z=t`，那么：:math:`\begin{cases}x_t &= y \\ y_t &= -(1+\epsilon\cos z)x \\ z_t &= 1\end{cases}`．


动力系统的几何概念
^^^^^^^^^^^^^^^^^^^^^^

通常，我们将系统中质点 :math:`\bx` 取值的空间 :math:`I\subseteq \uR^n` 称为 **相空间** (phase space)，而将 :math:`(t,\bx)` 取值的空间称为 **增广相空间** (extended phase space)．特别地，将一维运动背景的相空间称为相线 (phase line)，将二维运动背景的相空间称为相平面 (phase plane)．

在相空间中，动力系统方程 :eq:`ds-def` 右侧的函数 :math:`\boldsymbol{v}(\bx)` 定义了一个向量场．微分方程的解 *在相空间中* 对应的、与向量场吻合的光滑曲线，被称为 **轨线** (orbit)．需要指明， **积分曲线是位于增广相空间的，而轨线实质是其沿**  :math:`t` **轴向相空间的投影** ．

作图时，我们通常用箭头标出轨线随时间 :math:`t` 增大时质点的运动方向．

动力系统有两个重要的情形：

1. **平衡点** (equilibrium)：也称微分方程的奇点 (singular point)．指动力系统的流 :math:`\varphi_t(\bar{\bx})` 的不动点 (fixed point)： 
    
    .. math::

        \varphi_t(\bar{\bx}) = \bar{\bx}
    
    将上式代入方程 :eq:`ds-def` 中，可以发现它是方程右侧函数的零点： :math:`f(\bar{\bx})=\boldsymbol{0}`．平衡点的几何性质会在下文讨论．

2. 周期解 (periodic solution)：即存在 :math:`T>0` 使得 :math:`\bx(t+T) = \bx(t)`．那么随着 :math:`t\to \infty`，质点在轨线上作周而复始的运动．此时相空间中的轨线是闭合的曲线，称为闭轨 (closed orbit)． 

最后，我们指出，动力系统的研究主要侧重于流与质点轨迹的全局特性，例如稳定性 (stability)、周期性 (periodicity)、混沌 (chaos) 理论，以及分支 (bifurcation) 理论．其中，上述奇点与闭轨的分析是基础的定性分析问题．


量纲分析
^^^^^^^^^^^^^

量纲分析 (dimensional analysis) 是在实际建立动力系统模型时常用的手段．通过对参数与变量的量纲的分析，将变量乘上某些参数的组合，使其变为一个无量纲的（即量纲为 1）的新的变量，由此列出新的微分方程，这一过程就称为 **无量纲化** (non-/de- dimensionalizition)．我们用一个例子来说明这一点：

.. admonition:: 例子：无量纲化

    假设某种群数量 :math:`x \geq 0` 随时间 :math:`t` 变化的 Logistic 模型：

    .. math::

        x_t = \mu\left( 1 - \frac{x}{k} \right)x, \quad x(0) = x_0

    其中参数 :math:`\mu, k > 0` 均为常数．请列出无量纲化后的初值问题．

    **解：** 设种群数量的单位为 :math:`P` ，时间的单位为 :math:`T` ，那么微分方程中的两个变量 :math:`x, t` 分别具有单位 :math:`[x] = P, [t] = T` ．参数 :math:`k` 与变量 :math:`x` 相除后可与常数 1 作减法，因此其单位是 :math:`[k] = P` ；微分方程左侧的单位是随时间种群变化，即 :math:`P/T` ，由此可以推知 :math:`[\mu]=1/T` ．

    那么，无量纲化后的新变量可以取：:math:`\tilde{x}=x/k, \, \tilde{t}=\mu t` ，得到变换后的初值问题：

    .. math::

        x_t = x(1-x), \quad x(0) = \frac{x_0}{k}.

.. _toc-manifold:

流形*
^^^^^^^^

实际上，除了常规的 :math:`n` 维空间，质点运动空间 :math:`X` 也可以是其他 **流形** (manifold)．因此，有必要对流形这一概念做扼要的介绍．

简而言之，流形是指每点局部均近似于欧几里得空间的拓扑空间．这样说可能仍显抽象，但可以考虑地球表面作为例子：在近地点，局部的地球表面可以近似视为一个二维平面（尽管在实际上它是三维曲面），并且用二维坐标系就能标定该局面表面每个点的位置．因此，实际在三维曲面上运动的地球表面的质点，在此背景下却可以（局部地）视为二维流形，并用二维的动力系统进行描述．

虽然在此不深入探讨流形的严格定义，但为了更好地理解流形这一概念，在此介绍一个简单的流形作为例子：

.. admonition:: 例子：作为流形的圆
   :class: eg
   
    圆是一个简单的流形例子 |wiki-circle|_ ．考虑一个二维空间的单位圆 :math:`\mathbb{T}: x^2+y^2=1`．从局部观察，圆近似一条（曲）线段；而线段是一维对象．因此，我们可以用一维坐标来（局部地）描述圆．比如，在该圆位于 :math:`x` 轴上方的这一局部（即上半圆弧 :math:`\mathbb{T}_+`），我们可以该圆弧上的任意一点均可用其横坐标来唯一确定．即存在映射：

    .. math::
      
        f: (x, y) \to x, \quad (x,y)\in\mathbb{T}_+
   
    相应地，也存在逆映射：

    .. math::
      
        f^{-1}: x \to (x,\sqrt{1-x^2}), \quad x\in [-1,1]
    
    这样的映射 :math:`f` 称为流形 :math:`\mathbb{T}` 的一个 **坐标图** (coordinate chart)．将多个坐标图联合起来，可以确定流形上每个点，称这些坐标图为一个 **图册** (atlas)．显然，一个流形可以有多个图册．
    
    一个有趣的信息：该例的圆 :math:`\mathbb{T}` 的任何图册都包含不止一个坐标图（即不存在覆盖全圆的单一坐标图）．

流形的其他性质：

* 流形不必连通 (connected)，比如两个无交点的圆．
* 流形不必闭合 (closed)，比如一条两侧端点被挖去的线段．
* 流形不必有限 (finite)，比如一组双曲线．


动力系统的经典范例
======================

上文已经提到，从几何意义上说，动力系统描述了质点的运动．现在给出一些典型的物理学的例子，帮助读者更好地理解动力系统．虽然本章只有几个例子，但例中也给出了一些概念并温习了某些变换方程的基本手段，请读者耐心阅读．

.. _toc-newton-ds:

牛顿力学系统与守恒
------------------------

牛顿力学系统的通常微分描述是利用牛顿第二定律．下面是一个例子：

.. admonition:: 例子：宏观质点的运动
   :class: eg

    假设质量为 :math:`m` 的质点 :math:`\boldsymbol{q}=(q_1,q_2,\ldots,q_n)` 在 :math:`\uR^n` 空间运动，且在空间上任一点 :math:`\bx` 处该质点的受力为 :math:`\boldsymbol{F}(\boldsymbol{q})`．

    那么，由牛顿第二定律，我们得到自治微分方程：:math:`m\ddot{\boldsymbol{q}} = \boldsymbol{F}(\boldsymbol{q})`，其中点号表示对时间 :math:`t` 的微分．

    为了将上式化为一阶，引入新的变量 :math:`\boldsymbol{p}=m\dot{\boldsymbol{q}}` ，得到：

    .. math::

        \frac{\ud }{\ud t}\begin{pmatrix} \boldsymbol{q} \\ \boldsymbol{p} \end{pmatrix} = \begin{pmatrix} \dot{\boldsymbol{p}}/m \\ \boldsymbol{F}(\boldsymbol{q}) \end{pmatrix}
    
    注意到在以上换元中，变量 :math:`\boldsymbol{p}` 也具有实际的物理意义，即 **动量** (momentum)．


如果该力是保守力 [#f2]_ (conservative force)，即该系统是一个 **守恒系统** (conservative system)，或称保守系统．那么，由能量守恒定律，该力所做的功即为终点 **势能** (potential energy) 减去起点势能．将 :math:`\boldsymbol{q}` 处的势能记为 :math:`V(\boldsymbol{q})`，并将势能之差微分，那么有：

.. math::

    F = -\frac{\partial V}{\partial \boldsymbol{q}}

其中 :math:`\frac{\partial }{\partial \boldsymbol{q}}` 即为梯度算子 :math:`\nabla_{\boldsymbol{q}} = \left(\frac{\partial}{\partial q_1}, \frac{\partial}{\partial q_2}, \dots, \frac{\partial}{\partial q_n}\right)`．

关于守恒系统，我们在 :ref:`toc-conservative` 一节详细讨论．

.. _toc-hamiltonian:

哈密尔顿系统
-----------------

**哈密尔顿系统** (Hamiltonian system)，或译为哈密顿系统，其严格定义十分繁琐．简言之，哈密尔顿系统是一个由常量函数 :math:`H(\boldsymbol{q}, \boldsymbol{p}, t)` （称为哈密顿量）完整描述的动力系统．为了方便理解，此处给出一个简化定义：

.. admonition:: 简化定义：哈密尔顿系统
   :class: def

    假设粒子在 :math:`\uR^n` 中运动．哈密尔顿系统的状态用 :math:`\boldsymbol{r} = (\boldsymbol{q}, \boldsymbol{p})` 来表示，其中 :math:`\boldsymbol{p}\in\uR^n` 表示粒子的动量，而 :math:`\boldsymbol{q}\in\uR^n` 表示例子的位置．那么，哈密尔顿系统可以用以下状态演变方程描述：

    .. math::

        \frac{\ud \boldsymbol{p}}{\ud t} &= -\frac{\partial H}{\partial \boldsymbol{q}}

        \frac{\ud \boldsymbol{q}}{\ud t} &= \frac{\partial H}{\partial \boldsymbol{p}}

    而状态 :math:`\boldsymbol{r}(t)=(\boldsymbol{q}(t), \boldsymbol{p}(t))` 就是以上微分方程对应的初值问题的解．

哈密尔顿系统具有的性质是哈密尔顿量守恒，即对任意状态解 :math:`(\boldsymbol{q}(t), \boldsymbol{p}(t))`，哈密尔顿量在粒子的运动过程中始终是常量．这点容易验证：

.. math::

    \frac{\ud H(\boldsymbol{q}(t), \boldsymbol{p}(t))}{\ud t} = \frac{\partial H}{\partial \boldsymbol{q}}\frac{\partial \boldsymbol{q}}{\partial t} + \frac{\partial H}{\partial \boldsymbol{p}}\frac{\partial \boldsymbol{p}}{\partial t} = \frac{\partial H}{\partial \boldsymbol{q}}\frac{\partial H}{\partial \boldsymbol{p}} - \frac{\partial H}{\partial \boldsymbol{p}}\frac{\partial H}{\partial \boldsymbol{q}} = 0.


梯度系统
---------------

在 :ref:`toc-newton-ds` 一节中，我们介绍了势能的概念．针对物理学中的重力势能，我们可以用微分方程从数学上类似地描绘梯度系统．

特别指明，梯度系统也是一种守恒系统．

.. admonition:: 简化定义：梯度系统
   :class: def

    记在 :math:`\bx` 处质点的势能为标量 :math:`V(\bx)`，那么 **梯度系统** (gradient system) 可以由下式描述：

    .. math::

        \frac{\ud \bx}{\ud t} = - \frac{\partial V}{\partial \bx}


梯度系统的性质
^^^^^^^^^^^^^^^^^^^^

1. **势能** :math:`V` **随着时间** :math:`t` **而不增**，即

    .. math::

        \frac{\ud}{\ud t}V(\bx(t)) = \frac{\partial V}{\partial \bx}\frac{\ud \bx}{\ud t} = -\frac{\partial V}{\partial \bx}\frac{\partial V}{\partial \bx} = -\left\|\frac{\partial V}{\partial \bx}\right\|^2 \leq 0.

2. **梯度系统中（除平衡点处的）轨线总是与势能** :math:`V` **的水平面 (level surface)** :math:`V(\bx) = C` **（其中** :math:`C` **为常数）垂直，并指向** :math:`V` **减少的方向**．

    注意到 :math:`\frac{\partial V}{\partial \bx}` 实质上是 :math:`V` 的梯度，指向 :math:`V` 增长最快的质点运动方向．回到原微分方程，可知重力系统的轨线 :math:`\bx(t)` 随时间变化总是指向 :math:`V` 下降最快的方向，即相图中轨线总是垂直于曲线簇 :math:`V(\bx)=C`．


梯度系统的判定
^^^^^^^^^^^^^^^^^^^^

.. admonition:: 梯度系统的判定方法
   :class: def

    动力系统 :math:`\bx_t = \boldsymbol{F}(\bx) = (F_1(\bx), F_2(\bx), \ldots, F_n(\bx))` 当且仅当存在一个势能函数 :math:`V: \uR^n\to\uR` 使得下式成立：

    .. math::

        \boldsymbol{F}(\bx) = -\left(\frac{\partial }{\partial x_1}, \frac{\partial }{\partial x_2}, \ldots, \frac{\partial }{\partial x_n}\right)V

    或写为： :math:`F_i(x_1,x_2,\ldots,x_n) = -\frac{\partial V}{\partial x_i},\quad \forall i=1,2,\ldots,n` ．
   
特别地，以上判定条件在 :math:`n=1` 时，即： :math:`F(x) = -V'(x)`；在 :math:`n=2` 时，即： 

.. math::

    F_1(x, y) = -\frac{\partial V(x, y)}{\partial x}

    F_2(x, y) = -\frac{\partial V(x, y)}{\partial y}

或者在二阶偏导数连续的条件下写成下式，这点由克莱罗 (Clairaut) 定理易知 :math:`\partial^2 V / (\partial x \partial y) = \partial^2 V / (\partial y \partial x)`：

.. math::

    \frac{\partial F_1}{\partial y} = \frac{\partial F_2}{\partial x}


下面是几个梯度系统判定的例子：

.. admonition:: 例子：梯度系统的判定
   :class: eg

    判断以下动力系统是否是梯度系统；若是，求出它们的势能函数形式．

    .. math::

        (1) \begin{cases} x_t = xy \\ y_t = x^2+y^2 \end{cases}; \quad
        (2) \begin{cases} x_t = 2xy \\ y_t = x^2 + y^2 \end{cases}.

    **解：** 方程 (1) 有：:math:`\frac{\partial}{\partial y}(xy) = x, \frac{\partial}{\partial x}(x^2+y^2) = 2x`，二者不恒等，因此不是梯度系统．

    方程 (2) 可由类似的方法判定出是梯度系统．那么有：

    .. math::

        \frac{\partial V}{\partial x} = - 2xy, \quad \frac{\partial V}{\partial y} = -(x^2 + y^2)
    
    对左右两式求原函数，得：

    .. math::

        V(x, y) = -x^2 y + F(y) = -x^2 y - \frac{1}{3}y^3 + G(x)

    由此解出势能函数： :math:`V(x,y) = -x^2 y - \frac{1}{3} y^3 + C` ，其中 :math:`C` 是任意常数．


梯度系统的相图绘制*
^^^^^^^^^^^^^^^^^^^^^^^^

通用的相图绘制技巧，可以参考后文的内容．这里举一个梯度系统相图绘制的例子：

.. admonition:: 例子：梯度系统的相图绘制
   :class: eg

    …… 施工中 ……


.. _toc-conservative:

守恒系统
---------------

**守恒系统** (conservative system) 是重力系统中的重要内容．但由于其形式相比以上系统更复杂（存在二阶微分），因此在介绍上述系统后才于此处介绍守恒系统．上文提到的梯度系统就是一种守恒系统．


守恒系统的相图
^^^^^^^^^^^^^^^^^^^^^^

守恒系统的相图绘制我们在 :ref:`toc-conservative-phase` 一节着重进行讲解，这里给出一个示例，展示其相图的形式：

.. admonition:: 例子：守恒系统的相图
   :class: eg

    守恒系统 :math:`x_{tt} + x^2 - x = 0` 可以通过换元法 :math:`y=x_t` 降阶：

    .. math::

        \begin{dcases}
        \frac{\ud x}{\ud t} = y \\
        \frac{\ud y}{\ud t} = -\frac{1}{2}x^2 + x
        \end{dcases}

    下图画出了 :math:`(x, y)` （亦即 :math:`(x, x_t)` ）平面上，上述守恒系统的相图 [#f4]_ ．

    .. plot:: _static/img/conservative-system.py
       :align: center

    该系统有两个平衡点，即 :math:`(0,0), (1,0)` ．前者是鞍点，后者是中心点．


洛伦茨系统*
----------------

**洛伦茨系统** (Lorenz system) 由数学与气象学家 Edward Lorenz [#f3]_ 提出，是指具有以下形式的动力系统：

.. math::

    \begin{cases}
    x_t &= \sigma (y-x) \\
    y_t &= rx - y - xz \\
    z_t &= xy - bz 
    \end{cases}

其中，参数 :math:`\sigma, r, b` 均为常量．其相图是混沌理论中著名的洛伦茨蝴蝶 (Lorenz butterfly)，在此引用 `Matplotlib 绘图示例 <https://matplotlib.org/gallery/mplot3d/lorenz_attractor.html>`_：

.. plot:: _static/img/Lorenz-butterfly.py
    :align: center

它一个更正式的名称是洛伦茨吸引子 (Lorenz attractor)．

.. rubric:: 注释

.. [#f1] 这里 :math:`\varphi_t(\bx)` 的下标 :math:`t` 表示含参，而非对 :math:`t` 求导．
.. [#f2] 保守力 (conservative force)，又称守恒力．在物理学上，如果作用于质点的力，在质点从起点运动到终点的过程中做的功与质点运动路径无关，则称该力为保守力．例如，重力是保守力，而摩擦力却不是．
.. [#f3] 爱德华·洛伦茨 Edward Norton Lorenz (1917-2008)，美国数学与气象学家，混沌理论的奠基人．注意，他与荷兰物理学家、电磁学上洛伦兹力的提出者亨德里克·洛伦兹 Hendrik Antoon Lorentz (1853-1928) 并非同一个人；两人的姓氏拼写也并不相同．
.. [#f4] 本处绘图的代码使用的包 ode_toolkit 是作者自己编写使用的，因此读者直接复制是无法复现代码的．如有兴趣，可以参考附录以了解如何使用该包．

.. 链接

.. |wiki-circle| replace:: :superscript:`[source]`
.. _wiki-circle: https://en.wikipedia.org/wiki/Manifold#Circle
