# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi_value_float = weight / (height * height)

bmi_value = round(bmi_value_float)



if bmi_value < 18.5:
    print(f"Your BMI is {bmi_value} , you are underweight.")
elif bmi_value < 25.0:
    print(f"Your BMI is {bmi_value} , you have a normal weight.")
elif bmi_value < 30.0:
    print(f"Your BMI is {bmi_value} , you are slightly overweight.")
elif bmi_value < 35.0:
    print(f"Your BMI is {bmi_value} , you are obese.")
else:
    print(f"Your BMI is {bmi_value} , you are clinically obese.")