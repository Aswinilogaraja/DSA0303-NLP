import nltk


sample_text = "I have a cat named kushi."


training_data = [("I", "PRP"), ("have", "VB"), ("a", "DT"), ("cat", "NN"), ("named", "VBN"), ("kushi", "NNP"), (".", ".")]


rules = [
    (r'^[0-9]+$', 'CD'),            (r'.*ed$', 'VBD'),           
    (r'.*ing$', 'VBG'),          
    (r'^[A-Z][a-z]*$', 'NNP'),   
    (r'.*', 'NN')       
]


def transform_tag(sentence, rules):
    tagged_words = []
    for word in sentence:
        for pattern, tag in rules:
            if nltk.re.match(pattern, word):
                tagged_words.append((word, tag))
                break
        else:
            
            tagged_words.append((word, 'NN'))
    return tagged_words


words = nltk.word_tokenize(sample_text)


tagged_words = transform_tag(words, rules)


print(tagged_words)
