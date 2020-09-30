#list to store the values of powers
powers = []

#for loops to iterate through the numbers
for a in range(2,101):
	for b in range(2,101):
		powers.append(a**b)

#removing the duplicates using sets
powers = set(powers)

#printing the length of powers
print(len(powers))
