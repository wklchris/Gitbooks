配置家庭服务器（远程计算平台）
===============================

如果家庭有一台性能足够的台式机，可以安装 Ubuntu 然后将其配置成为计算平台。可以实现的功能包括：

* 用 ssh 命令行，通过局域网/互联网远程控制
* 用 xrdp 远程桌面，通过局域网/互联网远程控制
* 用 samba 访问共享文件夹，简单地复制与移动文件
* 同时允许多个远程设备接入（包括多个远程桌面）

对于编程人员来说，我还想指出以下内容：

* 用 VS Code 的内置 ssh 方便地进行远程代码编写
* 多用户可用的编译器/解释器（这部分会另开章节）
* 管理员安装一次 package，全用户都能用

最后，远程机可以是笔记本或者台式，且理论上 Linux/MacOS/Windows 系统的设备均可以实现以上的所有功能。我的配置：

* 远程机：Windows 10 笔记本
* 服务器：Ubuntu 18.04 LTS 普通版（非 Server 版）
* 其他需要的设备：  
    * 一块 8GB 的 U 盘，用于刻录和安装 Ubuntu
    * 普通的家庭路由器，需要有其管理员账户


安装 Ubuntu
----------------

从官网 `Ubuntu 官方网站 <https://www.ubuntu.com/#download>`_ 下载最新的长期支持版本（LTS）的 iso 文件，然后用刻录工具刻录到一个空闲的 U 盘上。

启动服务器机，插入 U 盘并进入 boot 菜单或 BIOS，设置以它来引导启动。如果该机不作他用，可以选择清除全盘并安装 Ubuntu。

*注意：安装时设置的用户会在后续过程中删除，因此名称与密码不必太过在意。事实上，在刚装机完成的时期，Ubuntu 清除账户与新建账户带来的门槛并不高。*

用户管理
------------

通过 root 用户加多个普通用户的形式，可以实现软件的共享。甚至在安装 Python 的库时，也只需要安装一次，所有用户便都可调用。

启用 root 账户
^^^^^^^^^^^^^^^^^

.. attention::

   在执行本节的内容前，请您查询浏览一些关于 root 账户的安全知识，并避免危险的操作。

在安装时设置的账户是拥有 sudo 权限的账户。不过为了方便安装软件（在 root 用户中安装软件，其他用户无须再次安装），我建议开启 root 账户：

.. code-block:: shell

   sudo passwd root

输入两次以设置密码，这样你的 root 账户就设置好了。之后，在 **任意登录用户** 的命令行中，都可以通过：

.. code-block:: shell
   
   su

命令以及密码来切换到 root 账户。之后，想要回到原登录用户，使用 :code:`exit` 命令即可。


添加普通用户
^^^^^^^^^^^^^^^

在服务器需要多个设备或多个用户连接时，添加普通用户就能解决问题。每个用户可以配置单独的用户路径，方便各自储存文件以及安装一些其他用户不需要的软件。

以名为 :code:`user1` 的为例，添加该用户的命令（这里因为使用的是 root 账户，因此不需要 sudo 命令，下同）是：

.. code-block:: shell

   adduser user1

用户在登录时的默认路径称为用户的主目录。你可以在 :code:`/etc/passwd` 文件中查看用户的主目录：

.. code-block:: shell
   
   # 没有 Vim 使用经验的用户不建议使用 vi 作为文本编辑器
   # 我推荐 nano，它在 ssh 远程中快捷键也有较好的表现。
   nano /etc/passwd

一般在该文件的末尾，可以找到类似以下行的内容：

.. code-block:: shell
   
   ...
   user1:x:1001:1001:UserName,,,:/home/user1:/bin/bash

这表示用户 :code:`user1` 的主目录在 :code:`/home/user1` 。你可以修改该行来改变你的主目录位置。


其他的用户操作
^^^^^^^^^^^^^^^^

.. danger::
    
    本小节中的操作内容不是必须的。如果你不清楚这些操作代表了什么，请跳过这些内容。

在登录界面添加 root 账户入口
""""""""""""""""""""""""""""""

如果你想在开机启动时的登录界面上显示 root 账户 [#f1]_ （**但并不建议以 root 账户登录，除非清楚地了解其中的风险**），可以再运行下列命令：

.. code-block:: shell
   
   sudo passwd -u root

或者用 :code:`sudo passwd -l root` 来取消这一功能。


.. rubric:: 本节注释

.. [#f1] 就算你不执行本小节的这些命令，只要设置了 root 账户的密码，你也可以在登录界面从“其他用户”那里，通过输入用户名“root”与密码进行登录。


为其他用户设置 sudo 权限
""""""""""""""""""""""""""

该权限的下放最重要的目的是安装软件；在一般情形下，普通用户不应当被允许安装软件。重申一遍：管理员在 **任何账户** 下，都可以通过 :code:`su` 命令加密码的方式切换到 root 账户，因此给予普通用户 sudo 权限是需要仔细考量的。

管理员可以使用 :code:`usermod` 命令来更改用户的组，比如将用户添加到 :code:`sudo` 组来使用户获得权限：

.. code-block:: shell

   usermod -aG sudo user1

以上操作将 :code:`user1` 用户添加到了 :code:`sudo` 用户组中，一般这样设置就足够了。如果仍有问题，请参考其他关于修改 :code:`/etc/sudoers` 文件的教程。


配置 SSH：远程加密连接
------------------------

SSH 从来不是传输速度最快的，但是由于其安全性、简明的命令、丰富的衍生应用，一直受到欢迎。在配置服务器机的过程中，我体会到了 SSH 的几个优点：

* 通过远程 ssh 连接，可以完成很多操作，包括大部分编程方面的需求。
* ssh 的连接非常稳定；由于不需要显卡渲染桌面，对网络的要求也很低。
* 在设备出现问题时，可以尝试从远程机 SSH 并通过命令行解决问题。这点对于倚重命令行的 Linux 系统来说非常实用。

这几点都是非常实用的。 **我个人强烈推荐你在安装驱动、远程桌面（甚至大部分软件）之前，就先配置好 SSH** —— 因为安装驱动或者远程桌面时，Linux 设备可能遇到一些借助远程机才方便解决的问题；这点在后面的内容你会读到。

最后，如果你的服务器机不幸是 Windows，那么推荐你阅读 `这篇文章 <https://devblogs.microsoft.com/powershell/using-the-openssh-beta-in-windows-10-fall-creators-update-and-windows-server-1709/>`_ ，我就不赘述了。


在服务器机上的准备
^^^^^^^^^^^^^^^^^^^

服务器机端由于是 Ubuntu，配置起来非常简单（本文所有安装命令都是在 root 账户状态下执行的，下同）：

.. code-block:: shell

   apt-get install openssh-server
   
然后启动服务：

.. code-block:: shell

   service ssh start

如有需要，可以尝试 :code:`service ssh restart` 命令来重启服务。

再然后，前往主目录，检查是否存在 :code:`~/.ssh` 目录。如果没有，创建一个：

.. code-block:: shell

   mkdir ~/.ssh


要查看服务器机的内网 ip，使用：

.. code-block:: shell

   hostname -I

一般的返回结果应为 :code:`192.168.x.x` 。


内网连接测试
^^^^^^^^^^^^^^^^^^^^^^

远程机是我的 Windows 10 笔记本，可以在 :code:`设置 - 应用程序 - 管理可选功能 - 添加功能` 中，选择 OpenSSH Clinet (Beta) 并安装。

多说一句，截至 2019 年 6 月，Windows 的测试版 OpenSSH 的 :code:`ssh-keygen` 命令仍未支持生成 rsa 密钥（微软：别催，在做了），只能生成 :code:`ed25519` 类型的密钥。虽然很别扭，但是好在不影响正常的使用。

然后，运行 cmd 或者 PowerShell，输入 :code:`ssh` 命令以确认成功安装。接着就可以连接了：

.. code-block:: powershell

   ssh user1@192.168.x.x

其中， :code:`user1` 是要连接到的服务器机的用户名， :code:`192.168.x.x` 是服务器机的内网 ip；连接时输入的密码是服务器机上 :code:`user1` 用户的登录密码。

首次连接时，会询问是否连接这个从未连接过的主机（Are you sure you want to continue?）。这时， **请输入"yes"并回车，而不是直接按回车** ，便可以正常进行连接了。


配置免密码的 SSH 连接
^^^^^^^^^^^^^^^^^^^^^^^^

按以下内容配置后，重新连接 SSH 时，应当就不需要密码了。

Ubuntu/MacOS 的配置
""""""""""""""""""""""""

如果你的服务器机上没有 :code:`~/.ssh/authorized_keys` 文件，使用 :code:`ssh-copy-id` 命令复制到服务器机：

.. code-block:: shell
   
   ssh-keygen -t rsa
   ssh-copy-id -i ~/.ssh/id_rsa.pub user1@192.168.x.x

如果你的服务器机上已存在 :code:`authorized_keys` 文件，可以：

.. code-block:: shell

   cat ~/.ssh/id_rsa.pub | ssh uers1@192.168.x.x "cat >> ~/.ssh/authorized_keys"

Windows 的配置
""""""""""""""""""""""""

事情在 Windows 上总是要复杂一点。首先，请尝试生成一个密钥（测试版的 OpenSSH 只能生成 ed25519 类型的）：

.. code-block:: powershell

   ssh-keygen

如果以上命令出错，尝试 [#f2]_ ：

.. code-block:: powershell

   ssh-keygen -t ed25519 -Z aes128-ctr

这个密钥可能被生成在 :code:`c:\users\username\.ssh\id_ed25519` 这个路径中。我们可以用 :code:`ssh-agent` 服务来管理它。以管理员运行 PowerShell：

.. code-block:: powershell

   Start-Service ssh-agent
   ssh-add c:\users\username\.ssh\id_ed25519

生成的密钥中， :code:`.pub` 结尾的是公钥，不带此后缀的是私钥。私钥不能泄漏；公钥用于分发给别人，然后与自己持有的私钥验证身份。SSH 免密就是通过此原理实现的。在 ssh-agent 服务完成密钥记录后，为了安全性考虑，你可以从本地将私钥删除了。 

最后，因为 Windows 中没有 :code:`ssh-copy-id` 的等效命令，我们使用 SSH 自带的文件复制命令 :code:`scp` 来复制公钥到服务器机。如果你的服务器机上事先不存在 :code:`~/.ssh/authorized_keys` 这个文件，你可以执行：

.. code-block:: powershell

   scp c:\users\username\.ssh\id_ed25519.pub user1@192.168.x.x:~/.ssh/authorized_keys

其中， :code:`authorized_keys` 是 Ubuntu 上默认的密钥文件。上述操作实质是将远程机的公钥复制到服务器机。

如果你的服务器机事先已有 :code:`~/.ssh` 与 :code:`authorized_keys` 文件，请将你的公钥以文本形式复制到文件后即可:

.. code-block:: powershell

   scp c:\users\username\.ssh\id_ed25519.pub user1@192.168.x.x
   
   ssh user1@192.168.x.x
   cat id_ed25519.pub | cat >> ~/.ssh/authorized_keys

SSH 的最后，一点闲话：由于 Linux 系统的配色，请调整合适的控制台颜色来获得较好的阅读体验。我个人在 Windows 上的配色使用的是：背景色（screen background）：RGB = 120,180,120，前景文字（screen text）纯黑。

.. rubric:: 本节注释

.. [#f2] 该命令参考了 PowerShell 的一个 `issue  <https://github.com/PowerShell/Win32-OpenSSH/issues/1037>`_ 中的解决方案。

外网 SSH 连接测试
^^^^^^^^^^^^^^^^^^^^^^

在局域网之外的设备，也是有方法通过 SSH 连接到服务器的。不过这需要动态 DNS（Dynamic DNS, DDNS）的支持。

首先，登录路由器的管理界面。寻找 DDNS 相关的选项，并确认该路由器型号可以使用的 DDNS 服务站。前往服务站并注册一个域名 [#f3]_ 。

然后，在 DDNS 界面填入刚才的注册信息，点击登录。这样就完成了 DDNS 部分的配置。

最后，要让 DDNS 服务与 SSH 协同，还需要在路由器的 Virtual Server（或 port forwarding）界面设置添加 ssh 的端口转发：

* 外部端口：任意指定一个未被占用的端口即可，例如 1234。
* 内部端口：默认应是 22
* 内部ip：192.168.x.x （你的服务器内网 ip）


此后，从外网设备应该可以通过 :code:`ssh -p external-port remote-user@domain-from-DDNS` 命令来连接了。例如：

.. code-block:: shell

   ssh -p 1234 user1@example.DDNS.org

.. attention::

   连接到该路由器的设备不能通过该方法登录，只能通过内网 ip 登录。一个常见的测试外网 SSH 方法是通过使用流量的手机。比如在安卓手机上安装 Termux 与 SSH 包，然后在流量连接状态下，测试是否能够成功 SSH。

.. rubric:: 本节注释

.. [#f3] 这类网站一般都会提供免费域名，不过免费域名一般是有时限的（比如一个月）。过期后需要重新注册。


配置 SSH 的别名
^^^^^^^^^^^^^^^^^^

记忆 ip 总是一件麻烦的事情，好在可以使用别名来管理。 SSH 别名的配置文件在 :code:`~/.ssh/config` ，或者 Windows 的 :code:`c:\users\username\.ssh\config` 。如果你的目录中没有这个名为 :code:`config` 的文件（该文件无扩展名），可以新建一个。

一个 config 文件内部书写的范例：

.. code-block:: shell

   Host useralias
       HostName 192.168.x.x
       User remote-user
       IdentityFile c:\users\username\.ssh\id_ed25519.pub
    
此后，在命令行就不需要 :code:`ssh user1@192.168.x.x` 来登录了，可以直接：

.. code-block:: powershell

   ssh useralias

来登录服务器机。


VS Code 通过 SSH 连接
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

在 2019 年 5 月，VS Code 在预览版中推出了 Remote 功能，其中就包括了 remote-ssh 功能。该功能只需在远程机上安装 VS Code Insider，然后安装 remote-ssh 插件即可。

这个功能对于编程人员来说非常实用：写完代码直接在服务器端运行，无须 scp 命令！无须复制文件！完全如同本地的操作体验，万分赞美！！


配置 Samba：文件共享服务
-----------------------------

听说 rsync 是一个速度很不错的解决方案，不过在 Windows 上实在够呛。Samba 的一大优点就是配置简单，速度 [#f4]_ 也可以接受  ，对 Windows 用户来说可能没什么比不折腾更重要的事情了。

在 **当前用户** 下（建议在主目录，方便）建立一个共享文件夹，比如我将其命名为 :code:`SambaShare`。我将其读写权限设置为了 777，这一步是否必要有待商榷。

.. code-block:: shell
   
   cd ~
   mkdir SambaShare
   chmod 777 /home/usereg/SambaShare

然后切换到 root 用户，并安装：

.. code-block:: shell

   su
   apt-get install samba samba-common
   # 添加一个 samba 用户
   smbpasswd -a sambauser

然后更改 Samba 的配置文件 :code:`/etc/samba/smb.conf` ，追加：

.. code-block::

   [folderName]
   comment = share folder
   browseable = yes
   path = /home/user1/SambaShare
   create mask = 0700
   directory mask = 0700
   valid users = sambauser
   force user = sambauser
   force group = sambauser
   public = yes 
   available = yes 
   writable = yes

其中，"folderName" 是你想要显示在远程操作机上的文件夹名称。最后，重启 samba 服务：

.. code-block:: shell

   service smbd restart

之后就可以切换回普通用户了。在远程端的 Windows，尝试连接：

1. 用 Win + R 呼出运行，输入 Ubuntu 服务器的内网 ip :code:`\\192.168.x.x` ；
2. 输入 sambauser 及其密码来登录；
3. 右键 folderName 文件夹，选择“映射网络驱动器”；
4. 此后，便可以从 “此电脑 -> 网络位置” 来访问 Ubuntu 服务器的 SambaShare 文件夹了。

.. rubric:: 本节注释

.. [#f4] 我的测试是大约10MB/s，没什么大文件要转的话，已经可以不用移动硬盘了。


配置远程桌面 xrdp
--------------------

首先，从服务器机 Ubuntu 的设置中启用屏幕共享：:code:`设置 共享 屏幕共享` ，启用。

从 root 账户安装：

.. code-block::

   apt-get install xserver-xorg-core
   apt-get install xserver-xorg-input-all

   # 如果你未安装过 xrdp
   apt-get install xrdp
   # 如果你已经安装过
   apt-get install xorgxrdp 

重新启动计算机，停留在开机登录页面，**不要登录任何账户** ；请记住，同一个账户不能既从远程接入又在本地登录。然后尝试从远程控制设备连接。

Windows 系统自带了 remote desktop 远程桌面软件（可以从系统搜索中找到），登录ip填写内网ip，然后连接。连接方式选择Xorg（默认），用户名与密码填写你想要连接的、 Ubuntu 服务机上的账户与密码。出现 Ubuntu 桌面背景表示连接成功。

想要从外部网络通过远程桌面连接，需要在路由器的 virtual server (或称 port forwarding) 中设置 3389 端口到服务机所在内网 ip；内部端口默认留空（或也填 3389）即可。


其他内容
-----------

上述的内容已经可以搭建一个很好的服务器了。本节介绍一些锦上添花的东西。

温度监控
^^^^^^^^^^^

正常情况下，Ubuntu 设备不需要关机。不过温度监控还是必要的，以下是控制台温度监控软件 :code:`sensors` 的安装：

.. code-block:: shell

   apt install lm-sensors hddtemp
   sensors-detect
   sensors

如果你正在使用桌面 Ubuntu，可以考虑：

* 如果想在任务栏上显示温度，可以安装 psensor： :code:`sudo apt install psensor` ，并在设置中每个想要显示的温度感应器下，勾选“Display sensors in the label”。
* 如果想要类似 AIDA64 的硬件总览，推荐使用 hardinfo： :code:`sudo apt-get install libcamberra-gtk-module hardinfo` 。
