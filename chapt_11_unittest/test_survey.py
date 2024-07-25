import unittest
from survey import AnonymousSurvey

class TestAnonmoyousSurvey(unittest.TestCase):

    """ Tests for AnonymousSurvey """

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        question = "What language did you first learn to speak?"

        language_survey = AnonymousSurvey(question)
        language_survey.store_response('English')

        self.assertIn('English', language_survey.responses)


unittest.main()