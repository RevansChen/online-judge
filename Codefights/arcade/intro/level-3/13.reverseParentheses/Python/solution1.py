# Python3

def reverseParentheses(s):
    l = s.find('(')
    if l >= 0:
        r, count = 0, 0
        for r in range(l, len(s)):
            if s[r] == '(':
                count += 1
            elif s[r] == ')':
                count -= 1
            if count == 0:
                break
        return s[:l] + reverseParentheses(s[l + 1:r])[::-1] + reverseParentheses(s[r + 1:])
    return s
