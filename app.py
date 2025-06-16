import streamlit as st

st.title("Kamu Mau Menjadi Apa? - Tema Olahraga😎") #Judul Quiz
st.header("Selamat datang di Quiz Masa Depan") #Header kata sambutan
name = st.text_input("Masukkan nama kamu di sini ya:") #menginputkan nama pengguna

if st.button("Mulai Quiz Sekarang"): #Button memulai quiz
    st.write(f"Halo, {name}! Ayo mulai kuisnya.")

#Nilai awal setiap katogorinya
score_pemainsepakbola = 0
score_atletangkatbesi = 0
score_atletsenam = 0 

#Beberapa pertanyaan yang akan ditanyakan 
# Pertanyaan Ke - 1
st.header("1. Kamu itu lebih suka olahraga yang mana?") 
q1 = st.radio("Pilih salah satu ya:", [
    "Ada strategi tim dan koordinasi antar pemain",
    "Menguji kekuatan dan daya tahan tubuh secara pribadi",
    "Menggunakan ketangkasan dan keseimbangan"
], key="q1")

# Pertanyaan Ke - 2
st.header("2. Ketika berlatih, kamu lebih fokus pada?")
q2 = st.radio("Pilih salah satu ya:", [
    "Kerja sama tim dan membangun chemistry",
    "Mencapai target pribadi dan memecahkan rekor",
    "Menyempurnakan gerakan dan teknik"
], key="q2")

# Pertanyaan Ke - 3
st.header("3. Kalimat Motivasi kamu apa?" )
q3 = st.radio("Pilih salah satu ya:", [
    "Together we are stronger",
    "Push your limits",
    "Grace and precision define success"
], key="q3")

#Penghitungan hasil akhir berdasarkan jawaban yang tersedia
if st.button("Lihat Hasil"):
    # Skoring berdasarkan jawaban
    if q1 == "Ada strategi tim dan koordinasi antar pemain":
        score_pemainsepakbola += 1
    elif q1 == "Mencapai target pribadi dan memecahkan rekor":
        score_atletangkatbesi += 1
    else:
        score_atletsenam += 1
        
    if q2 == "Kerja sama tim dan membangun chemistry":
        score_pemainsepakbola+= 1
    elif q2 == "Mencapai target pribadi dan memecahkan rekor":
        score_atletangkatbesi += 1
    else:
        score_atletsenam += 1
        
    if q3 == "Together we are stronger":
        score_pemainsepakbola += 1
    elif q3 == "Push your limits":
        score_atletangkatbesi += 1
    else: 
        score_atletsenam += 1

#Menampilkan hasil akhir atau final dengan gif penunjang
# Hasil Akhir
st.subheader("🙌 Hasil Kamu:")
if score_pemainsepakbola > score_atletangkatbesi and score_pemainsepakbola > score_atletsenam:
    st.success("⚽ Kamu cocok jadi PEMAIN SEPAK BOLA TIMNAS")
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ2M2YTVsYnFid25meXkyajVuZnU1aXF1dXkzczBzZjZ2djVyaWpiayZlcD12MV9naWZzX3NlYXJjaCZjdD1n/30ASDMluK9bCt2sWp9/giphy.gif")
elif score_atletangkatbesi > score_pemainsepakbola and score_atletangkatbesi > score_atletsenam:
    st.success("🏋️‍♂️ Kamu cocok jadi ANGKAT BESI KUAT")
    st.image("https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExeHc0ZnAzNHNyOHhnemVkeGYxcnhuYzhjeGMwcjR3ZzgzbHZla2I0OCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/by2h1l4Y21onoNtGUF/giphy.gif")
else: 
    st.success("🤸‍♂️ Kamu cocok jadi ATLET SENAM AKROBATIK")
    st.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExazc3amdndWY3ampicHFudmxmZmUwZHpwZHp3bGd2cnR3a28zcnNhNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/JpOnQ8gDz1T79N2I7o/giphy.gif")
    