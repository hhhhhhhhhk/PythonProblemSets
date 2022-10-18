# PythonProblemSets  
**Some introductory python programming questions**

## Question 1 Emirp 回文质数  
An emirp (prime spelled backward) is a nonpalindromic prime number whose reversal is also a prime.  
For example, both 17 and 71 are prime numbers, so 17 and 71 are emirps. Write a program that requires user to input an integer N, then displays the first N emirps. Display 10 numbers per line and align the numbers properly, as follows:  
     13  17  31  37  71  73  79  97  107 113  
    149 157 167 179 199 311 337 347  359 389  
    ....  
You can assume N ranges from 0 to 500.  
  
  
## Question 2 Integral 数值积分  
Given a function f(x), and a real interval [a, b], the numerical integration of f(x) over interval [a, b] can be calculated as:  
  
In equation above, n represents the number of sub-intervals into which the interval [a, b] will be divided; and it controls the accuracy of numerical integration.  
Write a program to allow the user to specify a trigonometric function f (f can only be sin, cos or tan), and input the interval end points a, b and number of sub-intervals n. Your program should then calculate the numerical integration of f over [a, b] using equation above, and output the result. Your program should be robust enough to handle possible improper inputs (e.g. the user inputs a floating point number as n; the user inputs a wrong function name).  
  
  
## Question 3 Locker puzzle 储物谜题
A school has 100 lockers and 100 students. All lockers are closed on the first day of school. As the students enter, the first student S1 opens every locker. Then the second student, S2, begins with the second locker, denoted as L2, and closes every other locker after L2 (which means 1,3,5,7… are opened and 2,4,6,8… are closed). Student S3 begins with the third locker and switches every third locker (closes it if it was open, and opens it if it was closed). Student S4 begins with locker L4 and changes every fourth locker. Student S5 starts with L5 and changes every fifth locker, and so on, until student S100 changes L100. After all the students have passed through the building and changed the lockers, which lockers are open? Write a program to find your answer, and print all indexes of lockers that are opened. Locker index starts from 1.(Hint: Use a list of 100 Boolean elements, each of which indicates whether a locker is open (True) or closed (False). Initially, all lockers are closed.)  
  
  
## Question 4 Binary Tree 二叉树  
Given a list of integers, build a class of binary tree (each node has at least two child nodes). For each node in the tree, value of its left child is always smaller than its own and value of its right child node is larger than its own.  
You are supposed to define classes of Node and BinaryTree.   
Node should contain properties of value, left and right children.  
BinaryTree must have functions as following,  
*_init_: initialize the class;  
insert: take integer as input. Starting from root node, place input to left side of existing node ifinput smaller than node value, and place it to right if larger than node value until an empty node found;  
search: take an integer as input, return node whose value equals to input, return None if no matched case;  
delete: take no input, delete all values in binary tree.  
printTree: print the numbers in tree in ascending order (Start with “Values in Tree:\n”; all numbers in one line). Print a “Nothing in Tree” if tree is empty.
Any other helper functions are allowed.*  
  
  
## Question 5 Permutation 排列  
Given a list of integers with no duplicated elements named numbers, sorted in ascending order. Print a list of all possible permutations (each element appears only once). You can assume the number of elements in list ranges from 1 to 100.  
Define a function named permute(), whose input is a list of integ.ers  
