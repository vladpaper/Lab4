import pandas as pd
from datetime import datetime

try:
    df = pd.read_csv('employees.csv')
except FileNotFoundError:
    print("Повідомлення про відсутність, або проблеми при відкритті файлу CSV.")
    exit()

current_year = datetime.now().year
df['Age'] = df['Date_birth'].apply(lambda x: current_year - int(x.split('-')[0]))

with pd.ExcelWriter('employees.xlsx', engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='all', index=False)
    df[df['Age'] < 18].to_excel(writer, sheet_name='younger_18', index=False)
    df[(df['Age'] >= 18) & (df['Age'] <= 45)].to_excel(writer, sheet_name='18-45', index=False)
    df[(df['Age'] > 45) & (df['Age'] <= 70)].to_excel(writer, sheet_name='45-70', index=False)
    df[df['Age'] > 70].to_excel(writer, sheet_name='older_70', index=False)

print("Ok, якщо програма завершила свою роботу успішно.")