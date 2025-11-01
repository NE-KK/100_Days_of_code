import pandas
data = pandas.read_csv("weather_data.csv")

temp_list = data["temp"].to_list()
temp_sum = sum(temp_list)

temp_average = temp_sum / len(temp_list)

print(temp_list)
print(f"{temp_average:.2f}")

print(data["temp"].mean())
print(data["temp"].max())
