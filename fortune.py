# fortune.py - Version 1.0

print("🔮 Welcome to Aryan Singh's Fortune Teller (21JE1234) 🔮")

mood = input("How are you feeling today? (happy/sad/neutral): ").lower()

if mood == "happy":
    print("✨ Your fortune: Great things await you, Aryan! Keep smiling. ✨")
elif mood == "sad":
    print("✨ Your fortune: Tough times don’t last. Good things are coming. ✨")
elif mood == "neutral":
    print("✨ Your fortune: Stay calm. A surprise is on the way. ✨")
else:
    print("✨ Your fortune: Embrace every emotion—it's all part of the journey. ✨")
