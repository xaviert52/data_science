# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(age, sex, bmi, num_of_children, smoker, name):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  output = 'The estimated insurance cost for ' + name + ' is ' + str(estimated_cost) + ' dollars.'
  return estimated_cost, output

# Initial variables for Maria 
# Estimate Maria's insurance cost
maria_insurance_cost, maria_output = calculate_insurance_cost(age = 28, sex = 0, bmi = 26.2, num_of_children = 3, smoker = 0, name = "Maria")

print(maria_output)

# Initial variables for Omar
# Estimate Omar's insurance cost 
omar_insurance_cost, omar_output = calculate_insurance_cost(age = 35, sex = 1, bmi = 22.2, num_of_children = 0, smoker = 1, name = "Omar")

print(omar_output)

# My estimate insurance cost
my_insurance_cost, my_output = calculate_insurance_cost(age = 26, sex = 1, bmi = 26, num_of_children = 0, smoker = 1, name = "Xavier")

print(my_output)

def difference(insurance1, insurance2):
  insuranceDiff = abs(insurance1 - insurance2)
  print('The difference in insurance cost is ' + str(insuranceDiff) + ' dollars.')

difference(maria_insurance_cost, omar_insurance_cost)