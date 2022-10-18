# ------------------------------------------------------ #
# abstract : assignment 1 Question 1 Emirp 回文质数
# author : hhk
# time : 2022.10.13
# ------------------------------------------------------ #
from math import sqrt

def is_prime(num):
    """
    whether it is prime or not 判断是否为质数
    """
    for rea in range(2,int(sqrt(num)+1)):
        if num==1 : return False
        if num%rea==0:
            return False
    return True

def is_palindrome(num):
    """
    whether it is Emirp or not 判断回文是不是质数、回文是否等于自己
    """
    temp=num
    total=0
    while temp>0:
        total=total * 10+temp % 10
        temp//=10
    return is_prime(total) and (total!=num)

# 输入
number = int(input('Please input an integer ：'))
a = 1
ans = []
while(number>0):
    if is_palindrome(a) and is_prime(a) :
        ans +=[a]
        number -=1
    a +=1

# 输出
for i in range(len(ans)):
    print(str(ans[i]).rjust(6), end='')      # .rjust补全n个字符
    if (i+1)%10 == 0:                        # 每10个数换行一次
        print("\n")

