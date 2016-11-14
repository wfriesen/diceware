import random

NUMBER_OF_WORDS = 7


def generatekey():
    rng = random.SystemRandom()
    return ''.join([str(rng.randint(1, 6)) for i in range(5)])


def generatephrase():
    with open('beale.wordlist.txt') as wordlist:
        words = {entry.split()[0]: entry.split()[1] for entry in wordlist}

    return ' '.join([words[generatekey()] for i in range(NUMBER_OF_WORDS)])

if __name__ == "__main__":
    print(generatephrase())
