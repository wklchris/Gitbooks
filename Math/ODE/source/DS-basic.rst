动力系统基础
=================

从此处，开始本笔记的第二部分，主要讲述动力系统的内容．


动力系统引言
-----------------

在此不讨论动力系统是否有严格数学意义上的定义．用描述性定义叙述，**动力系统** (dynamic system) 就是点 :math:`\bx` 与其允许运动的空间 :math:`X` 组成的随时间 :math:`t` 变化的系统．结合本笔记第一部分微分方程的概念，任何 **自治** 微分方程

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

.. _toc-manifold:

流形*
^^^^^^^^

实际上，除了常规的 :math:`n` 维空间，质点运动空间 :math:`X` 也可以是其他 **流形** (manifold)．因此，有必要对流形这一概念做扼要的介绍．

简而言之，流形是指每点局部均近似于欧几里得空间的拓扑空间．这样说可能仍显抽象，但可以考虑地球表面作为例子：在近地点，局部的地球表面可以近似视为一个二维平面（尽管在实际上它是三维曲面），并且用二维坐标系就能标定该局面表面每个点的位置．因此，实际在三维曲面上运动的地球表面的质点，在此背景下却可以（局部地）视为二维流形，并用二维的动力系统进行描述．

虽然在此不深入探讨流形的严格定义，但为了更好地理解流形这一概念，在此介绍一个简单的流形作为例子：

.. admonition:: 例子：作为流形的圆
   :class: def
   
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


.. rubric:: 注释

.. [#f1] 这里 :math:`\varphi_t(\bx)` 的下标 :math:`t` 表示含参，而非对 :math:`t` 求导．

.. 链接

.. |wiki-circle| replace:: :superscript:`[source]`
.. _wiki-circle: https://en.wikipedia.org/wiki/Manifold#Circle
