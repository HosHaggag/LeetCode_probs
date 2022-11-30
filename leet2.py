
import math
import re
nums = [1,2,3,4,1]




def func(s , t):


    if( 1 < len(s) <= 5*pow(10,4) and  1 < len(t) <= 5*pow(10,4) and len(re.findall("[a-z]", s)) == len(s) and len(re.findall("[a-z]", t)) == len(t) ):

       print('valid')
       for i in nums:
         if i > pow(10,9):
           print(i)
           print(pow(10,9))
           return
            



func("nums" , "muns")

    









