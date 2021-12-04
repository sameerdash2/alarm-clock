# AlarmClock

**GitHub repository**: https://github.com/sameerdash2/alarm-clock

## Class Documentation
The AlarmClock class models the common functions of a real alarm clock. The purpose of this class is to emulate alarm clock features such as setting the time, setting an alarm, and changing the brightness of the clock. To make things easier, each AlarmClock instance starts with the system's current time, but it can be modified later just like setting a physical clock. Additionally, the class can help manage a schedule by calculating how much time is remaining until the alarm or finding out whether a certain timestamp has already passed.

### Class variables
- `AlarmClock.default_brightness`: An integer that stores the default brightness value for AlarmClock objects. This is 3, but can be changed by the user.

### Data variables
- `AlarmClock.__time`: A datetime.time object that holds the current time of the alarm clock.
- `AlarmClock.__brightness`: An integer that stores the current brightness of the alarm clock.
- `AlarmClock.__alarm`: A datetime.time object that holds the time of the scheduled alarm. If no alarm has been set, this variable is `None`.

### Methods
- **Constructor**: `AlarmClock.__init__(brightness)`: This method takes an integer for the brightness of the alarm clock and initializes the alarm clock's time to the current time. It also initializes the alarm to `None`.
- `AlarmClock.get_time()`: Returns the current time of the alarm clock as a datetime.time object.
- `AlarmClock.set_time(new_time)`: Takes a datetime.time object and sets it as the alarm clock's new time. If the argument is not of type datetime.time, a TypeError is raised.
- `AlarmClock.get_brightness()`: Returns the current brightness of the alarm clock as an integer.
- `AlarmClock.set_brightness(new_brightness)`: Takes an integer from 1-5 and sets it as the brightness of the alarm clock. If the integer is out of the range [1, 5], a ValueError is raised and the method will use `AlarmClock.default_brightness` instead.
- `AlarmClock.get_alarm()`: Returns the current alarm time as a datetime.time object. If no alarm is set, this method returns `None`.
- `AlarmClock.set_alarm(new_alarm)`: Takes a datetime.time object and sets it as the clock's new alarm time. If the argument is not of type datetime.time, a TypeError is raised.
- `AlarmClock.time_until_alarm()`: Returns the amount of time until the alarm rings, as a datetime.timedelta object. If no alarm is set, this method returns `None`.
- `AlarmClock.has_time_passed(time)`: Takes a datetime.time object and returns a boolean of whether the given time of day has already passed today. This is based on the alarm clock's time, not the system's time.
- `AlarmClock.__str__()`: Magic method that returns a string representation of the clock's current time and alarm time.

## Demo Program Documentation

The demo program creates an AlarmClock instance and does several tasks using its methods. First, it uses the set_time method to set a new time for the alarm clock and print it. It then changes the brightness of the alarm clock using the set/get methods. Next, it sets an alarm for 8:15 AM and computes the amount of time remaining until that alarm goes off. After this, it uses the has_time_passed method to determine whether certain times of day have already passed, and also to choose a greeting message (Good morning, Good afternoon, or Good evening) based on the alarm clock's time. Finally, the program prints the alarm clock's status (current time and alarm time) using the `__str__` method.

### Instructions to run the demo program:
First, download the file [`alarm_clock.py`](alarm_clock.py). Open a terminal in the same directory as that file. Then enter `python3 alarm_clock.py` to run the program. The program will print results to the screen.
