"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    return annual_cost / SEMESTERS_PER_YEAR


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    return annual_cost / MONTHS_PER_YEAR


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    return cost_per_semester(annual_cost) / CLASS_DAYS_PER_SEMESTER


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    return cost_per_semester(annual_cost) / credits


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    return cost_per_credit(annual_cost, credits) * CS1430_CREDITS / CS1430_MEETINGS_PER_SEMESTER

def cost_of_skipped_classes(classes_skipped, annual_cost, credits):
    return cost_per_class(annual_cost, credits) * classes_skipped


# ---- PROGRAM ----

def main():
    annual_cost = float(input("Total cost for one year: $"))
    credits = int(input("Credits this semester: "))

    while True:
        print("Cost of College: ")
        print("1 Per semester")
        print("2 Per month")
        print("3 Per day")
        print("4 Per credit")
        print("5 Per CS 1430 class")
        print("6 Amount of CS 1430 classes wanting to skip")
        print("Q Quit")

        choice = input("Choose an option: ")
        if choice == "1":
            print(f"One semester of college costs: ${cost_per_semester(annual_cost):.2f}")
        
        elif choice == "2":
            print(f"One month of college costs: ${cost_per_month(annual_cost):.2f}")
        
        elif choice == "3":
            print(f"One day of college costs: ${cost_per_day(annual_cost):.2f}")

        elif choice == "4":
            print(f"One credit costs: ${cost_per_credit(annual_cost, credits):.2f}")

        elif choice == "5":
            print(f"One CS 1430 class costs: ${cost_per_class(annual_cost, credits):.2f}")

        elif choice == "6":
            classes_skipped = int(input("How many CS 1430 classes do you want to skip? "))
            print(f"{classes_skipped} CS 1430 classes skipped results in a loss of: ${cost_of_skipped_classes(classes_skipped, annual_cost, credits):.2f}")
        
        elif choice == "Q":
            print("Goodbye, have a great day!")
            break

        elif choice == "q":
            print("Goodbye, have a great day!")
            break

        else:
            print("Sorry, that is not a valid input. Please choose a different option: ")


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
