number = int(input("Please enter a positive number: "))
sum = 0
print(f"A: sum = {sum} - count = /")

for count in range(1, number+1):
    print(f"B: sum = {sum} - count = {count}")
    sum += count
    print(f"C: sum = {sum} - count = {count}")

print("The sum is:", sum)
