class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxcandy=max(candies)
        result=[]
        for i in candies:
            greatest=i+extraCandies>=maxcandy
            result.append(greatest)
        return result
        