def word_count(filepth) -> int:
    with open (filepth, "r") as file:
        text = file.read()
    words = text.split()
    return len(words)

def char_count(filepth) -> dict:
    with open (filepth, "r") as file:
        text = file.read()
    text = text.lower()
    counter = {}
    for i in range(len(text)):
        if text[i].isalpha():
            if text[i] in counter.keys():
                counter[text[i]] += 1
            else:
                counter[text[i]] = 1
    return counter        
