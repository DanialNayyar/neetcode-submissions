class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashmap = {}
        no_lucky = -1
        largest = []
        for i in arr:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] +=1

        
        for key, value in hashmap.items():
            if key == value:
                largest.append(value)

        
        if largest:
            return max(largest)
        else:
            return no_lucky