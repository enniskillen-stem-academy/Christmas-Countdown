import datetime

# TODO: Complete this function to calculate days until the event
def get_days_until_event(event_date):
    today = datetime.date.today()
    # Subtract today's date from the event_date to get the difference in days
    # Hint: Use (event_date - today).days
    pass  # Replace this with your code

# ASCII art for the event
def display_ascii_art():
    print("🎉🎉🎉")
    print("  *   ")
    print(" ***  ")
    print("***** ")

# Main function
def main():
    print("Welcome to the Event Countdown Program!")

    # TODO: Fix the errors in the code below
    event_name = input("Enter the name of the event (e.g., Birthday): ")
    year = input("Enter the year of the event (YYYY): ")  # Missing conversion to int
    month = input("Enter the month of the event (MM): ")  # Missing conversion to int
    day = input("Enter the day of the event (DD): ")  # Missing conversion to int

    try:
        # TODO: Fix this line to correctly create a date object
        event_date = datetime.date(year, month, day)

        # TODO: Call the get_days_until_event function and store the result
        days_left = None  # Replace this with the correct function call

        # Display the countdown
        print(f"Only {days_left} days left until {event_name}!")
        display_ascii_art()
    except:
        print("Oops! Something went wrong. Check your code and try again.")

# Run the program
if __name__ == "__main__":
    # TODO: Call the main function
    pass  # Replace this with the correct function call
