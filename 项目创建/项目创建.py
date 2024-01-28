import time
from pathlib import Path
import os

def cjj(name,path):
    os.chdir(path)
    Path(name).mkdir()
def cjnj(name,path,content):
    os.chdir(path)
    with open(name,"w",encoding="utf-8") as f:
        f.write(content)
while True:
    inp1 = input('''创建路径：''')
    inp2 = input('''文件夹名：''')
    inp3 = input('''语言（支持Python和JavaScript）：''')
    print("正在创建文件夹“"+inp2+"”...")
    cjj(inp2,inp1)
   
    if inp3.lower() == "python":
        print("正在创建文件“依赖.py”...")
        cjnj("依赖.py",inp1+inp2,'''import random
pnl = []
peolist = []
class ERROR(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __str__(self):
        return f"{self.code}\n{self.message}"
class people:
    def __init__(self):
        self.x = 100
        self.g = 10
        self.q = 0
        self.h = 100
        self.s = random.randint(1, 10)
def cjp(name):
    peolist.append(people())
    pnl.append(name)
def xdxc(f, c, to=""):
    try:
        ft_index = pnl.index(f)
        ft = 'peolist[{}]'.format(ft_index)
        if to:
            tot_index = pnl.index(to)
            tot = 'peolist[{}]'.format(tot_index)
        else:
            tot = 'None'
    except ValueError:
        raise ERROR("人物错误", "缺少人物，请检查传入参数")

    command = c + '(' + ft + ',' + tot + ')'
    eval(command)
def hit(f,t):
    f.h = f.h - 1
    t.x = t.x - 1
        
        ''')
        print("正在创建文件“main.py”...")
        cjnj("main.py",inp1+inp2,'''from 依赖 import *
        ''')
    elif inp3.lower() == "javascript":
        print("正在创建文件“依赖.js”...")
        cjnj("依赖.js",inp1+inp2,'''var pnl = [];
var peolist = [];
export function cjp () {
	peolist[peolist.length] = {x:100,g:10,q:0,h:100,s:Math.floor(Math.random() * 101)};
	pnl[pnl.length] = name;
	
	
}
export function xdxc (from,c,to){
	ft_index = pnl.indexOf(f);
	ft = 'peolist['+ft_index+']'.format(ft_index);
	tot_index = pnl.indexOf(to);
	tot = 'peolist['+tot_index+']';
	eval('(' + ft + ',' + tot + ')');
}
function hit (from,to) {
	from.h --;
	to.x --;
}

        ''')
        print("正在创建文件“main.js”...")
        cjnj("main.js",inp1+inp2,'''import {cjp,xdxc} from 'temp1.js'
        ''')
        if input("是否需要创建“index.html”?") == "是":
            cjnj("index.html",inp1+inp2,'''<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
		<script src="main.js" type="text/javascript"></script>
	</body>
</html>

''')
            
    print('''创建成功，1秒后继续\n--------------------------------------------------------------''')
    time.sleep(1)

































