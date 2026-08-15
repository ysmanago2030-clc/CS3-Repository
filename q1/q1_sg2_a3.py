zodiac_sign = [
    "Rat (鼠 / Shǔ)",
    "Ox (牛 / Niú)",
    "Tiger (虎 / Hǔ)",
    "Rabbit (兔 / Tù)",
    "Dragon (龙 / Lóng)",
    "Snake (蛇 / Shé)",
    "Horse (马 / Mǎ)",
    "Goat (羊 / Yáng)",
    "Monkey (猴 / Hóu)",
    "Rooster (鸡 / Jī)",
    "Dog (狗 / Gǒu)",
    "Pig (猪 / Zhū)"
]

user_year = int(input("Enter your birth year: "))

if user_year >= 1900:
    print("Your zodiac sign is :", zodiac_sign[user_year % 12])
    
elif user_year < 1900:
    print("Invalid Year, it should not be earlier than 1900")
    
else:
    print("Invalid Input, try again")
