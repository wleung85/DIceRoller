#! python3

from random import randrange

def parse_roll_string(input_str):
    # splitting input method
    result = 0              # final result of string
    result_list = [result]  # [0] = result, [1:] = dice rolls
    operation = '+'
    sub_result = 0
    pre_num = 0
    post_num = -1
    sided = False           # determine if 'd' has been encountered thus counting sided-ness

    for index, char in enumerate(input_str):
        if char.isdigit():
            if not sided:
                pre_num = pre_num * 10 + int(char)
            elif post_num < 0:
                post_num = int(char)
            else:
                post_num = post_num * 10 + int(char)
        elif char == ' ':
            pass
        elif char == 'd':
            sided = True
            # in case of no number of dice specified, default to 1 die
            if pre_num == 0:
                pre_num = 1
        if char in ['+', '-'] or index == len(input_str) - 1:
            if sided:
                for i in range(pre_num):
                    if post_num == 0:
                        roll = 0
                    elif post_num < 0:
                        raise ValueError("Can't parse die sidedness")
                    else:
                        roll = randrange(1, post_num + 1)
                    result_list.append(roll)
                    sub_result += roll
            else:
                sub_result = pre_num
            if operation == '+':
                result += sub_result
            elif operation == '-':
                result -= sub_result
            if index != len(input_str) - 1:
                # reset temp variables for next operation
                operation = char
                sub_result = 0
                pre_num = 0
                post_num = -1
                sided = False
    
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
