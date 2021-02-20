#choose what to convert
choose = input("What do you want to convert? \nInches to cm - i \npounds to kg - p \ncm to inches - cm \nkg to pounds - kg \nEnter value - ")
#convert cm to inches var
inch = 1 * 2.54
#convert pound to kg var
pound = 1 * 0.453592
#convert inches to cm var
cm = 1 / 2.54
#convert pounds to kg var
kg = 1 / 0.453592

#if statement to convert inches to cm
if choose == "i":
    cm = float(input("Inches to cm - Enter value: "))
    sum = inch * cm
    print(round(sum, 2))
#if statement to convert cm to inches
elif choose == "cm":
    inches = float(input("cm to inches - Enter value: "))
    sum2 = cm * inches
    print(round(sum2, 2))
#if statement to convert kg to pounds
elif choose == "p":
    kg = float(input("Pounds to kg - Enter value: "))
    sum1 = pound * kg
    print(round(sum1, 2))
#if statement to convert pounds to kg
elif choose == "kg":
    lbs = float(input("KG to pounds - Enter value: "))
    sum3 = kg * lbs
    print(round(sum3, 2))
#print for any other choose
else:
    print("Enter valid value")
