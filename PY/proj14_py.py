import random

stages = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    '''
]

words = {
    "fruits": ["apple", "banana", "mango", "orange"],
    "cities": ["chennai", "nellore", "delhi", "mumbai"],
    "tech": ["python", "laptop", "computer", "mobile"]
}

category = random.choice(list(words.keys()))
word = random.choice(words[category])

lives = 6
display = []
guessed_letters = []

for _ in range(len(word)):
    display.append("_")

print("🎮 WELCOME TO HANGMAN GAME 🎮")
print("Category:", category)
print("Word:", " ".join(display))

game_over = False

while not game_over:
    guess = input("\nGuess a letter: ").lower()

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter!")
        continue
    else:
        guessed_letters.append(guess)

    found = False

    for i in range(len(word)):
        if word[i] == guess:
            display[i] = guess
            found = True

    if not found:
        lives -= 1
        print("❌ Wrong guess!")
        print(stages[6 - lives])

    print("Word:", " ".join(display))
    print("Guessed letters:", guessed_letters)
    print("Lives left:", lives)

    if "_" not in display:
        print("\n🎉 CONGRATULATIONS! YOU WON 🎉")
        print("The word was:", word)
        game_over = True

    if lives == 0:
        print("\n💀 GAME OVER! YOU LOST 💀")
        print("The word was:", word)
        game_over = True
