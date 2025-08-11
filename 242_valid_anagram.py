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
        return sorted_s == sorted_t
   

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
    

# Solution 3: Usign arrays, making a hash table of all lower case letters
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = [0] * 26
        for i in range(len(s)):
            # ord('a') gives us the ASCII value of 'a', so we subtract it to get the index in the counter array
            # if they are anagrams, the counts will cancel out to zero
            # if not, the counts will not cancel out, and we will return false at the
            counter[ord(s[i]) - ord('a')] += 1
            counter[ord(t[i]) - ord('a')] -= 1

        for val in counter:
            if val != 0:
                return False
            
        return True

        
