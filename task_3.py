from random import randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def getjokes(joke_amount):
    i = 0
    i = int(i)
    joke_list = []
    while i < joke_amount:

        random_noun_ind = randrange(len(nouns))
        noun = nouns[random_noun_ind]

        random_adverb_ind = randrange(len(adverbs))
        adverb = adverbs[random_adverb_ind]

        random_adjective_ind = randrange(len(adjectives))
        adjective = adjectives[random_adjective_ind]

        joke_parts = noun + " " + adverb + " " + adjective

        joke_list.append(joke_parts)

        i = i + 1

    print(joke_list)
getjokes(int(input()))
