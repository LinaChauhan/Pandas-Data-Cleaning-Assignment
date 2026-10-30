# 🐼 School Data Cleaning Using Python Pandas

## 📌 About the Project

This project is a beginner-level Python Pandas assignment focused on **cleaning and preprocessing student marks data**.

The dataset contains student details such as roll number, name, class, and marks in English, Hindi, and Marathi.

Some records contain intentionally incorrect data, including:

- Missing values (empty cells).
- Incorrect data formats (e.g., `"abc"` in marks).
- Invalid marks (values below 1 or above 100).
- Duplicate student records.

The purpose of this project is to understand how to identify and handle these data quality issues using Python and Pandas.

## 🎯 Objectives

- Load CSV data into a Pandas DataFrame.
- Explore datasets using Pandas functions.
- Identify and handle missing values.
- Convert columns into appropriate data types.
- Detect and correct invalid data.
- Find and remove duplicate records.
- Export the cleaned dataset into a new CSV file.

## 🛠️ Technologies Used

- **Python** – Programming language.
- **Pandas** – Data manipulation and cleaning.
- **NumPy** – Handling missing and invalid values.
- **CSV** – Dataset storage format.

## 📂 Project Structure

text

```
School-Data-Cleaning/
│
├── school_data.csv
│
├── school_data_cleaning.py
│
└── README.md
```

| File | Description |
| --- | --- |
| `school_data.csv` | Original dataset containing incorrect data |
| `school_data_cleaning.py` | Python script containing all cleaning operations |
| `README.md` | Project documentation |

## 📊 Dataset Information

The dataset contains 25 student records with the following columns:

| Column | Description |
| --- | --- |
| `roll` | Student roll number |
| `name` | Student name |
| `class` | Student class |
| `eng` | English marks |
| `hin` | Hindi marks |
| `mar` | Marathi marks |

**Data cleaning challenges included:**

- Missing English and Hindi marks.
- `"abc"` as an incorrect English mark.
- `102` as an invalid Marathi mark.
- `150` as an invalid English mark.
- Duplicate records for students.

## 🧹 Data Cleaning Operations

The project covers the following operations:

### 1\. Loading Data

- Import Pandas and NumPy.
- Read the CSV file using `pd.read_csv()`.
- Display the first 10 rows.
- Check dataset information and data types.

### 2\. Handling Missing Values

- Identify missing values using `isnull()`.
- Replace missing marks with the subject mean using `fillna()`.
- Create an alternative dataset using `dropna()`.

### 3\. Handling Incorrect Data Formats

- Check column data types using `dtypes`.
- Convert marks columns into numeric values using `pd.to_numeric()`.
- Handle incorrect values such as `"abc"` using `errors="coerce"`.

### 4\. Handling Invalid Data

- Identify marks below 1 or above 100.
- Replace invalid marks with `NaN`.
- Fill invalid marks with the respective subject average.

### 5\. Removing Duplicates

- Identify duplicate records using `duplicated()`.
- Remove duplicate records using `drop_duplicates()`.
- Compare dataset size before and after removing duplicates.

### 6\. Exporting Cleaned Data

- Save the final cleaned dataset using `to_csv()`.

## ⚙️ Installation and Setup

### Prerequisites

Make sure Python is installed on your system.

### Step 1: Clone the Repository

bash

```
git clone https://github.com/LinaChauhan/Pandas-Data-Cleaning-Assignment/
```

### Step 2: Navigate to the Project Folder

bash

```
cd Pandas-Data-Cleaning-Assignment
```

### Step 3: Install Required Libraries

bash

```
pip install pandas numpy
```

### Step 4: Run the Python Script

bash

```
python PandasDataCleaning.py
```

### Step 5: Check the Output

After successful execution, a new file named `cleaned_school_data.csv` will be generated in the project folder.

## 📚 Pandas Functions Learned

| Function | Usage |
| --- | --- |
| `read_csv()` | Read CSV files |
| `head()` | Display first rows |
| `info()` | Display dataset information |
| `dtypes` | Check data types |
| `isnull()` | Identify missing values |
| `fillna()` | Fill missing values |
| `dropna()` | Remove missing-value rows |
| `to_numeric()` | Convert values into numbers |
| `mean()` | Calculate average |
| `duplicated()` | Identify duplicate records |
| `drop_duplicates()` | Remove duplicate records |
| `to_csv()` | Export cleaned data |

## 🎓 Learning Outcomes

Through this assignment, I learned:

- How to work with CSV files using Pandas.
- How to explore and understand datasets.
- How to handle missing and incorrect values.
- How to convert data into appropriate formats.
- How to identify invalid data and correct it.
- How to remove duplicate records.
- How to perform basic data preprocessing.

⭐ This project is part of my learning journey in Python, Pandas, and Data Analytics.

If you find this project helpful, feel free to explore the code and learn along with me\!
