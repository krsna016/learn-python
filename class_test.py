import unittest
from Anonymous_survey_class import AnonymousSurvey


# class Test_anonymous_class(unittest.TestCase):
#     """"""

#     def test_single_response(self):
#         """"""
#         question = "What's your hobby ? "
#         q_1 = AnonymousSurvey(question)
#         q_1.store_response("English")
#         self.assertIn("English", q_1.responses)

#     def test_multiple_response(self):
#         """"""
#         question = "What's your hobby ? "
#         q_1 = AnonymousSurvey(question)
#         responses = ["a", "b", "c"]
#         for resp in responses:
#             q_1.store_response(resp)
#         for resp in responses:
#             self.assertIn(resp,q_1.responses)
# unittest.main()
        
# Also:

class Test_anonymous_class(unittest.TestCase):
    """"""

    def setUp(self):
        """"""
        self.question = "What's your hobby ? "
        self.q_1 = AnonymousSurvey(self.question)
        self.responses = ["a", "b", "c"]

    def test_single_response(self):
        """"""
        self.q_1.store_response(self.responses[0])
        self.assertIn("a", self.q_1.responses)

    def test_multiple_response(self):
        """"""
        for resp in self.responses:
            self.q_1.store_response(resp)
        for resp in self.responses:
            self.assertIn(resp,self.q_1.responses)
unittest.main()

