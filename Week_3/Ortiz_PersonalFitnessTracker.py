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
    



workout_names = []
workout_durations = []
workout_calories = []
workout_name = ""
i = 0 #counter for workout_names
while len(workout_names) >= 0:
    workout_name = input('Workout name (enter "Done" if finished): ').title() #collects workout name
    if workout_name != "Done":
        workout_names.append(workout_name)
        duration = int(input("Enter the duration of workout in minutes: ")) #collects duration in minutes
        workout_durations.append(duration)
        calories = int(input("Enter the number of calories burned: ")) #collects callories burned
        workout_calories.append(calories)
        rate = calories_per_minute(calories, duration) #calls calories_per_minute function to return rate
        intensity = get_intensity(rate) #uses rate from calories_per_minute to return intensity
        print("Result: ", duration, " min", " | ", calories, " cal" ," | ", intensity) #prints summary line for current workout
else:
    print("summary goes here")