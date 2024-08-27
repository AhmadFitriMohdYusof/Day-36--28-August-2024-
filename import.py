import pandas as pd


# 1. Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)

# 2. Display the DataFrame
print("DataFrame:")
print(df)

# 3. Display the first few rows
print("\nFirst few rows:")
print(df.head())

# 4. Filter rows where Age is greater than 25
print("\nPeople older than 25:")
print(df[df['Age'] > 25])

# 5. Add a new column 'Senior' indicating if Age > 30
df['Senior'] = df['Age'] > 30
print("\nDataFrame with new 'Senior' column:")
print(df)

# 6. Save DataFrame to a CSV file
df.to_csv('people.csv', index=False)
print("\nDataFrame saved to 'people.csv'")
