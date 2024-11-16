import random
from art import logo, vs
from game_data import data

score = 0
game_on = True

# Pull 2 random people from the list that cannot be the same
def new_person():
    return random.choice(data)


def compare_people(p1, p2):
    if p1["follower_count"] > p2['follower_count']:
        return "A"
    else:
        return "B"


person1 = new_person()
person2 = new_person()

while person1 == person2:
    person2 = new_person()

# Display the logo, first person, vs., then second person
print(logo)
print(f"Compare A: {person1['name']}, a {person1['description']}, from {person1['country']}.")
print(vs)
print(f"Against B: {person2['name']}, a {person2['description']}, from {person2['country']}.")

while game_on:
    # Ask user to guess who has more followers
    guess = input("Who has more followers? Type 'A' or 'B': ")

    # Compare the follower count of person 1 vs person 2 to see if they were correct
    answer = compare_people(person1, person2)

    # If they were wrong, display the score and tell them they lose. End game.
    if guess != answer:
        print("\n" * 20)
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_on = False

    # if they were correct, add 1 to their score, put person 2 in person 1's spot, and get another random person that cannot be the same as the first
    else:
        score += 1
        print("\n" * 20)
        print(logo)
        print(f"You're right! Current score: {score}.")
        person1 = person2
        person2 = new_person()
        while person1 == person2:
            person2 = new_person()
        print(f"Compare A: {person1['name']}, a {person1['description']}, from {person1['country']}.")
        print(vs)
        print(f"Against B: {person2['name']}, a {person2['description']}, from {person2['country']}.")