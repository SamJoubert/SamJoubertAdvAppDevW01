# Program Name: A2.py
# Course: IT3883/Section W01
# Student Name: Sam Joubert
# Assignment Number: Lab 2
# Due Date: 9/19/2025
# Purpose: This program reads data from a text file, assigns integers to 9 name variables,
# averages the integers, and then prints them along with their respective strings in
# descending order.
# List Specific resources used to complete the assignment: Module 2-2-Files-Objects,
# W3Schools Python List sort() Method, W3Schools Python Lambda, W3Schools Python Lists

#gives A2.py access to the necessary text file
file_object = open('Assignment2input.txt', 'r')

#reads lines and closes the file
lines = file_object.readlines()
file_object.close()

#list to contain student values
students = []

for line in lines:
    parts = line.strip().split() #separates numbers and names into individual values
    name = parts[0]
    scores = list(map(float, parts[1:])) #converts score strings into floats

    average = sum(scores) / 6 #averages scores
    students.append((name, average))

#sorts the students by average score in descending order
students.sort(key=lambda x: x[1], reverse=True)

#prints the results
for name, avg in students:
    print(name + ": " + str(round(avg, 2)))

