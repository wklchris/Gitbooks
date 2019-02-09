深度自定义
============

深度自定义包括对所选用主题的修改。

例如，本站在 rtd 主题的基础上，在左侧导航栏的搜索框上方添加了一个链接，用来返回我的个人主页。

这一点的实现很简单：

1. 进入 `sphinx_rtd_theme` 的安装路径
2. 打开 layout.html 文件进行编辑
3. 加入如下内容：

   .. code-block:: html

      {# -- Customization begins -- #}
      <a href="https://wklchris.github.io/Gitbooks/homepage/" style="margin:0pt 2pt">
        · Site Homepage ·
      </a>

需要注意的是这种修改可能带来的后续问题，请保证自己的 HTML 能力可以应对可能的后果。
