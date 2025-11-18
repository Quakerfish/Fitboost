# Physical exercises
EasyPhy = [
    '5 Pushups', '5 Situps', '30 Second Plank', '10 Jumping Jacks',
    '20 Second Wall Sit', '5 Squats', '5 Lunges', '10 Arm Circles',
    '10 High Knees', '15 Second Side Plank'
]

MedPhy = [
    '10 Pushups', '10 Situps', '1 Minute Plank', '20 Jumping Jacks',
    '40 Second Wall Sit', '10 Squats', '10 Lunges', '20 Arm Circles',
    '20 High Knees', '30 Second Side Plank'
]

HardPhy = [
    '10 Pushups 3 Sets', '10 Situps 3 Sets', '1 Minute Plank 2 Sets',
    '20 Burpees', '50 Jumping Jacks', '20 Squats 3 Sets', '20 Lunges 3 Sets',
    '1 Minute Wall Sit', '30 High Knees 3 Sets', '1 Minute Side Plank 2 Sets'
]

# Mental exercises
EasyMen = [
    ("\nWhat is 1 + 1?\nAnswer: ", "2"),
    ("\nWhat is the opposite of white?\nAnswer: ", "black"),
    ("\nHow many sides is a triangle?\nAnswer: ", "3"),
    ("\nWhat is the closest planet to the sun?\nAnswer: ", "mercury"),
    ("\nWhat is the largest planet in the solar system?\nAnswer: ", "jupiter"),
    ("\nWhat is the name of the planet that we live in?\nAnswer: ", "earth"),
    ("\nWhat is 5 – 2?\nAnswer: ", "3"),
    ("\nWhat color is the sky on a clear day?\nAnswer: ", "blue"),
    ("\nWhat day comes after Monday?\nAnswer: ", "tuesday"),
    ("\nHow many legs does a spider have?\nAnswer: ", "8")
]

MedMen = [
    ("\nWhat is 15 × 6?\nAnswer: ", "90"),
    ("\nWho wrote Romeo and Juliet?\nAnswer: ", "william shakespeare"),
    ("\nWhat is the largest ocean on Earth?\nAnswer: ", "pacific ocean"),
    ("\nWhat color do you get when you mix blue and yellow?\nAnswer: ", "green"),
    ("\nWhat is 144 ÷ 12?\nAnswer: ", "12"),
    ("\nWhat gas do plants absorb from the atmosphere?\nAnswer: ", "carbon dioxide"),
    ("\nHow many continents are there on Earth?\nAnswer: ", "7"),
    ("\nWhat is 25 × 4?\nAnswer: ", "100"),
    ("\nWho painted the Mona Lisa?\nAnswer: ", "leonardo da vinci"),
    ("\nWhat is H2O commonly known as?\nAnswer: ", "water")
]

HardMen = [
    ("\nWhat is the square root of 81?\nAnswer: ", "9"),
    ("\nWho proposed the theory of relativity?\nAnswer: ", "albert einstein"),
    ("\nIf you have ₱1,000 and spend 35% of it, how much is left?\nAnswer: ", "650"),
    ("\nSolve: (25 ÷ 5) × (12 – 7)\nAnswer: ", "25"),
    ("\nWhat is 13 × 17?\nAnswer: ", "221"),
    ("\nName the smallest bone in the human body.\nAnswer: ", "stapes"),
    ("\nWhat is the chemical symbol for gold?\nAnswer: ", "au"),
    ("\nWhat is the capital city of Australia?\nAnswer: ", "canberra"),
    ("\nWhat is the cube of 3?\nAnswer: ", "27"),
    ("\nWho discovered penicillin?\nAnswer: ", "alexander fleming")
]

# Riddles
EasyRiddle = [
    ("What has hands but can’t clap?\nAnswer: ", "clock", "It tells time."),
    ("What has to be broken before you can use it?\nAnswer: ", "egg", "Often used in cooking."),
    ("What goes up but never comes down?\nAnswer: ", "age", "It increases every birthday.")
]

MedRiddle = [
    ("I speak without a mouth and hear without ears. What am I?\nAnswer: ", "echo", "You hear it in valleys."),
    ("The more you take, the more you leave behind. What are they?\nAnswer: ", "footsteps", "Think of hiking or walking."),
    ("What can fill a room but takes up no space?\nAnswer: ", "light", "It helps you see.")
]

HardRiddle = [
    ("I am the answer to this riddle. What am I?\nAnswer: ", "riddle", "You're solving one right now."),
    ("I exist only when you think of me. I vanish when ignored. What am I?\nAnswer: ", "thought", "It’s in your mind."),
    ("I am the mirror you avoid, the silence you fill, the question you fear. I am not the end, but I define your journey. What am I?\nAnswer: ", "purpose", "Think of why you wake up and what keeps you going.")
]

# Memory game
MemoryWord = [
    "R G B Y P", "L O V E S", "H A P P Y", "C O D E R",
    "S M A R T", "T R A I N", "F L A S H", "B R I G H T",
    "Q U I Z Z", "J U M P S", "A D V A N C E", "M I N D S",
    "G A M E R", "S K I L L S", "C R E A T E"
]

# Word scramble
Scrambled = [
    "exercise", "fitness", "stretch", "jumping", "running",
    "balance", "pushup", "situp", "agility", "strength",
    "basketball", "volleyball", "warmup", "endurance"
]

# ----------------- CARDS -----------------

PhysicalCards = [
    {"name": "Decrease 2 Reps", "description": "Subtract 2 reps from your next exercise", "type": "decrease_reps", "value": 2},
    {"name": "Increase 5 Seconds Hold", "description": "Increase hold duration by 5 seconds", "type": "debuff_increase_hold", "value": 5},
    {"name": "Add 3 Reps Challenge", "description": "Add 3 extra reps to your next exercise", "type": "debuff_increase_reps", "value": 3},
    {"name": "Rest Extra 10 Seconds", "description": "Take 10 extra seconds rest", "type": "rest_bonus", "value": 10}
]

MentalCards = [
    {"name": "Double Points", "description": "Your points for the next question are doubled", "type": "multiplier", "value": 2},
    {"name": "Skip Question", "description": "Skip one question safely", "type": "skip_question", "value": 0},
    {"name": "Extra Life", "description": "Gain one extra life", "type": "extra_life", "value": 1}
]
