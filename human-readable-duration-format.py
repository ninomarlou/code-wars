def main():
    x1 = 120
    a1 = format_duration(x1)
    print(a1)

def format_duration(seconds):
    if seconds == 0:
        return 'now'

    result_list = []
    units = [31536000, 86400, 3600, 60, 1]
    units_strings = [['year', 'years'], ['day', 'days'], ['hour', 'hours'], ['minute', 'minutes'],
                     ['second', 'seconds']]

    for i in range(0, len(units), 1):
        unit = units[i]
        unit_strings = units_strings[i]
        whole = int(seconds / unit)
        if whole > 1:
            result_list.append(str(whole) + ' ' + unit_strings[1])
        elif whole == 1:
            result_list.append(str(whole) + ' ' + unit_strings[0])
        seconds = seconds % unit

    result = ''
    if len(result_list) > 1:
        for i in range(0, len(result_list), 1):
            if i == len(result_list) - 1:
                result += ' and ' + result_list[i]
            elif i == len(result_list) - 2:
                result += result_list[i]
            elif i < len(result_list) - 2:
                result += result_list[i] + ', '
    else:
        result = result_list[0]

    return result

if __name__ == "__main__":
    main()
