def first_repeat(str):
    repeated = set()
    for word in str.split():
        if word in repeated:
            return word
        else:
            repeated.add(word)  
    return 'no repeats'

first_repeat('I was thinking that if I had had the opportunity')