class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_str = {}
        for i in strs:
            arr = [0]*26
            for j in i:
                arr[ord(j) - ord("a")] += 1

            temp = []
            for j in range(26):
                if arr[j]:
                    temp.append(chr(j + ord("a"))*arr[j])
            temp = "".join(temp)
            if temp not in sorted_str:
                sorted_str[temp] = [i]
            else:
                sorted_str[temp].append(i)

        ans = []
        for i in sorted_str:
            ans.append(sorted_str[i])
        return ans