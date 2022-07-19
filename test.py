import json
import main


def test_data_input_append_count():
    """
    Function to test the three function:
    data_input
    data_append
    count_overweight
    from the main
    """
    # open test json file
    with open("test.json", "r") as f:
        test_data = json.load(f)
        f.close()

    check_data = main.data_input(test_data)

    # check the final result returned from data_input and data_append
    for i in check_data:
        assert i['BMI'] == 29.4
        assert i['BMI Category'] == "Overweight"
        assert i['Health risk'] == "Enhanced risk"

    check = main.count_overweight(check_data)

    # check the final result returned by count_overweight
    assert check == 1
