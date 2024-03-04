import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title('Proyek Analisis Data: Bike Sharing Dataset')
st.markdown('- Nama: Mario Martua Aditia')
st.markdown('- Email: mariomartuaa@gmail.com')
st.markdown('- ID Dicoding: mariomartuaa')

st.markdown('Pertanyaan Bisnis:')
st.markdown('- Pada hari dan pukul berapakah sepeda paling banyak dipinjamkan?')
st.markdown('- Apakah kondisi cuaca memengaruhi jumlah peminjaman sepeda dalam rentang waktu?')


df_hour = pd.read_csv('hour.csv')
df_hour['dteday'] = pd.to_datetime(df_hour['dteday'])



tab1, tab2 = st.tabs(["Counting Hourly", " Counting Time Span"])

with tab1:
        
        min_date = df_hour['dteday'].min()
        max_date = df_hour['dteday'].max()

        date = st.date_input(
                label = 'Pilih Tanggal', 
                min_value=min_date,
                max_value=max_date,
                value= min_date)
        
        df = df_hour[df_hour['dteday'] == str(date)]
        
        st.subheader('Total of Bike Sharing Hourly')
        
        morning_data = df[df['hr'] <= 10]
        ttl_morning = morning_data['casual'].sum()
        ttl_morning2 = morning_data['registered'].sum()
        afternoon_data = df[(df['hr'] >= 11) & (df['hr'] <= 14)]
        ttl_afternoon = afternoon_data['casual'].sum()
        ttl_afternoon2 = afternoon_data['registered'].sum()
        evening_data = df[(df['hr'] >= 15) & (df['hr'] <= 17)]
        ttl_evening = evening_data['casual'].sum()
        ttl_evening2 = evening_data['registered'].sum()
        night_data = df[df['hr'] >= 18]
        ttl_night = night_data['casual'].sum()
        ttl_night2 = night_data['registered'].sum()

        total = [ttl_morning, ttl_afternoon, ttl_evening, ttl_night]
        total2 = [ttl_morning2, ttl_afternoon2, ttl_evening2, ttl_night2]
        
        time = ['Morning','Afternoon','Evening','Night']
        
        fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15,6))
        jam1 = ax[0].bar(x= time, height= total)
        jam2 = ax[1].bar(x= time, height= total2, color='orange')
        ax[0].set_title('Casual')
        ax[1].set_title('Registered')
        st.pyplot(fig)
        
        colors = ('#8B4513', '#FFF8DC', '#93C572', '#E67F0D')
        
        total = (ttl_morning, ttl_afternoon, ttl_evening, ttl_night)
        total2 = (ttl_morning2, ttl_afternoon2, ttl_evening2, ttl_night2)
        
        fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15,6))
        ax[0].pie(x=total, labels=time, autopct='%1.1f%%',colors=colors)
        ax[1].pie(x=total2, labels=time, autopct='%1.1f%%',colors=colors)
        ax[0].set_title('Casual')
        ax[1].set_title('Registered')
        st.pyplot(fig)
        
        st.markdown("Chart tersebut merepresentasikan nilai total peminjaman sepeda berdasarkan waktu:")
        st.markdown("- Pagi : pukul 00:00 - 10:59 WIB")
        st.markdown("- Siang : pukul 11:00 - 14:59 WIB")
        st.markdown("- Sore : pukul 15:00 - 17:59 WIB")
        st.markdown("- Malam : pukul 18:00 - 23:59 WIB")
        
        st.subheader('Total of Bike Sharing Hourly by Weather')
        
        sunny_data = df[df['weathersit'] == 1]
        ttl_sunny = sunny_data['casual'].sum()
        ttl_sunny2 = sunny_data['registered'].sum()
        cd_data = df[df['weathersit'] == 2]
        ttl_cd = cd_data['casual'].sum()
        ttl_cd2 = cd_data['registered'].sum()
        lr_data = df[df['weathersit'] == 3]
        ttl_lr = lr_data['casual'].sum()
        ttl_lr2 = lr_data['registered'].sum()
        hr_data = df[df['weathersit'] == 4]
        ttl_hr = hr_data['casual'].sum()
        ttl_hr2 = hr_data['registered'].sum()

        total = [ttl_sunny, ttl_cd, ttl_lr]
        total2 = [ttl_sunny2, ttl_cd2, ttl_lr2]
        
        weathers = ['Sunny', 'Cloudy/Misty', 'Rain']
        
        fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15,6))
        ax[0].bar(x= weathers, height= total)
        ax[1].bar(x= weathers, height= total2, color='orange')
        ax[0].set_title('Casual')
        ax[1].set_title('Registered')
        st.pyplot(fig)
        
        colors = ('#8B4513', '#FFF8DC', '#93C572', '#E67F0D')
        
        total = (ttl_sunny, ttl_cd, ttl_lr)
        total2 = (ttl_sunny2, ttl_cd2, ttl_lr2)
        
        fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15,6))
        ax[0].pie(x=total, labels=weathers, autopct='%1.1f%%',colors=colors)
        ax[1].pie(x=total2, labels=weathers, autopct='%1.1f%%',colors=colors)
        ax[0].set_title('Casual')
        ax[1].set_title('Registered')
        st.pyplot(fig)
        
        

with tab2:
        df_day = pd.read_csv('new_data.csv')
        df_day['date'] = pd.to_datetime(df_day['date'])
        
        min_date = df_day['date'].min()
        max_date = df_day['date'].max() 
        
        start_date, end_date = st.date_input(
                label='Rentang Waktu', min_value=min_date,
                max_value=max_date,
                value=[min_date, max_date])

        df = df_day[(df_day['date'] >= str(start_date)) & (df_day['date'] <= str(end_date))]
        df1 = df_hour[(df_hour['dteday'] >= str(date)) & (df_hour['dteday'] <= str(end_date))]
        
        st.subheader('Total of Bike Sharing')
        
        monday_data = df[df['day'] == "Monday"]
        ttl_monday = monday_data['total'].sum()
        tuesday_data = df[df['day'] == "Tuesday"]
        ttl_tuesday = tuesday_data['total'].sum()
        wednesday_data = df[df['day'] == 'Wednesday']
        ttl_wednesday = wednesday_data['total'].sum()
        thursday_data = df[df['day'] == 'Thursday']
        ttl_thursday = thursday_data['total'].sum()
        friday_data = df[df['day'] == 'Friday']
        ttl_friday = friday_data['total'].sum()
        saturday_data = df[df['day'] == 'Saturday']
        ttl_saturday = saturday_data['total'].sum()
        sunday_data = df[df['day'] == 'Sunday']
        ttl_sunday = sunday_data['total'].sum()
        
        total_day = [ttl_monday, ttl_tuesday, ttl_wednesday, ttl_thursday, ttl_friday, ttl_saturday, ttl_sunday]
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        
        
        fig, ax = plt.subplots(figsize=(15,6))
        barplot =  ax.bar(x= days, height= total_day)
        ax.bar_label(barplot, labels= total_day)
        st.pyplot(fig)
        
        colors = ('#8B4513', '#FFF8DC', '#93C572', '#E67F0D')
        
        fig, ax = plt.subplots(figsize=(15,6))
        ax.pie(
                x = total_day,
                labels = days,
                autopct='%1.1f%%',
                colors = colors
        )
        st.pyplot(fig)
        
        morning_data = df1[df1['hr'] <= 10]
        ttl_morning = morning_data['cnt'].sum()
        afternoon_data = df1[(df1['hr'] >= 11) & (df1['hr'] <= 14)]
        ttl_afternoon = afternoon_data['cnt'].sum()
        evening_data = df1[(df1['hr'] >= 15) & (df1['hr'] <= 17)]
        ttl_evening = evening_data['cnt'].sum()
        night_data = df1[df1['hr'] >= 18]
        ttl_night = night_data['cnt'].sum()
        
        totalh = [ttl_morning, ttl_afternoon, ttl_evening, ttl_night]
        time = ['Morning','Afternoon','Evening','Night']
        
        fig, ax = plt.subplots(figsize=(15,6))
        barplot2 = ax.bar(x= time, height= totalh)
        ax.bar_label(barplot2, labels = totalh)
        st.pyplot(fig)
        
        fig, ax = plt.subplots(figsize=(15,6))
        ax.pie(
                x = totalh,
                labels = time,
                autopct='%1.1f%%',
                colors = colors
        )
        st.pyplot(fig)
        
        st.markdown("Chart tersebut merepresentasikan nilai total peminjaman sepeda berdasarkan hari dan waktu.")

        sunny_data = df[(df['weather_map'] == 1) & (df['status'] == 'Weekday')]
        avg_sunnywd = sunny_data['total'].mean()
        cd_data = df[(df['weather_map'] == 2) & (df['status'] == 'Weekday')]
        avg_cdwd = cd_data['total'].mean()
        lr_data = df[(df['weather_map'] == 3) & (df['status'] == 'Weekday')]
        avg_lrwd = lr_data['total'].mean()

        avg = [avg_sunnywd, avg_cdwd, avg_lrwd]

        st.subheader('Average Weekday Bike Sharing Based On Weather')
        fig, ax = plt.subplots(figsize=(10,6))
        barplot = ax.bar(x= ['Sunny', 'Cloudy/Misty', 'Rain'], height= avg)
        ax.bar_label(barplot, labels=[f'{x:,.2f}' for x in avg], fontsize = 10)
        st.pyplot(fig)

        st.markdown('Chart tersebut merepresentasikan nilai rata-rata peminjaman sepeda pada hari bekerja (Senin - Jumat) berdasarkan cuaca.')

        sunny_data = df[(df['weather_map'] == 1) & (df['status'] == 'Weekend')]
        avg_sunnyw = sunny_data['total'].mean()
        cd_data = df[(df['weather_map'] == 2) & (df['status'] == 'Weekend')]
        avg_cdw = cd_data['total'].mean()
        lr_data = df[(df['weather_map'] == 3) & (df['status'] == 'Weekend')]
        avg_lrw = lr_data['total'].mean()

        avg = [avg_sunnyw, avg_cdw, avg_lrw]

        st.subheader('Average Weekend Bike Sharing Based On Weather')
        fig, ax = plt.subplots(figsize=(10,6))
        barplot = ax.bar(x= ['Sunny', 'Cloudy/Misty', 'Rain'], height= avg)
        ax.bar_label(barplot, labels=[f'{x:,.2f}' for x in avg], fontsize = 10)
        st.pyplot(fig)
        st.markdown('Chart tersebut merepresentasikan nilai rata-rata peminjaman sepeda pada akhir minggu (Sabtu & Minggu) berdasarkan cuaca.')

        sunny_data = df[(df['weather_map'] == 1) & (df['status'] == 'Holiday')]
        avg_sunnyh = sunny_data['total'].mean()
        cd_data = df[(df['weather_map'] == 2) & (df['status'] == 'Holiday')]
        avg_cdh = cd_data['total'].mean()
        lr_data = df[(df['weather_map'] == 3) & (df['status'] == 'Holiday')]
        avg_lrh = lr_data['total'].mean()

        avg = [avg_sunnyh, avg_cdh, avg_lrh]

        st.subheader('Average Holiday Bike Sharing Based On Weather')
        fig, ax = plt.subplots(figsize=(10,6))
        barplot = ax.bar(x= ['Sunny', 'Cloudy/Misty', 'Rain'], height= avg)
        ax.bar_label(barplot, labels=[f'{x:,.2f}' for x in avg], fontsize = 10)
        ax.set_title('Rata-rata peminjaman sepeda pada hari libur berdasarkan cuaca')
        st.pyplot(fig)
        st.markdown('Chart tersebut merepresentasikan nilai rata-rata peminjaman sepeda pada hari libur berdasarkan cuaca.')
        
        
        '''avg_sunnyt = (avg_sunnywd+avg_sunnyw+avg_sunnyh)/3
        avg_cdt = (avg_cdwd+avg_cdw+avg_cdh)/3
        avg_lrt = (avg_lrwd+avg_lrw+avg_lrh)/3'''
        
        sunny_data2 = df[df['weather_map'] == 1]
        avg_sunnyt = sunny_data2['total'].mean()
        cd_data2 = df[df['weather_map'] == 2]
        avg_cdt = cd_data2['total'].mean()
        lr_data2 = df[df['weather_map'] == 3]
        avg_lrt = lr_data2['total'].mean()
                        
        avgt = [avg_sunnyt, avg_cdt, avg_lrt]
        
        for i in range(len(avgt)):
                if np.isnan(avgt[i]):
                        avgt[i] = 0
        
        st.subheader('Percentage of Average Bike Sharing Based On Weather')
        fig, ax = plt.subplots(figsize=(15,6))
        ax.pie(
                x = avgt,
                labels = weathers,
                autopct='%1.1f%%',
                colors = colors
        )
        st.pyplot(fig)
        
        st.markdown('Chart tersebut merepresentasikan persentase nilai rata-rata peminjaman sepeda keseluruhan berdasarkan cuaca.')

        st.subheader('Bike Sharing by Temperature and Apparent Temperature')
        fig, ax = plt.subplots(figsize=(12,5))
        sns.scatterplot(data = df, x='total', y='temp',label='Suhu')
        sns.scatterplot(data = df, x='total', y='atemp', label='Suhu Jelas')
        ax.set_xlabel('Total')
        ax.set_ylabel('Suhu')
        ax.legend()

        st.pyplot(fig)
        st.markdown('Chart tersebut merepresentasikan total peminjaman sepada dengan suhu dan suhu yang dirasakan oleh pengguna')

        st.subheader('Correlation of Bike Sharing, Temperature and Apparent Temperature')
        fig, ax = plt.subplots(figsize=(5,5))
        korelasi = korelasi = df[['total','temp','atemp']].corr()
        sns.heatmap(korelasi, annot=True, cmap='coolwarm', fmt=".2f")
        ax.set_title('Correlation Heatmap')
        st.pyplot(fig)
        st.markdown('Heatmap tersebut merepresentasikan korelasi antara peminjaman sepeda, suhu dan suhu yang dirasakan oleh pengguna')

st.subheader('Conclusion')
st.markdown('- Pada hari dan pukul berapakah sepeda banyak dipinjamkan?')
st.markdown('Jawaban: Menurut hasil chart keseluruhan yang dimulai dari tanggal 2011/01/01 - 2012/12/31 peminjaman sepeda paling banyak pada hari jumat dengan persentase 14.8% dan pada malam hari dengan persentase 29.9%')
st.markdown('- Apakah cuaca dan suhu memengaruhi jumlah peminjaman sepeda dalam rentang waktu?')
st.markdown('Jawaban: Menurut hasil chart yang dimulai dari tanggal 2011/01/01 - 2012/12/31, sepeda paling banyak digunakan pada cuaca cerah dengan persentase 45.5% dan menurut heatmap, suhu berkorelasi dengan peminjaman sepeda sebesar 0.63')
