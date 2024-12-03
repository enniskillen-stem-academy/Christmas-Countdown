import datetime
import random

def get_days_until_christmas():
    today = datetime.date.today()
    christmas = datetime.date(today.year, 12, 25)
    if today > christmas:
        christmas = datetime.date(today.year + 1, 12, 25)
    return (christmas - today).days

def load_messages(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return ["Merry Christmas!", "Happy Holidays!", "Ho Ho Ho!"]

def display_ascii_art():
    print("    🎄   ")
    print("    *    ")
    print("   ***   ")
    print("  *****  ")
    print(" ******* ")

def main():
    days_left = get_days_until_christmas()
    messages = load_messages("messages.txt")
    print(random.choice(messages).strip())
    print(f"Only {days_left} days left until Christmas!")
    display_ascii_art()

if __name__ == "__main__":
    main()
