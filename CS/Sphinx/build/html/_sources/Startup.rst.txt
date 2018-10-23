安装和配置 Sphinx
====================

Sphinx 简介
-------------

Sphinx_ 是一个文档生成工具，致力于构建美观的文档．起初该项目是为了更好地撰写 Python_ 官方文档，但现在该项目的成就与名气已经不仅仅限于此了．


安装
-------------

要安装 Sphinx，建议首先前往 Python_ 安装 Python．对于已经安装 Python 的用户，可以使用：

.. code-block:: bat

   pip install -U Sphinx 

来完成安装．


初始化
-------------

前往你的文档文件夹，Shift + 鼠标右键呼出命令行，然后执行：

.. code-block:: bat

   sphinx-quickstart

然后按提示顺序进行设置即可．附上我的设置：

.. code-block:: bat
   :emphasize-lines: 1, 11-12, 15
   
   > Separate source and build directories (y/n) [n]: y
   > Name prefix for templates and static dir [_]:
   > Project language [en]: zh_CN
   > Source file suffix [.rst]:
   > Name of your master document (without suffix) [index]:
   > autodoc: automatically insert docstrings from modules (y/n) [n]:
   > doctest: automatically test code snippets in doctest blocks (y/n) [n]:
   > intersphinx: link between Sphinx documentation of different projects (y/n) [n]:
   > todo: write "todo" entries that can be shown or hidden on build (y/n) [n]:
   > coverage: checks for documentation coverage (y/n) [n]:
   > imgmath: include math, rendered as PNG or SVG images (y/n) [n]: y
   > mathjax: include math, rendered in the browser by MathJax (y/n) [n]:
   > ifconfig: conditional inclusion of content based on config values (y/n) [n]:
   > viewcode: include links to the source code of documented Python objects (y/n) [n]:
   > githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]: y

需要注意的问题我在上面已高亮，分别是：

* **是否将源与输出文件夹分开：** 选择“是”会将你的 rst 文件放置于 `source/` 目录下，而文档生成的结果放在 `build/` 目录下．
* **数学公式的生成：** imgmath 与 Mathjax 只需开启一个．用法可以参考 `Sphinx Math Support <http://www.sphinx-doc.org/en/master/usage/extensions/math.html>`_ 页面，也可以参考本手册仓库中的设置．
* **Github Pages 的支持：** 这一项的原因是 Github Pages 对于带下划线的路径访问不亲和，这时常造成页面不能正常显示．如果这一项勾选，那么 Sphinx 会自动为你添加一个插件，便于自动生成一个空的 `.nojekyll` 文件来避免这一问题 [#f1]_ ．


其他准备工作
-----------------

在上述步骤之后，你会在你的文档目录（假设名为 `bookfolder`）中，得到下述的一个目录结构::

   bookfolder
   |-- source
       |-- _static
       |-- _templates
       |-- conf.py
       |-- index.rst
   |-- make.bat
   |-- Makefile

其中，`conf.py` 就是该文档的配置文件，记录了刚才 `sphinx-quickstart` 运行结果的大部分信息．

要生成 HTML 文件，在根目录下运行命令行：

.. code-block:: bat

   make html

即可将 HTML 文件输出到 `build/html/` 目录．


路径的修改
^^^^^^^^^^^^^

如果对输入/输出路径不满意，可以用文本编辑器打开 Matkefile 文件，将其中的 `BUILDDIR` 项的值 build 改为其他．同理，`SOURCEDIR` 也可以进行修改．

如果要修改 `source` 目录下的 `_static` 或者 `_template` 路径名，请打开 `conf.py` 找到相应项进行修改．


主题
^^^^^^^^^^^^

如果对默认的主题不满意，可以使用更改 `html_theme` 项来使用别的主题．本文档使用的是 Read the Docs 的主题：

.. code-block:: python

   html_theme = 'sphinx_rtd_theme'

需要指出的是，该主题拥有一些细微的 bug [#f2]_ ；使用前请三思．


写给 Github Pages 用户
^^^^^^^^^^^^^^^^^^^^^^^^

*非 Github Pages 用户可以略过此节* ．

除了上文中提到的 `.nojekyll` 文件的问题，Github Pages 用户还面临另一个问题：仓库根目录与文档根目录的不匹配．这个问题体现在如果输入开启了 Github Pages 服务的项目页面：

.. code-block:: html

   https://username.github.io/reponame

往往会出现 404（因为你的根目录下并没有 `index.html`）．解决方法是手动创建一个 html 文件，写入：

.. literalinclude:: ../index.html

该文件的作用是完成了到 `build/html/index.html` 的跳转．


其他插件及疑难问题
-----------------------

其他的美观性问题大多可以用 CSS 的撰写来解决；读者可以参考本文文末的注释中提及的内容．

Matplotlib 绘图插件
^^^^^^^^^^^^^^^^^^^^^^

值得一提的还有 Matplotlib 提供的插件，定义了 `plot` 指令，可以直接从外部导入 .py 文件绘图，或者在 reST 文档中输入 Python 代码进行绘图（均需要在 `conf.py` 的插件中添加 `matplotlib.sphinxext.only_directives` 项）．下面是一个例子，具体请参考：`Matplotlib Extensions <https://matplotlib.org/sampledoc/extensions.html>`_ 页面．

.. code-block:: rest
   
   .. plot:: /draw/py-draw-circle.py
      :include-source: 

搜索功能
^^^^^^^^^^^^^^

至于搜索功能，在不同设备上的测试结果不尽相同．例如，在 `conf.py` 文件中将 `language` 项设为 `zh_CN` 一般可以正确地建立索引项．如果仍然不行，可以尝试安装 jieba 分词库：

.. code-block:: bat
   
   pip install jieba

如果你使用的是 Python 3，也可以尝试：

.. code-block:: bat

   pip3 install jieba3k

之后在构建 HTML 时，就能看到类似的命令行输出：

.. code-block:: bat

   Building prefix dict from e:\intelpython3.6\lib\site-packages\jieba\dict.txt ...
   Loading model from cache C:\Users\wklchris\AppData\Local\Temp\jieba.cache
   Loading model cost 0.9786026477813721 seconds.
   Prefix dict has been built succesfully.

最后说明一句：

1. 本地测试可以搜索功能，但只能显示搜索结果所在的章节或文件，词条结果的详细文本不会展开；因此，只要本地搜索能够正常搜到词汇，那么具体的显示效果还需要推送到服务器端才能查看．
#. 搜索功能并非完美，部分词汇可能不被识别．在测试搜索是否可用时，请尽量使用文中确定出现的、非生僻或术语的词汇进行测试．

.. 自定义链接

.. _Python: https://www.python.org/
.. _Sphinx: http://www.sphinx-doc.org


.. rubric:: 注释

.. [#f1] 即使加载了这一插件，并不一定就保证 Github Pages 服务上的结果；该插件带来的效果可能是脆弱的．如果仍然异常，可以尝试在 Github 仓库的根目录放置 `.nojekyll` 文件（Github Pages 更新有延后，有时在后续的推送后才能观察到之前推送引起的变化；建议每次对网页文字进行更改，以确定更新是否被延后了）．如果担心 Github Pages 的配置问题，可以尝试 Read the Docs 网站的在线文档服务．
.. [#f2] 读者如果想要使用 sphinx-rtd-theme 主题，可以在 `conf.py` 中追加一条配置：

   .. code-block:: python

      html_style = 'css/rtd-revised.css' 
   
   并在 `source\_static\css` 目录中创建一个 `rtd_revised.css` 文件．该文件的内容可以参考下述：

   .. literalinclude:: /_static/css/rtd-revised.css
   
   该 CSS 文件实现了两个功能：

   1. 使 RTD 主题的页面扩展到全屏宽度；
   2. 修正了 RTD 主题在行间公式中编号（即使用 `:label:`）时，编号数字不居右的问题．