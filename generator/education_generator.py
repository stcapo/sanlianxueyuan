# -*- coding: UTF-8 -*-

# Re-import necessary libraries after reset and re-define variables
import pandas as pd
import numpy as np

# Re-define the bachelor degree percentages and regions
bachelor_degrees_percentages = [
    21.79, 17.21, 14.06, 8.53, 8.42, 8.08, 8.03, 7.85, 7.81, 7.67,
    7.36, 6.89, 6.72, 6.63, 6.61, 6.54, 6.41, 6.41, 6.31, 6.20,
    5.99, 5.61, 5.49, 5.47, 5.17, 5.13, 4.97, 4.80, 4.73, 4.53, 4.46
]

regions = [
    '上海市', '北京市', '广东省', '天津市', '江苏省', '浙江省', '福建省', '山东省', '辽宁省', '重庆市',
    '四川省', '湖北省', '湖南省', '河北省', '河南省', '黑龙江省', '内蒙古自治区', '山西省', '安徽省', '江西省',
    '广西壮族自治区', '陕西省', '云南省', '贵州省', '甘肃省', '青海省', '西藏自治区', '宁夏回族自治区',
    '新疆维吾尔自治区', '海南省', '台湾省'
]

# Map the bachelor's degree percentages to the regions
bachelor_degree_mapping = dict(zip(regions, bachelor_degrees_percentages))

# Initialize the DataFrame from the provided code snippet, then modify it
degree_distribution_data = pd.DataFrame.from_dict(bachelor_degree_mapping, orient='index',
                                                           columns=['bachelor']).reset_index()
degree_distribution_data.rename(columns={'index': 'region'}, inplace=True)

# Generate random percentages for additional education levels for each region and ensure the total is 100%
np.random.seed(42)  # For reproducibility
additional_education_levels = ['uneducated', 'primary', 'middle', 'high', 'professional']

for index, row in degree_distribution_data.iterrows():
    remaining_percentage = 100 - row['bachelor']
    other_percentages = np.random.dirichlet(np.ones(len(additional_education_levels))).flatten() * remaining_percentage
    other_percentages = np.round(other_percentages, 2)  # Round to two decimal places

    for i, level in enumerate(additional_education_levels):
        degree_distribution_data.at[index, level] = other_percentages[i]

# Remove the 'Total Percentage' column
if 'Total Percentage' in degree_distribution_data.columns:
    degree_distribution_data.drop('Total Percentage', axis=1, inplace=True)


with open('../data/degree_distribution_data.csv', 'w') as f:
    degree_distribution_data.to_csv(f, index=False)
