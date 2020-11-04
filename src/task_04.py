"""
Given a string of words, return the length of the shortest word(s).

Notes:

The input string will never be empty and you do not need to validate for different data types.
[execution time limit] 4 seconds (py3)

[input] string input_str

[output] integer
"""


# Answer 
def csShortestWord(input_str):
    words = input_str.split()
    
    shortest_word_len = min(len(word) for word in words)
    
    return shortest_word_len
    
print(csShortestWord("Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live"))
print(csShortestWord("not great programmer; just good programmer with great habits."))
print(csShortestWord("Truth can only be found in one place: the code"))
print(csShortestWord("Give man program frustrate him for day Teach man program frustrate him for lifetime"))
print(csShortestWord("ZxuvWBoofsTUtasPIhsuCJjttHhBuuHZoxZk\tWZxAkjdCqDpML"))      