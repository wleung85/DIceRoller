#! python3

from random import randrange

def parse_string(input_str):
    # splitting input method
    result = 0
    operation = '+'
    sub_result = 0
    
    in_list = input_str.split()
    for item in in_list:
        if 'd' in item:
            item_split = item.split('d')
            num_dice = item_split[0]
            die = item_split[1]
            try:
                num_dice = int(num_dice)
                die = int(die)
            except ValueError:
                raise ValueError("Item %s could not be parsed" % item)
            for iter in range(num_dice):
                roll = randrange(die + 1)
                print("Rolled %d" % roll)
                sub_result += roll
            if operation == '+':
                result += sub_result
            elif operation == '-':
                result -= sub_result
        elif item in ['+', '-']:
            operation = item
        else:
            try:
                sub_result = int(item)
                if operation == '+':
                    result += sub_result
                elif operation == '-':
                    result -= sub_result
            except ValueError:
                raise ValueError("Item %s could not be parsed" % item)
    
    return result

if __name__ == "__main__":
    while True:
        user_in = input("Enter dice roll string:\n").lower()
        try:
            print(parse_string(user_in))
        except:
            print("User input could not be parsed")
