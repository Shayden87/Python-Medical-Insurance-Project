#####################################################################
# Author: Spencer Hayden
# Project: Medical Insurance Project
# Company: Code Academy 
# Date: 03/08/2022
# Version: v1.3
# Description: Basic Python project to highlight utilization of
# Python Syntax by creating formula that estimates a person's yearly
# insurance cost based on certain variables/criteria. Improved upon 
# v1.20 as a functions to provide more information to smokers and 
# those with higher BMI was added.
#####################################################################

# Function to provide user more info on lowering cost with regards to smoking status
def analyze_smoker(smoker_status):
  if smoker_status == 1:
    print("To lower your cost, you should consider quitting smoking.")
  else:
    print("Smoking is not an issue for you.")

# Function to provide user more info on lowering cost with regards to BMI value
def analyze_bmi(bmi_value):
  if bmi_value > 30:
    print("Your BMI is in the obese range. To lower your cost, you should significantly lower your BMI.")
  elif bmi_value >= 25 and bmi_value <= 30:
    print("Your BMI is in the overweight range. To lower your cost, you should lower your BMI.")
  elif bmi_value >= 18.5 and bmi_value < 25:
    print("Your BMI is in a healthy range.")
  elif bmi_value < 18.5: 
    print("Your BMI is in the underweight range. Increasing your BMI will not help lower your cost, but it will help improve your health.")

# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  analyze_smoker(smoker)
  analyze_bmi(bmi)
  return estimated_cost
 
# Estimate Keanu's insurance cost
keanu_insurance_cost = estimate_insurance_cost(name = 'Keanu', age = 29, sex = 1, bmi = 26.2, num_of_children = 3, smoker = 1)

# Estimate my insurance cost
my_insurance_cost = estimate_insurance_cost(name = 'Spencer', age = 34, sex = 1, bmi = 18.2, num_of_children = 0, smoker = 1)