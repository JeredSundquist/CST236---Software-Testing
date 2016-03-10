from source.question_answer import QA
from source.shape_checker import get_triangle_type, get_square_type
from story_checker import date_time, fib, pi_n, open_door, convert_metric, convert_ten_units, fav_num, mix_color, \
    color_print, e_n, sqrt_n, fact_n, joke, abs_n, hypo_xy, may_i_have_another
from source.git_utils import is_file_in_repo, get_git_file_info, get_file_info, get_repo_url, get_repo_branch
import time
import difflib

NOT_A_QUESTION_RETURN = "Was that a question?"
UNKNOWN_QUESTION = "I don't know, please provide the answer"
NO_QUESTION = 'Please ask a question first'
NO_TEACH = 'I don\'t know about that. I was taught differently'
LOG_FILE = open('logFile.log', 'a')


class Interface(object):
    def __init__(self):
        self.how_dict = {}
        self.what_dict = {}
        self.where_dict = {}
        self.who_dict = {}

        self.keywords = ['How', 'What', 'Where', 'Who', "Why", "Please", 'Open', 'Convert', 'My', 'Mix', 'Can', 'Is']
        self.question_mark = chr(0x3F)
        self.bang = chr(0x21)
        self.period = chr(0x2E)

        self.question_answers = {
            'What type of triangle is ': QA('What type of triangle is ', get_triangle_type),
            'What type of quadrilateral is ': QA('What type of quadrilateral is ', get_square_type),
            'What time is it ': QA('What time is it ', date_time),
            'What is the n digit of fibonacci ': QA('What is the n digit of fibonacci ', fib),
            'What is the n digit of pi ': QA('What is the n digit of pi ', pi_n),
            'Please clear memory ': QA('Please clear memory ', self.clear_mem),
            'Open the door hal ': QA('Open the door hal ', open_door),
            'Convert to ': QA('Convert to ', convert_metric),
            'What are numeric conversions ': QA('What are numeric conversions ', convert_ten_units),
            'My favorite number is ': QA('My favorite number is ', fav_num),
            'Mix and ': QA('Mix and ', mix_color),
            'What colors can be mixed ': QA('What colors can be mixed ', color_print),
            'What is the n digit of e ': QA('What is the n digit of e ', e_n),
            'What is the square root of ': QA('What is the square root of ', sqrt_n),
            'What is factorial ': QA('What is factorial ', fact_n),
            'What do you get when you put root beer in a square glass ': QA(
                'What do you get when you put root beer in a square glass ', joke),
            'What is the absolute value of ': QA('What is the absolute value of', abs_n),
            'What is the hypotenuse of and ': QA('What is the hypotenuse of and ', hypo_xy),
            'Can I have another story ': QA('Can I have another story', may_i_have_another),
            'Is the in the repo ': QA('Is the in the repo ', is_file_in_repo),
            'What is the status of ': QA('What is the status of ', get_git_file_info),
            'What is the deal with ': QA('What is the deal with ', get_file_info),
            'What branch is ': QA('What branch is ', get_repo_branch),
            'Where did come from ': QA('Where did come from ', get_repo_url)
        }

        self.question_answers_copy = {
            'What type of triangle is ': QA('What type of triangle is ', get_triangle_type),
            'What type of quadrilateral is ': QA('What type of quadrilateral is ', get_square_type),
            'What time is it ': QA('What time is it ', date_time),
            'What is the n digit of fibonacci ': QA('What is the n digit of fibonacci ', fib),
            'What is the n digit of pi ': QA('What is the n digit of pi ', pi_n),
            'Please clear memory ': QA('Please clear memory ', self.clear_mem),
            'Open the door hal ': QA('Open the door hal ', open_door),
            'Convert to ': QA('Convert to ', convert_metric),
            'What are numeric conversions ': QA('What are numeric conversions ', convert_ten_units),
            'My favorite number is ': QA('My favorite number is ', fav_num),
            'Mix and ': QA('Mix and ', mix_color),
            'What colors can be mixed ': QA('What colors can be mixed ', color_print),
            'What is the n digit of e ': QA('What is the n digit of e ', e_n),
            'What is factorial ': QA('What is factorial ', fact_n),
            'What do you get when you put root beer in a square glass ': QA(
                'What do you get when you put root beer in a square glass ', joke),
            'What is the absolute value of ': QA('What is the absolute value of', abs_n),
            'What is the hypotenuse of and ': QA('What is the hypotenuse of and ', hypo_xy),
            'Can I have another story ': QA('Can I have another story', may_i_have_another),
            'Is the in the repo ': QA('Is the in the repo ', is_file_in_repo),
            'What is the status of ': QA('What is the status of ', get_git_file_info),
            'What is the deal with ': QA('What is the deal with ', get_file_info),
            'What branch is  ': QA('What branch is  ', get_repo_branch),
            'Where did come from ': QA('Where did come from ', get_repo_url)
        }
        self.last_question = None

    def ask(self, question=""):
        self.time_to_log(self.question_logging, question)
        if not isinstance(question, str):
            self.last_question = None
            raise Exception('Not A String!')
        if question[-1] != self.bang and question[-1] != self.period:
            if question[-1] != self.question_mark or question.split(' ')[0] not in self.keywords:
                self.last_question = None
                return NOT_A_QUESTION_RETURN

        parsed_question = ""
        args = []
        units = ['tera', 'giga', 'mega', 'kilo', 'hecto', 'deka', 'noConvert', 'deci', 'centi', 'milli', 'micro',
                 'nano', 'pico']
        colors = ['red', 'blue', 'yellow']
        for keyword in question[:-1].split(' '):
            try:
                if keyword in units:
                    args.append(keyword)
                elif keyword in colors:
                    args.append(keyword)
                elif keyword[0] == '<' and keyword[-1] == '>':
                    args.append(keyword[1:-1])
                else:
                    args.append(float(keyword))
            except Exception as ex:  # <---ADDED
                print ex  # <---ADDED
                parsed_question += "{0} ".format(keyword)
        parsed_question = parsed_question[0:-1]
        self.last_question = parsed_question

        for answer in self.question_answers.values():
            if difflib.SequenceMatcher(a=answer.question, b=parsed_question).ratio() >= .90:
                if answer.function is None:
                    self.time_to_log(self.answer_logging, answer.value)
                    return answer.value
                else:
                    self.time_to_log(self.answer_logging, answer.function(*args))
                    return answer.function(*args)
                    # try:
                    #     return answer.function(*args)
                    # except Exception as ex:#<---ADDED
                    #     raise Exception("Too many extra parameters {}".format(ex))#<---ADDED
        else:
            return UNKNOWN_QUESTION

    def teach(self, answer=""):
        if self.last_question is None:
            return NO_QUESTION
        elif self.last_question in self.question_answers.keys():
            return NO_TEACH
        else:
            self.__add_answer(answer)

    def correct(self, answer=""):
        if self.last_question is None:
            return NO_QUESTION
        else:
            self.__add_answer(answer)

    def clear_mem(self):
        self.question_answers = {}
        self.question_answers = self.question_answers_copy.copy()
        return "Memory cleared..."

    def __add_answer(self, answer):
        self.question_answers[self.last_question] = QA(self.last_question, answer)

    # log file with question tag
    @staticmethod
    def question_logging(val):
        LOG_FILE.write('QUESTION: ' + str(val) + '\n')
        return

    # log file with answer tag
    @staticmethod
    def answer_logging(val):
        LOG_FILE.write('ANSWER: ' + str(val) + '\n')
        return

    # calculates time and logs speed
    @staticmethod
    def time_to_log(func, *args):
        start = time.clock()
        func(*args)
        elapsed = time.clock() - start
        LOG_FILE.write('SPEED: ' + str(elapsed) + '\n')  # formatted for milliseconds
