import random
import os
import time
from exercises import EasyMen, EasyPhy, MedMen, MedPhy, HardMen, HardPhy, MemoryWord, EasyRiddle, MedRiddle, HardRiddle, Scrambled, PhysicalCards, MentalCards

difficulty = random.randint(1, 3)

def slowprint(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.03)
    print()

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def physicalworkout():
    clear()
    slowprint("\n🎴 Select ONE card:")
    for i in range(1, 4):
        slowprint(f"{i}. Random Card")
    while True:
        chosencard = input("Choice (1/2/3): ").strip()
        if chosencard in ['1', '2', '3']:
            chosencard = int(chosencard)
            break
        else:
            slowprint("⚠️ Invalid choice! Please select 1, 2, or 3.")

    match difficulty:
        case 3:
            phy_activity = random.choice(EasyPhy)
        case 1:
            phy_activity = random.choice(MedPhy)
        case 2:
            phy_activity = random.choice(HardPhy)

    chosen_card = random.choice(PhysicalCards)
    modified_activity = phy_activity
    
    if chosen_card['type'] == 'decrease_reps':
        try:
            number, exercise = phy_activity.split(' ', 1)
            number = int(number) - chosen_card['value']
            number = max(number, 1)
            modified_activity = f"{number} {exercise}"
        except:
            pass

    elif chosen_card['type'] == 'debuff_increase_reps':
        try:
            number, exercise = phy_activity.split(' ', 1)
            number = int(number) + chosen_card['value']
            modified_activity = f"{number} {exercise}"
        except:
            pass

    elif chosen_card['type'] == 'debuff_increase_hold':
        modified_activity += f" + Hold {chosen_card['value']} sec extra"

    elif chosen_card['type'] == 'rest_bonus':
        modified_activity += f" (Rest {chosen_card['value']} sec extra)"

    slowprint("\n🔥 ---EXERCISE TIME!!--- 💯")
    slowprint(f"🏃 You have to do {modified_activity} 💪")
    slowprint(f"✨ Your card effect: {chosen_card['name']}\n   {chosen_card.get('description', 'No description')}")
    return modified_activity, chosen_card

def mentalworkout():
    available_cards = random.sample(MentalCards, 3)

    match difficulty:
        case 1:
            questions = random.sample(EasyMen, 5)
        case 2:
            questions = random.sample(MedMen, 5)
        case 3:
            questions = random.sample(HardMen, 5)

    score = 0
    lives = 3
    multiplier = 1

    for q, correct_answer in questions:
        answered = False
        while not answered:
            clear()
            if difficulty == 1:
                all_answers = [a for _, a in EasyMen]
            elif difficulty == 2:
                all_answers = [a for _, a in MedMen]
            else:
                all_answers = [a for _, a in HardMen]

            if correct_answer in all_answers:
                all_answers.remove(correct_answer)

            distractors = random.sample(all_answers, 3)
            options = distractors + [correct_answer]
            random.shuffle(options)
            labels = ['A', 'B', 'C', 'D']
            option_dict = dict(zip(labels, options))

            slowprint(f"\n🧩 {q}")
            for label in labels:
                slowprint(f"{label}. {option_dict[label]}")

            if available_cards:
                slowprint("\n💎 Power Card:")
                for i, card in enumerate(available_cards, start=1):
                    slowprint(f"{i}. {card['name']}")

            choice = input("✍️ Your choice (A-D or card number 1-3): ").strip().upper()

            if choice in [str(i) for i in range(1, len(available_cards)+1)]:
                chosen_card = available_cards.pop(int(choice)-1)
                slowprint(f"\n✨ You used: {chosen_card['name']}\n{chosen_card['description']}")

                if chosen_card['type'] == 'extra_life':
                    lives += chosen_card['value']

                elif chosen_card['type'] == 'skip_question':
                    slowprint("⏩ You skipped this question!")
                    answered = True

                elif chosen_card['type'] == 'multiplier':
                    multiplier = chosen_card['value']

                continue

            if choice in labels:
                user_answer = option_dict[choice].lower()
                if user_answer == correct_answer.lower():
                    slowprint(f"✅ Correct! 💖 Lives Remaining: {lives}")
                    score += 1 * multiplier
                    multiplier = 1
                else:
                    slowprint(f"❌ Wrong! The correct answer is 👉 {correct_answer}")
                    lives -= 1
                    slowprint(f"❤️ Lives Remaining: {lives}")
                answered = True
            else:
                slowprint(f"❌ Invalid input! The correct answer is 👉 {correct_answer}")
                lives -= 1
                slowprint(f"❤️ Lives Remaining: {lives}")
                answered = True

            if lives <= 0:
                slowprint("💀 Game Over ☠️")
                return questions, available_cards

    slowprint(f"\n🎉 Your total score is {score}/{len(questions)}")
    return questions, available_cards

def riddlegame():
    match difficulty:
        case 1:
            activity = random.sample(EasyRiddle, 1)
        case 2:
            activity = random.sample(MedRiddle, 1)
        case 3:
            activity = random.sample(HardRiddle, 1)

    score = 0
    lives = 3

    while True:
        for q, a, h in activity:
            user_input = input(f"❓ Riddle: {q} ").strip().lower()

        if user_input == a:
            print("✅ Correct!")
            score += 1
            print(f"💖 Lives Remaining: {lives}")
            break
        else:
            print("❌ Wrong!")
            print(f"💡 Hint: {h}")
            lives -= 1
            print(f"❤️ Lives Remaining: {lives}")

        if lives == 0:
            print(f"\n💀 Game Over ☠️\nThe answer was 👉 {a}")
            break

def memorygame():
    activity = random.choice(MemoryWord)
    for number in range(3, 0, -1):
        print(f"🧠 ---PATTERN IT!!---\n\nRemember this pattern: {activity}")
        print(f"⏳ Clearing in {number} seconds")
        time.sleep(1)
        print("🧹 Clearing...")
        clear()
    print("🔎 ---PATTERN MEMORY---")
    answer = input("What was the pattern?\n✍️ Answer: ").strip().upper()
    if answer.replace(" ", "") == activity.replace(" ", ""):
        print("\n✅ CORRECT! 🎉")
    else:
        print("\n❌ INCORRECT!! 😢")
    return activity

def wordle():
    print("🔤 ---WORD SCRAMBLE--- 🎲")
    activity = random.choice(Scrambled)
    letters = list(activity)
    random.shuffle(letters)
    scrambled = "".join(letters)
    score = 0
    lives = 3
    while True:
        print(f"🤔 Guess the word: {scrambled}")
        user_input = input("✍️ Your answer: ").strip().lower()
        if user_input == activity:
            print("✅ Correct!! 🎉")
            score += 1
            print(f"💖 Lives Remaining: {lives}")
            break
        else:
            print("❌ Wrong!")
            lives -= 1
            print(f"❤️ Lives Remaining: {lives}")
        if lives == 0:
            print(f"💀 ---GAME OVER!!!--- ☠️\nThe answer was 👉 {activity}")
            break

def reactiontime():
    print("⚠️  Press Enter to start the Reaction Time Test...")
    print("⏳ Get ready...")
    time.sleep(random.randint(2, 5))
    starting = time.time()
    input("🚀 Press Enter as fast as you can!")
    ending = time.time()
    reactiontime = ending - starting
    slowprint(f"⏱️  Your reaction time is {reactiontime:.3f} seconds!")

# def adventuregame():
#     def monsterencounter():
#         slowprint("You hear something coming towards you...")
#         choice3 = input("---DECISION!---\n1️⃣  Hide\n2️⃣  Wait")
#         while True:
#             if choice3 == '1' or choice3 == 'hide':
#                 slowprint("You narrowly hid and the monster went by...")
#                 return True
#             else:
#                 slowprint("The monster found you and chased you...\nThe monster eventually catched you and asked you a question...")
#                 break
#         gameselector = random.randint(1, 2)
#         match gameselector:
#             case 1:
#                 activity = random.sample(EasyMen, 1)
#                 for q, a in activity:
#                     user_input = input(f"🧩 {q} ").strip().lower()
#                 if user_input == a:
#                     slowprint("The monster spares you and leaves...")
#                     return True
#             case 2:
#                 activity = random.choice(Scrambled)
#                 letters = list(activity)
#                 random.shuffle(letters)
#                 scrambled = "".join(letters)
#                 print(f"🤔 Guess the word: {scrambled}")
#                 user_input = input("✍️ Your answer: ").strip().lower()
#                 if user_input == activity:
#                     slowprint("The monster spares you and leaves...")
#                     return True
#             case 3:
#                 activity = random.sample(EasyRiddle, 1)
#                 for q, a in activity:
#                     user_input = input(f"❓ Riddle: {q} ").strip().lower()
#                     if user_input == a:
#                         slowprint("The monster spares you and leaves...")
#                         return True
#         slowprint("The monster eats you")
#         slowprint("---GAME OVER---")
#         return False

#     slowprint("\n🏞️ ---ADVENTURE GAME--- 🏕️")
#     slowprint("You wake up in an abandoned classroom\nThere was no one around you and the room was dark")
#     slowprint("You: Where am I? What is this place?")
#     while True:
#         print("--DECISION!---\n1️⃣  Look around the room\n2️⃣  Sit and wait")
#         choice = input("✍️ Your choice: ").strip().lower()
#         if choice == '1' or choice == 'look around the room':
#             slowprint("You explore the room and find the door")
#             break
#         elif choice == '2' or choice == 'sit and wait':
#             slowprint("You sit and wait...\nA few minutes passed and nothing happened")
#     while True:
#         choice2 = input("--DECISION!---\n1️⃣  Open Door\n2️⃣  Explore\nChoice:").strip().lower()
#         if choice2 == '1' or choice2 == 'open door':
#             break
#         if choice2 == '2' or choice2 == 'explore':
#             slowprint("You explore the Room and find nothing!\nYou return back to the door...")
#     slowprint("You arrived in the Hallway! The hallway was dark and the building looked old with dust and vines coming out")
#     while True:
#         choice = input("---DECISION!!!---\n1️⃣  Explore\n2️⃣  Wait\nChoice:").strip().lower()
#         if choice == '1' or choice == 'explore':
#             break
#         elif choice == '2' or choice == 'wait':
#             game = monsterencounter()
#             if game == False:
#                 return
#         else:
#             slowprint("Time is ticking... Decide Now!")
