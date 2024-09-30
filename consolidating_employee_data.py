'''
Project instruction
Read in, merge, and clean the four datasets to make a single combined pandas DataFrame.
Create a single pandas DataFrame called employees_final containing:
Index: employee_id.
Columns: Ensure the DataFrame contains only the following columns, in the exact order listed: employee_first_name, employee_last_name, employee_country, employee_city, employee_street, employee_street_number, emergency_contact, emergency_contact_number, relationship, monthly_salary, team, title, office, office_country, office_city, office_street, office_street_number.
Assign employees to offices based on their country. For any columns that begin with office, replace missing data with "Remote".
!!! The code may not work because the datasets are not loaded. This project was taken from DataCamp for practice.
'''
# Import pandas
import pandas as pd

# Read in office_addresses.csv
offices = pd.read_csv("datasets/office_addresses.csv")

# Read in employee_information.xlsx
addresses = pd.read_excel("datasets/employee_information.xlsx")

# Declare a list of new column names
emergency_contacts_header = ["employee_id", "last_name", "first_name",
                             "emergency_contact", "emergency_contact_number", "relationship"]

# Read in employee_information.xlsx
emergency_contacts = pd.read_excel("datasets/employee_information.xlsx", 
                                   sheet_name="emergency_contacts", 
                                   header=None,
                                   names=emergency_contacts_header)

# Read in employee_roles.json
roles = pd.read_json("datasets/employee_roles.json", orient="index")

# Merge addresses with offices
employees = addresses.merge(offices, left_on="employee_country", right_on="office_country", how="left")

# Merge employees with roles
employees = employees.merge(roles, left_on="employee_id", right_on=roles.index)

# Merge employees with emergency_contacts
employees = employees.merge(emergency_contacts, on="employee_id")

# Fill null values in office columns
for col in ["office", "office_country", "office_city", "office_street", "office_street_number"]:
    employees[col].fillna("Remote", inplace=True)
    
# Create final columns
final_columns = ["employee_id", "employee_first_name", "employee_last_name", "employee_country", 
                 "employee_city", "employee_street", "employee_street_number", 
                 "emergency_contact", "emergency_contact_number", "relationship", 
                 "monthly_salary", "team", "title", "office", "office_country", 
                 "office_city", "office_street", "office_street_number"]

# Subset for the required columns
employees_final = employees[final_columns]

# Set employee_id as the index
employees_final.set_index("employee_id", inplace=True)