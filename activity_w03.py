from datetime import datetime



def compute_age(birth):
	birthday = datetime.strptime(birth, "%Y-%m-%d")
	today = datetime.now()

	# Compute the difference between today and the birthday in years.
	years = today.year - birthday.year

	# If necessary, subtract one from the difference.
	if birthday.month > today.month or \
      (birthday.month == today.month and birthday.day > today.day):
		years -= 1

	return years
	


def pound_to_kg(weight):

	return weight/2.205


def in_to_cm(height):

	return height*2.54


def bmi(weight, height):

	return (10000*weight )/ (height**2)


def basal_metabolic_rate(gender, weight, height, age):
  gender = gender.lower()

  if gender == "woman" or gender == "women" or gender == "female":
    return 447.593 + 9.247*weight + 3.098 *height - 4.330  * age

  elif gender == "man" or gender =="men" or gender == "male":
    return  88.362 + 13.397 * weight + 4.799* height - 5.677 *age

  else:
    return 88.362 + 13.397 * weight + 4.799* height - 5.677 *age
	
def main():
  gender = input('What is your gender: \n> ')
  birthday = input('What is your birhtday (YYYY-MM-DD):\n> ')
  user_height = int(input('What is your height in inches:\n> '))
  user_weight = int(input('What is your weight in pounds:\n> '))
  age = compute_age(birthday)
  new_weight = pound_to_kg(user_weight)
  new_height = in_to_cm(user_height)
  bmr = basal_metabolic_rate(gender , new_weight , new_height , age)
  user_bmi = bmi(new_weight , new_height)
  print(f'Age: {age}\nWeight: {round(new_weight)} \nHeight: {round(new_height)} \nBody Mass Index: {round(user_bmi)} \nBasal Metabolic Rate (kcal/day): {round(bmr)}')


main() 