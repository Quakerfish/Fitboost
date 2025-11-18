import random
import datetime
from workout import physicalworkout, mentalworkout, memorygame, adventuregame, wordle, riddlegame, reactiontime, slowprint, clear

def main_menu():
    clear()
    slowprint("💪🧠 --- FITBOOST --- 🎯\n")
    print("1️⃣  Play")
    print("2️⃣  Cards")
    print("3️⃣  Settings")
    print("4️⃣  Exit\n")

    while True:
        choice = input("Choose an option (1-4): ").strip()
        if choice == '1':
            play_game()
            break
        elif choice == '2':
            slowprint("📂 Cards feature coming soon!")
            input("Press Enter to return to main menu...")
            main_menu()
            break
        elif choice == '3':
            slowprint("⚙️ Settings feature coming soon!")
            input("Press Enter to return to main menu...")
            main_menu()
            break
        elif choice == '4':
            slowprint("Goodbye! 👋")
            exit()
        else:
            print("⚠️ Invalid input. Choose 1-4.")

def play_game():
    timedate = datetime.datetime.now()
    time = timedate.strftime("%H:%M %p")
    date = timedate.strftime("%B %d, %Y")

    name = input("👤 Name: ")
    course = input("📚 Course: ")
    print("\n---📌 SELECTION---\n")
    
    while True:
        slowprint("🤔 Choose activity:\n1️⃣ Physical 🏃\n2️⃣ Mental 🧩\n3️⃣ Random 🎲")
        type1 = input("🎯 Choice: ").strip().upper()
        if type1 in ['1','PHYSICAL']:
            chosen = 'Physical'
            break
        elif type1 in ['2','MENTAL']:
            chosen = 'Mental'
            break
        elif type1 in ['3','RANDOM']:
            chosen = 'Physical' if random.randint(1,2)==1 else 'Mental'
            break
        else:
            print("⚠️ Invalid input!")

    slowprint("\n🔥 ---EXERCISE TIME!!--- 💯")
    if chosen == 'Physical':
        currentactivity = physicalworkout()
    elif chosen == 'Mental':
        randomizer = random.randint(1, 5)
        match randomizer:
            case 1:
                currentactivity = memorygame()
            case 2:
                currentactivity = mentalworkout()
            case 3:
                currentactivity = wordle()
            case 4:
                currentactivity = riddlegame()
            case 5:
                currentactivity = reactiontime()
    
    slowprint("\n✅ Have you completed the Exercise?")
    input("(Yes/No): ")

    slowprint("\n🏆 ---RESULT!!--- 🎉\n")
    slowprint(f"👤 Name: {name}\n📚 Course: {course}")
    slowprint(f"🎯 Chosen Activity: {chosen}")
    slowprint(f"📅 Date Finished: {date}")
    slowprint(f"⏰ Time Finished: {time}\n")

    input("Press Enter to return to main menu...")
    main_menu()

# Start game
main_menu()
