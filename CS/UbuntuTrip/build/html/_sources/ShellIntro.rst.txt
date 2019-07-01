Shell 命令简介
==================

.. attention::

   本章的内容不是必须阅读的；您就算不阅读本章，也可以照搬后续章中提到的命令与解决方案。
   
   我建议读者对本章稍加翻阅，以便未来在搜索命令用法时有个大致的印象。

大多数 Linux 系统的 Shell 命令都是基于 Bash (Bourne Again SHell) 环境的；本章以 Ubuntu 下的 Bash 为例，使用的键盘是基于 Windows 键位的。


命令行终端
--------------

在 Linux 系统中，你几乎无法避免使用命令行终端（Terminal）。你可以通过 `Ctrl + Alt + T` 打开终端，它会显示：

.. code-block:: shell

   username@hostname$

其中， :code:`username` 是当前用户名， :code:`hostname` 是当前主机的名称。而美元符 :code:`$` 表示当前用户的权限是普通。用户可以在此界面下的美元符后输入 shell 命令，并以 `Enter` 键执行。

相对于普通用户，还有管理员用户。比如 Linux 中权限最高的用户，叫 :code:`root` ，在登入时不显示美元符而是显示井符 :code:`#` ：

.. code-block:: shell

   root@hostname#

一般地，我们不会用 :code:`root` 用户登入，而是使用拥有 :code:`sudo` 权限的普通用户登录，并通过 :code:`sudo` 指令运行高权限命令；这样与通过 :code:`root` 账户执行操作实质上是等同的。

主目录与 .bashrc
^^^^^^^^^^^^^^^^^^^^

一般用户的主目录即 :code:`/home/username` ，你也可以通过波浪符 :code:`~` 指代当前用户的主目录。

在打开终端时，shell 会调用用户的配置文件，一般位于 :code:`~/.bashrc` 。此外，登录主机时会启动一个登录 shell，它读取的是 :code:`~/.bash_profile` 。只有登录主机的 shell 是登录 shell，我们从桌面打开终端并不在此列。 

常见语法
^^^^^^^^^^^^^

在终端中可以使用的一些语法如下：

* 分号表示语句分隔，比如 :code:`$ cmd; cmd2` 实质上是 :code:`$ cmd` 与 :code:`$ cmd2` 两条内容。
* 行尾的 :code:`#` 之后的内容视为注释，不会被执行。
* 单引号与双引号都可以表示字符串。不过单引号中不能使用变量替换；而双引号字符串在传递给 :code:`echo` 输出命令时，可能需要添加额外的转义符号 :code:`\ ` 。

脚本文件的构成与运行
^^^^^^^^^^^^^^^^^^^^^^

shell 脚本通常是扩展名为 :code:`.sh` 的文件。它的首行以 shebang [#f1]_ 起始，最常见的是:

.. code-block:: shell

   #!/bin/bash

这表示脚本执行时会使用位于 :code:`/bin` 目录下的 :code:`bash` 解释器。在脚本文件编写完成并保存后，通过命令行可以运行（假设当前脚本位于终端的当前路径下）：

.. code-block:: shell

   bash example.sh

其中 :code:`example.sh` 是脚本的文件名；如果位于其他路径下，可以使用带有路径的命令 :code:`/path/to/script/example.sh` 。

另一种执行方法是先赋予脚本文件可执行权限，然后直接执行：

.. code-block:: shell
   
   chmod a+x example.sh
   ./script.sh

其中 :code:`chmod` 是一个更改文件访问/执行权限的命令，参数 :code:`a+x` 表示给所有的用户组添加执行权限。常见命令的用法会在后面介绍。第二行的 :code:`./` 表示当前目录。

.. rubric:: 本节注释

.. [#f1] shebang 的含义是指字符串 :code:`#!` ，因为在英文中 :code:`#` 读作 sharp， :code:`!` 读作 bang，而 shebang 则由这两个词组成而来。
