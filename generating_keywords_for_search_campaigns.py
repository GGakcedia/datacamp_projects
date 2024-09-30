'''Project Instructions
What keywords would help the client sell the listed products through search campaigns?
Save at least 60 unique keywords as a DataFrame called keywords_df and a CSV file called keywords.csv.
Both of these should contain four columns:
Ad Group: containing the product names
Keyword: containing the product and keyword combinations, combined in both directions (word + product, and product + word)
Campaign: with the value SEM_Sofas in every row
Criterion Type: with the value Exact in every row.
!!! The code may not work because the datasets are not loaded. This project was taken from DataCamp for practice.
'''
import pandas as pd

# Define product names and keywords
products = ['Sofa', 'Couch', 'Recliner', 'Loveseat', 'Sectional']
keywords = ['comfortable', 'cheap', 'leather', 'fabric', 'modern', 'small', 'big', 'luxury']

# Generate unique keyword combinations
data = []
for product in products:
    for keyword in keywords:
        # Create both combinations: product + keyword and keyword + product
        data.append({'Ad Group': product, 'Keyword': f'{product} {keyword}', 'Campaign': 'SEM_Sofas', 'Criterion Type': 'Exact'})
        data.append({'Ad Group': product, 'Keyword': f'{keyword} {product}', 'Campaign': 'SEM_Sofas', 'Criterion Type': 'Exact'})

# Ensure we have at least 60 unique entries
keywords_df = pd.DataFrame(data).drop_duplicates().reset_index(drop=True)
keywords_df = keywords_df.head(60)  # Ensure only the top 60 are taken if more than 60 are generated

# Save the DataFrame to a CSV file
keywords_df.to_csv('keywords.csv', index=False)

# Display the DataFrame
print(keywords_df)
