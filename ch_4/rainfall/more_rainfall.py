# Instead of printing the total rainfall for each city, print the total, as well as the average rainfall for reported days.
# Thus, if you were to enter 30, 20, and 40 for Boston, you would see that the total was 90, and that the average was 30.

# Option 1 - use .get()
def ave_total_rain():
    city_rainfall = {}
    numbers = []

    while True:
        city_name = input("Enter a city name: ")

        if not city_name:
            break
        else:
            try:
                rainfall_total = int(input("Enter the total rainfall: "))
            except ValueError:
                print("You need to enter a number. Please try again")
                print()
            city_rainfall[city_name] = city_rainfall.get(city_name, []) + [
                rainfall_total
            ]

    for rain in city_rainfall.values():
        print("Total rain:", sum(rain))
        print("Average rain:", int(sum(rain) / len(rain)))


# print(ave_total_rain())


# Option 2 - use defaultdict
from collections import defaultdict


def ave_total_rain():
    city_rainfall = defaultdict(list)

    while True:
        city_name = input("Enter a city name: ")

        if not city_name:
            break

        else:
            try:
                rainfall_total = int(input("Enter the total rainfall: "))
            except ValueError:
                print("You need to enter a number. Please try again")
                print()
                rainfall_total = int(input("Enter the total rainfall: "))
            city_rainfall[city_name].append(rainfall_total)

    for rain in city_rainfall.values():
        print("Total rain:", sum(rain))
        print("Average rainfall:", int(sum(rain) / len(rain)))
