疑难解答
=============

配置 Ubuntu 时，或者说从 Windows 转到 Linux 的用户在使用新系统时，会遇到各种各样的问题。这不足为奇。本章是本人遇到问题的记录。

大多基于 18.04 LTS 版本。

安装
---------

卡红点的界面（显卡问题）
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

这个问题简直是每个月都会有人遇到，与显卡有关。在安装前的 Grub 菜单选择界面（即用回车选择 Install Ubuntu）前，请将光标悬停其上：

.. code-block:: shell
   
   Try Ubuuntu without installing
   * Install Ubuntu
   OEM install
   ...


然后按 `e` 键进入编辑模式，找到以 `linux` 开头的一行（一般是倒数第二行），在结尾加上 :code:`nouveau.modeset=0` ：

.. code-block:: shell

   ... quite splash --- nouveau.modeset=0


然后 `Ctrl+X` 进入安装。这样就不会卡红点了。

.. attention::

   一个过时的指南是将 :code:`---` 改为 :code:`nomodeset`，但这样仍然会遇到一些问题，比如点不到按钮。


安装时分辨率太低/点不到按钮
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

如果你使用了上述的 :code:`nouveau.modeset=0`，一般不会出现分辨率问题。如果分辨率不影响安装，那也忍一忍吧。

如果不幸出现了因为低分辨率、按钮被挤出了屏幕外的问题，请用组合键 `Alt + F7` ，然后向上移动鼠标就能将当前窗口向上平移了。这样就能显示出下方的按钮了。（那些教你用 `tab` 的都再见吧！）


启动
---------

引导未失去但路径不正确
^^^^^^^^^^^^^^^^^^^^^^^

这种情形指的是较不严重的引导问题，往往是安装流程没有什么大的问题（例如双系统安装，一个UEFI一个Legacy，问题就比较大）、用户也没有在命令行干一些太作死的事情（例如把引导分区删了）。这些问题常见的有：

* 在 Windows 的物理机上安装 Ubuntu 双系统，然后 Grub 用匪夷所思的手法干掉了 Windows Boot Manager……尤其是当你尝试把 Ubuntu 安装到一块新硬盘上，比如原来的 Windows 在固态上、新的 Ubuntu 却在机械硬盘上时。
* 安装系统时的引导区给错了地方（别问我怎么把引导区划到 U 盘上的）。
* 意（shóu）外（jiàn）地修改了引导文件。

带来的问题可能有：

* 启动菜单是 Grub，但列表里没有原来的 Windows 系统；或者有 Windows 系统，选中了却无法启动。
* 根本没有见到启动菜单，一开机就奔 Windows 去了；Ubuntu 需要从键盘调用 boot menu 才能进入，甚至调用了也无法进入。
* 无法启动任何一个系统，你被导向到 grub rescue 命令行界面。

如果你的系统安装没有大差错，下面这个方法 [#f1]_ 可以说非常有效：

* 首先，去 BIOS 关闭 Secure boot，保存后重启
* 插上你的 Ubuntu 安装盘，从它启动
* 选择 Try Ubuntu without installing （如有独显问题，也请参照上文 :code:`nouveau.modeset=0` 加在 `linux` 行最后）
* 进入桌面后，打开 shell，安装 `boot-repair <https://help.ubuntu.com/community/Boot-Repair>`_ 这个软件：

    .. code-block:: shell

       sudo add-apt-repository ppa:yannubuntu/boot-repair  
       sudo apt-get update  
       sudo apt-get install -y boot-repair
    
* 运行这个工具： :code:`sudo boot-repair` ，并从 Advanced Options 中选择 “Reinstall GRUB”，点击 Apply
* 结束后，从命令行 :code:`sudo reboot` 来重启计算机

据我个人的体验，一般的双系统引导问题这样可以得到解决。


其他
---------

从 Ubuntu 关机时的嘎达声
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*（尚待验证）* 计算机的麦克风带来的问题，解决方法 [#f2]_ 是屏蔽 `pcspkr` 模块：

.. code-block:: shell

   gsettings set org.gnome.desktop.wm.preferences audible-bell false


.. rubric:: 注释

.. [#f1] 来源：`Boot-repair 方法解决 <https://askubuntu.com/questions/313757/black-screen-after-selecting-an-option-from-grub-boot-menu>`_
.. [#f2] 来源：`关机时的异常噪声 <https://www.reddit.com/r/linuxquestions/comments/9bs4tq/loud_popping_noise_on_shutdownreboot/>`_