import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Judul dan Deskripsi Dashboard
st.set_page_config(page_title="EduPath AI Dashboard", layout="wide")
st.title("🎓 EduPath AI: Dashboard Analisis Data Siswa")
st.write("Dashboard ini menampilkan hasil analisis interaktif dari data siswa yang telah dibersihkan.")

# 2. Membaca Data CSV
@st.cache_data
def load_data():
    df = pd.read_csv("cleaned_student_data.csv")
    return df

data = load_data()

# 3. Menampilkan Tabel Data
st.subheader("📋 Cuplikan Data Siswa")
st.dataframe(data.head()) 

# 4. Membuat Visualisasi Sederhana
st.subheader("📊 Distribusi Kategori Performa Siswa (Class)")
st.write("Data di bawah ini menunjukkan jumlah siswa di tiap kategori performa (Low, Middle, High).")


class_counts = data['Class'].value_counts()


fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(class_counts.index, class_counts.values, color=['#4CAF50', '#FFC107', '#F44336'])
ax.set_ylabel("Jumlah Siswa")
ax.set_xlabel("Kategori Kelas (Performa)")

st.pyplot(fig)

# 5. Fitur Interaktif (Filter Data)
st.subheader("🔍 Cari Data Spesifik")
# Membuat dropdown (pilihan) berdasarkan kolom Gender
pilihan_gender = st.selectbox("Pilih Gender:", data['gender'].unique())

# Memfilter data berdasarkan pilihan pengguna
data_terfilter = data[data['gender'] == pilihan_gender]
st.write(f"Menampilkan {len(data_terfilter)} siswa dengan gender: **{pilihan_gender}**")
st.dataframe(data_terfilter)import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Judul dan Deskripsi Dashboard
st.set_page_config(page_title="EduPath AI Dashboard", layout="wide")
st.title("🎓 EduPath AI: Dashboard Analisis Data Siswa")
st.write("Dashboard ini menampilkan hasil analisis interaktif dari data siswa yang telah dibersihkan.")

# 2. Membaca Data CSV
streamlit run app.py
@st.cache_data
def load_data():
    df = pd.read_csv("cleaned_student_data.csv")
    return df

data = load_data()

# 3. Menampilkan Tabel Data
st.subheader("📋 Cuplikan Data Siswa")
# Menampilkan 5 baris pertama saja agar rapi
st.dataframe(data.head()) 

# 4. Membuat Visualisasi Sederhana
st.subheader("📊 Distribusi Kategori Performa Siswa (Class)")
st.write("Data di bawah ini menunjukkan jumlah siswa di tiap kategori performa (Low, Middle, High).")

# Menghitung jumlah siswa di masing-masing 'Class' (performa)
class_counts = data['Class'].value_counts()

# Membuat grafik batang (Bar Chart)
fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(class_counts.index, class_counts.values, color=['#4CAF50', '#FFC107', '#F44336'])
ax.set_ylabel("Jumlah Siswa")
ax.set_xlabel("Kategori Kelas (Performa)")
# Menampilkan grafik ke Streamlit
st.pyplot(fig)

# 5. Fitur Interaktif (Filter Data)
st.subheader("🔍 Cari Data Spesifik")
# Membuat dropdown (pilihan) berdasarkan kolom Gender
pilihan_gender = st.selectbox("Pilih Gender:", data['gender'].unique())

# Memfilter data berdasarkan pilihan pengguna
data_terfilter = data[data['gender'] == pilihan_gender]
st.write(f"Menampilkan {len(data_terfilter)} siswa dengan gender: **{pilihan_gender}**")
st.dataframe(data_terfilter)