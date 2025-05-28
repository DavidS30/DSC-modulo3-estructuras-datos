
def reverse_sentence(setence):
    setence = setence.lower() # reverse this sentence
    sentence_list = setence.split(" ")
    sentence_list.reverse()
    sentence_list[0] = sentence_list[0].capitalize()
    return " ".join(sentence_list)

print(reverse_sentence("Reverse this sentence"))