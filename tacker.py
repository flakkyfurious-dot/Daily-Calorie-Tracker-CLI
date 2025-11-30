import datetime

def main():
    print("="*50)
    print(" Welcome to the Daily Calorie Tracker CLI ")
    print("="*50)
    print("This tool lets you log meals, track calories,")
    print("compare against your daily limit, and save logs.\n")

    # Task 2: Input & Data Collection
    meals = []
    calories = []

    try:
        num_meals = int(input("How many meals do you want to enter today? "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    for i in range(num_meals):
        meal_name = input(f"Enter meal {i+1} name: ")
        try:
            calorie_amount = float(input(f"Enter calories for {meal_name}: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return
        meals.append(meal_name)
        calories.append(calorie_amount)

    # Task 3: Calorie Calculations
    total_calories = sum(calories)
    avg_calories = total_calories / len(calories) if calories else 0

    try:
        daily_limit = float(input("\nEnter your daily calorie limit: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    # Task 4: Exceed Limit Warning System
    if total_calories > daily_limit:
        status_msg = f"⚠️ Warning: You exceeded your limit by {total_calories - daily_limit:.2f} calories!"
    else:
        status_msg = f"✅ Good job! You are within your limit. Remaining: {daily_limit - total_calories:.2f} calories."

    # Task 5: Neatly Formatted Output
    print("\nCalorie Summary Report")
    print("-"*40)
    print("Meal Name\tCalories")
    print("-"*40)
    for meal, cal in zip(meals, calories):
        print(f"{meal}\t\t{cal}")
    print("-"*40)
    print(f"Total:\t\t{total_calories}")
    print(f"Average:\t{avg_calories:.2f}")
    print(status_msg)

    # Task 6 (Bonus): Save Session Log to File
    save_choice = input("\nDo you want to save this session log? (yes/no): ").strip().lower()
    if save_choice == "yes":
        filename = "calorie_log.txt"
        with open(filename, "w") as f:
            f.write("Daily Calorie Tracker Log\n")
            f.write(f"Timestamp: {datetime.datetime.now()}\n")
            f.write("-"*40 + "\n")
            f.write("Meal Name\tCalories\n")
            for meal, cal in zip(meals, calories):
                f.write(f"{meal}\t\t{cal}\n")
            f.write("-"*40 + "\n")
            f.write(f"Total:\t\t{total_calories}\n")
            f.write(f"Average:\t{avg_calories:.2f}\n")
            f.write(status_msg + "\n")
        print(f"📁 Session saved to {filename}")

if __name__ == "__main__":
    main()