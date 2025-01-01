import random

def get_horoscope(zodiac_sign):
    horoscopes = {
        "Aries": ["Today is a great day for bold decisions.", "Stay cautious; unexpected challenges may arise."],
        "Taurus": ["Focus on self-care and relaxation today.", "Your persistence will pay off in unexpected ways."],
        "Gemini": ["New opportunities are on the horizon.", "Communication is key to resolving ongoing issues."],
        "Cancer": ["Embrace your emotions and trust your instincts.", "A close friend may need your support today."],
        "Leo": ["Your charisma will attract new opportunities.", "Avoid conflicts and stay positive today."],
        "Virgo": ["Your attention to detail will be rewarded.", "Take time to organize your thoughts and plans."],
        "Libra": ["Harmony in relationships will bring you joy.", "Be open to compromise in tough situations."],
        "Scorpio": ["Your passion will drive success today.", "Be mindful of your temper in challenging moments."],
        "Sagittarius": ["Adventure is calling; take the leap.", "Patience will be your best friend today."],
        "Capricorn": ["Hard work will bring recognition.", "Take a break to appreciate your achievements."],
        "Aquarius": ["Innovative ideas will flow freely today.", "Be mindful of how you express your opinions."],
        "Pisces": ["Let your creativity shine through today.", "Take time to reflect and recharge."]
    }

    return random.choice(horoscopes.get(zodiac_sign, ["Invalid zodiac sign."]))

def main():
    print("Welcome to the Zodiac Horoscope CLI!")
    print("Select your Zodiac Sign to get your daily horoscope:")

    zodiac_signs = [
        "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
        "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
    ]

    for i, sign in enumerate(zodiac_signs, start=1):
        print(f"{i}. {sign}")

    try:
        choice = int(input("Enter the number corresponding to your Zodiac Sign: "))
        if 1 <= choice <= 12:
            zodiac_sign = zodiac_signs[choice - 1]
            horoscope = get_horoscope(zodiac_sign)
            print(f"\nYour daily horoscope for {zodiac_sign} is:")
            print(f"{horoscope}\n")
        else:
            print("Invalid choice. Please select a number between 1 and 12.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()