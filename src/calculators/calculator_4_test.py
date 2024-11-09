from typing import Dict
from pytest import raises
from .calculator_4 import Calculator4

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_body_error():
    mock_request = MockRequest({})
    calculator_4 = Calculator4()

    with raises(Exception) as excinfo:
        calculator_4.calculate(mock_request)

    assert str(excinfo.value) == 'body mal formatado!'

def test_calculate():
    mock_request = MockRequest({ "numbers": [20,30,40,50] })
    calculator_4 =Calculator4()

    response = calculator_4.calculate(mock_request)
    
    assert response == {'data': {'Calculator': 4, 'average': 35.0}}