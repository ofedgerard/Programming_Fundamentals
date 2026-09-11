def calories_per_minute(calories, duration):
    rate = round(calories/duration,1)
    return rate

def get_intensity(rate):
    if rate < 5.0:
        return "Low"
    elif rate <= 9.9:
        return "Moderate"
    else:
        return "High"
    

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
break_word = "Done"
i = 0 #counter for workout_names
while len(workout_names) >= 0:
    workout_name = input('Workout name (enter "Done" if finished): ').title() #collects workout name
    workout_names.append(workout_name)
    if workout_name != break_word:
        duration = int(input("Enter the duration of workout in minutes: ")) #collects duration in minutes
        workout_durations.append(duration)
        calories = int(input("Enter the number of calories burned: ")) #collects callories burned
        workout_calories.append(calories)
        rate = calories_per_minute(calories, duration) #calls calories_per_minute function to return rate
        intensity = get_intensity(rate) #uses rate from calories_per_minute to return intensity
        print("Result: ", duration, " min", " | ", calories, " cal" ," | ", intensity) #prints summary line for current workout
    elif workout_names[0] == break_word:
        print("There were no workouts logged")
        break
    else:
        print("summary goes here")
        break