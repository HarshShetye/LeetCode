class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        best = total = sum(cardPoints[:k])
        for i in range (k-1, -1, -1):
            total += cardPoints[i + len(cardPoints) - k] - cardPoints[i]
            best = max(best, total)
        return best
    
        ''''
        total,i,j=0,0,-1
        if len(cardPoints)==k:
            return sum(cardPoints)
        elif k>2:
            total=cardPoints[0]+cardPoints[-1]
            i,j=1,-2
            for _ in range(k):
                if cardPoints[i]>cardPoints[j]:
                    total+=cardPoints[i]
                    i+=1
                else:
                    total+=cardPoints[j]
                    j-=1
                else:
                    if cardPoints[i]>cardPoints[j]:
                        total+=cardPoints[i]
                        i+=1
                    else:
                        total+=cardPoints[j]
                        j-=1

            return total   
            '''     