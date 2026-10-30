# -------------------- PART 1: LOAD DATA --------------------

# Q1. Import pandas
import pandas as pd
import numpy as np


# Q2. Load school_data.csv into a DataFrame
df = pd.read_csv("school_data.csv")


# Q3. Display the first 10 rows
print("\nQ3. First 10 Rows:")
print(df.head(10))


# Q4. Show dataset info and data types
print("\nQ4. Dataset Information:")
df.info()

print("\nData Types:")
print(df.dtypes)


# ============================================================
# PART 2: CLEANING DATA
# ============================================================


# -------------------- 1. CLEANING EMPTY CELLS --------------------

# Q1. Identify rows with missing values
print("\nQ1. Rows with Missing Values:")
print(df[df.isnull().any(axis=1)])


# Q2. Replace missing marks with the mean of that subject
# First convert marks into numeric values
marks = ["eng", "hin", "mar"]

for col in marks:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Fill missing marks with subject mean
for col in marks:
    df[col] = df[col].fillna(df[col].mean())

print("\nQ2. Missing Values Filled with Subject Mean:")
print(df)


# Q3. Create another version where rows with missing
# values are dropped
# Use the original data for this alternative version
df_original = pd.read_csv("school_data.csv")

df_dropped = df_original.dropna()

print("\nQ3. Dataset After Dropping Missing Values:")
print(df_dropped)


# -------------------- 2. CLEANING WRONG FORMAT --------------------

# Q1. Check data types of all columns
print("\nQ1. Data Types of All Columns:")
print(df.dtypes)


# Q2. Convert eng, hin, mar columns to numeric
for col in marks:
    df[col] = pd.to_numeric(df[col], errors="coerce")

print("\nQ2. Marks Columns Converted to Numeric:")
print(df.dtypes)


# Q3. Handle errors (e.g., "abc" in marks column)
# errors="coerce" converts incorrect values into NaN
print("\nQ3. Rows with Incorrect English Marks:")
print(df[df["eng"].isnull()])

# Fill incorrect values with subject mean
for col in marks:
    df[col] = df[col].fillna(df[col].mean())


# -------------------- 3. CLEANING WRONG DATA --------------------

# Marks should be between 1 and 100


# Q1. Find rows where marks are greater than 100
# or less than 1
print("\nQ1. Rows with Invalid Marks:")

invalid_marks = df[
    (df[marks] > 100).any(axis=1) |
    (df[marks] < 1).any(axis=1)
]

print(invalid_marks)


# Q2. Replace invalid marks with NaN
for col in marks:
    df.loc[(df[col] > 100) | (df[col] < 1), col] = np.nan

print("\nQ2. Invalid Marks Replaced with NaN:")
print(df)


# Q3. Fill invalid marks with the subject average
for col in marks:
    df[col] = df[col].fillna(df[col].mean())

print("\nQ3. Invalid Marks Filled with Subject Mean:")
print(df)


# -------------------- 4. REMOVING DUPLICATES --------------------

# Q1. Identify duplicate rows
print("\nQ1. Duplicate Rows:")
print(df[df.duplicated()])


# Q2. Remove duplicate student records

# Q3. Show dataset size before and after removing duplicates

# Display size before removing duplicates
print("\nQ3. Size Before Removing Duplicates:")
print(len(df))

# Remove duplicate records
df = df.drop_duplicates()

# Display size after removing duplicates
print("\nQ2. Dataset After Removing Duplicates:")
print(df)

print("\nQ3. Size After Removing Duplicates:")
print(len(df))


# -------------------- FINAL CLEANED DATASET --------------------

print("\nFINAL CLEANED SCHOOL DATA:")
print(df)


# Save the cleaned dataset into a new CSV file
df.to_csv("cleaned_school_data.csv", index=False)

print("\nCleaned dataset saved successfully!")
