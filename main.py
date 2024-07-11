def count_words():
    # Prompt the user to enter a sentence or paragraph
    user_input = input("Please enter a sentence or paragraph: ").strip()

    # Check if the input is empty
    if not user_input:
        print("Error: No input provided. Please enter a valid sentence or paragraph.")
        return

    # Split the input into words
    words = user_input.split()

    # Count the number of words
    word_count = len(words)

    # Print the word count to the console
    print(f"Word Count: {word_count}")

# Call the function to execute the word counting logic
count_words()
