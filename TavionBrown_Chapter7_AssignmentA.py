def main():
# Use to store the sentences
    sentences = []
# Letting the user enter X amount of sentences
    print("Enter your sentences (type 'END' to finish):")

# Infinite loop until you enter 'END'
    while True:
        sentence = input()
        if sentence.upper() == 'END':
            break
        sentences.append(sentence)

# Print the results on how many sentences you made
    print("\nYou entered the following sentences:")
    for sentence in sentences:
        print(sentence)

# Print the total results
    print(f"\nTotal number of sentences: {len(sentences)}")

# Execute the main function if the code is run directly
if __name__ == "__main__":
    main()
