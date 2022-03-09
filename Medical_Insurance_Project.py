#####################################################################
# Author: Spencer Hayden
# Project: Medical Insurance Project
# Company: Code Academy 
# Date: 03/08/2022
# Description: Basic Python project to highlight utilization of
# Python Syntax by creating formula that estimates a person's yearly
# insurance cost based on certain variables/criteria.
#####################################################################
# create the initial variables to calculate medical insurance cost
age = 28
sex = 0
bmi = 26.2
num_of_children = 3
smoker = 0

# Add insurance estimate formula below
insurance_cost = ((250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (24000 * smoker) - 12500)
print("This person's insurance cost is", str(insurance_cost), "dollars")

# Age Factor
age += 4

new_insurance_cost = ((250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (24000 * smoker) - 12500)

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in cost of insurance after increasing the age by 4 years is", str(change_in_insurance_cost), "dollars")

# BMI Factor
age = 28
bmi += 3.1

new_insurance_cost = ((250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (24000 * smoker) - 12500)

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated insurance cost after increasing the BMI by 3.1 years is", str(change_in_insurance_cost), "dollars")

# Male vs. Female Factor
bmi = 26.2
sex = 1

new_insurance_cost = ((250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (24000 * smoker) - 12500)

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated cost for being male instead of female is", str(change_in_insurance_cost), "dollars")
