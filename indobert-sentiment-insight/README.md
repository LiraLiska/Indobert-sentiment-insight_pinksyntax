# 🎀 IndoBERT Sentiment Insight

Aplikasi analisis sentimen berbasis **Deep Learning** menggunakan **IndoBERT** untuk mengklasifikasikan teks berbahasa Indonesia ke dalam tiga kategori sentimen, yaitu **Positive**, **Negative**, dan **Neutral**. Aplikasi ini dibangun menggunakan **Streamlit** sebagai antarmuka pengguna dan memanfaatkan model **Transformer (IndoBERT)** dari Hugging Face.

---

## 📌 Deskripsi Proyek

Proyek ini bertujuan untuk melakukan analisis sentimen terhadap teks berbahasa Indonesia menggunakan model IndoBERT yang telah di-fine-tuning. Pengguna cukup memasukkan sebuah kalimat atau ulasan, kemudian sistem akan memprediksi kelas sentimennya.

---

## ✨ Fitur

- Analisis sentimen secara real-time
- Antarmuka berbasis Streamlit
- Model Deep Learning berbasis IndoBERT
- Prediksi 3 kelas sentimen:
  - 😊 Positive
  - 😐 Neutral
  - 😞 Negative

---

## 🛠️ Teknologi yang Digunakan

| Teknologi | Keterangan |
|-----------|------------|
| Python | Bahasa Pemrograman |
| Streamlit | User Interface |
| PyTorch | Deep Learning Framework |
| Hugging Face Transformers | Model IndoBERT |
| NumPy | Pengolahan Data |

---

# 📂 Struktur Proyek

```
indobert-sentiment-insight/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
└── model_akhir/
    ├── config.json
    ├── model.safetensors
    ├── tokenizer.json
    └── tokenizer_config.json
```

---

# 🚀 Cara Menjalankan

### Clone Repository

```bash
git clone https://github.com/USERNAME/REPOSITORY.git
```

### Masuk ke Folder

```bash
cd REPOSITORY
```

### Install Library

```bash
pip install -r requirements.txt
```

### Jalankan Streamlit

```bash
streamlit run app.py
```

---

# 🖥️ Dokumentasi User Interface

## Halaman Utama

> <img width="1918" height="905" alt="image" src="https://github.com/user-attachments/assets/f7e72b04-c6eb-4bc8-8ef6-f9503bfb73da" />


---

## Input Teks

> <img width="1917" height="901" alt="image" src="https://github.com/user-attachments/assets/1afe9ca3-985f-4a46-96e6-0de2a822d28c" />



---

## Hasil Prediksi

> <img width="1918" height="873" alt="image" src="https://github.com/user-attachments/assets/2fab0898-798a-44e4-b0ec-1d05fd600b2c" />Sistem menampilkan hasil klasifikasi sentimen.


---

# 🔄 Alur Sistem

1. Pengguna memasukkan teks.
2. Tokenizer IndoBERT memproses teks.
3. Model IndoBERT melakukan prediksi.
4. Sistem menentukan kelas sentimen.
5. Hasil ditampilkan pada antarmuka Streamlit.

---

# 📊 Label Sentimen

| Label | Arti |
|--------|------|
| Positive | Sentimen Positif |
| Neutral | Sentimen Netral |
| Negative | Sentimen Negatif |

---

# 📷 Contoh Penggunaan

Input

```
Pelayanannya sangat memuaskan dan produknya berkualitas.
```

Output

```
Positive 🌸
```

---

Input

```
Barang datang terlambat dan kualitasnya buruk.
```

Output

```
Negative 🌸
```

---

Input

```
Produknya sesuai deskripsi.
```

Output

```
Neutral 🌸
```

---

# ⚠️ Catatan Deployment
Aplikasi ini telah dipersiapkan untuk deployment menggunakan Hugging Face Spaces. Namun, proses deployment tidak dapat diselesaikan karena repository telah mencapai batas penyimpanan (Repository Storage Limit Reached), sehingga file model (model.safetensors) tidak dapat diunggah.

Sesuai arahan dosen, dokumentasi antarmuka (UI) aplikasi disertakan pada README ini sebagai pengganti hasil deployment.

Model yang telah dilatih dapat diunduh melalui Google Drive berikut untuk menjalankan aplikasi secara lokal:

Google Drive:

[https://drive.google.com/file/d/1smSrQtgUqXeOsmLGaUk2oLG17RDdomyW/view?usp=sharing]

Setelah diunduh, letakkan file model pada folder model_akhir/ (atau sesuai dengan path yang digunakan pada source code) sebelum menjalankan aplikasi.


Sebagai pengganti hasil deployment, dokumentasi antarmuka aplikasi disertakan pada README ini sesuai arahan dosen.

---

# 👩‍💻 Pengembang

**Team PinkSyntax**

Program Studi Teknik Informatika

STT Terpadu Nurul Fikri

---

# 📄 Lisensi

Proyek ini dibuat untuk keperluan akademik.
