"""
Day 1
"""


def find_calibration_in_line(calib_line):
    # Find two numbers in the line or return a double version
    str_numbers = [char for char in calib_line if char.isdigit()]
    # Take the first and last str number and concat, then turn into an int
    return int(str_numbers[0] + str_numbers[-1])


# Main loop
with open('/workspaces/advent-of-code-2023/day-1/input-day-1.txt') as file:
    sum_calibrations = 0
    while True:
        line = file.readline()
        # If we find an empty string we have reached the end
        if len(line) == 1:
            break
        # Otherwise we still have more numbers to find
        calibration_found = find_calibration_in_line(line)
        sum_calibrations += calibration_found

    print(f"Final sum of calibrations: {sum_calibrations}")
