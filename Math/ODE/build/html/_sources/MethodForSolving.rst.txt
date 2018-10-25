初等积分法
==============

本章介绍基础微分方程的解法．通过初等函数的有限次积分的表达式来求解微分方程的方法，统称为初等积分法．虽然刘维尔 (Liouville) 已在 1841 年证明了绝大多数的微分方程不能用初等积分法求解，但这类求解法仍然是学习微分方程基础与解决实际微分问题中要求的知识．


全微分方程（恰当方程）
----------------------

首先，我们介绍最易于求解的一类微分方程：

.. admonition:: 定义：全微分方程
   :class: def

    对一阶微分方程

    .. math::
       :label: symmetric-ode
        
        P(x, y)\ud x + Q(x, y)\ud y = 0,

    如果存在一个可微函数 :math:`\Phi(x,y)`，使得其全微分满足下式 [#f3]_

    .. math::

        \ud \Phi(x, y) = P(x, y)\ud x + Q(x, y)\ud y
    
    则称式 :eq:`symmetric-ode` 为 **全微分方程** (total differential equation)，也称恰当方程 (exact equation)．

由定义中的函数 :math:`\Phi(x, y)` 所确定的式 :math:`\Phi(x,y)=C`（或其对应的隐函数 :math:`y=u(x)`）显然就是微分方程的通解；这点由对等式两侧积分就可简单得到．


.. admonition:: 例子：全微分方程
   :class: eg

    求解微分方程： :math:`xy^2\ud x + x^2y\ud y = 0`．

    观察左侧的式的形式，我们可以令 :math:`\Phi(x,y) = \frac{1}{2}x^2y^2`，那么：

    .. math::

        \frac{\partial \Phi}{\partial x} = xy^2, \quad \frac{\partial \Phi}{\partial y} = x^2y.

    因此，原方程的左侧可以写作全微分的形式，再对等号两端积分：

    .. math::

        LHS = \ud \Phi(x,y) = RHS = 0 \implies x^2y^2 = C

    其中 :math:`C` 是任意常数．此即该微分方程的通解．


通过观察形式的方式判断一个微分方程是否是全微分方程，显然不是可靠的方式．这里我们介绍一个定理来判定全微分方程：

.. admonition:: 定理：全微分方程的判定充要条件
   :class: theorm

    设函数 :math:`P(x, y)` 与 :math:`Q(x,y)` 在区域 :math:`G: [\alpha, \beta]\times [\gamma, \delta] \subseteq \uR^2` 上连续，且有连续的偏导数 :math:`\frac{\partial P}{\partial y}` 与 :math:`\frac{\partial Q}{\partial x}`，那么微分方程 :eq:`symmetric-ode` 是全微分方程的充要条件是

    .. math::

        \frac{\partial P}{\partial y} \equiv \frac{\partial Q}{\partial x}

    在区域 G 上恒成立．

    【证】必要性可由偏导连续性和混合偏导数的连续性可直接证得．下证充分性．为满足 :math:`\frac{\partial \Phi}{\partial x} = P`，我们构造一个下述的函数 :math:`\Phi(x, y) = \int_{x_0}^x P(x,y)\ud x + \psi(y)`，其中函数 :math:`\psi(y)` 是待由 :math:`\frac{\partial \Phi}{\partial y} = Q` 确定的一个函数．代入此式中，得：

    .. math::
       
        \frac{\partial \Phi}{\partial y} = \frac{\partial}{\partial y} \int_{x_0}^x P(x,y)\ud x + \psi(y) = \int_{x_0}^x \frac{\partial}{\partial y}P(x, y)\ud y + \psi'(y)
    
    由给定恒等式得：

    .. math::
        
        \frac{\partial \Phi}{\partial y} = \int_{x_0}^x \frac{\partial}{\partial x}Q(x, y)\ud x + \psi'(y) = Q(x,y) - Q(x_0, y) + \psi'(y)
    
    因此，只需取 :math:`\psi'(y) = Q(x_0,y)` 即可．将其积分，然后代入到之前的表达式中：

    .. math::
        
        \Phi(x, y) = \int_{x_0}^x P(x,y)\ud x + \int_{y_0}^y Q(x_0, y)\ud y.
    
    如果在构造 :math:`\Phi(x,y)` 时先满足 :math:`\frac{\partial \Phi}{\partial y} = Q`，那么将得到：

    .. math::

        \Phi(x, y) = \int_{x_0}^x P(x,y_0)\ud x + \int_{y_0}^y Q(x, y)\ud y. \quad\qedsymbol


.. rubric:: 注释

.. [#f3] 全微分满足该式，等价于其偏微分满足：
    
    .. math::

        \frac{\partial \Phi}{\partial x} = P(x, y),\quad  \frac{\partial \Phi}{\partial y} = Q(x, y)