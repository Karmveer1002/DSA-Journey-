class Solution:    
    def anagramStrings(self, s, t):
        if len(s)!=len(t):
            return False
        freq={}
        for i in range(len(s)):
            if s[i] in freq:
                freq[s[i]]+=1
            else:
                freq[s[i]]=1
        for i in range(len(t)):
            if t[i] not in freq:
                return False
            freq[t[i]]-=1
        for i in freq:
            if freq[i]!= 0:
                return False
        return True