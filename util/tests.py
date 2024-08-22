from typing import Optional, Callable
from util.data_structures import ListNode, convert_list_to_linked_list

def run_test_case(function, input, expected_output):
    print(f"Input: {input}")
    print(f"Expected output: {expected_output}")
    result = function(*input)
    print(f"Result: {result}")
    print()
    assert result == expected_output

def run_test_case_any_order(function, input, expected_output):
    print(f"Input: {input}")
    print(f"Expected output: {expected_output}")
    result = function(*input)
    print(f"Result: {result}")
    print()
    assert set(result) == set(expected_output)

def run_test_case_linked_list(function : Callable[..., Optional[ListNode]], input, expected_output : list):
    print(f"Input: {input}")
    print(f"Expected output: {expected_output}")
    result = function(convert_list_to_linked_list(input[0]), convert_list_to_linked_list(input[1]))
    result_list = []
    while result:
        result_list.append(result.val)
        result = result.next
    print(f"Result: {result_list}")
    print()
    assert result_list == expected_output