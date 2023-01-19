class Solution:
    def strongPasswordCheckerII(self, s: str) -> bool:
        if len(s) < 8:
            return False
        sp = "!@#$%^&*()-+"
        flag_low, flag_up, flag_d, flag_sp = False, False, False, False
        for i, c in enumerate(s):
            if c.islower():
                flag_low = True
            if c.isupper():
                flag_up = True
            if c.isdigit():
                flag_d = True
            if c in sp:
                flag_sp = True
            if i >= 1 and c == s[i-1]:
                return False
             
        return flag_low and flag_up and flag_d and flag_sp
           
        

                
        
        
        