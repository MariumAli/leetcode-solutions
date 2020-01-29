def maxProfit(self, k: int, prices: List[int]) -> int:
    if len(prices)<2 or k<=0:
        return 0
    n=len(prices)
    if k>= len(prices)//2:
        return sum(prices[i+1]-prices[i] if prices[i+1]-prices[i]>0 else 0 for i in range(n-1))

    lo,hi=0,0
    profits,trans=[],[]
    while True:
        lo=hi
        while lo< n-1 and prices[lo+1]<=prices[lo]:
            lo+=1
        hi=lo
        while hi< n-1 and prices[hi+1]>=prices[hi]:
            hi+=1
        
        if lo==hi:
            break
            
        while trans:
            if prices[lo]<=prices[trans[-1][0]]:
                buy,sell=trans.pop()
                hq.heappush(profits,prices[sell]-prices[buy])
                if len(profits)>k:
                    hq.heappop(profits)
            elif prices[hi]>prices[trans[-1][1]]:
                buy,sell=trans.pop()
                hq.heappush(profits,prices[sell]-prices[lo])
                if len(profits)>k:
                    hq.heappop(profits)
                lo=buy
            else:
                break
        trans.append([lo,hi])
        
    while trans:
        buy,sell=trans.pop()
        hq.heappush(profits,prices[sell]-prices[buy])
        if len(profits)>k:
            hq.heappop(profits)
            

    return sum(profits)
    

    #####
        # def maxProfit(self, k: int, prices: List[int]) -> int:
        #     def compress(prices): 
        #         # remove intermediate values
        #         c = []
        #         n = len(prices)
        #         if len(prices) < 2:
        #             return c
        #         low, high = 0, 0
        #         while low < n - 1:
        #             while low < n - 1 and prices[low + 1] <= prices[low]:
        #                 low += 1
        #             high = low + 1
        #             while high < n - 1 and prices[high + 1] >= prices[high]:
        #                 high += 1
        #             if high <= n - 1:
        #                 c.extend([prices[low], prices[high]])
        #                 low = high + 1
        #         return c

        #     def reduce_one_pair(p):
        #         # Use triple to represent 
        #         # 1. index of pairs to remove or merge
        #         # 2. cost of remove or merge, we want to minimize cost
        #         # 3. action, 'r' for remove, 'm' for merge
        #         index, cost, action = 0, p[1] - p[0], 'r'
        #         for i in range(2, len(p), 2):
        #             a, b, c, d = p[i-2: i+2]
        #             if d - c < cost:
        #                 index, cost, action = i, d - c, 'r'
        #             if a < c < b and c < b < d and b - c < cost:
        #                 index, cost, action = i, b - c, 'm'
        #         i = index
        #         if action == 'm':
        #             p[i-1] = p[i+1]
        #         p[i:] = p[i+2:]
        #         return p


        #     prices = compress(prices)
        #     if not prices or k < 1:
        #         return 0
        #     while len(prices) > 2 * k:
        #         prices = reduce_one_pair(prices)
        #     return sum([prices[i] - prices[i-1] for i in range(1, len(prices), 2)])