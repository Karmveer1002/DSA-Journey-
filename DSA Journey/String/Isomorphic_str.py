class Solution:
    def isomorphicString(self, s, t):
        if len(s)!=len(t):
            return False
        mapst={}
        mapts={}

        for i in range (len(s)):
            c_s = s[i]
            c_t = t[i]

            if c_s in mapst:
                if mapst[c_s]!=c_t:
                    return False
                
            elif c_t in mapts:
                if mapts[c_t]!=c_s:
                    return False
            else:
                mapst[c_s]=c_t
                mapts[c_t]=c_s
        return True