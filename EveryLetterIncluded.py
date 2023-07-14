o = " "
i = "#"

letter_dict = {
     'A': [
        [o, i, i, i, i, i, o],
        [i, o, o, o, o, o, i],
        [i, o, o, o, o, o, i],
        [i, i, i, i, i, i, i],
        [i, o, o, o, o, o, i],
        [i, o, o, o, o, o, i],
        [i, o, o, o, o, o, i]
    ],
    'B': [
        [i, i, i, i, i, o],
        [i, o, o, o, o, i],
        [i, o, o, o, o, i],
        [i, i, i, i, i, o],
        [i, o, o, o, o, o],
        [i, o, o, o, o, o],
        [i, o, o, o, o, o]
    ],
    'C': [
        [o, i, i, i, i, o],
        [i, o, o, o, o, i],
        [i, o, o, o, o, o],
        [i, o, o, o, o, o],
        [i, o, o, o, o, i],
        [i, o, o, o, o, i],
        [o, i, i, i, i, o]
    ],
    'D': [
        [i, i, i, i, o, o],
        [i, o, o, o, i, o],
        [i, o, o, o, o, i],
        [i, o, o, o, o, i],
        [i, o, o, o, o, i],
        [i, o, o, o, i, o],
        [i, i, i, i, o, o]
    ],
    'E': [
        [i, i, i, i, i, i],
        [i, o, o, o, o, o],
        [i, o, o, o, o, o],
        [i, i, i, i, o, o],
        [i, o, o, o, o, o],
        [i, o, o, o, o, o],
        [i, i, i, i, i, i]
    ],
    'F': [
        [i, i, i, i, i, i],
        [i, o, o, o, o, o],
        [i, o, o, o, o, o],
        [i, i, i, i, o, o],
        [i, o, o, o, o, o],
        [i, o, o, o, o, o],
        [i, o, o, o, o, o]
    ],
    'G': [
        [o, i, i, i, i, o],
        [i, o, o, o, o, i],
        [i, o, o, o, o, o],
        [i, o, o, i, i, i],
        [i, o, o, o, o, i],
        [i, o, o, o, o, i],
        [o, i, i, i, i, o]
    ],
    'H': [
        [i, o, o, o, o, i],
        [i, o, o, o, o, i],
        [i, o, o, o, o, i],
        [i, i, i, i, i, i],
        [i, o, o, o, o, i],
        [i, o, o, o, o, i],
        [i, o, o, o, o, i]
    ],
    'I': [
        [i, i, i],
        [o, i, o],
        [o, i, o],
        [o, i, o],
        [o, i, o],
        [o, i, o],
        [i, i, i]
    ],
    'J': [
        [o, o, o, o, o, i],
        [o, o, o, o, o, i],
        [o, o, o, o, o, i],
        [o, o, o, o, o, i],
        [o, o, o, o, o, i],
        [i, o, o, o, o, i],
        [o, i, i, i, i, o]
    ],
    'K': [
        [i, o, o, o, i, o],
        [i, o, o, i, o, o],
        [i, o, i, o, o, o],
        [i, i, o, o, o, o],
        [i, o, i, o, o, o],
        [i, o, o, i, o, o],
        [i, o, o, o, i, o]
    ],
    'L': [
        [i, o, o, o, o, o],
        [i, o, o, o, o, o],
        [i, o, o, o, o, o],
        [i, o, o, o, o, o],
        [i, o, o, o, o, o],
        [i, o, o, o, o, o],
        [i, i, i, i, i, i]
    ],
    'M': [
        [i, o, o, o, o, o, i],
        [i, i, o, o, o, i, i],
        [i, o, i, o, i, o, i],
        [i, o, o, i, o, o, i],
        [i, o, o, o, o, o, i],
        [i, o, o, o, o, o, i],
        [i, o, o, o, o, o, i]
    ],
    'N': [
        [i, o, o, o, o, o, i],
        [i, i, o, o, o, o, i],
        [i, o, i, o, o, o, i],
        [i, o, o, i, o, o, i],
        [i, o, o, o, i, o, i],
        [i, o, o, o, o, i, i],
        [i, o, o, o, o, o, i]
    ],
    'O': [
        [o, i, i, i, i, o],
        [i, o, o, o, o, i],
        [i, o, o, o, o, i],
        [i, o, o, o, o, i],
        [i, o, o, o, o, i],
        [i, o, o, o, o, i],
        [o, i, i, i, i, o]
    ],
    'P': [
        [i, i, i, i, i, o],
        [i, o, o, o, o, i],
        [i, o, o, o, o, i],
        [i, i, i, i, i, o],
        [i, o, o, o, o, o],
        [i, o, o, o, o, o],
        [i, o, o, o, o, o]
    ],
    'Q': [
        [o, i, i, i, i, o],
        [i, o, o, o, o, i],
        [i, o, o, o, o, i],
        [i, o, o, o, o, i],
        [i, o, i, o, o, i],
        [i, o, o, i, o, i],
        [o, i, i, i, i, o]
    ],
    'R': [
        [i, i, i, i, i, o],
        [i, o, o, o, o, i],
        [i, o, o, o, o, i],
        [i, i, i, i, i, o],
        [i, o, o, i, o, o],
        [i, o, o, o, i, o],
        [i, o, o, o, o, i]
    ],
    'S': [
        [o, i, i, i, i, i],
        [i, o, o, o, o, o],
        [i, o, o, o, o, o],
        [o, i, i, i, i, i],
        [o, o, o, o, o, i],
        [o, o, o, o, o, i],
        [i, i, i, i, i, o]
    ],
    'T': [
        [i, i, i, i, i, i, i],
        [o, o, o, i, o, o, o],
        [o, o, o, i, o, o, o],
        [o, o, o, i, o, o, o],
        [o, o, o, i, o, o, o],
        [o, o, o, i, o, o, o],
        [o, o, o, i, o, o, o]
    ],
    'U': [
        [i, o, o, o, o, i],
        [i, o, o, o, o, i],
        [i, o, o, o, o, i],
        [i, o, o, o, o, i],
        [i, o, o, o, o, i],
        [i, o, o, o, o, i],
        [o, i, i, i, i, o]
    ],
    'V': [
        [i, o, o, o, o, o, i],
        [i, o, o, o, o, o, i],
        [i, o, o, o, o, o, i],
        [o, i, o, o, o, i, o],
        [o, i, o, o, o, i, o],
        [o, o, i, o, i, o, o],
        [o, o, i, o, i, o, o]
    ],
    'W': [
        [i, o, o, o, o, o, i],
        [i, o, o, o, o, o, i],
        [i, o, o, o, o, o, i],
        [i, o, o, i, o, o, i],
        [i, o, o, i, o, o, i],
        [i, o, o, i, o, o, i],
        [o, i, i, o, i, i, o]
    ],
    'X': [
        [i, o, o, o, o, o, i],
        [o, i, o, o, o, i, o],
        [o, o, i, o, i, o, o],
        [o, o, o, i, o, o, o],
        [o, o, i, o, i, o, o],
        [o, i, o, o, o, i, o],
        [i, o, o, o, o, o, i]
    ],
    'Y': [
        [i, o, o, o, o, i],
        [i, o, o, o, o, i],
        [o, i, o, o, i, o],
        [o, o, i, i, o, o],
        [o, o, o, o, o, o],
        [o, o, o, o, o, o],
        [o, o, o, o, o, o]
    ],
    'Z': [
        [i, i, i, i, i, i],
        [o, o, o, o, o, i],
        [o, o, o, o, i, o],
        [o, o, o, i, o, o],
        [o, o, i, o, o, o],
        [o, i, o, o, o, o],
        [i, i, i, i, i, i]
    ]
}

Sentence = ['W', 'E', 'L', 'C', 'O', 'M', 'E']

letter_count = len(Sentence)


for letters in Sentence:

    height = len(letter_dict[letters])
    width = len(letter_dict[letters][0])

    for y in range(height):

        for x in range(width):
            print(letter_dict[letters][y][x], end='')
        print()
    print()
