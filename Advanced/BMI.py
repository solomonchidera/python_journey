def calculate_bmi(height, weight):
    """
    Calculates the Body Mass Index (BMI) using height and weight.
    Formula: BMI = weight / (height * height)
    """
    bmi = weight / (height * height)
    return bmi


def get_bmi_category(bmi):
    """
    Returns the BMI category based on the calculated BMI value.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 24.9 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"


def main():
    # Get height and weight from user
    height = float(input("Enter your height in meters: "))
    weight = float(input("Enter your weight in kilograms: "))

    # Calculate BMI
    bmi = calculate_bmi(height, weight)

    # Get BMI category
    category = get_bmi_category(bmi)

    # Display the result
    print("Your BMI is: {:.2f}".format(bmi))
    print("BMI Category: ", category)


if __name__ == "__main__":
    main()
