    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        lst = list(moves)
        
        if lst.count('U') == lst.count('D') and lst.count('R') == lst.count('L'):
            return True
        return False
