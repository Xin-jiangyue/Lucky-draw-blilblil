import pandas as pd
import random as rnd
blist = pd.read_excel("./抽奖名单.xlsx")
MaxNum=len(blist)
print(MaxNum)
print(blist)
rndNum=rnd.randint(1,MaxNum)
LUCYMAN=blist.iloc[rndNum,2]
print("获奖者是：",LUCYMAN)

