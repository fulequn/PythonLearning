#BatchInstall.py
import os

#自动安装库，只需要在下面输入要安装的库，使用os中的命令行操作
libs = {"numpy","matplotlib","pillow","sklearn","requests",\
        "jieba","beautifulsoup4","wheel","networkx","sympy",\
        "pyinstaller","django","flask","werobot","pyqt5",\
        "pandas","pyopengl","pypdf2","docopt","pygame"}
try:
    for lib in libs:
        os.system("pip3 install "+lib)
    print("Successful")      
    #安装成功
except:
    print("Failed Somehow")
    #安装失败
