# Start coding here
# Use as many cells as you need
# Question 1
# Import pandas
import pandas as pd
from matplotlib import pyplot as plt

# Load the CSV data into DataFrames
tv = pd.read_csv("datasets/tv.csv")

# Display the TV data to inspect
tv.head()

# Find the year with the highest TV viewership
plt.plot(tv.super_bowl, tv.avg_us_viewers)
plt.title('Average Number of US Viewers')
viewership_increased = True
print(f"Super Bowl viewership increased over time.")

# Question 2

# Load the CSV data into DataFrames
super_bowls = pd.read_csv("datasets/super_bowls.csv")

# Display the Super Bowls data to inspect
super_bowls.head()

# Filter the data for point difference >40
difference = len(super_bowls[super_bowls["difference_pts"]>40])

# You can also plot a histogram of point differences to visualize the result
plt.hist(super_bowls.difference_pts)
plt.xlabel('Point Difference')
plt.ylabel('Number of Super Bowls')
plt.show()

print(f"The matches finishing with a point difference over 40 were: {difference}")

# Question 3
# Load the CSV data into DataFrames
halftime_musicians = pd.read_csv("datasets/halftime_musicians.csv")

# Display the halftime musicians data to inspect
halftime_musicians.head()

# Count halftime show songs for each musician
halftime_appearances = halftime_musicians.groupby('musician').sum('num_songs')
halftime_appearances = halftime_appearances.sort_values('num_songs', ascending=False)

most_songs = "Justin Timberlake"