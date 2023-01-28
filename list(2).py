prime_numbers = [2, 3, 5]
print("List1:", prime_numbers)

#We use the extend() method to add all items of one list to another

even_numbers = [4, 6, 8]
print("List2:", even_numbers)

# join two lists
prime_numbers.extend(even_numbers)

print("List after append:", prime_numbers)