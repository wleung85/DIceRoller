#! python3

from random import randrange

def parse_roll_string(input_str):
    # splitting input method
    result = 0              # final result of string
    result_list = [result]  # [0] = result, [1:-1] = dice rolls
    operation = '+'
    sub_result = 0
    
    in_list = input_str.split()
    for item in in_list:
        if 'd' in item:
            sub_result = 0
            item_split = item.split('d')
            num_dice = item_split[0]
            die = item_split[1]
            try:
                num_dice = int(num_dice)
                die = int(die)
            except ValueError:
                raise ValueError("Item %s could not be parsed" % item)
            for iter in range(num_dice):
                roll = randrange(1, die + 1)
                result_list.append(roll)
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
    
    result_list[0] = result
    return result_list

if __name__ == "__main__":
    while True:
        user_in = input("Enter dice roll string:\n").lower()
        try:
            roll_result = parse_roll_string(user_in)
            print("Final result = %d" % roll_result[0])
            if len(roll_result) > 1:
                print("Individual rolls:")
                for roll in roll_result[1:]:
                    print(roll, end = ' ')
                print()
            else:
                print ("No individual rolls")

        except:
            print("User input could not be parsed")
