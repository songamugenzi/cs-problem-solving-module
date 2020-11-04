"""
Given a string, return a new string with all the vowels removed.

Examples:

csRemoveTheVowels("Lambda School is awesome!") -> "Lmbd Schl s wsm!"

Notes:

For this challenge, "y" is not considered a vowel.
[execution time limit] 4 seconds (py3)

[input] string input_str

[output] string
"""


# Answer 
def csRemoveTheVowels(input_str):
    vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    new_str = input_str

    for x in input_str:
        if x in vowels:
            new_str = new_str.replace(x, "") 
    return new_str


print(csRemoveTheVowels("Lambda School is awesome!"))
print(csRemoveTheVowels("Talk is cheap. Show me the code."))
print(csRemoveTheVowels("f!a fbs,rI\\H[P^f}!h;!<\tyu>/`uD^d,xGDWPj{HU$m~$|_e#"))
print(csRemoveTheVowels("Programs must be written for people to read, and only incidentally for machines to execute."))
print(csRemoveTheVowels("km%]jf&rSit&*g#M,.hba?}\\k^%tT>E^pdS\\A,*IIZtVhrPGXr"))