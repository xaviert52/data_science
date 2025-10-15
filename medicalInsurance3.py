# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  return estimated_cost
 
# Estimate Maria's insurance cost
maria_insurance_cost = estimate_insurance_cost(name = "Maria", age = 31, sex = 0, bmi = 23.1, num_of_children = 1, smoker = 0)

# Estimate Rohan's insurance cost
rohan_insurance_cost = estimate_insurance_cost(name = 
"Rohan", age = 25, sex = 1, bmi = 28.5, num_of_children = 3, smoker = 0)

# Estimate Valentina's insurance cost
valentina_insurance_cost = estimate_insurance_cost(name = "Valentina", age = 53, sex = 0, bmi = 31.4, num_of_children = 0, smoker = 1)

# Estimate Akira's insurance cost
akira_insurance_cost = estimate_insurance_cost(name = "Akira", age = 19, sex = 1, bmi = 27.1, num_of_children = 0, smoker = 0)

# Add your code here
names = ["Maria", "Rohan", "Valentina"]
names.append("Akira")
insurance_costs = [4150.0, 5320.0, 35210.0]
insurance_costs.append(2930.0)
insurance_data = list(zip(names, insurance_costs))
print("\nHere is the actual insurance cost data:\n" + str(insurance_data))

estimated_insurance_data = []

estimated_insurance_data.append(("Maria", maria_insurance_cost))
estimated_insurance_data.append(("Rohan", rohan_insurance_cost))
estimated_insurance_data.append(("Valentina", valentina_insurance_cost))
estimated_insurance_data.append(("Akira", akira_insurance_cost))

print("\nHere is the estimated insurance cost data:\n" + str(estimated_insurance_data))

insurance_cost_difference = [[insurance_data[0][0], abs(insurance_data[0][1] - estimated_insurance_data[0][1])], [insurance_data[1][0], abs(insurance_data[1][1] - estimated_insurance_data[1][1])], [insurance_data[2][0],abs(insurance_data[2][1] - estimated_insurance_data[2][1])], [insurance_data[3][0], abs(insurance_data[3][1] - estimated_insurance_data[3][1])]]

print("\nHere is the difference between estimated and actual insurance cost data:\n" + str(insurance_cost_difference))

