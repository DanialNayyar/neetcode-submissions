class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        hashmap = {}
        max_allowed = (len(nums))/3
        answer = []

        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] +=1

        for key, value in hashmap.items():
            if value > max_allowed:
                print(f"print worked: {hashmap}")
                print(f"Only Keys: {hashmap.keys()}")
                print(f"Only Values: {hashmap.values()} ")
                answer.append(key)
                print(f"Answer: {answer}")


        return answer                        