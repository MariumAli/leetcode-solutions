    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        skyline_lr = []
        skyline_tb = grid[0][:]
        for inner_list in grid:
            skyline_lr.append(max(inner_list))
            for i,val in enumerate(inner_list):
                if skyline_tb[i] < val:
                    skyline_tb[i] = val
        diff=[]
        
        for ind, inner_list in enumerate(grid):
            temp = []
            for x in skyline_tb:
                if skyline_lr[ind] < x:
                    temp.append(skyline_lr[ind])
                else:
                    temp.append(x)    
            diff.append(sum([j - i for i, j in zip(inner_list, temp)]))
            
        return(sum(diff))
