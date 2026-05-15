import sys
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import random as rnd


root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(
    title="选择名单"
)
if not file_path:
    print("未选择")
    exit()
print(file_path)
blist = pd.read_excel(file_path)
MaxNum=len(blist)
print("参与抽奖的人数：",MaxNum)
print(blist)
while True:
    cmd = input("\n名单已输出，请按 Y 键继续抽奖,N结束抽奖: ").strip().upper()
    if cmd == 'Y':
        break
    if cmd == 'N':
        sys.exit()
    else:
        print("输入无效，请输入 Y 继续抽奖,N结束抽奖。")
rndNum=rnd.randint(1,MaxNum)
LP=blist.iloc[rndNum,1]
print("获奖者是：",LP)

