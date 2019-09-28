    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        stones= list(S)
        for jewel in J:
            count += stones.count(jewel)
        return count
