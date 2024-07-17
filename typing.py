# type: ignore
from typing import Dict

def add(elem1: int, elem2: float) -> Dict:
    response = elem1 + elem2
    return { "sum": response }

val1 = add(2,4.67)

print(val1)

# int, float, str, bool = True
# Dict, List, Tuple