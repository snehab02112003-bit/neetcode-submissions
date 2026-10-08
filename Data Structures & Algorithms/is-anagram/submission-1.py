class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
     c_s = {}
     c_t={}
     
     for char in s : 
        if char in c_s:
            c_s[char]+=1
        else :
            c_s[char]=1
        
     for char in t : 
        if char in c_t:
            c_t[char]+=1
        else :
            c_t[char]=1 
     
     return c_s == c_t 