class Solution:
    def groupAnagrams(self, strs):  
        str_list = list(strs)
        used = [False] * len(str_list)
        result = []

        for i in range(len(str_list)):
            if used[i]:
                continue

            group = [str_list[i]]          #new group with i
            used[i] = True
            chars_i = list(str_list[i])    #once per i

            for j in range(i + 1, len(str_list)):
                # skip if already grouped or lengths differ
                if used[j] or (len(str_list[i]) != len(str_list[j])):
                    continue

                #copy of j for the removal test
                temp_list_j = list(str_list[j])

                is_anagram = True
                for ch in chars_i:         #reuse chars_i 
                    if ch in temp_list_j:
                        temp_list_j.remove(ch)
                    else:
                        is_anagram = False
                        break

                if is_anagram:
                    group.append(str_list[j])  # j to THIS group
                    used[j] = True             # regroup j later

            result.append(group)               # finished this group's scan

        return result
