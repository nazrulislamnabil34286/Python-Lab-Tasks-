import pandas as pd
import matplotlib.pyplot as plt


titanic = pd.read_csv("titanic.csv")


print("Titanic Dataset:")
print(titanic.head())



plt.plot(
    titanic["PassengerId"].head(20),
    titanic["Fare"].head(20)
)

plt.title("Passenger Fare")
plt.xlabel("Passenger ID")
plt.ylabel("Fare")
plt.show()



plt.scatter(
    titanic["Age"],
    titanic["Fare"]
)

plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()



survived = titanic["Survived"].value_counts()

plt.bar(
    ["Did Not Survive", "Survived"],
    survived
)

plt.title("Passenger Survival")
plt.xlabel("Survival Status")
plt.ylabel("Number of Passengers")
plt.show()



plt.hist(
    titanic["Age"].dropna(),
    bins=10
)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()



passenger_class = titanic["Pclass"].value_counts().sort_index()

plt.pie(
    passenger_class,
    labels=["Class 1", "Class 2", "Class 3"],
    autopct="%1.1f%%"
)

plt.title("Passenger Distribution by Class")
plt.show()



fig, ax = plt.subplots(1, 2)

ax[0].hist(
    titanic["Age"].dropna(),
    bins=10
)

ax[0].set_title("Age Distribution")
ax[0].set_xlabel("Age")
ax[0].set_ylabel("Frequency")


ax[1].bar(
    ["Class 1", "Class 2", "Class 3"],
    passenger_class
)

ax[1].set_title("Passengers by Class")
ax[1].set_xlabel("Passenger Class")
ax[1].set_ylabel("Number of Passengers")

plt.tight_layout()
plt.show()