print("Student Performance Analysis Project")
print("Welcome to my Data Science Project!")

print("Project started successfully.")

import pandas as pd
import numpy as np

np.random.seed(42)

students = {
    "Student_ID": range(1, 101),
    "Attendance": np.random.randint(40, 101, 100),
    "Study_Hours": np.random.randint(1, 9, 100),
    "Maths_Marks": np.random.randint(30, 101, 100),
    "Science_Marks": np.random.randint(30, 101, 100),
    "English_Marks": np.random.randint(30, 101, 100)
}

df = pd.DataFrame(students)

df["Final_Score"] = df[
    ["Maths_Marks", "Science_Marks", "English_Marks"]
].mean(axis=1).round(2)

df.to_csv("./data/student_data.csv", index=False)
print("Dataset created successfully!")
print(df.head())

print("\n--- DATA ANALYSIS ---")

print("Dataset Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\n--- STUDENT PERFORMANCE ---")

print("Average Attendance:",
      df["Attendance"].mean().round(2))

print("Average Study Hours:",
      df["Study_Hours"].mean().round(2))

print("Average Maths Marks:",
      df["Maths_Marks"].mean().round(2))

print("Average Science Marks:",
      df["Science_Marks"].mean().round(2))

print("Average English Marks:",
      df["English_Marks"].mean().round(2))

print("Average Final Score:",
      df["Final_Score"].mean().round(2))

import matplotlib.pyplot as plt

print("\nCreating Visualizations...")

plt.figure(figsize=(8, 5))

plt.hist(df["Attendance"], bins=10)

plt.title("Student Attendance Distribution")
plt.xlabel("Attendance (%)")
plt.ylabel("Number of Students")

plt.savefig("charts/attendance_distribution.png")

plt.show()

plt.figure(figsize=(8, 5))

plt.scatter(df["Study_Hours"], df["Final_Score"])

plt.title("Study Hours vs Final Score")
plt.xlabel("Daily Study Hours")
plt.ylabel("Final Score")

plt.savefig("charts/study_hours_vs_score.png")

plt.show()

subjects = ["Maths", "Science", "English"]

average_marks = [
    df["Maths_Marks"].mean(),
    df["Science_Marks"].mean(),
    df["English_Marks"].mean()
]

plt.figure(figsize=(8, 5))

plt.bar(subjects, average_marks)

plt.title("Subject-wise Average Marks")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")

plt.savefig("charts/subject_average_marks.png")

plt.show()

def categorize_performance(score):
    if score >= 75:
        return "High Performer"
    elif score >= 50:
        return "Average Performer"
    else:
        return "Low Performer"


df["Performance_Category"] = df["Final_Score"].apply(
    categorize_performance
)

print("\n--- PERFORMANCE CATEGORIES ---")
print(df["Performance_Category"].value_counts())

df.to_csv("data/student_data.csv", index=False)

print("\nUpdated dataset saved successfully!")

print("\n--- FINAL PROJECT SUMMARY ---")

print("Total Students:", len(df))

print("High Performers:",
      (df["Performance_Category"] == "High Performer").sum())

print("Average Performers:",
      (df["Performance_Category"] == "Average Performer").sum())

print("Low Performers:",
      (df["Performance_Category"] == "Low Performer").sum())

print("\nProject Completed Successfully!")