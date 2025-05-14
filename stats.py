def count_words(text):    
    return text.split()

def count_characters(text):
    letterCount = {}
    for c in text:
        letter = c.lower()
        if letter in letterCount:
            letterCount[letter] += 1
        else:
            letterCount[letter] = 1
    return letterCount
    
def pretty_print(letterDict):
    sortedLetters = sorted(letterDict.keys())

    for letter in sortedLetters:
        if letter.isalpha():
            print(f"{letter}: {letterDict[letter]}")