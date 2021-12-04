# Sameer Dash
# Assignment 10.1: Your Own Class
# This program implements an AlarmClock class that represents a basic alarm clock and has methods to manage the clock.

# Acknowledgements:
# Python datetime documentation: https://docs.python.org/3/library/datetime.html

import datetime


class AlarmClock:
    # Set a default brightness for alarm clocks
    default_brightness = 3

    def __init__(self, brightness):
        # Initialize the clock's time to current time
        self.__time = datetime.datetime.now().time()
        # Use set method to set the brightness
        self.set_brightness(brightness)
        # Start without an alarm.
        self.__alarm = None

    # Returns the clock's current time
    def get_time(self):
        return self.__time

    # Takes a datetime.time object and sets it as the clock's new time
    def set_time(self, new_time):
        # Raise TypeError if wrong input type given
        if type(new_time) is not datetime.time:
            raise TypeError("New time must be a datetime.time object")
        else:
            self.__time = new_time

    # Returns the current brightness of the clock
    def get_brightness(self):
        return self.__brightness

    # Takes an integer and sets it as the clock's new brightness
    def set_brightness(self, new_brightness):
        # Make sure the brightness is between 1-5
        if (new_brightness >= 1 and new_brightness <= 5):
            self.__brightness = new_brightness
        else:
            # If brightness is out of range, use default brightness and raise ValueError
            self.__brightness = AlarmClock.default_brightness
            raise ValueError("New brightness must be a number from 1-5")

    # Returns the clock's current alarm, which may be None
    def get_alarm(self):
        return self.__alarm

    # Takes a datetime.time object andd sets it as the clock's new alarm
    def set_alarm(self, new_alarm):
        # Raise TypeError if wrong input type given
        if type(new_alarm) is not datetime.time:
            raise TypeError("New alarm must be a datetime.time object")
        else:
            self.__alarm = new_alarm

    # Returns a datetime.timedelta object representing the time until the alarm rings.
    def time_until_alarm(self):
        if (self.__alarm is None):
            return None

        # Create datetime objects for the current time and alarm time (using today's date)
        current_datetime = datetime.datetime.combine(datetime.date.today(), self.__time)
        alarm_datetime = datetime.datetime.combine(datetime.date.today(), self.__alarm)

        # If the alarm is in the past, increment it to the next day.
        if (alarm_datetime < current_datetime):
            alarm_datetime += datetime.timedelta(days=1)

        # Subtract the datetime objects to get the difference as datetime.timedelta
        difference = alarm_datetime - current_datetime
        return difference

    # Takes a datetime.time object and returns a boolean of whether the given time has passed today.
    def has_time_passed(self, time):
        # Raise TypeError if wrong input type given
        if type(time) is not datetime.time:
            raise TypeError("Time must be a datetime.time object")

        # Determine whether the clock's time has passed the given time
        # by seeing if it is greater
        has_passed = self.__time > time
        return has_passed

    # Magic method that gives a string representation of the clock's current time and alarm time.
    def __str__(self):
        return f"Time: {self.get_time()}, Alarm: {self.get_alarm()}"


def main():
    # Create an AlarmClock object for demonstration
    my_clock = AlarmClock(2)

    print("The clock's time is:", my_clock.get_time())

    # Set the clock's time to 5:30:04 PM using set_time
    new_time = datetime.time(hour=17, minute=30, second=4)
    my_clock.set_time(new_time)
    print("The clock's new time is:", my_clock.get_time())

    # Test clock's brightness set/get methods
    print("The clock's brightness is:", my_clock.get_brightness())
    my_clock.set_brightness(5)
    print("The clock's brightness is now:", my_clock.get_brightness())

    # Set an alarm for 8:15 AM
    my_clock.set_alarm(datetime.time(hour=8, minute=15, second=0))
    print("The alarm is now set for:", my_clock.get_alarm())
    # Use time_until_alarm method to find how much time until the alarm goes off.
    time_to_alarm = my_clock.time_until_alarm()
    # Convert the time to hours (timedelta objects only provide "seconds" and "days" attributes)
    time_in_hours = time_to_alarm.seconds / 60 / 60
    print(f"It will go off in {time_in_hours:.2f} hours.")

    # Use the has_time_passed method to see if certain times have passed in the current day.
    print(f"Is it past my bedtime of 9 PM? -> {my_clock.has_time_passed(datetime.time(21, 0, 0))}.")
    print(f"Is it past 12 PM (noon)? -> {my_clock.has_time_passed(datetime.time(12, 0, 0))}.")

    # Use the has_time_passed method to print a greeting based on the clock's time
    print("Greeting based on clock's time of day:")
    if my_clock.has_time_passed(datetime.time(18, 0, 0)):
        print("Good evening")
    elif my_clock.has_time_passed(datetime.time(12, 0, 0)):
        print("Good afternoon")
    else:
        print("Good morning")

    # Use __str__ helper to print current status of alarm clock
    print("Status of the alarm clock:", my_clock)


if __name__ == "__main__":
    main()
