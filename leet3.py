
import math
import re




def func(s):


    if( 1 <= len(s) <= pow(10,4) ):

       out = []

      

       if len(s) == 1:
        return [-1]
       max = -1
       s.reverse()
       print(s)
       for i in range(len(s)):
         print(s[i])

         if s[i] > pow(10,5):
           return []

         out.append(max)

         if max < s[i]:
              max = s[i]
    out.reverse()      
    return out


          

            

print(func([17,18,5,4,6,1]))

    
# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/








