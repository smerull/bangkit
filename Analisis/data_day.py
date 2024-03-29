# -*- coding: utf-8 -*-
"""data_day.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aR6r-tYoMXJRS2QUqDVRD0zKBSJ4PJb9

# Proyek Analisis Data: [Input Nama Dataset]
- **Nama:** Deriansyah
- **Email:** M381D4KY1608@bangkit.academy
- **ID Dicoding:** M381D4KY1608

## Menentukan Pertanyaan Bisnis

- Apakah terdapat Perbedaan Penggunaan Sepeda antara Hari Kerja dan Hari Libur?
- Apakah terdapat perbedaan yang signifikan orang yang menyewa pada setiap musim?

## Import Semua Packages/Library yang Digunakan

## import library dari numpy hingga seaborn
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""## Data Wrangling

### Gathering Data

### membaca day.csv dan menampilkan tablenya
"""

day_df = pd.read_csv("day.csv")
day_df.head()

"""### membaca hour.csv dan menampilkan tablenya"""

hour_df = pd.read_csv("day.csv")
hour_df.head()

"""### Assessing Data

#### assesing day
"""

day_df.info()

day_df.isna().sum()

print("Jumlah duplikasi: ", day_df.duplicated().sum())

day_df.describe()

plt.figure(figsize=(12, 8))
plt.boxplot(day_df['windspeed'])
plt.title('Boxplot of Several Variables')
plt.xlabel('None')
plt.ylabel('None')
plt.xticks(rotation=45)  # Rotasi label sumbu x
plt.grid(True)  # Tambahkan grid
plt.tight_layout()  # Atur layout agar rapi
plt.show()

"""Terdapat Outlier dalam coloumn windspeed"""

plt.figure(figsize=(12, 8))
plt.boxplot(day_df['hum'])
plt.title('Boxplot of Several Variables')
plt.xlabel('None')
plt.ylabel('None')
plt.xticks(rotation=45)  # Rotasi label sumbu x
plt.grid(True)  # Tambahkan grid
plt.tight_layout()  # Atur layout agar rapi
plt.show()

"""Terdapat Outlier pada coloumn hum"""

plt.figure(figsize=(12, 8))
plt.boxplot(day_df['cnt'])
plt.title('Boxplot of Several Variables')
plt.xlabel('None')
plt.ylabel('None')
plt.xticks(rotation=45)  # Rotasi label sumbu x
plt.grid(True)  # Tambahkan grid
plt.tight_layout()  # Atur layout agar rapi
plt.show()

"""Terdapat Outlier dalam Coloumn cnt

#### Assesing hour
"""

hour_df.info()

hour_df.isna().sum()

print("Jumlah duplikasi: ", hour_df.duplicated().sum())

"""### Cleaning Data

#### cleaning data day
"""

day_df.drop_duplicates(inplace=True)
print("Jumlah duplikasi: ", day_df.duplicated().sum())

"""Membersihkan data yang duplikasi"""

datetime_columns = ["dteday",]

for column in datetime_columns:
  day_df[column] = pd.to_datetime(day_df[column])

day_df.info()

"""membersihkan data type yang keliru"""

day_df.dropna(inplace=True)

day_df.fillna(value=day_df.mean(), inplace=True)

day_df = pd.read_csv('day.csv')

hour_df = pd.read_csv('hour.csv')

day_df.interpolate(method='linear', limit_direction='forward', inplace=True)

day_df.head()

day_df.rename(columns={'dteday' : 'date', 'yr' : 'year', 'mnth' : 'month', 'cnt' : 'count'}, inplace=True)
day_df.head()

"""## Exploratory Data Analysis (EDA)

### Explore ...
"""

day_df.describe(include="all")

day_df.groupby(by=["workingday", "weekday"]).agg({
    "casual": "sum",
    "registered": "sum",
    "count": "sum",
})

day_df.groupby(by=["season", "date"]).agg({
    "casual": "sum",
    "registered": "sum",
    "count": "sum",
})

"""## Visualization & Explanatory Analysis

### Pertanyaan 1:
"""

day_df.groupby(by=["workingday", "weekday"]).agg({
    "casual": "sum",
    "registered": "sum",
    "count": "sum",
})

grouped_data = day_df.groupby("weekday")["count"].sum().reset_index()

plt.figure(figsize=(10, 6))
plt.bar(grouped_data["weekday"], grouped_data["count"], color='skyblue')
plt.xlabel('Weekday')
plt.ylabel('Total Count')
plt.title('Total Count by Weekday')
plt.xticks(rotation=45)
plt.show()

grouped_data = day_df.groupby("workingday")["count"].sum().reset_index()

plt.figure(figsize=(2, 6))
plt.bar(grouped_data["workingday"], grouped_data["count"], color='skyblue')
plt.xlabel('Workingday')
plt.ylabel('Total Count')
plt.title('Total Count by workingday')
plt.xticks(rotation=45)
plt.show()

grouped_data = day_df.groupby("weekday")["casual"].sum().reset_index()

grouped_data = day_df.groupby("weekday")[["casual", "registered"]].sum().reset_index()

# Plot the stacked bar chart
plt.figure(figsize=(10, 6))
plt.bar(grouped_data["weekday"], grouped_data["casual"], color='skyblue', label='Casual')
plt.bar(grouped_data["weekday"], grouped_data["registered"], color='orange', bottom=grouped_data["casual"], label='Registered')
plt.xlabel('Weekday')
plt.ylabel('Total Count')
plt.title('Total Count by Weekday (Stacked)')
plt.xticks(rotation=45)
plt.legend()
plt.show()

"""### Pertanyaan 2:"""

day_df.head()

plt.figure(figsize=(10, 4))
plt.bar(day_df["season"], day_df["count"], color="#72BCD4")
plt.title("Number of Orders per Season", fontsize=20)
plt.xlabel("Season", fontsize=14)
plt.ylabel("Number of Orders", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

"""## Conclusion

- Conclution pertanyaan 1

  Untuk pertanyaan pertama mengenai Total rental pada weekday dan holiday. untuk jumlah orang yang rental rata rata menunjukan jumlah yang sama pada tiap harinya kecuali untuk hari minggu dan senin datau index 0 dan 1 terdapat jumlah yang relatif lebih rendah dari yang lain.

- Conclution pertanyaan 2

 mengenai jumlah rental tiap musim nuntuk Conclution pertanyaan kedua telihat yang paling banyak jumlah orang yang menyewa terdapat pada musim ke tiga atau saat Light Snow,
Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds dibandingkan yang lain.
"""