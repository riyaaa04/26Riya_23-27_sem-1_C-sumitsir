#Write a program to compute the frequency of the words from the input. Theoutput should output after sorting the key alphanumerically.
def word_frequency(input_text):
    words = input_text.split()
    word_freq = {}

    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    sorted_word_freq = dict(sorted(word_freq.items()))
    return sorted_word_freq

# Get user input
user_input = input("Enter a sentence or phrase: ")

# Calculate word frequency and sort alphanumerically
result = word_frequency(user_input)

# Display the sorted word frequency
print("Word Frequency (Alphanumerically Sorted):")
for word, frequency in result.items():
    print(f"{word}: {frequency}")
