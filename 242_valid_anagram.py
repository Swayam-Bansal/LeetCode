#Solution 1: Brute force (sort arrays)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if two given strings are not of equal lens just return false, since they can never be anagrams
        if len(s) != len(t):
            return False
        
        # sort the strings given ...
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        # now compare the given sorted strings
        # if they are equal then they are anagram, else just return false
        if sorted_s == sorted_t:
            return True

        return False
    

# Solution 2: Use hashmaps ... 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if two given strings are not of equal lens just return false, since they can never be anagrams
        if len(s) != len(t):
            return False
        
        hashmap_s = {}
        hashmap_t = {}

        for char in s:
            hashmap_s[char] = hashmap_s.get(char, 0) + 1

        for char in t:
            hashmap_t[char] = hashmap_t.get(char, 0) + 1

        for char in hashmap_s :
            if hashmap_s.get(char) != hashmap_t.get(char, 0):
                return False
            
        return True
        
