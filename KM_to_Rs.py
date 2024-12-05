#Q5-Program for transport company fare calculation
distance = float(input("Enter the distance traveled (in Km): "))

if distance <= 50:
    fare = distance * 8
elif distance <= 100:
    fare = distance * 10
else:
    fare = distance * 12

print("The total fare is Rs.", fare)
