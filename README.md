# Proyek Akhir Video Games Recommendation System

#### Disusun oleh : Zaky Abdullah Basith

## Project Overview
Video game telah menjadi salah satu bentuk hiburan yang paling populer di seluruh dunia. 
Industri video game terus berkembang sejak pertama kali diperkenalkan pada tahun 1970-an. 
Saat ini, video game telah menjadi industri yang bernilai miliaran dolar dengan ribuan judul 
game yang dirilis setiap tahun. Pertumbuhan ini didorong oleh kemajuan teknologi yang 
memungkinkan pembuatan game yang semakin realistis dan kompleks. Seiring dengan peningkatan 
kualitas game, popularitasnya semakin meningkat dan penggemar game berasal dari berbagai 
lapisan masyarakat.
<br>
Sistem rekomendasi video games dikembangkan untuk membantu pengguna menemukan game yang mereka 
sukai dan meningkatkan pengalaman bermain game mereka. Dalam industri game, terdapat ribuan 
judul game yang dirilis setiap tahun, dan ini membuat sulit bagi pengguna untuk menemukan game 
yang sesuai dengan preferensi mereka. Oleh karena itu, pengembang dan perusahaan game berusaha untuk  
mengembangkan sistem rekomendasi yang memanfaatkan data tentang genre video games. 

## Business Understanding
Proyek ini dibangun untuk perusahaan yang bergerak di bidang video game seperti:
- Perusahaan pengembang video games.
- Perusahaan distribusi games seperti Steam, GOG, dan Epic Games Store
### Problem statement
Dari permasalahan diatas muncul sebuah pertanyaan Bagaimana cara membuat sistem rekomendasi 
video games berdasarkan data genre dari video games tersebut.
### Goal
Tujuan proyek ini adalah dapat membuat sistem rekomendasi video games berdasarkan genre video games.
### Solution Statement
1. Membangun sistem rekomendasi dengan metode content based filtering berdasarkan data genre.
2. Sistem rekomendasi tersebut dibangun dengan mengggunakan TFIDF vectorizer dan cosine similarity.

## Data Understanding
Dataset yang digunakan pada proyek ini adalah dataset [Video Games Sales](https://www.kaggle.com/datasets/gregorut/videogamesales)
yang diunduh dari website kaggle. <br>
berikut informasi dari dataset:
- dataset terdiri dari 16598 baris dan 11 kolom (7 kolom kategorikal dan 4 kolom numerikal)
- dataset berformat CSV( Comma Separated Value).
- dataset memiliki data duplikat sebanyak 5101
- tedapat 11495 judul video games dan 12 genre
<br>
Dataset tersebut berisi beberapa fitur sebagai berikut:
<br><br>tabel 1. tabel fitur dataset California House Price

| nama fitur | tipe data | deskripsi | 
|------------|-----------|-----------| 
| Rank | Integer | Urutan dalam penjualan
| Name | String | Judul video game 
| Platform | String | Tempat perilisan video games (contoh. PS2,PC, Xbox)
| Year | Integer  | Tahun perilisan 
| Genre | String | Genre video games
| Publisher | String | Perusahaan yang mem-publish video game
| NA_Sales | Integer | Penjualan di Amerika Utara
| EU_Sales | Integer | Penjualan di Eropa
| JP_Sales | Integer | Penjualan di Jepang
| Other_Sales | Integer | Penjualan di negara lainnya
| Global_Sales| Integer | Total Penjualan


### EDA
- Jumlah video games tiap platform
    ![output](https://user-images.githubusercontent.com/55694756/229278518-566e01d2-456d-442a-9c3b-00ea3594d4ac.png)
    gambar 1. Jumlah video games tiap platform
    
    Terlihat video games yang rilis di platform Nintendo DS dan PS2 terbanyak diantara platform lainnya.
    
- Jumlah video games tiap tahun
    ![output2](https://user-images.githubusercontent.com/55694756/229278556-de140e78-8d5a-4193-933c-50e62f454d43.png)
    gambar 2. Jumlah video games tiap platform
    Pada gambar 2 terlihat, pada tahun 2008 dan 2009 merupakan tahun paling banyak merilis video games.
- Perbadingan genre video games
    ![output3](https://user-images.githubusercontent.com/55694756/229278577-98a84ebc-09f7-4174-8e20-07dac2f58069.png)
    gambar 3. Perbadingan genre video games
    Pada gmabar 3 terlihat genre action merupakan genre yang paling banyak diikuti oleh genre sports.


## Data Preparation
- Mengambil kolom 'Name' dan 'Genre
Karena proyek ini membangun sistem rekomendasi dengan content based learning, maka data yang dipakai hanya kolom judul game dan genre sebagai content dari video games. 
- Menghilangkan hyphen pada kolom genre
Karena TFIDF menerima kata yang dipisahkan dengan tanda hubung / hypen (-) menjadi dua kata, maka value di kolom genre yang berisi hyphen dihilangkan. Contohnya kata 'Role-Playing' menjadi 'RolePlaying
- membuang nilai yang duplikat 
Nilai duplikat dapat mempengarhi proses TFIDF. Oleh karena itu nilai duplikat harus dibuang.

## Modeling and Results
### Content Based Filtering
Sistem yang dibangun pada proyek ini adalah sistem rekomendasi berdasarkan genre video games berbasis content based filtering.
<br>
Cara kerja dari sistem rekomendasi berbasis konten adalah merekomendasikan item yang mirip dengan item yang disukai pengguna di masa lalu.
Dalam kasus ini, dua video games dikatakan mirip bila kedua video games memiliki genre yang sama.
contoh nya ada seseorang yang menyukai video game NBA 2K14 yang bergenre 'sports', sistem rekomendasi akan merekomendasikan
game yang bergenre 'Sports' lainnya seperti NASCAR '15

![Untitled Diagram drawio](https://user-images.githubusercontent.com/55694756/229278304-613b9fcf-4d06-4537-9b12-0441ea1195f2.png)

gambar 4. gambaran sistem rekomendasi berbasis konten

### TFIDF Vectorizer
TF-IDF (Term Frequency-Inverse Document Frequency) adalah sebuah metode penghitungan bobot pada 
suatu kata dalam sebuah dokumen atau kumpulan dokumen. Metode ini digunakan untuk mengevaluasi 
seberapa penting suatu kata dalam konteks dokumen tersebut atau dalam kumpulan dokumen yang 
lebih besar. 

Bobot TF-IDF diperoleh dari perkalian antara frekuensi kemunculan kata (term frequency) dan 
invers frekuensi dokumen (inverse document frequency). Term frequency mengukur seberapa sering 
suatu kata muncul dalam dokumen tersebut, sedangkan inverse document frequency mengukur seberapa
sering kata tersebut muncul di seluruh kumpulan dokumen.

Pada proyek ini TFIDF digunakan untuk menemukan representasi fitur penting dari setiap genre video game.
Proyek ini menggunakan salah satu fungsi dari library sklearn, yakni `tfidfvectorizer()`

### Consine Similarity
Cosine similarity adalah salah satu teknik dalam analisis data dan pemrosesan teks yang 
digunakan untuk mengukur sejauh mana kemiripan antara dua buah vektor dalam ruang 
multidimensional. Pada pemrosesan teks, cosine similarity digunakan untuk membandingkan 
kedekatan antara dua dokumen teks berdasarkan pada kata-kata yang terdapat di dalam dokumen 
tersebut. Konsep cosine similarity berdasarkan pada sudut yang terbentuk antara dua buah vektor.
Semakin besar sudut antara dua vektor, semakin jauh kedua vektor tersebut dari kemiripan. 
Sebaliknya, semakin kecil sudut antara dua vektor, semakin dekat kedua vektor tersebut secara 
kemiripan. 

Cosine similarity menghasilkan skor yang berkisar antara 0 hingga 1. Nilai 1 
menunjukkan bahwa dua buah vektor adalah sama persis, sedangkan nilai 0 menunjukkan bahwa dua 
buah vektor tidak memiliki kesamaan sama sekali. Semakin tinggi skor cosine similarity, semakin 
dekat kedua vektor secara kemiripan.

Proyek ini memanfaatkan salah satu fungsi dari library sklearn, yaitu `cosine_similarity()`.
cosine similarity digunakan untuk menghitung derajat kedekatan antar video game

### Result
Untuk mendapatkan suatu rekomendasi dari sebuah input, maka dibuatkanlah fungsi `get_recommendations()`. 
Fungsi akan mencari rekomendasi berdasarkan similarity yag telah dibuat sebelumnya. 

Berikut contoh hasil pencarian daftar 10 judul teratas yang mirip dengan video game NBA 2K14:
| Nama | Genre
|------|------
|NBA 09: The Inside	|Sports
|World Stadium 4	|Sports
|Kawa no Nushi Tsuri	|Sports
|Let's Ride: Sunshine Stables	|Sports
|International Superstar Soccer Deluxe	|Sports
|Jikkyou Powerful Pro Yakyuu 3 '97 Haru	|Sports
|Pro Yaky? Spirits 3	|Sports
|Wakeboarding Unleashed Featuring Shaun Murray	|Sports
|Ready 2 Rumble Revolution	|Sports
|VR Golf '97	|Sports

Terlihat tabel diatas merupakan rekomendasi dari input NBA 2K14. NBA 2K14 merupakan video games yang bergenre sports. 
Sistem rekomendasi berhasil menampilkan 10 daftar video game yang genrenya mirip dengan NBA 2K14

## Evaluation
Untuk menghitung performa dari sistem rekomendasi yang telah dibuat, proyek ini menggunakan formula precision
![W8rc6](https://user-images.githubusercontent.com/55694756/229278423-a27494a0-57eb-4281-a9ff-a58e2276a98b.png)


dari formula tersebut, didapatkan nilai precision sistem rekomendasi video game NBA 2K14 sebesar (10/10) atau 100%
