#Python program to calculate the sum of first 749302 natural numbers using while loop
total_sum = 0
num = 1

while num <= 749302:
    total_sum += num
    num += 1

print(f"The sum of the first 749302 natural numbers is: {total_sum}")