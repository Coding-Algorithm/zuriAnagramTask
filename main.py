# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    wordInvert = word[::-1]

    if (wordInvert == anagram):
        return True
    else:
        return False


find_anagram('owk', 'ewo')
