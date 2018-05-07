# SimpleMultithreadedDownloader
Phi 写的一个非常简易的下载器，嗯，我把它搬到 GitHub，哪位有闲心了改改优化下


原作者的话：

依赖requests, tqdm  
改THREAD_NUMBER = 100来改线程数  
用pyinstaller来打包成一个exe或其他平台二进制文件, pip install pyinstaller安装pyinstaller, pyinstaller -F cf.py来打包成一个exe  
如果打包机器是python>=3.5并且windows 10, 为了能让打包出来的结果能在windows10以下版本运行, 需要安装windows 10 sdk https://dev.windows.com/en-us/downloads/windows-10-sdk , 并在打包时用pyinstaller -p C:\Program Files (x86)\Windows Kits\10\Redist\ucrt\DLLs\x86 -F cf.py来打包. 注意这里x86是32位, 可能64位python需要改为x64.
或者直接用windows 10以下版本的机器来打包.