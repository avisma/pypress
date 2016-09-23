# letter dist. test

import random
import string

def showRandomLetters(n):

    letters = []
    number = []
    alph = string.ascii_uppercase

    for i in range(n):

        letters.append(random.choice(string.ascii_uppercase))

    for i in range(len(string.ascii_uppercase)):

        number.append(letters.count(alph[i]))

        number[i] = round(number[i] / n, 3)

    for i in range(len(string.ascii_uppercase)):

        print("{0}: {1}%".format(alph[i], number[i]))

    print('Total %: {0}%'.format(sum(number)))

def getRandomLetterDistribution(n):

    maxVowels = random.randint(5,8)

    print(maxVowels)

    letterList = []

    finished = False

    letterProb = [8.167, 9.658999999999999, 12.440999999999999,
                  16.694, 29.396, 31.624000000000002, 33.639,
                  39.733000000000004, 46.699000000000005, 46.852000000000004,
                  47.624, 51.649, 54.055, 60.804, 68.311, 70.24000000000001,
                  70.33500000000001, 76.322, 82.649, 91.705, 94.463,
                  95.44099999999999, 97.80099999999999, 97.951, 99.925, 99.999]

    lowLimit = 0
    hiLimit = 1
    vowels = 0

    while len(letterList) < n:
        finished = False
        lowLimit = 0
        hiLimit = 1

        x = random.choice(range(100)) / 100

        while not finished:

            if lowLimit == 0 and x < (letterProb[lowLimit] / 100):
                if not vowels >= maxVowels:
                    letterList.append('A')
                    #print('A')
                    vowels = vowels + 1
                    letter = 'A'
                else:
                    print('-----------------Nope------------------')
                finished = True

            elif (letterProb[lowLimit] / 100) <= x < (
                                            letterProb[hiLimit] / 100):
                
                letter = string.ascii_uppercase[hiLimit]
                letterList.append(letter)

                if letter == 'Q':
                    letterList.append('U')
                if letter in ['A', 'E', 'I', 'O', 'U']:
                    vowels = vowels + 1
                    if vowels >= maxVowels:
                        print('----------------Nope----------------', letter)
                        del letterList[-1]
                        
                finished = True

            else:

                lowLimit = lowLimit + 1
                hiLimit = hiLimit + 1
        print("{0:02}, {1:02}, {2:4.2}, {3:5.2f}, {4}".format(lowLimit, hiLimit, letterProb[hiLimit], x, letter))

    return letterList

def main():

    print('What would you like to do?')
    print('Type "a" to see a random letter selection, or "b" to get a')
    ans = input('random letter distribution suitable for word games. ')
    n = int(input('How many letters would you like the program to retrieve? '))

    if ans == 'a':
        showRandomLetters(n)
    elif ans == 'b':
        letterList = getRandomLetterDistribution(n)
        print(letterList)
    else:
        print('Sorry, the input was not correct. Please type either "a" or "b" without'
              'quotation marks. Please run the program again.')

    

if __name__ == '__main__':
    main()

##letterProbs = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094,
##               6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929,
##               0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150,
##               1.974, 0.074]

##    for i in range(len(letterProbs)):
##        number.append(sum(letterProbs[0:i + 1]))
##    print(number)

##A   8.167%     F   2.228%     K   0.772%     P   1.929%     U   2.758%     Z   0.074%
##B   1.492%     G   2.015%     L   4.025%     Q   0.095%     V   0.978%
##C   2.782%     H   6.094%     M   2.406%     R   5.987%     W   2.360%
##D   4.253%     I   6.966%     N   6.749%     S   6.327%     X   0.150%
##E  12.702%     J   0.153%     O   7.507%     T   9.056%     Y   1.974%

        

    
