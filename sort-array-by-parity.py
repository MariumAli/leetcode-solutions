    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = []
        for x in A:
            if x % 2 == 0:
                res.insert(0, x)
            else:
                res.append(x)
        return res
                    
