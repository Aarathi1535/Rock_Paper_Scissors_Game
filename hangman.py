import random
import stages
word_list = ['apple','beautiful','potato']
chosen_word = random.choice(word_list)

display = []
for i in range(len(chosen_word)):
    display += '_'
print(display)
lives = 6
game_over = False

while not game_over:
    guess_letter = input("Enter your letter:").lower()
    for i in range(len(chosen_word)):
        if chosen_word[i]==guess_letter:
            display[i] = guess_letter
    print(display)
    if guess_letter not in chosen_word:
        lives -= 1
        if lives==0:
            game_over = True
            print("You lost!")
    if '_' not in display:
        game_over = True
        print("You win!!")
    print(stages.stages[lives])
print("The word shosen was:",chosen_word)


