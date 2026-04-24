class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #built in method
        #s.reverse()
        #print(s)
        
        #not built in method
        temp = []
        for i in range(len(s)-1, -1,-1):
            temp.append(s[i])
        #print("TEMP:", temp)

        for i in range(len(s)):
            s[i]=temp[i]
        #print("S:", s)
        return s
