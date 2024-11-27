import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('employees.csv')

gender_counts = df['Gender'].value_counts()
print("Кількість співробітників за статтю:")
print(gender_counts)

gender_counts.plot(kind='bar', title='Кількість співробітників за статтю')
plt.show()

df['Age'] = df['Date_birth'].apply(lambda x: 2024 - int(x.split('-')[0]))

age_bins = [0, 18, 45, 70, 150]
age_labels = ['younger_18', '18-45', '45-70', 'older_70']
df['Age_category'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels)

age_group_counts = df['Age_category'].value_counts()
print("Кількість співробітників за віковими категоріями:")
print(age_group_counts)

age_group_counts.plot(kind='bar', title='Кількість співробітників за віковими категоріями')
plt.show()

gender_age_group_counts = df.groupby(['Age_category', 'Gender']).size().unstack(fill_value=0)
print("Кількість співробітників за статтю та віковими категоріями:")
print(gender_age_group_counts)

gender_age_group_counts.plot(kind='bar', stacked=True, title='Кількість співробітників за статтю та віковими категоріями')
plt.show()
