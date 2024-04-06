import random
print("Name : Jay Kumar\nURN : 2203844 ")
articles = ["the", "a", "an"]
nouns = ["boy", "girl", "dog", "cat", "ball", "bat"]
verbs = ["kicked", "played", "took", "threw", "jumped"]
prepositions = ["on", "over", "under", "around", "through"]
conjunctions = ["and", "but", "or"]
adjectives = ["red", "big", "sore", "happy", "tall"]

def generate_sentence():
    sentence = []

    # Add optional adjective
    if random.random() < 0.5:
        sentence.append(random.choice(adjectives))

    sentence.append(random.choice(articles))
    sentence.append(random.choice(nouns))
    sentence.append(random.choice(verbs))
    sentence.append(random.choice(articles))
    sentence.append(random.choice(nouns))

    # Add optional prepositional phrase
    if random.random() < 0.5:
        sentence.append(random.choice(prepositions))
        sentence.append(random.choice(articles))
        sentence.append(random.choice(nouns))

    # Add optional conjunction and second independent clause
    if random.random() < 0.5:
        sentence.append(random.choice(conjunctions))
        sentence.append(random.choice(articles))
        sentence.append(random.choice(nouns))
        sentence.append(random.choice(verbs))
        sentence.append(random.choice(articles))
        sentence.append(random.choice(nouns))

    return " ".join(sentence)

print(generate_sentence())
