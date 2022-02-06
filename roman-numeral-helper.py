class RomanNumerals:
    UNITS = [1000, 500, 100, 50, 10, 5, 1]
    UNITS_STRINGS = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    NO_REPEAT_UNITS_STRINGS = ['D', 'L', 'V']

    def to_roman(val):
        return ''

    def from_roman(roman_num):
        return RomanNumerals.UNITS[0]



def main():
    x1 = 0
    a1 = RomanNumerals.from_roman(x1)

    print(a1)


if __name__ == '__main__':
    main()
