# fortune.py - Version 1.2

import random

print("🔮 Welcome to Pritam Chakraborty's Fortune Teller (21JE0701) 🔮")

mood = input("How are you feeling today? (happy/sad/neutral): ").lower()

fortunes = {
    "happy": [
        "Great things await you, Pritam! Keep smiling.",
        "Happiness attracts success—stay positive!"
    ],
    "sad": [
        "Tough times don't last. Good things are coming.",
        "Even the darkest night ends with dawn."
    ],
    "neutral": [
        "Stay calm. A surprise is on the way.",
        "Balance is beautiful—enjoy the stillness."
    ],
    "stressed": [
        "Take a deep breath. You are stronger than you think.",
        "Calmness is your superpower, Pritam!"
    ]
}

if mood in fortunes:
    print(f"✨ Your fortune: {random.choice(fortunes[mood])} ✨")
else:
    print("✨ Your fortune: Embrace every emotion—it's all part of the journey. ✨")
