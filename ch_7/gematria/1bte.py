# Create a dictionary whose keys are city names, and whose values are temperatures in Fahrenheit.
# Now use a dict comprehension to transform this dict into a new one, keeping the old keys but turning the values into the temperature in degrees Celsius.


city_temp_farenheit = {"Boston": 10, "Columbus": 20, "Chicago": 30}


city_temp_celsius = {
    city: int(((temp - 32) * 5) / 9) for city, temp in city_temp_farenheit.items()
}
print(city_temp_celsius)
