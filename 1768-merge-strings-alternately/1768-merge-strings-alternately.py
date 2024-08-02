class Solution(object):
    def mergeAlternately(self, word1, word2):
        result=""
        i,j=0,0
        len1,len2=len(word1),len(word2)
        while i<len1 and j<len2:
            result +=word1[i]+word2[j]
            i+=1
            j+=1
        result+=word1[i:]+word2[j:]
        return result
        