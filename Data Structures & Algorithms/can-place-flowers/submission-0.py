class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        # bed = [1,0,0,0,1], n = 1
        potential_spots = []
        for i in range(len(flowerbed)):
            if flowerbed[i]!=0:
                continue

            left_check = (i==0) or (flowerbed[i-1]==0)
            right_check = (i== len(flowerbed)-1) or (flowerbed[i+1]==0)

            if left_check and right_check:
                potential_spots.append(i)
                flowerbed[i] =1
            
        return len(potential_spots) >= n