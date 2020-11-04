"""
Given two strings that include only lowercase alpha characters, str_1 and str_2, write a function that returns a new sorted string that contains any character (only once) that appeared in str_1 or str_2.

Examples:

csLongestPossible("aabbbcccdef", "xxyyzzz") -> "abcdefxyz"
csLongestPossible("abc", "abc") -> "abc"

[execution time limit] 4 seconds (py3)

[input] string str_1

[input] string str_2

[output] string
"""


# Answer
def csLongestPossible(str_1, str_2):    
    new_str = str_1 + str_2
    sorted_str = "".join(sorted(set(new_str)))
    
    return sorted_str
    
 
print(csLongestPossible("aretheyhere", "yestheyarehere"))
print(csLongestPossible("loopingisfunbutdangerous", "lessdangerousthancoding"))
print(csLongestPossible("inmanylanguages", "theresapairoffunctions"))
print(csLongestPossible("etxtxgxqxkrwu", "fvaqjrvnzeyed"))
print(csLongestPossible("lgdfstfrwoqow", "exqxomaynxdgx"))