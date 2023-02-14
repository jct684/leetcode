class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #O(m*n log n) time complexity
        #O(m*n) space complexity
        ana_dict = {}
        for word in strs:
            curr_word = sorted(word)
            curr_word = str(curr_word)
            if (ana_dict.get(curr_word, 0) == 0):
                ana_dict[curr_word] = [word]
            else:
                ana_dict[curr_word].append(word)
        ans = []
        for value in ana_dict.values():
            ans.append(value)
        return ans
        