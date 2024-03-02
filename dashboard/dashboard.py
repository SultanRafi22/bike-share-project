import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set_theme(style='dark')
st.title("Bike Sharing Analysis :bike: :sparkles: ")

# day_df = pd.read_csv('../dashboard/main_data/day_bike_data.csv')
day_df = pd.read_csv('https://raw.githubusercontent.com/SultanRafi22/bike-share-project/main/dashboard/main_data/day_bike_data.csv')
# hour_df = pd.read_csv('../dashboard/main_data/hour_bike_data.csv')
hour_df = pd.read_csv('https://raw.githubusercontent.com/SultanRafi22/bike-share-project/main/dashboard/main_data/hour_bike_data.csv')

st.sidebar.title("Bike Sharing Analysis :bike:")
with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    st.sidebar.write("Selamat Datang di Projek Akhir Analisis Data dengan Python")

st.subheader('Menampilkan tren rata-rata peminjaman pada minggu pertama bulan Januari 2011')
def show_rentals_visualization(day_df, start_date, end_date):
    
    # Memilih data sesuai rentang tanggal
    selected_data = day_df[(day_df['date'] >= start_date) & (day_df['date'] <= end_date)]

    # Menghitung rata-rata peminjaman sepeda
    average_rentals = selected_data['total'].mean()

    # Membuat visualisasi menggunakan Matplotlib
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(selected_data['date'], selected_data['total'], label='Total Peminjaman')
    ax.set_title(f'Peminjaman Sepeda - {start_date} to {end_date}')
    ax.set_xlabel('Tanggal')
    ax.set_ylabel('Jumlah Peminjaman')
    ax.set_ylim(0)
    ax.legend()

    # Menampilkan plot di Streamlit
    st.pyplot(fig)

    # Menampilkan rata-rata peminjaman sepeda
    st.write(f"Rata-rata peminjaman sepeda pada rentang tanggal {start_date} sampai {end_date}: {average_rentals:.2f} peminjaman\n\n")

def show_hourly_rentals_visualization(hour_bike_data, date_1, date_2):
    st.subheader('\nMenampilkan perbandingan antara peminjaman sepeda pada tanggal 1 Januari 2011 dengan 1 Januari 2012\n\n')
    # Menseleksi data untuk tanggal pertama
    data_1 = hour_bike_data[hour_bike_data['date'] == date_1]

    # Menseleksi data untuk tanggal kedua
    data_2 = hour_bike_data[hour_bike_data['date'] == date_2]

    # Membuat visualisasi untuk tanggal pertama
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    axes[0].bar(data_1['hour'], data_1['total'])
    axes[0].set_title(f'Peminjaman Sepeda - {date_1}')
    axes[0].set_xlabel('Jam')
    axes[0].set_ylabel('Jumlah Peminjaman')

    # Membuat visualisasi untuk tanggal kedua
    axes[1].bar(data_2['hour'], data_2['total'])
    axes[1].set_title(f'Peminjaman Sepeda - {date_2}')
    axes[1].set_xlabel('Jam')
    axes[1].set_ylabel('Jumlah Peminjaman')

    # Menyesuaikan tata letak
    plt.tight_layout()

    # Menampilkan plot di Streamlit
    st.pyplot(fig)


def show_wind_speed_vs_total_scatter(day_bike_data, start_date, end_date):
    st.subheader('\nMenampilkan pengaruh antara kecepatan angin dengan jumlah peminjaman sepeda\n\n')
    # Menseleksi data sesuai rentang tanggal
    selected_data = day_bike_data[(day_bike_data['date'] >= start_date) & (day_bike_data['date'] <= end_date)]

    # Membuat scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    scatter = ax.scatter(selected_data['wind_speed'], selected_data['total'], c=selected_data['total'], cmap='viridis', alpha=0.5, label='Data Peminjaman Sepeda')
    ax.set_title(f'Pengaruh Kecepatan Angin Terhadap Total Peminjaman Sepeda ({start_date} - {end_date})')
    ax.set_xlabel('Wind Speed')
    ax.set_ylabel('Total Peminjaman')

    # Menambahkan colorbar untuk menunjukkan 'total'
    cbar = plt.colorbar(scatter)
    cbar.set_label('Total Peminjaman')

    # Menampilkan plot di Streamlit
    st.pyplot(fig)

# Memanggil fungsi untuk menampilkan visualisasi
show_rentals_visualization(day_df, '2011-01-01', '2011-01-07')
show_hourly_rentals_visualization(hour_df, '2011-01-01', '2012-01-01')
show_wind_speed_vs_total_scatter(day_df, '2012-01-01', '2012-12-31')
    
st.caption("Copyright (c) Sultan Rafi 2024")
