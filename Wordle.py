# Wordle.py - Created by Kevin Struna on 12/29/2024
# It's a Python cmd program meant to help solve wordles

# Global Variables
remainingLetters = list(map(chr, range(97, 123)))
excludedLetters = []
correctLetters = ['', '', '', '', '']
misplacedLetters = {}  # Dictionary to track misplaced letters
guesses = 0

def main():
    # Open the Words text file containing the dictionary of 5-letter words
    with open("words.txt", "rt") as file:
        wordList = file.read().splitlines()
    
    global guesses
    
    print("\nWelcome to the Wordle Solver!")
    while guesses < 6:
        # User makes a guess
        print("\nEnter your guess (must be 5 letters):")
        wordle = input().lower()
        if len(wordle) != 5 or not wordle.isalpha():
            print("Error: Wordle guesses must be 5 alphabetic characters.")
            continue
        
        # Update guesses
        guesses += 1

        # Process correct letters
        print("Did you guess any letters correctly? (y/n):")
        answer = input().lower()
        while answer == "y":
            print("Enter the correct letter:")
            letter = input().lower()
            print("Enter its position (0-4):")
            position = int(input())
            if 0 <= position <= 4:
                correctLetters[position] = letter
            else:
                print("Invalid position. Try again.")
            
            print("Do you have more correct letters? (y/n):")
            answer = input().lower()
        
        # Process misplaced letters
        print("Did you guess any letters correctly but in the wrong position? (y/n):")
        answer = input().lower()
        while answer == "y":
            print("Enter the misplaced letter:")
            letter = input().lower()
            print("Enter the position it was in (0-4):")
            position = int(input())
            if 0 <= position <= 4:
                if letter not in misplacedLetters:
                    misplacedLetters[letter] = []
                misplacedLetters[letter].append(position)
            else:
                print("Invalid position. Try again.")
            
            print("Do you have more misplaced letters? (y/n):")
            answer = input().lower()

        # Process excluded letters
        print("Enter letters to exclude (one at a time). Type 'done' when finished:")
        while True:
            letter = input().lower()
            if letter == 'done':
                break
            if letter.isalpha() and letter not in excludedLetters:
                excludedLetters.append(letter)
        
        # Filter word list based on user input
        filteredWords = filter_words(wordList, correctLetters, excludedLetters, misplacedLetters)
        if not filteredWords:
            print("No possible words found. Check your inputs!")
            break
        
        print(f"\nPossible words: {', '.join(filteredWords)}")
        if len(filteredWords) == 1:
            print("Congratulations! The word is:", filteredWords[0])
            break

    if guesses == 6:
        print("Game over! Better luck next time.")

def filter_words(wordList, correctLetters, excludedLetters, misplacedLetters):
    filtered = []
    for word in wordList:
        # Check correct letters
        if not all(letter == '' or word[i] == letter for i, letter in enumerate(correctLetters)):
            continue
        
        # Check excluded letters
        if any(letter in word for letter in excludedLetters):
            continue

        # Check misplaced letters
        if any(letter in word and word[i] == letter for letter, positions in misplacedLetters.items() for i in positions):
            continue
        if not all(letter in word for letter in misplacedLetters):
            continue

        filtered.append(word)
    return filtered

main()
