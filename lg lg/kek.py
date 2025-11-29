def welcome(name):
    print('Hello, ' + name)
    
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

def vowel_count(s):
    vowels = "aeiouAEIOU"
    count = 0
    for i in s:
        if i in vowels:
            count += 1
    return count

def consonant_count(s):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0
    for i in s:
        if i in consonants:
            count += 1
    return count

def reverse_string(s):
    return s[::-1]

person1 = {
    'name': 'Sok',
    'age': 23,
    'country': 'Cambodia'
}