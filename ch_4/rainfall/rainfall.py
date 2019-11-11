# Option 1
def rainfall_counter():
    city_rainfall = {}
    count = 0
    while True:
        name = input("Enter a city name: ")
        if name == "":
            for city, number in city_rainfall.values():
                print(f"{city}\n{number}")
            break
        else:
            rainfall = int(input("Enter the amount of rainfall: "))
            count += 1
            city_rainfall[count] = [name, rainfall]


# print(rainfall_counter())


# Option 2: use .get()
def rainfall_counter():
    city_rainfall = {}

    count = 0
    while True:
        city_name = input("Enter a city name: ")
        if not city_name:
            return "\n".join([city for city in city_rainfall.values()])
            break
        else:
            rainfall = input("Enter the amount of rainfall: ")
            city_rainfall[count] = city_rainfall.get(count, city_name + "\n") + rainfall
            count += 1


# print(rainfall_counter())


# Option 3: use try/except for rainfall amount, version 1


def rainfall_counter():
    city_rainfall = {}

    while True:
        city_name = input("Enter a city name: ")

        if not city_name:
            return " ".join([f"{city} {rain}" for city, rain in city_rainfall.items()])
            break
        else:
            try:
                rainfall = int(input("Enter the amount of rainfall: "))
            except ValueError:
                print("You need to enter a number.")
                rainfall = int(input("Enter the amount of rainfall: "))
            city_rainfall[city_name] = city_rainfall.get(city_name, 0) + rainfall


print(rainfall_counter())


# Option 3: use try/except for the rainfall input version 2
rainfall = {}

while True:
    city_name = input("Enter city name: ")
    if not city_name:
        break
    try:
        mm_rain = int(input("Enter mm rain: "))
    except ValueError:
        print("You need to enter a number")
        continue
    rainfall[city_name] = rainfall.get(city_name, 0) + int(mm_rain)

for city, rain in rainfall.items():
    print(f"{city}: {rain}")


# Option 4: use isdigit() to see if the user enters the appropriate value for rainfall
rainfall = {}

while True:
    city_name = input("Enter city name: ")

    if not city_name:
        break

    mm_rain = input("Enter mm rain: ").strip()
    if mm_rain.isdigit():
        mm_rain = int(mm_rain)
    else:
        print("You didn't enter a valid number; try again.")
        continue
    rainfall[city_name] = rainfall.get(city_name, 0) + mm_rain
for city, rain in rainfall.items():
    print(f"{city}: {rain}")

# Option 5: use defaultdict
from collections import defaultdict

city_rainfall = defaultdict(int)


while True:
    city_name = input("Enter a city name: ")
    if not city_name:
        break
    else:
        try:
            rainfall = int(input("Enter the amount of rainfall: "))
        except ValueError:
            print("You need to enter a number.")
            rainfall = int(input("Enter the amount of rainfall: "))
        city_rainfall[city_name] += rainfall

for name, rain in city_rainfall.items():
    print(name, rain)
