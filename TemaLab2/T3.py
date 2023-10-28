# exercitiile sunt preluate de pe https://www.w3schools.com/python/exercise.asp?filename=exercise_lists1

#Exercise 1
print("\nExercise 1:\n")

# Print the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#Exercise 2
print("\nExercise 2:\n")

# Change the value from "apple" to "kiwi", in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

print(fruits)

#Exercise 3
print("\nExercise 3:\n")

# Use the append method to add "orange" to the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

print(fruits)

#Exercise 4
print("\nExercise 4:\n")

# Use the insert method to add "lemon" as the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")

print(fruits)

#Exercise 5
print("\nExercise 5:\n")

# Use the remove method to remove "banana" from the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

print(fruits)

#Exercise 6
print("\nExercise 6:\n")

# Use negative indexing to print the last item in the list.
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#Exercise 7
print("\nExercise 7:\n")

# Use a range of indexes to print the third, fourth, and fifth item in the list.
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#Exercise 8
print("\nExercise 8:\n")

# Use the correct syntax to print the number of items in the list.
fruits = ["apple", "banana", "cherry"]
print(len(fruits))
