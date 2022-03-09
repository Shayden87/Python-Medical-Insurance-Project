#####################################################################
# Author: Spencer Hayden
# Project: Medical Insurance Project
# Company: Code Academy 
# Date: 03/08/2022
# Version: v1.2
# Description: Basic Python project to highlight utilization of
# Python Syntax by creating formula that estimates a person's yearly
# insurance cost based on certain variables/criteria. Improved upon 
# v1.0 as a function to calculate insurance cost was added.
#####################################################################

# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(age, sex, bmi, num_of_children, smoker, name):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print("The estimated insurance cost for " + name + " is " + str(estimated_cost) + " dollars.")
  return estimated_cost

# Initial variables for Maria 
age = 28
sex = 0  
bmi = 26.2
num_of_children = 3
smoker = 0  
name = "Maria"
# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost(age, sex, bmi, num_of_children, smoker, name)

# Initial variables for Omar
age = 35
sex = 1 
bmi = 22.2
num_of_children = 0
smoker = 1  
name = "Omar"
# Estimate Omar's insurance cost 
omar_insurance_cost = calculate_insurance_cost(age, sex, bmi, num_of_children, smoker, name)

age = 34
sex = 1 
bmi = 16.2
num_of_children = 0
smoker = 1  
name = "Spencer"
# Estimate my insurance cost 
my_insurance_cost = calculate_insurance_cost(age, sex, bmi, num_of_children, smoker, name)