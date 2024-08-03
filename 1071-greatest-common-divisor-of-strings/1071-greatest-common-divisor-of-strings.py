class Solution(object):
    def gcdOfStrings(self, str1, str2):
        len1,len2=len(str1),len(str2)
        if str1+str2!=str2+str1:
            return ""
        elif str1==str2:
            return str1
        elif len1>len2:
            return self.gcdOfStrings(str1[len2:],str2)
        else:
            return self.gcdOfStrings(str2[len1:],str1)
        
        