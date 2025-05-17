import pandas as pd

# Load the dataset
data = pd.read_csv('data/cybersecurity_intrusion_data.csv')  # replace with your file name
#data.head()  # Show the first 5 rows to inspect the data
# Check for missing values
missing_values = data.isnull().sum()
print("Missing values per column:\n", missing_values)

# Summary statistics
summary_stats = data.describe(include='all')
print("\nSummary statistics:\n", summary_stats)

# Distribution of attack_detected
attack_distribution = data['attack_detected'].value_counts()
print("\nAttack detected distribution:\n", attack_distribution)

# Visualize the attack distribution
import matplotlib.pyplot as plt

attack_distribution.plot(kind='bar', color=['green', 'red'])
plt.title('Attack Detected Distribution')
plt.xlabel('Attack Detected (0 = No, 1 = Yes)')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(8, 5))
data['login_attempts'].hist(bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Login Attempts')
plt.xlabel('Number of Login Attempts')
plt.ylabel('Frequency')
plt.show()

# Boxplot to see login_attempts by attack_detected
plt.figure(figsize=(8, 5))
data.boxplot(column='login_attempts', by='attack_detected', grid=False)
plt.title('Login Attempts by Attack Detected')
plt.suptitle('')
plt.xlabel('Attack Detected (0 = No, 1 = Yes)')
plt.ylabel('Number of Login Attempts')
plt.show()

# Distribution of protocol_type
protocol_counts = data['protocol_type'].value_counts()
protocol_counts.plot(kind='bar', color='cornflowerblue')
plt.title('Session Count by Protocol Type')
plt.xlabel('Protocol Type')
plt.ylabel('Number of Sessions')
plt.show()

# Attack rate by protocol_type
attack_by_protocol = data.groupby('protocol_type')['attack_detected'].mean()
attack_by_protocol.plot(kind='bar', color='salmon')
plt.title('Attack Rate by Protocol Type')
plt.xlabel('Protocol Type')
plt.ylabel('Attack Rate')
plt.ylim(0, 1)
plt.show()

# Boxplot: login_attempts by protocol_type
plt.figure(figsize=(8, 5))
data.boxplot(column='login_attempts', by='protocol_type', grid=False)
plt.title('Login Attempts by Protocol Type')
plt.suptitle('')
plt.xlabel('Protocol Type')
plt.ylabel('Number of Login Attempts')
plt.show()
