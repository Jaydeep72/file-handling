def unique_words():
    print("Unique words:", set(words))  # set does not repeat values
def count_unique_words():
    print("Count of unique words:", len(set(words)))
def no_of_lines():
    print("The number of lines is:", len(paralines))
def first_last_capital():
    paragraph = ''.join(paralines).strip() # Join lines into a single paragraph
    capitalized = paragraph[0].upper() + paragraph[1:-2] + paragraph[-2].upper()+"."
    print("Paragraph with first and last letters capitalized:", capitalized)