import random
import hangman_art
import hangman_words 


lives = 6

word_list=  hangman_words.word_list

display =[]
print(hangman_art.logo)


word = random.choice(word_list)
word_length = len(word)
for i in range(word_length):
    display += '_'


end_of_game = False

while end_of_game == False:
  guess = input("Enter your guess: ")
 
  if guess in display:
    print(f'you have already guessed {guess}')
  for position in range(word_length):
    letter = word[position]
    if letter == guess:
      display[position] = letter

  if guess not in word:
     
    lives -= 1
    if lives == 0:
      end_of_game =True
      print("You lose")
  print(f"{''.join(display)}")
  print(f"The word is {word}")
 

  if '_' not in display:
    end_of_game = True
    print('You win')

  print(hangman_art.stages[lives])
