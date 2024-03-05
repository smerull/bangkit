import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')


# Membaca data dari file CSV
all_df = pd.read_csv("all_data.csv")

# Mengonversi kolom 'date' ke dalam tipe data datetime64[ns]
all_df['date'] = pd.to_datetime(all_df['date'])

# Sidebar
st.sidebar.image("logo.png")

# Mengambil nilai min_date dan max_date
min_date = all_df['date'].min()
max_date = all_df['date'].max()

# Filter by date
st.sidebar.subheader('Filter by Date')
start_date = st.sidebar.date_input('Start Date', min_value=min_date, max_value=max_date, value=min_date)
end_date = st.sidebar.date_input('End Date', min_value=min_date, max_value=max_date, value=max_date)

# Filter data berdasarkan rentang tanggal yang dipilih
filtered_df = all_df[(all_df['date'] >= pd.Timestamp(start_date)) & (all_df['date'] <= pd.Timestamp(end_date))]

# Menampilkan data yang telah difilter
st.write('### Filtered Data')
st.write(filtered_df)


# Menghitung rata-rata jumlah penyewaan sepeda per hari untuk hari kerja dan hari libur
weekday_data = filtered_df[filtered_df['holiday'] == 0]
holiday_data = filtered_df[filtered_df['holiday'] == 1]

avg_count_weekday = weekday_data.groupby(weekday_data['date'].dt.day)['count'].mean()
avg_count_holiday = holiday_data.groupby(holiday_data['date'].dt.day)['count'].mean()

# Visualisasi perbedaan penggunaan sepeda antara hari kerja dan hari libur
plt.figure(figsize=(10, 6))
plt.plot(avg_count_weekday.index, avg_count_weekday.values, label='Weekday', marker='o')
plt.plot(avg_count_holiday.index, avg_count_holiday.values, label='Holiday', marker='o')
plt.xlabel('Day of Month')
plt.ylabel('Average Count')
plt.title('Average Bike Rentals: Weekday vs Holiday')
plt.legend()
plt.grid(True)

# Menampilkan plot menggunakan Streamlit
st.pyplot()

average_orders_per_season = all_df.groupby("season")["count"].mean()

# Visualisasi rata-rata jumlah pesanan per musim
plt.figure(figsize=(8, 5))
average_orders_per_season.plot(kind='bar', color='skyblue')
plt.xlabel('Season')
plt.ylabel('Average Number of Orders')
plt.title('Average Number of Orders per Season')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Menampilkan plot menggunakan Streamlit
st.pyplot()