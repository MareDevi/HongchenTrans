import sys
import tkinter as tk
import translator
import function

class Root:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ChaosShotTranslation")
        VerifPage(self.root)

class VerifPage:

    def __init__(self, root):
        
        self.root = root
        
        if translator.appid != '' and translator.secretKey != '':
            MainPage(self.root)
        
        else:
            self.verifpage = tk.Frame(self.root)
            idlabel = tk.Label(self.verifpage,text='请输入百度翻译ID')
            keylabel = tk.Label(self.verifpage, text='请输入密钥')
            self.identry = tk.Entry(self.verifpage)
            self.keyentry = tk.Entry(self.verifpage)
            surebutton = tk.Button(self.verifpage, text="确定", command=self.saveinfo)

            idlabel.grid(column=0,row=0)
            keylabel.grid(column=0,row=1)
            self.identry.grid(column=1,row=0)
            self.keyentry.grid(column=1,row=1)
            surebutton.grid(row=3)
            self.verifpage.grid()

    def saveinfo(self):
        idget = 'appid: '+self.identry.get()
        keyget = 'secretKey: '+self.keyentry.get()
        with open('config.yaml','w') as f:
            f.write(idget+'\n'+keyget)
        self.verifpage.destroy()
        sys.exit()
        

class MainPage:
    
    def __init__(self, root):
        self.root = root
        self.mainpage = tk.Frame(self.root)

        surebutton = tk.Button(self.mainpage, text='截屏',command=self.shot)

        surebutton.pack()
        self.mainpage.pack()

    def shot(self):
        self.mainpage.destroy()
        run()
        Transpage(self.root)
        
class Transpage:

    def __init__(self, root):
        self.root = root
        self.transpage = tk.Frame(self.root)
        soulabel = tk.Label(self.transpage, text='原文')
        reslabel = tk.Label(self.transpage, text='译文')
        sourcetext = tk.Text(self.transpage)
        resulttext = tk.Text(self.transpage)
        surebutton = tk.Button(self.transpage, text='确定', command=self.sure)

        source = function.source
        result = function.result

        sourcetext.insert('end', source)
        resulttext.insert('end', result)

        soulabel.grid(row=0,column=0)
        reslabel.grid(row=0,column=1)
        sourcetext.grid(row=1,column=0)
        resulttext.grid(row=1,column=1)
        surebutton.grid(row=2)
        self.transpage.grid()

    def sure(self):
        self.transpage.destroy()
        MainPage(self.root)

def run():
    function.run()
    
def main():
    Page = Root()
    Page.root.mainloop()