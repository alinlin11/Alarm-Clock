from datetime import datetime
from playsound import playsound


def validate_time(alarm_time_input):
    if len(alarm_time_input) != 11:
        return "Invalid time format!"
    else:
        if int(alarm_time_input[0:2]) > 12:
            return "Invalid HOUR format!"
        elif int(alarm_time_input[3:5]) > 59:
            return "Invalid MINUTE format!"
        elif int(alarm_time_input[6:8]) > 59:
            return "Invalid SECOND format!"

        # if str(alarm_time_input[9:].upper()) != "AM" or str(alarm_time_input[9:].upper() != "PM"):
        #     s = str(alarm_time_input[9:].upper())
        #     return "Invalid AM/PM format!"
        else:
            return "Accepted"


def validate_period(s):
    if len(s) == 2:
        if s == "AM" or s == "PM":
            print("YES")
            return True
    else:
        return False


while True:
    alarm = input("Enter time in HH:MM:SS AM/PM format: ")
    check = validate_time(alarm)

    if not validate_period(alarm[9:].upper()):
        print("Invalid AM/PM format!")
        if check != "Accepted":
            print(check)
    else:
        print(f"Setting alarm for: {alarm}")
        break

alarm_hour = alarm[0:2]
alarm_minute = alarm[3:5]
alarm_second = alarm[6:8]
alarm_period = alarm[9:].upper()

while True:
    time_now = datetime.now()

    current_hour = time_now.strftime("%I")
    current_minute = time_now.strftime("%M")
    current_second = time_now.strftime("%S")
    current_period = time_now.strftime("%p")

    if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_minute == current_minute:
                if alarm_second == current_second:
                    print("Time's up!")
                    break
