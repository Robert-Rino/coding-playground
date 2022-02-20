'''
Description:
    REF: https://leetcode.com/problems/count-number-of-teams/submissions/
    
    There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

    You have to form a team of 3 soldiers amongst them under the following rules:

    Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
    A team is valid if: 
    - (rating[i] < rating[j] < rating[k]) or 
    - (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
    Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

Examples:
    Example 1:
    Input: rating = [2,5,3,4,1]
    Output: 3
    Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 

    Example 2:
    Input: rating = [2,1,3]
    Output: 0

Solution:
Find for each position, how many integer lesser/greater than this position.
sum up all lesser/grester case base on desending/accending case.
'''

class Solution:
    def numTeams(self, rating: list[int]) -> int:
        result = 0
        
        if len(rating) < 3:
            return result
        
        greater_and_lesser = []
        for i in range(len(rating)):
            lesser = 0
            greater = 0
            for j in range(i+1, len(rating)):
                if rating[i] > rating[j]:
                    lesser += 1
                elif rating[i] < rating[j]:
                    greater += 1
            greater_and_lesser.append((lesser, greater))
        
        for i in range(len(rating)):
            for j in range(i+1, len(rating)):
                if rating[i] > rating[j]:
                    # NOTE: descending,, find number lesser than rating[j]
                    result += greater_and_lesser[j][0]
                elif rating[i] < rating[j]:
                    # NOTE: accending, find number greater than rating[j]
                    result += greater_and_lesser[j][1]
        
        return result
