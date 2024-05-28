import random

words = ["umbrella", "computer", "telescope", "smartphone"]
word = random.choice(words).upper()

total_chance = 7
guessed_word = "-" * len(word)
guessed_letters = []

while total_chance != 0:
    print(guessed_word)
    letter = input("Guess a letter: ").upper()
    
    if letter in guessed_letters:
        print("You already guessed that letter. Try again.")
        continue
    else:
        guessed_letters.append(letter)

    if letter in word:
        new_guessed_word = ""
        for index in range(len(word)):
            if word[index] == letter:
                new_guessed_word += letter
            else:
                new_guessed_word += guessed_word[index]
        guessed_word = new_guessed_word
        
        if guessed_word == word:
            print("Congratulations, you won!")
            print("The word was:", word)
            break
    else:
        total_chance -= 1
        print("Incorrect guess!")
        print("You have", total_chance, "chances left")

    if total_chance == 0:
        print("Game over. The word was:", word)
