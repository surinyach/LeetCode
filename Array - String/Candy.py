class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        
        n = len(ratings)
        candy = n
        right = 1
        left = 1

        cont_right = 0

        for i in range(0, n - 1):
            r = ratings[i + 1]
            l = ratings[i]

            if l > r:
                if  left == cont_right:
                    left += 1

                if right > 1:
                    right = 1
                else:
                    candy += left
                    left += 1
                  
            elif r > l:
                if right ==  1:
                    cont_right = 0
                candy += right
                right += 1
                cont_right += 1
                if left > 1: left = 1
                
            else:
                left = 1
                right = 1
                cont_right = 0

        return candy