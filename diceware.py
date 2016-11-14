import random
import sys


def generatekey():
    rng = random.SystemRandom()
    return ''.join([str(rng.randint(1, 6)) for i in range(5)])


def generatephrase(number_of_words):
    with open('beale.wordlist.txt') as wordlist:
        words = {entry.split()[0]: entry.split()[1] for entry in wordlist}

    return ' '.join([words[generatekey()] for i in range(number_of_words)])


def main():
    try:
        number_of_words = int(sys.argv[1])
    except (ValueError, IndexError):
        print('Usage: python diceware.py NUMBER_OF_WORDS')
        sys.exit(1)

    print(generatephrase(number_of_words))

if __name__ == "__main__":
    main()
