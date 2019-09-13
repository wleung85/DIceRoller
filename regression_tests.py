from diceroller import parse_roll_string

# later test cases:
# 1d0
# 3d12+1d2

if __name__ == "__main__":
    result_list = parse_roll_string('3d12 + 1d2')
    result = result_list[0]
    print(result_list)
    for index, value in enumerate(result_list):
        if 0 < index < 4 and value > 12 or index > 4 and value > 2:
            raise ValueError("Dice did not roll within bounds")
        if index != 0:
            result -= value
    if result != 0:
        raise ValueError("Dice did not sum up to given result")
    # except:
    #     print("FAIL: String '3d12 + 1d2' could not be parsed")