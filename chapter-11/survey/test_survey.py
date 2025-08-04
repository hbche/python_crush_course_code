from survey import AnonymousSurvey
import pytest

# 夹具
@pytest.fixture
def language_survey():
    """一个可供所有测试函数使用的AnonymousSurvey实例"""

    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    """测试单个答案是否会被妥善保存"""

    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_responses(language_survey):
    """测试三个答案是否会被妥善保存"""

    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)
        
    for response in responses:
        assert response in language_survey.responses