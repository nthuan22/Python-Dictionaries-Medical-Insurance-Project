# Add your code here
#create an empty dictionary called medical_costs
medical_costs = {}

#adding the following key-value pairs
medical_costs["Marina"] = 6607.0
medical_costs["Vinay"] = 3225.0

#add the following three patients to the medical_costs dictionary
medical_costs.update({"Connie" : 8886.0, "Isaac" : 16444.0, "Valentina" : 6420.0})

#Print medical_costs
#print(medical_costs)

#Update the value associated with Vinay to 3325.0 
medical_costs["Vinay"] = 3325.0
#print(medical_costs)

#calculate the average medical cost of each patient
total_costs = 0
for cost in medical_costs.values():
  total_costs += cost

#create a variable called average_cost that stores the total_cost divided by the length of the medical_costs dictionary
average_cost = total_costs / len(medical_costs)
print("Average Insurance Cost: " + str(average_cost))

#create two lists called names and ages
names = ['Marina', 'Vinay', 'Connie', 'Isaac', 'Valentina']
ages = [27, 24, 43, 35, 52]

#create a variable called zipped_ages that is a zipped list of pairs between the names list and the ages list
zipped_ages = zip(names, ages)

#Create a dictionary called names_to_ages by using a list comprehension that iterates through zipped_ages and turns each pair into a key : value item
names_to_ages = {name:age for name, age in zipped_ages}
print(names_to_ages )

#Use .get() to get the value of Marina’s age and store it in a variable called marina_age
marina_age = names_to_ages.get("Marina", None)
print("Marina's ages is: " + str(marina_age))

#create an empty dictionary called medical_records
medical_records = {}

#add "Marina" to medical_records as a key with the value being a dictionary of medical data
medical_records["Marina"] = {"Age" : 27, "Sex" : "Female", "BMI": 31.1, "Children" : 2, "Smoker" : "Non-smoker", "Insurance_cost" : 6607.0}

#Do the same for the remaining individuals
medical_records["Vinay"] = {"Age" : 22, "Sex" : "Male", "BMI": 26.9, "Children" : 0, "Smoker" : "Non-smoker", "Insurance_cost" : 3225.0}
medical_records["Connie"] = {"Age" : 43, "Sex" : "Female", "BMI": 25.3, "Children" : 3, "Smoker" : "Non-smoker", "Insurance_cost" : 8886.0}
medical_records["Isaac"] = {"Age" : 35, "Sex" : "Male", "BMI": 20.6, "Children" : 4, "Smoker" : "Smoker", "Insurance_cost" : 16444.0}
medical_records["Valentina"] = {"Age" : 52, "Sex" : "Female", "BMI": 18.7, "Children" : 1, "Smoker" : "Non-smoker", "Insurance_cost" : 6420.0}

#Print medical_records
#print(medical_records)

#Print out Connie’s insurance cost 
print("Connie's insurance cost is " + str(medical_records["Connie"]["Insurance_cost"])  + " dollar.")

#Remove Vinay from medical_records
medical_records.pop("Vinay")

#Use a for loop to iterate through the items of medical_records.
for name, record in medical_records.items():
  print(name + " is a " + str(record["Age"]) + \
  " year old " + record["Sex"] + " " + record["Smoker"] \
  + " with a BMI of " + str(record["BMI"]) + \
  " and insurance cost of " + str(record["Insurance_cost"]))









