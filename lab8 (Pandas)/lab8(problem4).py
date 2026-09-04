import pandas as pd

titanic = pd.read_csv("titanic.csv")

print("Original Dataset:")
print(titanic.head())

print("\nOriginal Dataset Information:")
titanic.info()


# --------------------------------------------------
# 1. Handle Empty Cells
# --------------------------------------------------

titanic["Age"] = titanic["Age"].fillna(titanic["Age"].mean())


titanic["Embarked"] = titanic["Embarked"].fillna(
    titanic["Embarked"].mode()[0]
)
titanic["Cabin"] = titanic["Cabin"].fillna("Unknown")


# --------------------------------------------------
# 2. Handle Wrong Format
# --------------------------------------------------

titanic["Age"] = pd.to_numeric(titanic["Age"], errors="coerce")

titanic["Fare"] = pd.to_numeric(titanic["Fare"], errors="coerce")


# --------------------------------------------------
# 3. Handle Wrong Data
# --------------------------------------------------

titanic = titanic[titanic["Age"] >= 0]

titanic = titanic[titanic["Fare"] >= 0]

titanic["Sex"] = titanic["Sex"].str.strip().str.lower()


# --------------------------------------------------
# 4. Remove Duplicate Rows
# --------------------------------------------------

titanic = titanic.drop_duplicates()


# --------------------------------------------------
# Display Cleaned Dataset
# --------------------------------------------------

print("\nCleaned Dataset:")
print(titanic.head())

print("\nMissing Values After Cleaning:")
print(titanic.isnull().sum())

print("\nCleaned Dataset Information:")
titanic.info()