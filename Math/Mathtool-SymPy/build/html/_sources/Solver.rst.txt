解方程
===========

SymPy 作为符号运算库，自然可以求解方程的解析解．

通用求解器
---------------

通用求解函数是 :code:`solveset(eq, var, domain=S.Complexes))` ．其中，方程可以用上文介绍过的 :code:`Eq(LHS, RHS)` 表示，也可以用 :code:`expr` 代替以求解 :code:`expr=0` 的方程：

.. ipython:: python

    from sympy import *
    x, y = symbols('x y')
    solveset(Eq(x**2, -1), x)
    # Same equation as above
    solveset(x**2 + 1, x)

其中，第三参数表示求解域：

.. ipython:: python

    # Exclude complex roots
    solveset((x**2 + 1) * (x - 1), x)
    solveset((x**2 + 1) * (x - 1), x, domain=S.Reals)

除了上述虚数的情形，特殊的还有：

* 在复数域上无解（返回 :code:`EmptySet` ）
* 解为全复数域
* 方程在形式上无解析解（返回一个 :code:`ConditionSet` ）

.. ipython:: python

    solveset(exp(x), x)  # Solve exp(x) = 0
    solveset(x - x, x)  # Solve x - x =0
    solveset(x - sin(x), x)  # Try to solve x - sin(x) = 0

重根
-------

注意， :code:`solveset(eq, var)` **不会强调重根** ．如果想要计算重根，使用 :code:`roots(expr, var)` 函数：

.. ipython:: python

    f = x**2 * (x - 1)
    solveset(f, x)
    roots(f, x)


线性方程组
-------------

线性求解器 :code:`linsolve(eqsystem, vars)` 将在未来并入 :code:`solveset` 函数中；但至少在目前的版本，仍需要调用 :code:`linsolve` 来求解线性方程组．

下例求解了： :math:`\begin{cases} x+y-4 = 0 \\ x-y+2 = 0 \end{cases}`

.. ipython:: python

    x, y = symbols('x y')
    linsolve([ x + y - 4, x - y + 2 ], (x, y))

或者，以上方程组，我们也写成矩阵形式 :math:`\boldsymbol{A}\boldsymbol{x} = \boldsymbol{b}` ：

.. math::

    \begin{pmatrix}
    1 & 1 \\ 1 & -1
    \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix}
    = \begin{pmatrix}
    4 \\ -2
    \end{pmatrix}

并用线性求解器的另一种输入格式 :code:`linsolve((A, b), vars)` ：

.. ipython:: python

    M = Matrix(( [1, 1, 4], [1, -1, -2] ))
    A = M[:, :-1]
    b = M[:, -1]
    A
    b
    # Format 1: M is a extended matrix: [A, b]
    linsolve(M, (x, y))
    # Format 2: Input A and b seperately
    linsolve((A, b), (x, y))

最后，线性方程组可以是不定解的，例如两个方程构成的三元线性方程组：

.. ipython:: python

    x, y, z = symbols('x:z')
    A = Matrix(( [1, 1, 0], [1, -1, 0] ))
    b = Matrix(( [4], [-2] ))
    linsolve((A, b), (x, y, z))


非线性方程组
----------------

用法与线性方程组类似，不过使用的是 :code:`nonlinsolve(eqsystem, vars)` ：

.. ipython:: python

    nonlinsolve([x*y - 1, x + y - 1], (x, y))


注意，如果方程组中含有三角函数，请使用 :code:`solve()` 而不是 :code:`nonlinsolve()` ：

.. ipython:: python

    solve([sin(x + y), cos(x - y)], (x, y))

以上求得的含三角函数的方程组的解，并不是其所有的解．


微分方程
------------

利用 :code:`dsolve(eq, var)` 可以解微分方程，需要先定义一个函数 :code:`f` ：

.. ipython:: python

    f = symbols('f', cls=Function)
    diffeq = Eq(f(x).diff(x, 2) + 12 * x**2 - 6 * x, 0)
    dsolve(diffeq, f(x))

微分方程组也可以用类似线性、非线性方程的解的格式进行处理，比如下例的微分方程组：

.. math::

    \begin{dcases}
    \frac{\ud}{\ud x}f(x) &= g(x) \\[4pt]
    \frac{\ud}{\ud x}g(x) &= 0
    \end{dcases}

可以如下解 :code:`dsolve(eqs, vars)` ：

.. ipython:: python

    v = symbols('f g', cls=Function)
    dsolve([ v[0](x).diff(x) - v[1](x), v[1](x).diff(x) ], (v[0](x), v[1](x)))
