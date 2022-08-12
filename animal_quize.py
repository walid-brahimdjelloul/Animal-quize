# Are you a fan of quizzes? 
# In this project, you’ll build an animal quiz.
# Even though the questions are about animals,
# this project can be easily modified to be about any other topic

#What happens The program asks the player some questions about animals.
# They get three chances to answer each question
# you don’t want to make the quiz too difficult! 
# Each correct answer will score one point. 
# At the end of the quiz, 
# the program reveals the player’s final score.

scoore = 0

def get_answer(repose, answer):
     global scoore
     mistake = 0
     stil_guessing = True
     
     while stil_guessing and mistake <3:
          if repose.lower() == answer.lower():
               print('Correct answer')
               stil_guessing = False
               scoore += 1 
          else:
               if mistake < 2:
                    repose = input('wrong answer try again :')
               mistake += 1
          
          
     
     if mistake == 3:
          print('The right answer is this :', answer)
     print('your scoore is: ', scoore)

print('Hello to the animal quize ...')
repose = input('Which bear lives at the North Pole? ')
get_answer(repose, 'pole bear')

### you can put any think you want such as multipal choice quize
guess = input('Which one of these is a fish? \
A) Whale B) Dolphin C) Shark D) Squid.\
\n Type A, B, C, or D : ') 
get_answer(guess, 'C')