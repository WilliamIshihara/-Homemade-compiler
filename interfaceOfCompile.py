import sys
import string
from PyQt5.QtWidgets import QWidget, \
                              QPushButton, \
                              QToolTip, \
                              QMessageBox, \
                              QApplication, \
                              QDesktopWidget, \
                              QMainWindow, \
                              QAction, \
                              qApp, \
                              QVBoxLayout, \
                              QHBoxLayout, \
                              QTextBrowser, \
                              QLineEdit, \
                              QLabel, \
                              QInputDialog, \
                              QColorDialog, \
                              QFontDialog, \
                              QFileDialog, \
                              QGridLayout, \
                              QTextEdit, \
                              QFrame, \
                              QSplitter, \
                              QStyleFactory
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, \
                          QIcon

data =""
z =""
letters = string.ascii_letters + "_"
    # 空白字符
blank = " \n\r\t"
    # 保留字数组
reserved_words = ["char", "int", "if", "else", "var", "return", "break", "do", 
                    "while", "for", "double", "float", "short", "scanf", "case", "void"]
    # 符号表
signs = {"=": 27, "<=": 28, "<>": 29, "<": 30, ">=": 31, ">": 32, "+": 33, "-": 34, 
            "*": 35, "==": 53, "/": 36, "//": 37, ":": 38, ";": 39, "(": 40, ")": 41,
            "{": 42, "}": 43, "[": 44, "]": 45, "\"": 46, ",": 47, "'": 48, "!=": 49,
            "&": 50, "&&": 51, "||": 52, "==": 53, "|": 54, "%": 55, "?": 56}


keyward = set('')

# keywards = {}
# #关键字
# keywards['auto'] = 101
# keywards['break'] = 102
# keywards['case'] = 103
# keywards['char'] = 104
# keywards['const'] = 105
# keywards['continue'] = 106
# keywards['default'] = 107
# keywards['do'] = 108
# keywards['double'] = 109
# keywards['else'] = 110
# keywards['enum'] = 111
# keywards['extern'] = 112
# keywards['float'] = 113
# keywards['for'] = 114
# keywards['goto'] = 115
# keywards['if'] = 116
# keywards['int'] = 117
# keywards['long'] = 118
# keywards['register'] = 119
# keywards['return'] = 120
# keywards['short'] = 121
# keywards['signed'] = 122
# keywards['sizeof'] = 123
# keywards['static'] = 124
# keywards['struct'] = 125
# keywards['switch'] = 126
# keywards['typedef'] = 127
# keywards['union'] = 128
# keywards['unsigned'] = 129
# keywards['void'] = 130
# keywards['volatile'] = 131
# keywards['while'] = 132
# keywards['inline'] = 133
# keywards['restrict'] = 134
# keywards['_Bool'] = 135
# keywards['_Complex'] = 136
# keywards['_Imaginary'] = 137
# keywards['_Alignas'] = 138
# keywards['_Alignof'] = 139
# keywards['_Atomic'] = 140
# keywards['_Static_assert'] = 141
# keywards['_Noreturn'] = 142
# keywards['_Threturn'] = 143
# keywards['_Thread_local'] = 144
# keywards['_Generic'] = 145

# #运算符
# keywards['+'] = 201
# keywards['-'] = 202
# keywards['*'] = 203
# keywards['/'] = 204
# keywards['%'] = 205
# keywards['++'] = 206
# keywards['--'] = 207
# keywards['=='] = 208
# keywards['!='] = 209
# keywards['>'] = 210
# keywards['<'] = 211
# keywards['>='] = 212
# keywards['<='] = 213
# keywards['&&'] = 214
# keywards['||'] = 215
# keywards['!'] = 216
# keywards['&'] = 217
# keywards['|'] = 218
# keywards['^'] = 219
# keywards['~'] = 220
# keywards['<<'] = 221
# keywards['>>'] = 222
# keywards['='] = 223
# keywards['+='] = 224
# keywards['-='] = 225
# keywards['*='] = 226
# keywards['/='] = 227
# keywards['%='] = 228
# keywards['<<='] = 229
# keywards['>>='] = 230
# keywards['&='] = 231
# keywards['^='] = 232
# keywards['|='] = 233
# keywards['sizeof()'] = 234
# keywards['?:'] = 235
# keywards[','] = 236
# # keywards['[]'] = 237
# # keywards['()'] = 238
# keywards['.'] = 239
# keywards['->'] = 240

# #界符
# keywards['('] = 301
# keywards[')'] = 302
# keywards['['] = 303
# keywards[']'] = 304
# keywards['{'] = 305
# keywards['}'] = 306
# keywards['/*'] = 307
# keywards['*/'] = 308
# keywards['"'] = 309
# keywards["'"] = 310
# keywards['<'] = 311
# keywards['//'] = 312
# keywards[';'] = 313
# keywards[':'] = 314

# #转义字符
# keywards['\a'] = 401
# keywards['\b'] = 402
# keywards['\f'] = 403
# keywards['\n'] = 404
# keywards['\r'] = 405
# keywards['\t'] = 406
# keywards['\v'] = 407
# keywards['\\'] = 408
# keywards["\'"] = 409
# keywards['\"'] = 410
# keywards['\?'] = 411
# keywards['\0'] = 412
# keywards['\\ooo'] = 413
# keywards['\\xhh'] = 414

# #单词类别
# keywards['整数'] = 500
# keywards['字符'] = 600
# keywards['字符串'] = 700
# keywards['标识符'] = 800
# keywards['实数'] = 900




class Example(QMainWindow):
    # letters = string.ascii_letters + "_"
    # # 空白字符
    # blank = " \n\r\t"
    # # 保留字数组
    # reserved_words = ["char", "int", "if", "else", "var", "return", "break", "do", 
    #                 "while", "for", "double", "float", "short", "scanf", "case", "void"]
    # # 符号表
    # signs = {"=": 27, "<=": 28, "<>": 29, "<": 30, ">=": 31, ">": 32, "+": 33, "-": 34, 
    #         "*": 35, "==": 53, "/": 36, "//": 37, ":": 38, ";": 39, "(": 40, ")": 41,
    #         "{": 42, "}": 43, "[": 44, "]": 45, "\"": 46, ",": 47, "'": 48, "!=": 49,
    #         "&": 50, "&&": 51, "||": 52, "==": 53, "|": 54, "%": 55, "?": 56}
    da = ""
    def __init__(self):
        super().__init__()

        self.initUI() #界面绘制交给InitUi方法
    
    def initUI(self):
        #设置窗口的标题
        self.setWindowTitle('Compiler')
        #设置窗口的图标,引用当前目录下的web.png图片
        self.setWindowIcon(QIcon('G:/Code/python/Complier/source/图片1.png'))
        #设置窗口和位置大小
        self.showMaximized()
        self.add_menu()
        # self.add_layout()


    def add_menu(self):
        #------------------------布局---------------------
        #左侧

       
        #-------------------------工具栏------------------------------------
        #后退
       
        BackToolAction = QAction(QIcon('G:/Code/python/Complier/source/toor/撤回.png'),'&Back',self)
        #BackToolAction.setShortcut('ctrl+Q')
        BackToolAction.setStatusTip('back application')
        #BackToolAction.triggered.connect(qApp.quit)
        #前进
        ForwardToolAction = QAction(QIcon('G:/Code/python/Complier/source/toor/前进.png'),'&Forward',self)
        #ForwardToolAction.setShortcut('ctrl+Q')
        ForwardToolAction.setStatusTip('Forward application')
        #ForwardToolAction.triggered.connect(qApp.quit)
        #打印
        PrintToolAction = QAction(QIcon('G:/Code/python/Complier/source/toor/print.png'),'&Print',self)
        #ForwardToolAction.setShortcut('ctrl+Q')
        PrintToolAction.setStatusTip('Print application')
        #ForwardToolAction.triggered.connect(qApp.quit)
        #文件
        FoldToolAction = QAction(QIcon('G:/Code/python/Complier/source/toor/folder.png'),'&Fold',self)
        #ForwardToolAction.setShortcut('ctrl+Q')
        FoldToolAction.setStatusTip('Fold application')
        #ForwardToolAction.triggered.connect(qApp.quit)
        #保存
        SaveToolAction = QAction(QIcon('G:/Code/python/Complier/source/toor/edit-tools.png'),'&Save',self)
        #ForwardToolAction.setShortcut('ctrl+Q')
        SaveToolAction.setStatusTip('Save application')
        #ForwardToolAction.triggered.connect(qApp.quit)
        #搜索
        SearchToolAction = QAction(QIcon('G:/Code/python/Complier/source/toor/search.png'),'&Search',self)
        #ForwardToolAction.setShortcut('ctrl+Q')
        SearchToolAction.setStatusTip('Search application')
        #ForwardToolAction.triggered.connect(qApp.quit)
        #设置
        SetToolAction = QAction(QIcon('G:/Code/python/Complier/source/toor/setup.png'),'&Set',self)
        #ForwardToolAction.setShortcut('ctrl+Q')
        SetToolAction.setStatusTip('set application')
        #ForwardToolAction.triggered.connect(qApp.quit)
        #debug
        DebugToolAction = QAction(QIcon('G:/Code/python/Complier/source/toor/test.png'),'&Debug',self)
        #ForwardToolAction.setShortcut('ctrl+Q')
        DebugToolAction.setStatusTip('Debug application')
        #ForwardToolAction.triggered.connect(qApp.quit)
        #取消
        CancelToolAction = QAction(QIcon('G:/Code/python/Complier/source/toor/叉.png'),'&Cancel',self)
        #ForwardToolAction.setShortcut('ctrl+Q')
        CancelToolAction.setStatusTip('Cancel application')
        #ForwardToolAction.triggered.connect(qApp.quit)
        #数据
        DataToolAction = QAction(QIcon('G:/Code/python/Complier/source/toor/数据.png'),'&Data',self)
        #ForwardToolAction.setShortcut('ctrl+Q')
        DataToolAction.setStatusTip('Data application')
        #ForwardToolAction.triggered.connect(qApp.quit)
        #编译运行
        RunToolAction = QAction(QIcon('G:/Code/python/Complier/source/toor/对号.png'),'&Run',self)
        #ForwardToolAction.setShortcut('ctrl+Q')
        RunToolAction.setStatusTip('Run application')
        #ForwardToolAction.triggered.connect(qApp.quit)








        #--------------------------菜单栏----------------------------------

        #打开文件选项
        openFileAction = QAction(QIcon('G:/Code/python/Complier/source/atm.png'),'&File',self)
        openFileAction.setShortcut('ctrl+o')
        openFileAction.setStatusTip('open file')
        openFileAction.triggered.connect(self.funOpenFile)

        
        #退出选项
        exitAction = QAction(QIcon('G:/Code/python/Complier/source/退出 (2).png'),'&Exit',self)
        exitAction.setShortcut('ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)



        self.statusBar()

        # self.setGeometry(100,100,800,900)
        #创建状态栏的小窗口,显示信息
        self.statusBar().showMessage('Ready')
        
        #创建一个菜单栏
        menubar = self.menuBar()
        #添加菜单,只添加菜单，未添加行为事件
        fileMenu = menubar.addMenu('&File[F]')
        editMenu = menubar.addMenu('&Edit[E]')
        lexMenu = menubar.addMenu('&LexicalAnalysis[L]')
        synMenu = menubar.addMenu('&SyntaxAnalysis[S]')
        intMenu = menubar.addMenu('&IntermediateCode[I]')
        objMenu = menubar.addMenu('&ObjectCodeGeneration[O]')
        viewMenu = menubar.addMenu('&View[V]')
        helpMenu = menubar.addMenu('&Help[H]')
        #添加事件
        fileMenu.addAction(openFileAction)
        fileMenu.addAction(exitAction)
#--------------------------状态栏------------------------------------
        # 状态栏1，有关文件
        toolbar1 = self.addToolBar('tool1')
        toolbar1.addAction(FoldToolAction)
        toolbar1.addAction(SaveToolAction)
        toolbar1.addAction(PrintToolAction)

        #状态栏2，前进后退
        toolbar2 = self.addToolBar('tool2')
        toolbar2.addAction(BackToolAction)
        toolbar2.addAction(ForwardToolAction)
        
        #状态栏3 编译运行
        toolbar3 = self.addToolBar('tool3')
        toolbar3.addAction(RunToolAction)
        toolbar3.addAction(DebugToolAction)
        toolbar3.addAction(CancelToolAction) 
        
        #状态栏4 数据
        toolbar4 = self.addToolBar('tool4')
        toolbar4.addAction(DataToolAction)
        toolbar4.addAction(SetToolAction)
        toolbar4.addAction(SearchToolAction)

        self.text1 = QTextEdit()
        self.text2 = QTextEdit()
        self.text3 = QTextEdit()

        #QMainWindow的中心窗口部件
        mainwidget = QWidget()
        #创建布局
        layout = QHBoxLayout()
        layout.addWidget(self.text1)
        self.text1.setMaximumWidth(600)
        vbox = QVBoxLayout()
        vbox.addWidget(self.text2)
        vbox.addWidget(self.text3)
        layout.addLayout(vbox)
        

        mainwidget.setLayout(layout)
        self.setCentralWidget(mainwidget)

    #右侧显示分词结果
    #预处理，将文件中的空格，换行等无关字符处理掉
    def output(self,_str):
        
        try: # 尝试是否能通过数字形式输出，如果能即为常数，否则为字符
            z = f"{int(_str)}\t26"+"\n"
        except ValueError:
            if _str in reserved_words: # 判断是否为保留字
                z =  f"{_str}\t{reserved_words.index(_str) + 1}\t保留字"+"\n"
                word = ""
            elif _str in signs: # 判断是否为符号
                z = f"{_str}\t{signs[_str]}"+"\n"
            else: # 否则为标识符
                z = f"{_str}\t25\t标识符"+"\n"
                word = ""
        self.da += z


    def LexicalAnalysis(self):
        if self.fname[0]:
            f = open(self.fname[0],'r')
            sign = 0
            with f:
                code = f.read()
        for line in code.split("\n"): # 按行迭代
            word = "" # 类似缓冲区的作用
            flag = False # 标记是否为123这类常数
            _pass = False # 标记是否跳过这一个字符
            for index, letter in enumerate(line):
                if _pass: # 判断是否跳过当前字符
                    _pass = False
                    continue
                if letter in string.digits: # 判断当前是否为数字
                    flag = not bool(word) # 如果word里没有字符，而当前又读到了数字，那么就打上标记
                    word += letter # 将字符加入缓冲区
                    continue
                elif letter in letters: # 判断当前是否为字母
                    if flag: # 如果打过了标记， 而此时读到了字母，标识符是不能以数字开头的，所以分开
                        self.output(word) # 输出数字
                        word = "" # 清空缓冲区
                        flag = False # 取消标记
                    word += letter # 将当前的字母加入缓冲区
                    continue
                else: # 此时当前字符既不是数字也不是字母，为符号或空白字符
                    if word: # 判断缓冲区内是否有字符，有则输出
                        self.output(word)
                        word = ""
                    if letter in blank: # 如果当前为空白字符（空格、回车）则跳过
                        continue
                    if line[index:index + 2] == "//": # 处理掉注释
                        break # 直接break，跳出行迭代
                    # 判断当前字符是否为最后一个以及和下一个字符能否组成一组符号
                    if index != len(line) - 1 and line[index:index + 2] in signs: 
                        self.output(line[index:index + 2]) # 输出组合的字符
                        _pass = True # 跳过下一个字符
                    else: # 输出单个字符
                        self.output(letter)
                    word = "" # 清空缓冲区
        
        
        self.text2.setText(self.da)
    
    #左侧代码显示

    def funOpenFile(self):
        self.fname = QFileDialog.getOpenFileName(self,'打开文件','*.c')
        if self.fname[0]:
            f = open(self.fname[0], 'r')
            with f:
                data = f.read()    
                self.text1.setText(data)
        self.LexicalAnalysis()
        
    #def 

if __name__ =='__main__':
    #创建应用程序和对象
    app=QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())