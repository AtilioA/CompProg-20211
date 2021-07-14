from itertools import permutations


words = {}
while True:
    noSucessor = None
    inputString = input()
    if inputString == '#':
        break

    inputStringPermutations = sorted({''.join(permutation) for permutation in permutations(inputString)})

    words[inputString] = {
        'perm': inputStringPermutations,
        'index': inputStringPermutations.index(inputString)
    }

for word in words:
    if (words[word]['index'] + 1 == len(words[word]['perm'])):
        print("No Sucessor")
    else:
        print(words[word]['perm'][words[word]['index'] + 1])
