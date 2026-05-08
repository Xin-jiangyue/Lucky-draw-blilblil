import tkinter as tk
from tkinter import filedialog
import pandas as pd
import random as rnd

from pip._internal.utils import filetypes

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(
    title="选择名单"
)
print(file_path)
blist = pd.read_excel(file_path)
MaxNum=len(blist)
print("参与抽奖的人数：",MaxNum)
print(blist)
rndNum=rnd.randint(1,MaxNum)
LP=blist.iloc[rndNum,2]
print("获奖者是：",LP)

