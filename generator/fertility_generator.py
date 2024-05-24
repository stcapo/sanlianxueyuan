# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np

# Define the parameters for generating the dataset
education_levels = ['未受过正式教育', '小学', '初中', '高中', '大专', '本科及以上']

# Initialize a DataFrame to hold the fertility data
fertility_data_columns = ['Year', 'Education Level', 'Average Number of Children']
fertility_data = pd.DataFrame(columns=fertility_data_columns)
years_extended = range(2000, 2024)

# Initialize a DataFrame to hold the extended fertility data
fertility_data_extended = pd.DataFrame(columns=fertility_data_columns)

# Adjust the base number of children for the different time periods
# 2000-2010: Strong fertility desire
# 2011-2014: Transition period
# 2015-2023: Significant decrease in fertility desire
base_children_numbers_2000_2010 = np.linspace(3, 1, num=len(education_levels))  # Higher fertility
base_children_numbers_2015_2023 = np.linspace(2, 0.5, num=len(education_levels))  # Lower fertility

for year in years_extended:
    if year <= 2010:
        base_children_numbers = base_children_numbers_2000_2010
    elif year >= 2015:
        base_children_numbers = base_children_numbers_2015_2023
    else:
        # Transition period, linear interpolation between the two periods
        transition_ratio = (year - 2010) / (2015 - 2010)
        base_children_numbers = base_children_numbers_2000_2010 + (
                    base_children_numbers_2015_2023 - base_children_numbers_2000_2010) * transition_ratio

    for level in education_levels:
        avg_children = np.random.normal(loc=base_children_numbers[education_levels.index(level)], scale=0.1)
        avg_children = round(max(avg_children, 0),
                             2)  # Ensure the average number of children is non-negative and rounded

        fertility_data_extended = fertility_data_extended._append({
            'Year': year,
            'Education Level': level,
            'Average Number of Children': avg_children
        }, ignore_index=True)
with open('../data/fertility.csv', 'w') as f:
    fertility_data_extended.to_csv(f, index=False)
