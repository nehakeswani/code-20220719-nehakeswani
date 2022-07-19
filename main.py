import json
from typing import List


class HealthDetails:
    """Class to store details of patients

        gender : str         : gender of patient
        height : int         : height of patient in cm
        weight : int         : weight of patient in kg
        bmi(kg/m2) : float   = mass(kg) / height(m)2)
        category : str       : Health category based upon BMI
        Risk  : str          : Health risk based upon BMI    """

    # INITIALIZE PARAMETERS
    def __init__(self, gender, height, weight):
        self.gender = gender
        self.height = height
        self.weight = weight
        self.bmi = float('%.2f' % (weight / ((height / 100) ** 2)))
        self.category, self.risk = self.bmi_category()

    # CALCULATE CATEGORY AND RISK
    def bmi_category(self):
        if self.bmi <= 18.4:
            return "Underweight", "Malnutrition risk"
        elif 18.5 <= self.bmi <= 24.9:
            return "Normal weight", "Low risk"
        elif 25 <= self.bmi <= 29.9:
            return "Overweight", "Enhanced risk"
        elif 30 <= self.bmi <= 34.9:
            return "Moderately obese", "Medium risk"
        elif 35 <= self.bmi <= 39.9:
            return "severely obese", "High risk"
        elif self.bmi >= 40:
            return "severely obese", "Very high risk"


def data_input(input_data: list) -> list:
    """
    Function to read data from input file
    and calculate BMI, category and risk based on given data.

    param input_data : list of all input elements
    return output_data : list of objects of class HealthDetails

    Function calls data_append function that returns a list of updated details of patients
    """

    output_data: list[HealthDetails] = []
    for i in input_data:
        output_data.append(HealthDetails(i['Gender'], i['HeightCm'], i['WeightKg']))
    output_data = data_append(output_data)

    return output_data


def data_append(output_data: list) -> list:
    """
    Function to create a new list that contains updated details of patients
    by reading them from the respective objects of class HealthDetails.

    param output_data: list of objects of class HealthDetails
    return result : list of dictionary containing details of patients
    """

    result: list = []
    for o in output_data:
        result.append({'Gender': o.gender, 'HeightCm': o.height, 'WeightKg': o.weight, 'BMI': o.bmi,
                       'BMI Category': o.category, 'Health risk': o.risk})
    return result


def count_overweight(result: list) -> int:
    """
    Function to count the total number of overweight patients in given data

    param result: list of dictionary containing details of patients
    return: count: Overweight patients
    """
    count = 0
    for r in result:
        if 25 <= r['BMI'] <= 29.9:
            count += 1
    return count


if __name__ == '__main__':
    # Read json file
    fo = open("input.json", "r")
    input_data = json.load(fo)
    fo.close()

    output_data = data_input(input_data)

    # write the final result in new json file
    final_json_file = open("result.json", "w")
    json.dump(output_data, final_json_file, indent=2)
    final_json_file.close()

    # write count of overweight patient in new text file
    f = open("overweight.txt", "w")
    f.write("Total number of overweight people are : ")
    f.write(str(count_overweight(output_data)))
    f.close()
