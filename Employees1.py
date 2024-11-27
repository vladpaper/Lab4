import csv
import random
from faker import Faker
fake = Faker(locale='uk_UA')
print(fake.first_name())

fake = Faker('uk_UA')
num_employees = 2000
employees = []

for _ in range(num_employees):
    gender = 'Male' if random.random() > 0.4 else 'Female'
    first_name = fake.first_name_male() if gender == 'Male' else fake.first_name_female()
    last_name = fake.last_name_male() if gender == 'Male' else fake.last_name_female()
    birth_date = fake.date_of_birth(minimum_age=16, maximum_age=85)
    job_title = fake.job()
    city = fake.city()
    address = fake.address()
    phone = fake.phone_number()
    email = fake.email()

    employees.append([last_name, first_name,  gender, birth_date, job_title, city, address, phone, email])

with open('employees.csv', 'w', newline='', encoding='UTF-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Last_name', 'Name',  'Gender', 'Date_birth', 'Position', 'City', 'Address', 'Phone', 'Email'])
    writer.writerows(employees)