print("This is a Body Mass Index Calculator \n" "To calculate your BMI we'll need some information from you first")
height = input("\nEnter your height in inches: ")
weight = input("Enter your weight in lbs: ")
new_height = float(height)
new_weight = int(weight)
result = round((new_weight / new_height ** 2) * 703, 2)
print("\nThis is your BMI:" + str(result))
print("\nThe CDC states that a healthy BMI ranges from 18.5 - 24.9")
