import random
import string

def hangman():
    words = ["python", "developer", "programming", "hangman", "keyboard", "challenge"]
    word = random.choice(words).lower()
    word_letters = set(word)  # Letters in the word
    guessed_letters = set()   # Correctly guessed letters
    alphabet = set(string.ascii_lowercase)  # All lowercase letters
    
    attempts = 6  # Number of tries
    
    print("\n🎮 Welcome to Hangman! Try to guess the word. 🎮")
    
    while len(word_letters) > 0 and attempts > 0:
        print("\nWord: ", " ".join([letter if letter in guessed_letters else "_" for letter in word]))
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Attempts left: {attempts}")
        
        guess = input("\nGuess a letter: ").lower().strip(string.punctuation)
        
        if guess in guessed_letters:
            print("⚠️ You already guessed that letter. Try again!")
        elif guess in word_letters:
            guessed_letters.add(guess)
            word_letters.remove(guess)
            print("✅ Correct!")
        elif guess not in alphabet:
            print("❌ Invalid input. Please enter a letter.")
        else:
            attempts -= 1
            print(f"❌ Wrong guess! You lost 1 attempt.")
        
    # Game Over
    if attempts == 0:
        print(f"\n😞 You lost! The word was: {word}")
    else:
        print(f"\n🎉 Congratulations! You guessed the word: {word}")

# Run the game
hangman()


