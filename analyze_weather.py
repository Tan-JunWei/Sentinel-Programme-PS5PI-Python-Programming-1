weather_data = [
    {"date": "2023-02-01", "temperature": 26, "humidity": 75, "precipitation": 0.2},
    {"date": "2023-02-02", "temperature": 32, "humidity": 80, "precipitation": 0.0},
    {"date": "2023-02-03", "temperature": 22, "humidity": 90, "precipitation": 0.5},
    # More entries can be added here
]

temperature_sum = 0
highest_humidity = 0
total_precipitation = 0
for dict in weather_data:
    temperature_sum += dict["temperature"] 

    humidity = dict["humidity"]
    if humidity > highest_humidity:
        highest_humidity = humidity

    total_precipitation += dict["precipitation"]

# calculation of average temp in °F
average_temperature_in_celsius = temperature_sum / len(weather_data)
# note that average temperature printed must be in °F
average_temperature_in_fahrenheit = average_temperature_in_celsius * 1.8 + 32 # according to formula on google

# finding date with highest humidity
for dict in weather_data:
    if dict["humidity"] == highest_humidity:
        highest_humidity_dict = dict
date_with_highest_humidity = highest_humidity_dict["date"]

# example output states 67.67°F but its likely wrong, according to the formula found across multiple sources on google
print(f"Average temperature: {average_temperature_in_fahrenheit}°F") 

print(f"Day with Highest Humidity: {date_with_highest_humidity} ({highest_humidity}%)")
print(f"Total Precipitation: {total_precipitation} inches")