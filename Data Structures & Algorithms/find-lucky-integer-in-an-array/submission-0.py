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
            else:
                largest.append(no_lucky)

        largest.sort(reverse = True)

        print(largest[0])

        return largest[0]