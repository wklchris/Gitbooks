动力系统解的存在与唯一性
=============================

本章引言
------------

回忆之前的内容，我们介绍过皮卡定理 (Picard theorem) 与皮阿诺定理 (Peano theorem) 在标量微分方程上的应用：前者对应解的唯一性，后者对应解的存在性．

通过几个例子来说明这一点：

.. admonition:: 例子：标量常系数线性系统
   :class: eg
   
    考虑标量的常系数线性自治系统的初值问题：

    .. math::

        \begin{cases}
        x_t = ax \\
        x(0) = x_0
        \end{cases}

    **解：** 容易解出：:math:`x(t) = x_0\ue^{at}` ，并得到流： :math:`\varphi_t(x) = x\ue^{at}`．此时解在 :math:`t\in\uR` 上是存在且唯一的．

.. admonition:: 例子：标量常系数非线性系统
   :class: eg
   
    考虑标量的常系数非线性自治系统的初值问题．特别地，此例中的函数 :math:`f(x)` 连续但并非处处可微．

    .. math::

        \begin{cases}
        x_t = |x|^{\frac{1}{2}} \\
        x(0) = x_0
        \end{cases}

    **解：** 考虑 :math:`x(t) > 0` 时的解，有：

    .. math::

        \int \frac{\ud x}{\sqrt{x}} = \int \ud t \implies x(t) = \frac{1}{4}(t+C)^2

    代入 :math:`t=0` 时的初值条件，得到： :math:`C=2\sqrt{x_0}` ．于是得到初值为正时的解：

    .. math::

        x(t) = \frac{1}{4}(t+2\sqrt{x_0})^2, \quad (x_0 > 0)

    类似我们可以考虑 :math:`x(t) < 0` 的情况．

    特别地，我们考虑 :math:`x_0 = 0` 的情况，上式即： :math:`x(t) = \frac{1}{4}t^2 \, (t>0)` ，容易验证这是方程的解．但注意到，:math:`x(t) = 0` 也是方程的解，因此方程的解不是唯一的．

    在 :math:`t<0` 时，以上解可以向负向延伸为 :math:`x(t) = 0` 或者 :math:`-\frac{1}{4}t^2` ．因此，该方程在 :math:`x_0=0` 时的一个解可以写作：

    .. math::

        x(t) = \begin{cases}
        \frac{1}{4}t^2, & t\geq 0 \\
        0, & t < 0.
        \end{cases}
    
    由自治系统的沿 :math:`t` 轴平移性，我们知道以下形式的任意 :math:`t_0\geq 0` 均为原方程在 :math:`x_0 = 0` 时的解：

    .. math::

        x(t) = \begin{cases}
        \frac{1}{4}(t - t_0)^2, & t\geq t_0 \\
        0, & t < t_0.
        \end{cases}
    
    该动力系统解的不唯一是因为方向场函数 :math:`|x|^{\frac{1}{2}}` 虽然连续但在 :math:`x=0` 处并不可导（或者从 Picard 定理的角度阐述，它在此处不是 Lipschitz 的）．如果方向场是光滑的，则无此问题．


解的存在性与唯一性
--------------------------------

解的存在性利用 Picard 定理进行判断、唯一性则利用 Peano 定理进行判断，这些与我们在 :ref:`toc-unique-and-exist` 一章讨论的内容相似，不过在自治系统中就省去对 :math:`t` Lipschitz 的讨论．
