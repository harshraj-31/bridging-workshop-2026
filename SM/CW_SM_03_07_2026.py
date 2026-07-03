import pandas as pd

# Read CSV file
df = pd.read_csv(r"C:\Insight Files\Student_Result.csv")

# Display DataFrame
print(df)

# Mean of Math marks
math_mean = df["Math"].mean()
print("Mean of Math:", math_mean)

# Variance of English marks
english_var = df["English"].var()
print("Variance of English:", english_var)

# Standard Deviation of English marks
english_std = df["English"].std()
print("Standard Deviation of English:", english_std)

# Create a new DataFrame
df_new = df[["Math", "Science", "English"]]
print(df_new)

# Import libraries for visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Histogram
plt.figure(figsize=(5, 7))
plt.title("Histogram")
sns.histplot(df["Science"], bins=6)
plt.xlabel("Science")
plt.ylabel("Frequency")
plt.show()

# Box Plot
df_new = df[["Math", "Science", "English", "Computer"]]

plt.boxplot(df_new["Math"])
plt.title("Boxplot")
plt.ylabel("Math")
plt.show()

# Correlation Matrix
correlation = df_new.corr()
print(correlation)

# Heatmap
plt.figure(figsize=(10, 10))
sns.heatmap(correlation, annot=True)
plt.title("Heatmap of Marks")
plt.show()