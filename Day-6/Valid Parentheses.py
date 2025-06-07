class Solution:
    def isOk(self,ch, top):
        if (ch == ']' and top == '[') or (ch =='}' and top == '{') or (ch ==')' and top == '('):
            return True
        else:
            return False
    def isValid(self, s: str) -> bool:
        st = []
        if len(s) == 0:
            return True
        
        for ch in s:
            if ch in '({[':
                st.append(ch)
            elif not st or not self.isOk(ch,st[-1]):
                st.append(ch)
            else:
                st.pop()

        return not st
        