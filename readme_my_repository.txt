使用库函数时，需要将路径加入环境变量中。有两种解决方法。

方法一：
step1:修改path_of_my_repository内容为本函数库【文件夹】所在地址。
step2: 将path_of_my_repository.pth 复制到python使用的Interpreter路径下的site-packages路径中。例如 C:\ProgramData\Anaconda3\Lib\site-packages

方法二：
将此文件夹使用pycharm-project打开，并在左上角右击my_repository文件夹，选择make as source root