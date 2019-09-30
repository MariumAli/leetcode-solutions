import math
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        res=[]
        deck.sort(reverse=True)
        for num in deck:
            res.insert(0, num)
            res.insert(1, res.pop())
        return res
        
#         deck.sort()
#         new_deck = [] 
        
#         while deck: 
#             n = deck.pop() 
#             new_deck.insert(0,n)
#             end = new_deck.pop()
#             new_deck.insert(0,end)
            
#         front = new_deck.pop(0)
#         new_deck.append(front)
            
#         return new_deck
