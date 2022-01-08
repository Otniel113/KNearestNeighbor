# KNearestNeighbor
Penerapan KNN untuk rekomendasi mobil berdasarkan 5 karakteristik yang diinginkan

## Input Output Program
Program membaca dataset mobil.xls dengan dan mengeluarkan file rekomendasi.xlsx berisi 3 rekomendasi mobil berdasarkan kriteria inputan user.

## Dataset
Diberikan file mobil.xls berupa himpunan data 17 data mobil dengan 5 (lima) atribut:
1. Ukuran akan bernilai dari 0-10 dimana semakin besar angkanya semakin besar ukuran mobil.
2. Kenyamanan akan bernilai 0-10 dimana semakin besar angkanya semakin nyaman mobilnya.
3. Irit akan bernilai 0-10 dimana semakin besar angkanya akan semakin irit.
4. Kecepatan akan bernilai 0-10 dimana semakin besar akan semakin cepat.
5. Harga akan bernilai ratus juta, jika bernilai 1 maka akan senilai 100 juta, 3,75 artinya mobil akan berharga 375 juta.

## Hal yang Diobservasi
| Parameter Observasi | Nilai |
| -- | -- |
| Jarak | Euclidan Distance |
| Praproses | Validasi nilai inputan user agar bernilai 0-10 kecuali untuk harga agar tidak bernilai negatif |
| Nilai K | K = 3 |

## Hasil Akhir
Saat menjalankan program, akan memiliki tampilan seperti ini <br>
![image](https://user-images.githubusercontent.com/57952404/148643110-9c196540-2792-4130-93df-446c99b5174d.png)
<br>
Dan hasil outputan file rekomendasi.xlsx seperti ini  <br>
![image](https://user-images.githubusercontent.com/57952404/148643127-02024c7a-52ad-4e13-a26c-daaa0c20407d.png)

## Lebih Lanjut
Untuk informasi lebih lanjut bisa dilihat di file Laporan PDF dan Slide PPT

## Video Penjelasan
[Klik untuk pergi ke video](https://drive.google.com/file/d/11VoYh9KsN9zO7SHcSZZiX4hCEwYlOZtf/view?usp=sharing)
