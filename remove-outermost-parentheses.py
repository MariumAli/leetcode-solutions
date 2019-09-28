class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        res, opened = [], 0
        for c in S:
            if c == '(' and opened > 0: res.append(c)
            if c == ')' and opened > 1: res.append(c)
            opened += 1 if c == '(' else -1
        return "".join(res)
    
    """
    Solution 2
    res = []
        balance = 0
        index = 0
        for j in range(len(S)):
            if S[j] == "(":
                balance += 1
            elif S[j] == ")":
                balance -= 1
            if balance == 0:
                res.append(S[index+1:j])
                index = j+1
        return "".join(res)
        """
