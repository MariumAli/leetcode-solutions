    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [reversed((self.invertZerosAndOnes(lst))) for lst in A]
        
    def invertZerosAndOnes(self, lst):
        for i in range(0,len(lst)):
            lst[i] = 0 if lst[i] == 1 else 1
        return lst
