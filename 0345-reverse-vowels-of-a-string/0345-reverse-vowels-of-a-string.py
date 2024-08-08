class Solution(object):
    def reverseVowels(self, s):
        c=list(s)
        i=0
        j=len(s)-1
        v="aeiouAEIOU"
        while i<j:
            while i<j and c[i] not in v:
                i+=1
            while i<j and c[j] not in v:
                j-=1
            c[i],c[j]=c[j],c[i]
            i+=1
            j-=1
        return "".join(c)