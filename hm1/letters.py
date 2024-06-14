import string
# function that count letter amount in file
def letter_count(file = 'frost.txt'):
    # reads file and converts into a string (lowercase with no spaces)
    f = open(file)
    str = f.read()
    str = str.replace(' ', '').replace('\n', '').lower()

    # makes letter dictionary (all letters = 0)
    dict = {}
    dict = dict.fromkeys(string.ascii_lowercase,0)

    # counts the amount of letters within a string
    # Goes through all the letters within the string then adds them to the dictionary
    for letter in str:
        if letter in dict:
            dict[letter] +=1
    return dict    

#function that counts the frequency of each letter
def letter_frequency(input):
    # input is a dictionary
    total = 0
    # go to the dictionary and add to total 
    for letter in input:
        total += input[letter]

    d = {}
    # Gets the frequency of each letter by dividing by total
    for letters in input:
        d[letters] = input[letters]/total
    return d
    
file_name = 'frost.txt'
experiment_count = letter_count(file_name)
experiment_freqency = letter_frequency(letter_count(file_name))

print(letter_count(file_name))
print(letter_frequency(letter_count(file_name)))

# assert function for letter_count
expected_count = {'a': 13, 'b': 2, 'c': 6, 'd': 10, 'e': 23, 'f': 12, 'g': 2, 'h': 12, 'i': 23, 'j': 0, 'k': 2, 'l': 6, 'm': 3, 'n': 9, 'o': 20, 'p': 1, 'q': 0, 'r': 14, 's': 14, 't': 20, 'u': 5, 'v': 2, 'w': 8, 'x': 0, 'y': 3, 'z': 0}
assert(expected_count == experiment_count )

# assert function for letter_frequency 
expected_frequency = {'a': 13/210, 'b': 2/210, 'c': 6/210, 'd': 10/210, 'e': 23/210, 'f': 12/210, 'g': 2/210, 'h': 12/210, 'i': 23/210, 'j': 0/210, 'k': 2/210, 'l': 6/210, 'm': 3/210, 'n': 9/210, 'o': 20/210, 'p': 1/210, 'q': 0/210, 'r': 14/210, 's': 14/210, 't': 20/210, 'u': 5/210, 'v': 2/210, 'w': 8/210, 'x': 0/210, 'y': 3/210, 'z': 0/210}
assert(expected_frequency == experiment_freqency )

