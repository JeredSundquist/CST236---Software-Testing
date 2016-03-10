from source.main import Interface
from unittest import TestCase
from test.plugins.ReqTracer import requirements
from test.plugins.ReqTracer import story
from source.story_checker import date_time


class TestStoryResult(TestCase):
    @story('When I ask "What time is it?" I want to be given the current date/time so I can stay up to date')
    def test_dateTime_story(self):
        obj = Interface()
        result = obj.ask('What time is it?')
        self.assertEqual(result, date_time())  # result may be different from the time executed to the time tested

    @story(
        'When I ask "What is the n digit of fibonacci?" I want to receive the answer so I don\'t have to figure it out '
        'myself')
    @requirements(['#0053'])
    def test_fib_story(self):
        obj = Interface()
        result = obj.ask('What is the 3 digit of fibonacci?')
        self.assertEqual(result, 2)

    @story(
        'When I ask "What is the n digit of pi?" I want to receive the answer so I don\'t have to figure it out myself')
    @requirements(['#0054'])
    def test_piN_story(self):
        obj = Interface()
        result = obj.ask('What is the 11 digit of pi?')
        self.assertEqual(result, '5')

    @story(
        'When I ask "What is the n digit of pi?" I want to receive the answer so I don\'t have to figure it out myself')
    def test_piNOne_story(self):
        obj = Interface()
        result = obj.ask('What is the 1 digit of pi?')
        self.assertEqual(result, '3')

    @story(
        'When I ask "What is the n digit of pi?" I want to receive the answer so I don\'t have to figure it out myself')
    def test_piNZero_story(self):
        obj = Interface()
        result = obj.ask('What is the 0 digit of pi?')
        self.assertEqual(result, 'invalid')

    @story(
        'When I ask "Please clear memory." I was the application to clear user set questions and answers so I can reset'
        ' the application')
    def test_clearMem_story(self):
        obj = Interface()
        result = obj.ask('Please clear memory.')
        self.assertEqual(result, 'Memory cleared...')

    @story(
        'When I say "Open the door hal!", I want the application to say "I\'m afraid I can\'t do that <user name> so I '
        'know that is not an option')
    def test_openDoor_story(self):
        obj = Interface()
        result = obj.ask('Open the door hal!')
        self.assertEqual(result, 'I\'m afraid I can\'t do that Jered')

    @story(
        'When I ask "Convert <number> <units> to <units>." I want to receive the converted value and units so I can '
        'know the answer.')
    @requirements(['#0055'])
    def test_convertMetric_story(self):
        obj = Interface()
        result = obj.ask('Convert 10 kilo to centi.')
        self.assertEqual(result, '1000000.0 centi')

    @story('When I ask "What are numeric conversions?" I want at least 10 different units I can convert from/to')
    def test_convertTenUnits(self):
        obj = Interface()
        result = obj.ask('What are numeric conversions?')
        self.assertEquals(result, "tera: 6, giga: 5, mega: 4,"
                                  "kilo: 3, hecto: 2,deka: 1,"
                                  "noConvert: 0, deci: -1, centi: -2,"
                                  "milli: -3, micro: -4, nano: -5, pico: -6")

    @story('When I say "What is your favorite number?", I want the number returned with an opinion')
    def test_favNum_story(self):
        obj = Interface()
        result = obj.ask('My favorite number is 1.')
        self.assertEqual(result, 'My number 13.0 is better than your number!')

    @story('When I say "What is your favorite number?", I want the number returned with an opinion')
    def test_favNumMatch_story(self):
        obj = Interface()
        result = obj.ask('My favorite number is 13.')
        self.assertEqual(result, 'Hey we are favorite number 13.0 buddies!')

    @story('When I say "What two colors to mix?", I want two colors I can mix to make a new color')
    @requirements(['#0056'])
    def test_mixColor_story(self):
        obj = Interface()
        result = obj.ask('Mix red and blue.')
        self.assertEqual(result, 'purple')

    @story('When I say "What two colors to mix?", I want two colors I can mix to make a new color')
    @requirements(['#0056'])
    def test_mixRedYellow_story(self):
        obj = Interface()
        result = obj.ask('Mix red and yellow.')
        self.assertEqual(result, 'orange')

    @story('When I say "What two colors to mix?", I want two colors I can mix to make a new color')
    @requirements(['#0056'])
    def test_mixBlueYellow_story(self):
        obj = Interface()
        result = obj.ask('Mix blue and yellow.')
        self.assertEqual(result, 'green')

    @story('When I say "What two colors to mix?", I want two colors I can mix to make a new color')
    @requirements(['#0056'])
    def test_mixRedRed_story(self):
        obj = Interface()
        result = obj.ask('Mix red and red.')
        self.assertEqual(result, 'red')

    @story('When I say "What two colors to mix?", I want two colors I can mix to make a new color')
    @requirements(['#0056'])
    def test_mixBlueBlue_story(self):
        obj = Interface()
        result = obj.ask('Mix blue and blue.')
        self.assertEqual(result, 'blue')

    @story('When I say "What two colors to mix?", I want two colors I can mix to make a new color')
    @requirements(['#0056'])
    def test_mixYellowYellow_story(self):
        obj = Interface()
        result = obj.ask('Mix yellow and yellow.')
        self.assertEqual(result, 'yellow')

    @story('When I ask "What colors can be mixed?", I want to see the primary colors')
    def test_colorPrint(self):
        obj = Interface()
        result = obj.ask('What colors can be mixed?')
        self.assertEquals(result, 'Red, Yellow, and Blue are the color that can be mixed')

    @story(
        'When I ask "What is the n digit of e?" I want to receive the answer so I don\'t have to figure it out myself')
    def test_eN_story(self):
        obj = Interface()
        result = obj.ask('What is the 2 digit of e?')
        self.assertEqual(result, '7')

    @story(
        'When I ask "What is the n digit of e?" I want to receive the answer so I don\'t have to figure it out myself')
    def test_eNOne_story(self):
        obj = Interface()
        result = obj.ask('What is the 1 digit of e?')
        self.assertEqual(result, '2')

    @story(
        'When I ask "What is the n digit of e?" I want to receive the answer so I don\'t have to figure it out myself')
    def test_eNZero_story(self):
        obj = Interface()
        result = obj.ask('What is the 0 digit of e?')
        self.assertEqual(result, 'invalid')

    @story('When I ask "What is the square root of n?" I want to get the square root of n')
    def test_sqrtN_story(self):
        obj = Interface()
        result = obj.ask('What is the square root of 4?')
        self.assertEqual(result, '2.0')

    @story('When I ask "What is n factorial?" I want to get n factorial')
    def test_factN_story(self):
        obj = Interface()
        result = obj.ask('What is 5 factorial?')
        self.assertEqual(result, '120')

    @story('When I ask "What do you get when you put root beer in a square glass?" I want to hear what you get')
    def test_joke_story(self):
        obj = Interface()
        result = obj.ask('What do you get when you put root beer in a square glass?')
        self.assertEqual(result, 'beer')

    @story('When I ask "What is the absolute value of n?" I want the absolute value of n')
    def test_absN_story(self):
        obj = Interface()
        result = obj.ask('What is the absolute value of -5?')
        self.assertEqual(result, '5.0')

    @story('When I ask "What is the hypotenuse of x and y?" I want to be returned the answer')
    @requirements(['#0057'])
    def test_hypo_xy_story(self):
        obj = Interface()
        result = obj.ask('What is the hypotenuse of 2 and 2?')
        self.assertEqual(result, '2.82842712475')

    @story('When I ask "Can I have another story?" I want the answer')
    def test_mayIHaveAnother_story(self):
        obj = Interface()
        result = obj.ask('Can I have another story?')
        self.assertEqual(result, 'Uuum no...')
