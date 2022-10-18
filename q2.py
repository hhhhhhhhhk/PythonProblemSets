# ------------------------------------------------------ #
# abstract : assignment 1 Question 2 Integral 数值积分
# author : hhk
# time : 2022.10.13
# ------------------------------------------------------ #
import math
from math import sin,cos,tan

# set up a dict to hold available functions
func_dict = {
    "sin": sin,
    "cos": cos,
    "tan": tan,
}

def Intergral(funcName,a,b,n):                # 实参下划线，形参区分大小写
    """
    computer integral 计算数值积分
    """
    func = func_dict[funcName]     # 函数名能直接传
    ans = 0
    for i in range(1,n+1):
        ans += (b-a)/n*func(a+(b-a)/n*(i-1/2))
    print("answer is ",ans,end="\n")
    return ans

# --------- main part --------- #
while(1):
    print("hello,welcome!")
    # input function name
    func_name= input("please input a trigonometric function  ")             # input进来的都是str
    if not func_dict.__contains__(func_name):  # not表示取反，~按位取反
        print("input wrong function\n")
        continue
    # input a,b
    a = float(input("please input a bigger interval end points  "))
    b = float(input("please input a smaller interval end points  "))
    if b<a:
        print("input wrong a and b\n")
        continue
    # input n
    n = input("please input a number of sub-intervals n  ")
    if (not str.isdigit(n)) or int(n)<0:          # 判断字符串是否为整数
        print("input wrong n\n")
        continue
    n = int(n)
    # func_name,a,b,n = "sin",0,math.pi,20
    Intergral(func_name,a,b,n)
    print("bye~")
    break


