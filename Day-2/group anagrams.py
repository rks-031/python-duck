class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        m = defaultdict(list)

        for str in strs:
            s = ''.join(sorted(str))

            if s in m:
                m[s].append(str)
            else:
                m[s] = [str]

        for k,v in m.items():
            ans.append(v)
        
        return ans