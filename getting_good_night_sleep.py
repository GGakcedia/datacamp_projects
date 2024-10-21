import pandas as pd
# Read in the data 
sleep_df = pd.read_csv('sleep_health_data.csv')

# 1. Which occupation has the lowest average sleep duration? Save this in a string variable called `lowest_sleep_occ`.

# Groupby occupation and calculate mean sleep duration 
sleep_duration = sleep_df.groupby('Occupation')['Sleep Duration'].mean()
# Get occupation with lowest average sleep duration
lowest_sleep_occ = sleep_duration.sort_values().index[0]

# 2. Which occupation had the lowest quality of on average? Did the occupation with the lowest sleep duration also have the worst sleep quality?

# Groupby occupation and calculate average sleep quality
sleep_quality = sleep_df.groupby('Occupation')['Quality of Sleep'].mean()  
# Get occupation with lowest average sleep quality 
lowest_sleep_quality_occ = sleep_quality.sort_values().index[0]

# Compare occupation with the least sleep to occupation with the lowest sleep quality
if lowest_sleep_occ == lowest_sleep_quality_occ:
  same_occ = True
else:
  same_occ = False
  
# 3. Let's explore how BMI Category can affect sleep disorder rates. Start by finding what ratio of app users in each BMI category have been diagnosed with Insomnia.

# Normal
# Filter the full dataframe to only rows where BMI Category is Normal and Sleep Disorder is Insomnia.
normal = sleep_df[(sleep_df["BMI Category"] == "Normal") &  
                  (sleep_df["Sleep Disorder"] == "Insomnia")]
normal2 = sleep_df[(sleep_df["BMI Category"] == "Normal Weight") &  
                  (sleep_df["Sleep Disorder"] == "Insomnia")]
# Total normal rows               
total_normal = len(sleep_df[sleep_df["BMI Category"] == "Normal"])  
# Calculate normal insomnia ratio               
normal_insomnia_ratio = round(len(normal) / total_normal, 2) 


# Overweight
# Filter the full dataframe to only rows where BMI Category is Overweight and Sleep Disorder is Insomnia.
overweight = sleep_df[(sleep_df["BMI Category"] == "Overweight") &   
                      (sleep_df["Sleep Disorder"] == "Insomnia")]  
# Total overweight rows
total_overweight = len(sleep_df[sleep_df["BMI Category"] == "Overweight"])  
# Calculate overweight insomnia ratio 
overweight_insomnia_ratio = round(len(overweight) / total_overweight, 2)


# Obese
# Filter the full dataframe to only rows where BMI Category is Obese and Sleep Disorder is Insomnia.
obese = sleep_df[(sleep_df["BMI Category"] == "Obese") &  
                  (sleep_df["Sleep Disorder"] == "Insomnia")]
# Total obese rows          
total_obese = len(sleep_df[sleep_df["BMI Category"] == "Obese"])  
# Calculate obese insomnia ratio
obese_insomnia_ratio = round(len(obese) / total_obese, 2)


# Create dictionary to store the ratios for each BMI category 
bmi_insomnia_ratios = {
    "Normal": normal_insomnia_ratio,  
    "Overweight": overweight_insomnia_ratio,
    "Obese": obese_insomnia_ratio 
}