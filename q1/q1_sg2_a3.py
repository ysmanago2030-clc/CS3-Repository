#list containing all zodiac signs per year, assigned to a certain index
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

#main input statement where it asks the integer value of user's birth year
user_year = int(input("Enter your birth year: "))

#calculates zodiac year and checks for valid inputs (>= 1900)
if user_year >= 1900:
    print("Your zodiac sign is :", zodiac_sign[(user_year - 1900) % 12])
else:
    print("Invalid Year, it should not be earlier than 1900")
