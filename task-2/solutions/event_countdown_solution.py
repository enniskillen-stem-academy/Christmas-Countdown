import datetime

# Function to calculate days until the event
def get_days_until_event(event_date):
    today = datetime.date.today()
    return (event_date - today).days

# ASCII art for the event
def display_ascii_art():
    print("🎉🎉🎉")
    print("  *   ")
    print(" ***  ")
    print("***** ")

# Main function
def main():
    print("Welcome to the Event Countdown Program!")

    # Get event details from the user
    event_name = input("Enter the name of the event (e.g., Birthday): ")
    year = int(input("Enter the year of the event (YYYY): "))
    month = int(input("Enter the month of the event (MM): "))
    day = int(input("Enter the day of the event (DD): "))

    try:
        # Create a date object for the event
        event_date = datetime.date(year, month, day)

        # Calculate days left until the event
        days_left = get_days_until_event(event_date)

        # Display the countdown
        print(f"Only {days_left} days left until {event_name}!")
        display_ascii_art()
    except ValueError:
        print("Invalid date entered. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
