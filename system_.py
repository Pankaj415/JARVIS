import psutil


def battery_remaining():
    """

    :return: The percentage left of the device battery
    """
    global adv
    percent = psutil.sensors_battery().percent

    if percent <= 20:
        adv = 'Please plugin the charger battery is very low'
    elif 20 < percent <= 80:
        adv = 'You should plugin charger'
    elif 80 < percent <= 100:
        adv = 'The device is well Charged'

    return f"{percent} % battery is remaining, {adv}"


def battery_time():
    """

    :return: The battery time left of the device battery
    """
    charging = psutil.sensors_battery().power_plugged            # Checks whether charger is plugged in or not

    if charging:
        return "Device is plugged in"
    else:
        time = psutil.sensors_battery().secsleft            # Total battery life left in seconds

        # Converts the battery life left in hours and seconds
        hrs = time // 3600
        minutes = (time % 3600)//60

        if hrs == 0:
            return f"Battery life remaining is {minutes} minutes"
        else:
            return f"Battery life remaining is {hrs} hours and {minutes} minutes"


def usage(sec):
    if sec == "memory":
        use = psutil.virtual_memory()                   # Returns the usage of memory
        return f"Currently memory in use if {use}"
    elif sec == "disk":
        use = psutil.disk_usage()
        return f"Currently Disk usage is {use}"


def boot_time_():
    time = psutil.boot_time()
    hrs = time // 3600
    minutes = (time % 3600) // 60
    return hrs, minutes


