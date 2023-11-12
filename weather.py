import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

# TASK 1
# -------------------------------------------------------------------------
#     """Takes a temperature and returns it in string format with the degrees
#         and celcius symbols.
#     Args:
#         temp: A string representing a temperature.
#     Returns:
#         A string contain the temperature and "degrees celcius."
#     """

def format_temperature(temp):
    return f"{temp}{DEGREE_SYBMOL}"

# -------------------------------------------------------------------------

# TASK 2
# -------------------------------------------------------------------------
#     """Converts and ISO formatted date into a human readable format.
#     Args:
#         iso_string: An ISO date string..
#     Returns:
#         A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
#     """

def convert_date(iso_string):
    date_format = datetime.fromisoformat(iso_string)
    convert_date = date_format.strftime("%A %d %B %Y")

    return convert_date

# # -------------------------------------------------------------------------

# TASK 3
# -------------------------------------------------------------------------
#     """Converts an temperature from farenheit to celcius.
#     Args:
#         temp_in_farenheit: float representing a temperature.
#     Returns:
#         A float representing a temperature in degrees celcius, rounded to 1dp.
#     """

def convert_f_to_c(temp_in_fahrenheit):
    fahrenheit = float(temp_in_fahrenheit)
    return round((fahrenheit - 32) * 5.0/9.0, 1)

# -------------------------------------------------------------------------

# TASK 4
# -------------------------------------------------------------------------
#     """Calculates the mean value from a list of numbers.
#     Args:
#         weather_data: a list of numbers.
#     Returns:
#         A float representing the mean value.
#     """

def calculate_mean(weather_data):
    total_temp = 0
    count = 0

    for data in weather_data:
        total_temp += float(data)
        count += 1
    
    if count > 0:
        mean_temp = total_temp / count
        
    return mean_temp

# -------------------------------------------------------------------------

# TASK 5
# -------------------------------------------------------------------------
#     """Reads a csv file and stores the data in a list.
#     Args:
#         csv_file: a string representing the file path to a csv file.
#     Returns:
#         A list of lists, where each sublist is a (non-empty) line in the csv file.
#     """

def load_data_from_csv(csv_file):
    data_list = []

    with open(csv_file, encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
 
        for row in reader:
            if not row:
                continue
            row[0] = str(row[0])
            row[1] = int(row[1])
            row[2] = int(row[2])
            data_list.append(row)

    return data_list

# -------------------------------------------------------------------------

# TASK 6
# -------------------------------------------------------------------------
#     """Calculates the minimum value in a list of numbers.
#     Args:
#         weather_data: A list of numbers.
#     Returns:
#         The minium value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
#     """

def find_min(weather_data):
    if not weather_data:
        return ()
    
    weather_data = [float(temp) for temp in weather_data]
    min_temp = min(weather_data)
    min_temp_index = (len(weather_data) - 1) - (weather_data [::-1].index(min_temp))
    
    return min_temp, min_temp_index

# -------------------------------------------------------------------------

# TASK 7
# -------------------------------------------------------------------------
#     """Calculates the maximum value in a list of numbers.
#     Args:
#         weather_data: A list of numbers.
#     Returns:
#         The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
#     """

def find_max(weather_data):
    if not weather_data:
        return ()
    
    weather_data = [float(temp) for temp in weather_data]
    max_temp = max(weather_data)
    max_temp_index = (len(weather_data) - 1) - (weather_data [::-1].index(max_temp))
    
    return max_temp, max_temp_index

# -------------------------------------------------------------------------

# TASK 8
# -------------------------------------------------------------------------
#     """Outputs a summary for the given weather data.
#     Args:
#         weather_data: A list of lists, where each sublist represents a day of weather data.
#     Returns:
#         A string containing the summary information.
#     """

def generate_summary(weather_data):
    if not weather_data:
        return () 

    min_temp = convert_f_to_c(weather_data[0][1])
    max_temp = convert_f_to_c(weather_data[0][2]) 
    min_temp_date = convert_date(weather_data[0][0]) 
    max_temp_date = convert_date(weather_data[0][0]) 
    total_low_temp = 0
    total_high_temp = 0

    for row in weather_data:
        date = convert_date(row[0])
        low_temp = convert_f_to_c(row[1])
        high_temp = convert_f_to_c(row[2])

        total_low_temp += low_temp
        total_high_temp += high_temp

        if low_temp < min_temp:
            min_temp = low_temp
            min_temp_date = date

        if high_temp > max_temp:
            max_temp = high_temp
            max_temp_date = date

    average_low = round(total_low_temp / len(weather_data), 1)
    average_high = round(total_high_temp / len(weather_data), 1)

    summary = f"{len(weather_data)} Day Overview\n  The lowest temperature will be {format_temperature(min_temp)}, and will occur on {(min_temp_date)}.\n  The highest temperature will be {format_temperature(max_temp)}, and will occur on {(max_temp_date)}.\n  The average low this week is {format_temperature(average_low)}.\n  The average high this week is {format_temperature(average_high)}.\n"
    return summary

# -------------------------------------------------------------------------

# TASK 9
# -------------------------------------------------------------------------
#     """Outputs a daily summary for the given weather data.
#     Args:
#         weather_data: A list of lists, where each sublist represents a day of weather data.
#     Returns:
#         A string containing the summary information.
#     """

def generate_daily_summary(weather_data):
    if not weather_data:
        return ()
    
    daily_summary = ""
    for row in weather_data:
        date = convert_date(row[0])
        low_temp = convert_f_to_c(row[1])
        high_temp = convert_f_to_c(row[2])
              
        daily_summary += f"---- {date} ----\n  Minimum Temperature: {format_temperature(low_temp)}\n  Maximum Temperature: {format_temperature(high_temp)}\n\n"
    
    return daily_summary

# -------------------------------------------------------------------------