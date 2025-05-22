"""
Movie Age Check

Write a program that asks the user for their age and checks if they
are old enough to watch a PG-13 movie.

This activity practices using a simple if statement.
"""

# Instructions for students:
# 1. Ask the user for their age (convert input to an integer)
# 2. Check if they are 13 or older
# 3. If they are 13 or older, print a message saying they can watch the movie

# Solution HERE

user_age = int(input("How old are you? "))

if user_age >= 13:
    print("You can watch the movie.")
else:
    print("You cannot watch the movie.")


# to take this further

allowed_age_for_movie = 13
user_age = int(input("How old are you? "))

if user_age >= 13:
    print("You can watch the movie.")
else:
    print(f"You are too young. Come back in {abs(allowed_age_for_movie - user_age)} years.")



"""
Weather Activity Recommender

Create a program that:
1. Asks the user for today's weather (sunny, rainy, or snowy)
2. Uses if-else to recommend an appropriate activity
3. Tells the user to have a great day

This provides a practical, relatable example for if-else statements.
"""

# Instructions for students:
# 1. Ask the user for the current weather
# 2. Based on their input, recommend a suitable activity
# 3. Handle invalid inputs with a default message

# my solution

current_weather = input("Is it sunny, raining or snowy? ")

if current_weather.lower() == "sunny":
    print("You could go to the park for a picnic.")
elif current_weather.lower() == "raining":
    print("You could stay inside and read a book.")
elif current_weather.lower() == "snowy":
    print("You could build a snowman.")
else:
    print("Please input the weather: sunny, raining or snowy?")


# to do this weather using the or statement, use the method .lower() to convert to lower case

current_weather = input("Is it sunny, raining or snowy? ")

if current_weather == "Sunny" or current_weather == "sunny":
    print("You could go to the park for a picnic.")
elif current_weather == "Raining" or current_weather == "raining":
    print("You could stay inside and read a book.")
elif current_weather == "Snowy" or current_weather == "snowy":
    print("You could build a snowman.")
else:
    print("Please input the weather: sunny, raining or snowy?")





"""
Meal Recommendation System

Create a program that recommends what to eat based on the time of day.
The program will:
1. Ask the user for the current time (in hours, using 24-hour format)
2. Recommend a meal or snack based on the time
3. Add a friendly message with the recommendation
"""

# Instructions for students:
# 1. Ask the user for the current time in hours (0-23)
# 2. Convert the input to an integer
# 3. Use if-elif-else to recommend different meals based on time ranges
# 4. Include a default option for unusual times

# Solution HERE

current_time = int(input("What hour of the day is it? "))

if 0 <= current_time <5:
    print("You should be in bed!")
elif 5 <= current_time < 12:
    print("You could eat breakfast.")
elif 12 <= current_time < 16:
    print("You could eat lunch.")
elif 16 <= current_time < 21:
    print("You could eat dinner.")
elif 21 <= current_time <= 23:
    print("You could eat a dessert.")
else:
    print("Please enter the hour of the day e.g. 2")