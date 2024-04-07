
# prompt the user to enter the number of males in a class.
number_of_males = int(input("Enter the number of male students: "))

# prompt the user to enter the total number of females in the class.
number_of_females = int(input("Enter the number of female: "))

# calculating the percentage of each gender.
total_students = number_of_males + number_of_females
male_percentage = (number_of_males / total_students) * 100
female_percentage = (number_of_females / total_students) * 100

print(f"The percentage of male students is: {male_percentage:.2f}%")
print(f"The percentage of female students: {female_percentage:.2f}%")
print(f" The total number of students in the class is: {total_students}")
