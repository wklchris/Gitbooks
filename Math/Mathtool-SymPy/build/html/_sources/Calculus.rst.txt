微积分与极限
================

符号计算自然不能少了微积分的内容．

.. ipython:: python

    from sympy import *

导数
--------

函数的导数使用 :code:`diff(expr, var1, [order1,] var2, [order2], ... )` 或 :code:`f.diff(...)` 来求得．其中，如果导数是一阶的，那么 :code:`order` 参数可以省略．

下例分别求出了 :math:`\partial f/\partial x` 与 :math:`\partial^3 f/(\partial x^2 \partial y)` ：

.. ipython:: python

    x, y = symbols('x y')
    f = x**4 + 3 * x ** 2 * y ** 2 + y**4
    diff(f, x)
    f
    f.diff(x, 2, y)
    f

以上两种调用 :code:`diff` 的方式并无差别．


积分
----------

不定积分，例如 :math:`\int \ue^{-x} \ud x` 的计算：

.. ipython:: python

    integrate(exp(-x), x)

定积分的计算只需要将第二参数换成一个元组 :code:`(var, lower_limit, upper_limit)` 即可，比如 :math:`\int_0^\infty \ue^{-x} \ud x` ：

.. ipython:: python

    integrate(exp(-x), (x, 0, oo))

多重积分，比如 :math:`\int_{-\infty}^\infty \int_{-\infty}^\infty \ue^{-x^2-y^2} \ud x\ud y` ：

.. ipython:: python

    integrate(exp(-x**2 - y**2), (x, -oo, oo), (y, -oo, oo))


极限
---------

用 :code:`limit(func, var, point, direction)` 来计算极限，其中第四参数省略时表示双侧（即通常意义上的）极限，用 :code:`+/-` 表示从正向/负向接近的一侧的极限：

.. ipython:: python

    limit(sin(x)/x, x, 0)
    limit(1/x, x, 0, '+')
    limit(-1/x, x, 0)


高阶项与 Taylor 展开
-----------------------

高阶项在 SymPy 中可以直接用 :code:`O(var**k)` 的形式 [#f1]_ 写入表达式中，表示在变量趋向无穷时式中等于或高于 k 阶的项（因此，这些项的形式与系数在式中不再详细给出）：

.. ipython:: python

    x**2 * O(x)
    # Might not be good if using non-poly terms
    sin(x) * O(x)
    exp(x) * O(1)  

将表达式在某点附近作 Taylor 展开会涉及到上述的高阶记号．Taylor 展开可使用 :code:`expr.series(var, point, n)` 函数：

.. math::

    \cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} + O(x^6)

.. ipython:: python

    f = cos(x)
    f.series(x, 0, 6)  # omit x**k (k>=6) term

可以用 :code:`removeO()` 函数（移除大 O）来移除高阶项：

.. ipython:: python

    f.series(x, 0, 6).removeO()


.. rubric:: 注释

.. [#f1] 数学中的大 O(x**k) 记号表示忽略 k 阶及 k 阶以上的高阶项；而计算机中的复杂度记号 O(n**k) 表示 n 趋向无穷时它渐进的速度，通常用于描述算法的时间或空间消耗与输入数据大小的关系．二者请勿混淆．
