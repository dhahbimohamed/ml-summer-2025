import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Create sample dataset with missing values
data = {
    'Age': [25, 30, 35, None, 40],
    'Salary': [50000, 60000, 80000, 90000, None],
    'Target': [0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

# Fill missing values with column mean
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

# Separate features and labels
X = df[['Age', 'Salary']]
y = df['Target']

# Split into training and test sets (80% / 20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features (mean=0, std=1)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Print results
print("Cleaned Data:\n", df)
print("\nScaled X_train:\n", X_train_scaled)
print("\nScaled X_test:\n", X_test_scaled)