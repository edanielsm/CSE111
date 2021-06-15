def print_death_age(people_dict):
    """For each person in the people dictionary,
    print the person's name and age at death.
    
    Parameter
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    
    for item in people_dict.items():
        key = item[0]
        person_age = item[1]

        age = person_age[DEATH_YEAR_INDEX]
        age2 = person_age[BIRTH_YEAR_INDEX]
        age3 = age - age2
        name = person_age[NAME_INDEX]
        
      

        print(f'{name}, {age3}')

