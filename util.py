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
