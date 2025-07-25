import random

subject = [
    "nawaz shareef",
    "imran khan",
    "babar azam",
    "a lahore car",
    "a group of monkeys",
    "prime minister",
    "an auto rikshaw driver from lahore"
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war",
    "orders",
    "celebrates"
]

placesorthings = [
    "at red fort",
    "lahore local train",
    "a plate of samosa",
    "inside parliament",
    "at ganga ram hospital",
    "during PSL match",
    "at Pakistan"
]

while True:
    chosen_subject = random.choice(subject)
    chosen_action = random.choice(actions)
    chosen_place = random.choice(placesorthings)

    headline = f"BREAKING NEWS: {chosen_subject} {chosen_action} {chosen_place}"
    print("\n" + headline)

    user_input = input("Do you want another headline (yes/no)? ").strip().lower()
    if user_input == "no":
        break

print("Thanks for using fake news generator!")
