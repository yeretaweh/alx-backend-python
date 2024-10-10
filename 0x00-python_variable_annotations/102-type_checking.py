#!/usr/bin/env python3
from typing import List, Tuple, Union

def zoom_array(lst: Union[List[int], Tuple[int, ...]], factor: int = 2) -> List[int]:
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)  # Changed 3.0 to 3 (factor should be an integer)

