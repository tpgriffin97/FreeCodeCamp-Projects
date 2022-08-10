# Time Calculator for Freecodecamp's Scientific Computing with Python certification

# Create add_time function that takes two require parameters and one optional parameter:

# (Required) A start time in the 12-hour clock format(ending in AM or PM)
# (Required) A duration time that indicates the number of hours and minutes
# (Optional) A starting day of the week, case-insensitive

# Function should add duration time to start time and return result

# If the result will be the next day, it should show (next day) AFTER the TIME
# If the result will be MORE than one day later, it should show (n days later)...
# ... where n = NUMBER OF DAY LATER

# If the function given optional, starting day of the week parameter, output should display...
# ... day of the week of the result.
# Day of the week output should appear after time and before (number of days later)

# Examples of desired outputs:

# add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

# add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

# add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

# add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

# add_time("11:43 PM", "24:20", "tuesday")
# Returns: 12:03 AM, Thursday (2 days later)

# add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)

# DO NOT IMPORT ANY PYTHON LIBRARIES!
# ASSUME START TIMES ARE VALID
# MINUTES IN THE DURATION WILL BE A WHOLE NUMBER > 60, BUT HOURS CAN BE ANY WHOLE NUMBER

# NOTES:
# MINUTES and HOUR must be calculated separately, but printed on the same line
# How can I take the start time and ADD to it...? Addition maybe?

def add_time(start, duration):
    # Principal variables

    # I need to separate the hours from the minutes in each argument.
    # May need to use array and conversion
    hours = ""
    minutes = ""

    # After a bit of research, I may need to use map(), need to understand it
    time_of_day = ["AM", "PM"]
    week_day = ["Sunday", "Monday", "Tuesday",
                "Wednesday", "Thursday", "Friday", "Saturday"]

    if start == str:
        print(type(start))
        hour_split = start.split(":")
        minute_split = hour_split[1].split(" ")
        time_of_day_split = minute_split[1].split(" ")
        adding_time = str(int(hour_split[0]) + int(minute_split[0]))
        hours = adding_time
        print(hours)

    if duration == str:
        hour_split = duration.split(":")
        minute_split = hour_split[1].split(" ")
        time_of_day_split = minute_split[1].split(" ")
        adding_time = str(int(hour_split[0]) + int(minute_split[0]))
        minutes = adding_time
        print(minutes)


print(add_time("3:50 PM", "3:10"))
