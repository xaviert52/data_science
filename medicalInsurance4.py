names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add your code here
names.append("Priscilla")
insurance_costs.append(8320.0)

medical_records = list(zip(insurance_costs, names))
print(medical_records)

num_medical_records = len(medical_records)
print('\nThere are ' + str(num_medical_records) + ' medical records')

first_medical_record = medical_records[0]
print('\nHere is the first medical record:\n' + str(first_medical_record))

medical_records.sort(reverse = True)
print('\nHere are the medical records sorted by insurance cost:\n' + str(medical_records))

cheapest_three = medical_records[-3:]
print('\nHere are the three cheapest insurance costs in our medical records:\n' + str(cheapest_three))

priciest_three = medical_records[0:3]
print('\nHere are the three most expensive insurance costs in our medical records:\n' + str(priciest_three))

occurrences_paul = names.count("Paul")
print('\nThere are ' + str(occurrences_paul) + ' individuals with the name Paul in our medical records.')

medical_records_by_names = list(zip(names, insurance_costs))
medical_records_by_names.sort()
print('\nThe medical records sorted by names:\n'+ str(medical_records_by_names))

middle_five_records = medical_records[3:7]
print('\nHere are the middle five records:\n' + str(middle_five_records))