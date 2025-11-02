class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])
out = Solution()
print(out.reverseWords("Here   We Go!!"))

##Better version/ simpler too

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        return " ".join(s).strip()
out = Solution()
print(out.reverseWords("Here   We Go!!"))
