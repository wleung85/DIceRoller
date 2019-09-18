from diceroller import parse_roll_string
import unittest 

class TestDiceRoller(unittest.TestCase):
    # test simple arithmetic
    def test_constant_arithmetic(self):
        result_list = parse_roll_string('5 + 20')
        self.assertEqual(result_list[0], 25)

        result_list = parse_roll_string('5 - 20')
        self.assertEqual(result_list[0], -15)

    # test one set of dice rolls (2d6)
    def test_one_dice_roll_set(self):
        result_list = parse_roll_string('2d6')
        sum = 0

        # test to make sure every roll is within dice bounds
        for roll in result_list[1:]:
            self.assertLessEqual(roll, 6)
            sum += roll

        # test to make sure sum equals answer given
        self.assertEqual(result_list[0], sum)

    # test rolling a zero sided die
    def test_zero_sided_die(self):
      result_list = parse_roll_string('3d0')
      # should return 0
      self.assertEqual(result_list[0], 0)

    # test rolling one set of dice rolls and adding a constant
    def test_roll_add_constant(self):
        result_list = parse_roll_string('4d4 + 1')
        sum = 0

        for roll in result_list[1:]:
            sum += roll
        
        self.assertEqual(result_list[0], sum + 1)

    # test rolling two dice sets and adding them
    def test_two_dice_roll_set_add(self):
        result_list = parse_roll_string('3d12 + 1d8')
        sum = 0
        
        for roll in result_list[1:4]:
            self.assertLessEqual(roll, 12)
            sum += roll

        for roll in result_list[4:]:
            self.assertLessEqual(roll, 8)
            sum += roll

        self.assertEqual(result_list[0], sum)

    # test rolling two dice sets and subtracting them
    def test_two_dice_roll_set_subtract(self):
        result_list = parse_roll_string('3d12 - 1d8')
        sum = 0

        for roll in result_list[1:4]:
            self.assertLessEqual(roll, 12)
            sum += roll

        for roll in result_list[4:]:
            self.assertLessEqual(roll, 8)
            sum -= roll

        self.assertEqual(result_list[0], sum)

    # test parsing string with no whitespace
    def test_no_whitespace(self):
        result_list = parse_roll_string('2d20+4d6')
        sum = 0

        for roll in result_list[1:3]:
            self.assertLessEqual(roll, 20)
            sum += roll

        for roll in result_list[3:]:
            self.assertLessEqual(roll, 6)
            sum += roll

        self.assertEqual(result_list[0], sum)

    # test parsing string with no multiplier to dice
    def test_no_multiplier(self):
        result_list = parse_roll_string('d20 + 2d6 - 4')
        sum = 0

        for roll in result_list[1]:
            self.assertLessEqual(roll, 20)
            sum += roll

        for roll in result_list[1:]:
            self.assertLessEqual(roll, 6)
            sum += roll

        self.assertEqual(result_list[0], sum - 4)

    # test parsing empty string
    def test_empty_string(self):
        result_list = parse_roll_string('')
        # should return 0 with no rolls made
        self.assertEqual(result_list, [0])

    # test negative sided die
    def test_negative_sided_die(self):
        with self.assertRaises(ValueError):
            parse_roll_string('2d-6')

if __name__ == "__main__":
    unittest.main()