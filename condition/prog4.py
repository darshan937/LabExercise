'''Task -----------------condition------------------------------
Weight converter:
Input the weight of a person in either kg or lbs. If the person provides his/her
weight in kg then convert it into lbs
else convert it to kg.
'''
weight = int(input("enter the weight: "))
unit = input("enter the unit for weight (kg/lbs): ").lower()
if unit == "kg":
    convert = weight * 2.20426
    print(f"{weight} kg is {convert} lbs")
elif unit == "lbs":
    convert = weight * 0.453592
    print(f"{weight} lbs is {convert} kg ")
else:
    print("need to use either kg or lbs as unit")