# Python Practical File — Krish Behura
# Roll Number: 2501420072
# B.Tech — CSE (Data Science)
# Subject: Python Programming / Data Analysis Practical

import pandas as pd
import matplotlib.pyplot as plt

import pandas as pd

data = {
    "Student": ["Aarav", "Diya", "Kabir", "Anaya", "Vivaan",
                "Ishita", "Arjun", "Meera", "Reyansh", "Sara",
                "Aditya", "Myra", "Rohan", "Kiara", "Dev"],
    "Marks": [78, 92, 67, 85, 74, 89, 56, 95, 81, 72, 88, 63, 79, 91, 69],
    "Attendance": [88, 96, 75, 91, 82, 94, 68, 98, 87, 79, 93, 72, 85, 97, 77],
    "Study_Hours": [3, 5, 2, 4, 3, 5, 1, 6, 4, 2, 5, 2, 3, 6, 2]
}

df = pd.DataFrame(data)
print(df)

plt.hist(df['Marks'], bins=5, edgecolor='black')
plt.title('Distribution of Marks')
plt.xlabel('Marks')
plt.ylabel('Number of Students')
plt.tight_layout()
plt.show()
