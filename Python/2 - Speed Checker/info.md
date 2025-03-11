# **2 - Speed Tracker**

Create a program that takes a time for a car going past a speed camera, the time going past the next one and the distance between them to calculate the average speed for
the car in mph. The cameras are one mile apart.
Extensions:
1. Speed cameras know the timings of each car going past, through number plate recognition. Valid number plates are two letters, two numbers and three letters afterwards,
for example XX77 787. Produce a part of the program that checks whether a number plate matches the given pattern. Tell the user either way.
2. Create a program for creating a file of details for vehicles exceeding the speed limit set for a section of road. You will need to create a suitable file with test data, including
randomised number plates and times. You will then use the code you’ve already written to process this list to determine who is breaking the speed limit (70mph) and who
has invalid number plates.

## Planning:

First, I will create a function for finding the average mph, based on 2 timestamps (hh/mm/ss), and the distance between the two timestamps (so to speak)
I will then make a function to check whether something was over the speed limit, based on 2 parameters.
I will continue to make a function which will check if a numberplate's format is standard or not. I will show an example of the first and third subroutine I made. (how to use them)
Following this, I'll make a txt file with number-plates, and their timestamps, in the aim to iterate through each line, finding if the numberplates are standard, and if they're going over the speed limit.

## Evaluation:

This was simple enough, but I found the question slightly ambiguous. I enjoyed coming up with a way to store "2D arrays" in a way that can be stored in a txt file