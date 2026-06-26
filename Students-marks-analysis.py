import pandas as pd
import matplotlib.pyplot as plt

# Create Dataset
data = {
    "Name": ["Aman", "Riya", "Rahul", "Neha", "Mohit"],
    "Maths": [85, 92, 70, 88, 60],
    "Science": [90, 88, 75, 91, 65],
    "English": [80, 95, 72, 89, 70]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Student Marks Analysis")
print(df)

print("\nHead")
print(df.head())

# Calculate Average Marks
df["Average Marks"] = (
    df["Maths"] +
    df["Science"] +
    df["English"]
) / 3

# Highest Maths Marks
Highest_Maths = df["Maths"].max()
print("\nHighest Maths Marks:", Highest_Maths)

# Calculate Total Marks
df["Total"] = (
    df["Maths"] +
    df["Science"] +
    df["English"]
)

# Calculate Percentage
df["Percentage"] = df["Total"] / 3

# Highest Percentage
Highest_Percentage = df["Percentage"].max()
print("Highest Percentage:", Highest_Percentage)

# Result Column
df["Result"] = df["Percentage"].apply(
    lambda x: "Pass" if x >= 75 else "Needs Improvement"
)

# Final Data
print("\nFinal Data")
print(df)

# Bar Chart
plt.bar(df["Name"], df["Total"])
plt.title("Student Marks Analysis")
plt.xlabel("Student Names")
plt.ylabel("Total Marks")
plt.show()