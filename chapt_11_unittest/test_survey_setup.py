import unittest
from survey import AnonymousSurvey


class TestAnonmoyousSurveySetUp(unittest.TestCase):

    """ Tests for AnonymousSurvey """

    def setUp(self):
        """creates a survey and set of responses that
          can be used across testing methods."""
        
        question = "What language did you first learn to speak?"  
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """ tests whether a single response was stored correctly. """
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """ tests if three responses were stored correctly. """
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


unittest.main()