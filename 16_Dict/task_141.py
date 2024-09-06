def converter(number):
    points = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'
    }

    ten_to_twenty = {
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen'

    }

    tens = {
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety'
    }

    if 0 < number < 10:
        return points[number]
    elif 9 < number < 20:
        return ten_to_twenty[number]
    elif 19 < number < 100:
        return tens[number // 10 * 10] + ' ' + points[number % 10]
    elif 99 < number < 1000:
        remainder = number % 100
        if not remainder:
            return points[number // 100] + ' hundred'
        elif remainder in ten_to_twenty:
            return points[number // 100] + ' hundred ' + ten_to_twenty[number % 100]
        else:
            return points[number // 100] + ' hundred ' + tens[number % 100 // 10 * 10] + ' ' + points[number % 10]

def main():
    number = int(input('Enter number 1-999: '))
    converted = converter(number)
    print(converted)

if __name__ == '__main__':
    main()