from letters import letter_count, letter_frequency

# Function that returns the letter with the highest frequency
def highest_freq(letter):
    # Returns the max value 
    x = letter_frequency(letter_count(letter))
    max_value = max(x.values())

    #returns the letter with the max value
    max_letter = max(x, key = x.get)
    return (max_letter, max_value)

experiment_highest_freq = highest_freq('frost.txt')
print(highest_freq('frost.txt'))
# assertion statement for the highest frequency
expected_highest_frequency = ('e', 0.10952380952380952)
assert(expected_highest_frequency  == experiment_highest_freq)
