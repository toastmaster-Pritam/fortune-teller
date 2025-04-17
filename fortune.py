# fortune.py - Version 1.0

print("🔮 Welcome to Pritam Chakraborty's Fortune Teller (21JE0701) 🔮")

mood = input("How are you feeling today? (happy/sad/neutral): ").lower()

if mood == "happy":
    print("✨ Your fortune: Great things await you, Pritam! Keep smiling. ✨")
elif mood == "sad":
    print("✨ Your fortune: Tough times don't last. Good things are coming. ✨")
elif mood == "neutral":
    print("✨ Your fortune: Stay calm. A surprise is on the way. ✨")
else:
    print("✨ Your fortune: Embrace every emotion—it's all part of the journey. ✨")
