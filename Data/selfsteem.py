print('''
This program is an implementation of the Rosenberg Self-Esteem Scale.
This program will show you ten statements that you could possibly
apply to yourself. Please rate how much you agree with each of the
statements by responding with one of these four letters:

D means you strongly disagree with the statement.
d means you disagree with the statement.
a means you agree with the statement.
A means you strongly agree with the statement.''')

def get_answer(response):
  if response == "A":
    return 3
  elif response == "D":
    return 0
  elif response == "d": 
    return 1
  elif response == "a":
    return 2

def get_negative_answer(response):
  if response == 'A':
    return 0
  elif response == 'a':
    return 1
  elif response == 'd':
    return 2
  elif response == 'D':
    return 3
# def compute_score: 
    

answer_one = input('1. I feel that I am a person of worth, at least on an equal plane with'
'others.\n> ')
final1 = get_answer(answer_one)

answer_two = input('2. I feel that I have a number of good qualities.\n> ')
final2 = get_answer(answer_two)

answer_three = input('3. All in all, I am inclined to feel that I am a failure.\n> ')
final3 = get_negative_answer(answer_three)

answer_four = input('4. I am able to do things as well as most other people.\n> ')
final4 = get_answer(answer_four)

answer_five = input('5. I feel I do not have much to be proud of.\n> ')
final5 = get_negative_answer(answer_five)

answer_six = input('6. I take a positive attitude toward myself.\n> ')
final6 = get_answer(answer_six)

answer_seven = input('7.On the whole, I am satisfied with myself.\n> ')
final7 = get_answer(answer_seven)

answer_eight = input('8.I wish I could have more respect for myself.\n> ')
final8 = get_negative_answer(answer_eight)

answer_nine = input('9. I certainly feel useless at times.\n> ')
final9 = get_negative_answer(answer_nine)

answer_ten = input('10. At times I think I am no good at all.\n> ')
final10 = get_negative_answer(answer_ten)

true_final = final1 + final2 + final3 + final4 + final5 + final6 + final7 + final8 + final9 + final10

print(f'Your scores is {true_final}')
print('A score below 15 may indicate problematic low self-esteem.')