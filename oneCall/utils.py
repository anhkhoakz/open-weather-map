import datetime


def unix_to_normal_time(unix_time):
    normal_time = datetime.datetime.fromtimestamp(
        int(unix_time)).strftime('%d-%m-%Y %H:%M:%S')
    return normal_time


def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return '{:.2f}'.format(round(celsius, 2))


def get_moon_phase(moon_phase_value):
    if moon_phase_value == 0 or moon_phase_value == 1:
        return 'New Moon'
    elif moon_phase_value == 0.25:
        return 'First Quarter Moon'
    elif moon_phase_value == 0.5:
        return 'Full Moon'
    elif moon_phase_value == 0.75:
        return 'Last Quarter Moon'
    elif moon_phase_value > 0 and moon_phase_value < 0.25:
        return 'Waxing Crescent'
    elif moon_phase_value > 0.25 and moon_phase_value < 0.5:
        return 'Waxing Gibbous'
    elif moon_phase_value > 0.5 and moon_phase_value < 0.75:
        return 'Waning Gibbous'
    elif moon_phase_value > 0.75 and moon_phase_value < 1:
        return 'Waning Crescent'
    else:
        return 'Invalid moon phase value'
