# ChaosShotTranslation
一款基于python完成的简陋截屏翻译。  
项目基于[Textshot](https://github.com/ianzhao05/textshot)，鄙人菜鸡一枚，只能在大佬的基础上一顿胡改╮(๑•́ ₃•̀๑)╭，如有错误请各路大佬指正。  
另外不会Qt所以拿tkinter简单写了个GUI....  
# 安装
项目OCR使用的为tesseract，需要按单独安装tesseract环境和训练包，archlinux我写了个安装脚本，别的发行版请自行安装╮(๑•́ ₃•̀๑)╭  
克隆本仓库后，终端运行
```bash
./install.sh
```
即可完成安装
```bash
python main.py
```
# 使用
本项目API使用的为百度翻译的接口，需要自行注册账号获取appid与key.
