如何使用 ode_toolkit 包绘制相图*
=====================================

此包是作者自行编写的用于相图绘制的包，其实质上没有任何技术难点，仅仅是基于 Matplotlib 作了新的函数定义．

我的建议是使用 Python 3 读者直接阅读包的内容，并有选择地加以使用．如果读者很懒却又希望使用该包，也可以直接下载使用，其用法如下：

1. 前往 ode_toolkit 页面下载该包到本地的用户包仓库，比如 :code:`d:\my-pkg` ．
2. 前往本地的 Python 的 \Lib\site-packages 路径，新建一个 pth 文件，例如 :code:`my-pkg.pth` ．
3. 在文件内添加你的本地包仓库的位置，即在第一行写： :code:`d:\my-pkg` ．这一步的作用是将你的本地包仓库添加到你的 :code:`sys.path` 变量中（注意：这会永久改变该变量的值，除非删除给文件；如介意请酌情操作）．
4. 打开 Python 命令行，测试 :code:`import ode_toolkit` 是否能正常加载．
5. 如果能正常加载，即可进行使用．例如：

    .. code-block:: python

        import ode_toolkit.phaseplot as pp

        pp.plot_phase2d(ax, f, x_interval, y_interval, ...)
    
    要查看帮助，使用如 :code:`help(pp.plot_phase2d)` 的命令．所有函数均配有英文文档．