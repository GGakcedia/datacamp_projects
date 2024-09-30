'''Project instruction
    Does increased electric vehicle sales lead to more public or private charging ports?
How many vehicles were sold in 2018 in total? Save the answer as a numeric variable called ev_sales_2018.
Plot trends for private ports, public ports, and sales, saving this as fig, ax objects.
Did vehicle sales and number of private and public ports show the same trend (either increasing or decreasing) between the years 2015 and 2018? Save your answer as same or different to a variable called trend.
!!! The code may not work because the datasets are not loaded. This project was taken from DataCamp for practice.
'''

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
private_ev_charging = pd.read_csv("private_ev_charging.csv")
public_ev_charging = pd.read_csv("public_ev_charging.csv")
ev_sales = pd.read_csv("ev_sales.csv")

# Perform an outer join to keep only the rows with complete information
df_combined = private_ev_charging.merge(public_ev_charging, on='year', how='outer', indicator=True)
df_temp = df_combined[df_combined['_merge'] == 'both']

# Drop the _merge column as it's no longer needed
df_temp = df_temp.drop(columns=['_merge'])

# Get total sales grouping by each year
ev_total_sales = ev_sales.groupby('year')['sales'].sum().reset_index()

# Inspect the data and save the variable
print(ev_total_sales)
ev_sales_2018 = 361315

# Left-join with sales
df_complete = df_temp.merge(ev_total_sales, how='left', on='year')

# Drop any rows with null values
df_complete = df_complete.dropna(subset="sales")

# Create a figure and axis object
fig, ax = plt.subplots()

# Plot each line
sns.lineplot(data=df_complete, x='year', y='private_ports', label='Private Ports')
sns.lineplot(data=df_complete, x='year', y='public_ports', label='Public Ports')
sns.lineplot(data=df_complete, x='year', y='sales', label='Total Sales', linestyle=':')

# Adding titles and labels
ax.set_title('EV Ports and Sales Over Time')
ax.set(xlabel='Year', ylabel='Count')

# Show the legend
ax.legend(loc='upper left')

# Show the plot
plt.show()

# Did vehicle sales and number of private and public ports show the same trend?
trend = "same"