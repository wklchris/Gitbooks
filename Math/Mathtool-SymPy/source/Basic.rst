SymPy 基础
===============

如何安装 SymPy 请参考官方文档．下面只介绍 SymPy 的用法．

在本笔记中，SymPy 以贪心的方式加载（这也是官方默认的加载方式）：

.. ipython:: python

    from sympy import *

本笔记使用 Sphinx 的 `IPython.sphinxext.ipython_directive` 插件来实现 Python 代码执行．

符号
--------

符号计算的首先需要指明哪些变量是符号，这点与编译编程语言的声明变量有异曲同工之妙：

.. ipython:: python

    x = symbols('x')
    y, z = symbols('y zzz')
    z + 1

从上例可以看出，符号与变量名不一定需要对应．

* 对于连续字母，可以简写：
    
    .. ipython:: python
    
        symbols('x:z')  # x, y, z
        symbols(':d')  # a, b, c, d

* 对于一系列脚标的变量，可以有这些简写：
    
    .. ipython:: python

        symbols('x:5')  # x0, x1, ..., x4
        symbols('x5:10')   # x5, x6, ..., x9
        symbols('x1(:4)') # x10, x11, x12, x13
        symbols('x(:c)')  # xa, xb, xc; Note that 'c' is included

* 声明时指出其他性质：

    .. ipython:: python

        symbols('a b', real=True)  # Two real numbers
        symbols('a b', positive=True)  # Two positive numbers
        symbols('f1 g1', cls=Function)  # Two functions

* 如果声明的变量含有括号，在声明时请双写括号；如果含逗号、分号或空格，请用反斜杠 :code:`\ ` 逃逸．

表达式
-----------------

其实上一节中已经展示了表达式的使用：

.. ipython:: python

    x, y = symbols('x y')
    f = sqrt(x) + 1

这里的 :code:`f` 就是一个表达式，即数学上的 :math:`f = \sqrt{x} + 1` ．


表达式代入值
^^^^^^^^^^^^^^^^

注意，对符号对应的变量进行赋值 **不能** 计算出表达式的值：

.. ipython:: python

    x = 1
    f

这是因为变量 :code:`x` 的改变已经无法影响符号 :code:`x` 了．

上述“错误”的操作不仅导致表达式无法计算，而且会在代入值时出现问题．因此，我们需要重新定义变量 :code:`x` ．如果要计算表达式的值，使用与 Matlab 语法近似的 :code:`subs()` 函数：

.. ipython:: python

    x, y = symbols('x y')
    # Single variable
    f.subs(x, 8)
    # Multiple variables
    g = sqrt(x) + y**2
    g.subs([(x, 3), (y, 1)])
    h = x + x**2 + 2 * x**4
    h.subs([(x**i, i * y) for i in range(5) if i % 2 == 0])

读者可能注意到，SymPy 还进行了 :math:`\sqrt{8}=2\sqrt{2}` 的化简．这也是 SymPy 的有趣之处．

一些注意：

1. 代入值不会改变表达式的内容，除非你显示地将其又赋给该表达式（如 :code:`f=f.subs(x, 8)`）
#. 代入值可以是另一个表达式：

    .. ipython:: python
        
        g.subs(x, x + y)
        g  # Doesn't change the original expression

#. 如果要计算表达式的最终浮点结果，使用 :code:`evalf(subs={x: xval, ...})` 的形式．

    .. ipython:: python

        g = sqrt(x) + y**2
        g.subs([(x, 2), (y, 0)])
        g.evalf(subs={x: 2, y: 0})
    
    函数 :code:`evalf()` 在下面介绍．

evalf 函数
^^^^^^^^^^^^^^^

函数 :code:`evalf(num, subs={}, chop=False)` 可以以浮点形式计算结果．它主要有以下参数：

* 首参数 :code:`num` 表示精度，默认是 15 位．
* 参数 :code:`subs` 传入一个给变量代入值的字典．
* 参数 :code:`chop` 表示是否忽略极小的精度误差．

例子：

.. ipython:: python

    pi.evalf()
    pi.evalf(20)
    expr = sin(x)**2 + cos(x)**2 - 1
    expr.evalf(subs={x: 1})
    expr.evalf(subs={x: 1}, chop=True)

sympify 与 lambdify 函数
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

使用 :code:`sympify(str)` 函数，可以将字符串转为表达式：

.. ipython:: python

    sympify("x**2 + 1")

用 :code:`lambdify(sym, expr, pkg)` 函数，可以将表达式转为一个函数．这样做的目的是 SymPy 在大规模代入值计算上的速度不如其他库，比如 NumPy：

.. ipython:: python

    import numpy as np
    a = np.linspace(0, 2 * np.pi, 5)
    expr = sin(x)
    f = lambdify(x, expr, "numpy")
    f(a)


等式与恒等判断
-----------------

Sympy 中的等式使用 :code:`Eq(LHS, RHS)` 来表示．例如，下例表示等式 :math:`\sin x = 1` ：

.. ipython:: python

    Eq(sin(x), 1)

恒等判断是个有趣的话题：

* 连等号“==”只判断两式在形式上是否逐字符相等，不涉及展开、变换等数学上的相等
* 利用 :code:`simplify(a - b)` ，或者 :code:`a.equals(b)` ，可以判断两式是否数学意义上相等

.. ipython:: python

    a = (x + 1)**2 
    b = x**2 + 2 * x + 1 
    # Symbolically equal
    a == b
    # Mathematically equal
    simplify(a - b)
    a.equals(b)


^ 与 / 的慎重使用*
-----------------------

首先讲 :code:`^` 符号．这个符号在 SymPy 中不是乘方（乘方使用与 Python 原生一致的 :code:`**` 符号），而是异或判断．

.. ipython:: python

    True ^ True  # Xor(True, True)

其次是除法 :code:`/` 符号，它是需要慎重对待的运算符．显然，加法和减法不会改变变量类型，比如两个整数相减仍是整型，整数减去浮点数得到浮点数．但是，两个整数相除在 Python 的不同版本中可能并不得到相同的数据类型．

为了避免这一问题，SymPy 将整数相除视作其内置的有理数类型．也建议在 SymPy 中，使用 :code:`Rational(a,b)` 函数表示整数相除：

.. ipython:: python

    x + Rational(1, 2)  # Instead of '1/2'


展开与化简
-------------

SymPy 有一个通用的化简函数 :code:`simplify(expr)` ，但并不推荐，因为较慢．

.. ipython:: python

    simplify(sin(x)**2 + cos(x)**2)


多项式的展开与因式分解
^^^^^^^^^^^^^^^^^^^^^^^^^^

多项式形式的因式分解在某些角度看像是“化简”，但 :code:`simplify()` 函数不能完成这一工作．请使用 :code:`factor` ．与之相反的功能，即多项式展开，可以使用 :code:`expand` 函数：

.. ipython:: python

    factor(x**2 + 2 * x * y + y**2)
    expand((x+y)**2)

分式的分解与化简
^^^^^^^^^^^^^^^^^^^^

分式的部分分式分解使用 :code:`apart` 函数：

.. ipython:: python

    expr = 1 / (x * (x+1))
    apart(expr)

对于可约分的分式，使用 :code:`cancel` 函数化简速度更快：

.. ipython:: python

    expr = (x**3 - 1) / (x**2 - 1)
    cancel(expr)

三角函数的展开与化简
^^^^^^^^^^^^^^^^^^^^^^^^

使用 :code:`trigsimp` 与 :code:`expand_trig` 函数：

.. ipython:: python

    trigsimp(sin(x) * cos(x) + cos(x) * sin(x))
    expand_trig(sin(2*x))


多项式的合并同类项
^^^^^^^^^^^^^^^^^^^^^

函数 :code:`collect(expr, sym)` 可以将表达式按 :code:`sym` 变量的各次项来合并系数：

.. ipython:: python

    expr = x*y + x + x ** 2 * y
    collect(expr, x)
    collect(expr, y)

可以利用 :code:`coef(sym, n)` 来计算对应变量的 :math:`n` 次项的系数：

.. ipython:: python

    collect(expr, x).coeff(x, 2)
 

其他展开与化简
^^^^^^^^^^^^^^^^^^

其他的展开与化简还包括幂函数（powsimp, expand_power_exp/expand_power_base），对数函数（expand_log, logcombine）．同时，一些特殊的函数（如 :math:`\Gamma(x)` ）也有基于其的化简函数．具体的内容请参考官方手册．


其他运算符
---------------

其他运算符包括：

* 阶乘 :math:`n!` 
* 排列组合 :math:`\binom{n}{k}=\mathrm{C}^k_n` 
* 伽马函数 :math:`\Gamma(x) = \int_0^\infty t^{x-1}\ue^{-t}\ud t`

.. ipython:: python

    n, k = symbols('n k')
    factorial(n)    
    binomial(n, k)
    gamma(x)
