#Part 1 - Create a List of Random Numbers
from random import randint #This line imports the randint function from the random module. The randint function generates a random integer between two specified values


ranNums = [] #name your list and make sure it is empty!
for index in range(10): #for loop appends 5 numbers to your list, but make sure you name your variable
    ranNums.append(randint(1,50)) #this adds a random number between 1-50 to the list
print("List of numbers/Original list", ranNums) #print the list!


# Generates a list of 5 or 10 random integers between 1 and 50 inclusive.
#User input - Part 3
user_input = input("Enter a number between 1 and 50 to search for: ")
random_number_to_search = int(user_input)


#Part 2a
print("Searching for number", random_number_to_search)

if random_number_to_search in ranNums:
    print("Number",random_number_to_search,"found in the list!")
else:
    print("Number",random_number_to_search,"not found in the list!")

#Part 2b
comparisons = 0  # Initialize the counter for comparisons
found = False  # Variable to track if the number was found

for part2b in ranNums:  # Name your variable in the for loop
    comparisons += 1  # Increment the counter for each comparison
    if part2b == random_number_to_search:
        found = True  # Set found to True if the number is in the list
        break  # Exit the loop early if the number is found

print("After",comparisons,"comparisons")

#Part 3, finding min
smallest_value = min(ranNums)
print("The smallest value in the list is:", smallest_value)

#Part 3, finding max
largest_value = max(ranNums)
print("The largest value in the list is:", largest_value)

#Part 3, finding sum
sum_list = ranNums
list_sum = 0
for index in ranNums:
    list_sum = list_sum + index
print("Sum of all elements in the list:", list_sum)

#Part 3, sorting
sort_list= sorted (ranNums)
print("The sorted list is", sort_list)

#Part 3, fun functions
#1. Reverse
ranNums.reverse()
print("The orignal list reversed is:", ranNums)

#2. Find the position of the smallest number in the index
smallest_position = ranNums.index(smallest_value)
print("The smallest value is at index:", smallest_position)

#3. Pop, remove and save last number
last_num = ranNums.pop()
print("I popped",last_num,"off the end of the list! The list is now",ranNums)