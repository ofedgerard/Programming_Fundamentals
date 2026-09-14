"""
Author: Gerard Ortiz
Date: 9/13/2026
Tier Level: Intermediate

Description:
program will collect information about a series of workout sessions and 
report on the user's performance for each one using loops and functions
"""

#Takes calories and duration to calculate the rate of calroeis burned per min
def calories_per_minute(calories, duration):
    rate = round(calories/duration,1)
    return rate

#Takes the rate from calories_per_minute and determines intestity of workout
def get_intensity(rate):
    if rate < 5.0:
        return "Low"
    elif rate <= 9.9:
        return "Moderate"
    else:
        return "High"#

#takes a list and uses a for loop to calculate and return the total and lenght of the list
def calculate_total(list):
    list_total = 0
    List_lenght = 0
    for i in list:
        list_total += i
        List_lenght = List_lenght + 1
    return list_total, List_lenght

#Uses calculate_total to calculate the average of a list
def calculate_average (list):
    list_total, list_lenght = calculate_total(list)
    list_average = round(list_total/list_lenght,1)
    return list_total, list_average

#Takes a the list of user input workout_names and calories burned and returns which workout burned the most calories
def find_best_workout(names, calories):
    best_workout_name = ""
    best_workout_calories = 0
    for names, calories in zip(names, calories):
        if calories > best_workout_calories:
            best_workout_calories = calories
            best_workout_name = names
        elif calories == best_workout_calories:
            best_workout_calories = best_workout_calories
            best_workout_name = best_workout_name
    return best_workout_calories, best_workout_name


def get_workout(durations): #this function calls the calories_per_minute and get_intensity functions to shorten the main body
    duration = int(input("Enter the duration of workout in minutes: ")) #collects duration in minutes
    calories = int(input("Enter the number of calories burned: ")) #collects callories burned
    rate = calories_per_minute(calories, duration)
    intensity = get_intensity(rate)
    durations.append(duration)
    return duration, calories, rate, intensity

workout_names = []
workout_durations = []
workout_calories = []
workouts_logged = 1

while len(workout_names) >= 0:
    print("--- Workout ", workouts_logged , " ---")
    workout_name = input('Workout name (enter "Done" if finished): ').title() #collects workout name
    workout_names.append(workout_name)
    if workout_name != "Done":
        duration = int(input("Enter the duration of workout in minutes: ")) #collects duration in minutes
        workout_durations.append(duration)
        calories = int(input("Enter the number of calories burned: ")) #collects callories burned
        workout_calories.append(calories)
        rate = calories_per_minute(calories, duration) #calls calories_per_minute function to return rate
        intensity = get_intensity(rate) #uses rate from calories_per_minute to return intensity
        print("Result: ", duration, " min", " | ", rate, " cal/min" ," | ", "Intensity: ",intensity) #prints summary line for current workout
        workouts_logged = workouts_logged +1
        print()
    elif workout_names[0] == "Done":
        workout_names.remove("Done")
        break
    else:
        workout_names.remove("Done")
        print()
        print("="*6, "Session Summary", "="*6)
        print("Workouts logged: ", workouts_logged-1)
        total_calories, average_calories = calculate_average(workout_calories)
        print("Total Calories: ", total_calories, "\nAverage Calories: ", average_calories)
        best_workout_calories, best_workout_name = find_best_workout(workout_names, workout_calories)
        print("Most Calories Burned: ", best_workout_calories, "\nWorkout Name: ", best_workout_name)
        print("="*29, "\n")
        break

if len(workout_names) > 0:
    print("All workouts logged. Great job staying active!", "\n")
else:
    print("There were no workouts logged", "\n")
