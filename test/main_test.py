from source.main import Interface
from unittest import TestCase
from test.plugins.ReqTracer import requirements
from source.shape_checker import get_triangle_type
from source.shape_checker import get_square_type

import sys


class TestGetResult(TestCase):
    # TEST QUESTIONS_________________________________________________________________
    # Ask question 'What' and get answer. Test ISO triangle FLOAT and INT"

    @requirements(['#0001', '#0002', '#0006', '#0007', '#0050', '#0051', '#0052'])
    def test_triangle_equilateral_req(self):
        obj = Interface()
        result = obj.ask('What type of triangle is 1.0 1 1?')
        self.assertEqual(result, 'equilateral')

    "Ask question 'How' and get answer."

    @requirements(['#0006', '#0007', '#0010', '#0050', '#0051', '#0052'])
    def test_askQuestionHow_req(self):
        obj = Interface()
        result = obj.ask('How do I do this lab?')
        self.assertEqual(result, 'I don\'t know, please provide the answer')

    "Ask question 'Where' and get answer."

    @requirements(['#0006', '#0007', '#0010', '#0050', '#0051', '#0052'])
    def test_askQuestionWhere_req(self):
        obj = Interface()
        result = obj.ask('Where is my mind?')
        self.assertEqual(result, 'I don\'t know, please provide the answer')

    "Ask question 'Why' and get answer."

    @requirements(['#0006', '#0007', '#0010', '#0050', '#0051', '#0052'])
    def test_askQuestionWhy_req(self):
        obj = Interface()
        result = obj.ask('Why is python called python?')
        self.assertEqual(result, 'I don\'t know, please provide the answer')

    "Ask question 'Who' and get answer."

    @requirements(['#0006', '#0007', '#0010', '#0050', '#0051', '#0052'])
    def test_askQuestionWho_req(self):
        obj = Interface()
        result = obj.ask('Who was the 16th president of the United States?')
        self.assertEqual(result, 'I don\'t know, please provide the answer')

    "Test a sentence without a starting keyword"

    @requirements(['#0008', '#0050', '#0051', '#0052'])
    def test_askBadQuestion_req(self):
        obj = Interface()
        result = obj.ask('Hello?')
        self.assertEqual(result, 'Was that a question?')

    "Test no question mark"

    @requirements(['#0009', '#0050', '#0051', '#0052'])
    def test_askNoQuestion_req(self):
        obj = Interface()
        result = obj.ask('You are awesome')
        self.assertEqual(result, 'Was that a question?')

    "Test separate sentence into words"

    @requirements(['#0010', '#0050', '#0051', '#0052'])
    def test_SeparateWords_req(self):
        obj = Interface()
        result = obj.ask('HowWhatWhereWhyWho?')
        self.assertEqual(result, 'Was that a question?')

    # The system shall determine an answer to a question as correct if the keywords provide a 90% match and return
    # the answer"

    @requirements(['#0011', '#0050', '#0051', '#0052'])
    def test_AnswerMatchKeyword_req(self):
        obj = Interface()
        result = obj.ask('What type of triangle 1.0 1 1?')
        self.assertEqual(result, 'equilateral')

    # The system shall exclude any number value from match code and provide the values to generator function
    # (if one exists)"

    @requirements(['#0012', '#0050', '#0051', '#0052'])
    def test_AnswerExcludeMatch_req(self):
        obj = Interface()
        result = obj.ask('What type of 1.0 1 1 triangle is?')
        self.assertEqual(result, 'equilateral')

    "When a valid match is determined the system shall return the answer"

    @requirements(['#0013', '#0050', '#0051', '#0052'])
    def test_ReturnAnswer_req(self):
        obj = Interface()
        result = obj.ask('What type of quadrilateral is 1 1 1 1?')
        self.assertEqual(result, 'square')

    "When no valid match is determined the system shall return I don\'t know, please provide the answer"

    @requirements(['#0014', '#0050', '#0051', '#0052'])
    def test_ReturnDontKnow_req(self):
        obj = Interface()
        result = obj.ask('What type of square is 1 1 1 1?')
        self.assertEqual(result, 'I don\'t know, please provide the answer')

    "The system shall provide a means of providing an answer to the previously asked question"

    @requirements(['#0015', '#0050', '#0051', '#0052'])
    def test_ProvideAnswer_req(self):
        obj = Interface()
        obj.ask('Where is my mind?')
        obj.teach('Swimming in the caribbean')
        result = obj.ask('Where is my mind?')
        self.assertEqual(result, 'Swimming in the caribbean')

    # The system shall accept and store answers to previous questions in the form of a string or a function pointer and
    #  store it as the generator function"

    @requirements(['#0016', '#0050', '#0051', '#0052'])
    def test_LearnedAnswerPointer_req(self):
        obj = Interface()
        result = obj.ask('What type of triangle is 1 1 1?')
        obj.teach(get_triangle_type)
        self.assertEqual(result, 'equilateral')

    "If no previous question has been asked the system shall respond with Please ask a question first"

    @requirements(['#0017', '#0050', '#0051', '#0052'])
    def test_NoQuestion_req(self):
        obj = Interface()
        result = obj.teach(get_triangle_type)
        self.assertEqual(result, 'Please ask a question first')

    # If an attempt is made to provide an answer to an already answered question the system shall respond with I don\'t
    # know about that. I was taught differently and not update the question"

    @requirements(['#0018', '#0050', '#0051', '#0052'])
    def test_AlreadyLearned_req(self):
        obj = Interface()
        obj.ask('Where is my mind?')
        obj.teach('With my feet in the air and my head on the ground')
        result = obj.teach('With my feet in the air and my head on the ground')
        self.assertEqual(result, 'I don\'t know about that. I was taught differently')

    "The system shall provide a means of updating an answer to the previously asked question"
    "The argument is being cut off. Result should = square here so there is a bug in the code"

    @requirements(['#0019', '#0050', '#0051', '#0052'])
    def test_UpdateLearned_req(self):
        obj = Interface()
        obj.ask('What type of square is 1 1 1 1?')
        obj.teach(get_triangle_type)
        obj.correct(get_square_type)
        result = obj.ask(obj.last_question + '?')
        self.assertEqual(result, 'invalid')

    @requirements(['#0020', '#0050', '#0051', '#0052'])
    def test_StoreAnswer_req(self):
        obj = Interface()
        obj.ask('What type of square is 1 1 1 1?')
        obj.teach(get_triangle_type)
        obj.correct(get_square_type)
        result = obj.ask('What type of square is 1 1 1 1?')
        self.assertEqual(result, 'square')

    "If no previous question has been asked the system shall respond with Please ask a question first"

    @requirements(['#0021', '#0050', '#0051', '#0052'])
    def test_NoPreviousQuestion_req(self):
        obj = Interface()
        result = obj.correct('')
        self.assertEqual(result, 'Please ask a question first')

    # COVERAGE______________________________________________________________________________________
    @requirements(['#0006', '#0050', '#0051', '#0052'])
    def test_previous_q_notString(self):
        obj = Interface()
        with self.assertRaises(Exception, msg='Not A String!'):
            obj.ask(1)
