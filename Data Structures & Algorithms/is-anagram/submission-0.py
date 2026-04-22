class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        length_of_s = len(s)
        length_of_t = len(t)
        if (len(s) == len(t) and "".join(sorted(s)) == "".join(sorted(t))):
            return True
        else:
            return False

