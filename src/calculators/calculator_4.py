from typing import Dict, List
from flask import request as FlaskRequest

from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator4:

    def calculate(self,request: FlaskRequest)-> Dict: # type: ignore
        body = request.json
        numbers = self.__validate_body(body)
        
        result = sum(numbers) / len(numbers)
        response = self.__format_response(result)

        return response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("body mal formatado!")
        
        input_data = body["numbers"]

        return input_data
    
    def __format_response(self, average: float) -> Dict:
        return {
            "data": {
                "Calculator": 4,
                "average": round(average, 2)
            }
        }
