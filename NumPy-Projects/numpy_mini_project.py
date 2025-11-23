#Student Marks Data Analysis using NumPy

# This project uses NumPy to analyze students’ marks — 
# it calculates mean, median, highest score, lowest score, and standard deviation.

import numpy as np

# --- Student Marks Data ---
# Each row = [Math, Science, English]
marks = np.array([
    [85, 78, 92],
    [74, 88, 90],
    [96, 94, 89],
    [64, 70, 72],
    [88, 90, 85]
])

students = np.array(["Aman", "Riya", "Rohit", "Neha", "Tanya"])

# --- Analysis using NumPy ---
average_marks = np.mean(marks, axis=1)
subject_avg = np.mean(marks, axis=0)
highest_marks = np.max(marks)
lowest_marks = np.min(marks)
std_dev = np.std(marks)

# --- Output ---
print("=== Student Marks Data Analysis ===\n")
for i in range(len(students)):
    print(f"{students[i]} -> Average Marks: {average_marks[i]:.2f}")

print("\n=== Subject Averages ===")
print(f"Math: {subject_avg[0]:.2f}, Science: {subject_avg[1]:.2f}, English: {subject_avg[2]:.2f}")

print("\nHighest mark in the class:", highest_marks)
print("Lowest mark in the class:", lowest_marks)
print("Standard Deviation of all marks:", round(std_dev, 2))

print("\n=== Students Scoring Above Class Average ===")
class_avg = np.mean(average_marks)
above_avg = students[average_marks > class_avg]
print(above_avg)
