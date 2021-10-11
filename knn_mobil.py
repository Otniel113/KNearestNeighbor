import pandas as pd
import math

#Melakukan import data dari mobil.xls
def importData():
    data = pd.read_excel("mobil.xls")
    nama_mobil = data['Nama Mobil'].to_list()
    ukuran = data['Ukuran'].to_list()
    kenyamanan = data['Kenyamanan'].to_list()
    irit = data['Irit'].to_list()
    kecepatan = data['Kecepatan'].to_list()
    harga = data['Harga (Ratus Juta)'].to_list()
    data_mobil = []
    for i in range (0,len(nama_mobil)):
        tampung = []
        tampung.append(nama_mobil[i])
        tampung.append(ukuran[i])
        tampung.append(kenyamanan[i])
        tampung.append(irit[i])
        tampung.append(kecepatan[i])
        tampung.append(harga[i])
        data_mobil.append(tampung)
    return data_mobil

#Pre Processing data dengan validasi inputan agar sesuai range
def validasiInput1sd10(inputan):
    if (0 <= inputan <= 10):
        print("Inputan berhasil")
        return True
    else:
        print("Tolong masukkan Angka yang valid dari 1-10")
        return False

def validasiInputHarga(harga):
    if (harga >= 0):
        print("Inputan berhasil")
        return True
    else:
        print("Tolong masukkan Angka positif yang valid >0 ")
        return False

#Menampung inputan dari User dari 5 kriteria
def inputDariUser():
    mobil = []
    print("Masukkan kriteria angka yang ingin Anda cari rekomandasi mobilnya : ")
    while True:
        ukuran = float(input("Masukkan angka untuk ukuran (dari 1 sampai 10): "))
        if validasiInput1sd10(ukuran):
            mobil.append(ukuran)
            break
    while True:
        kenyamanan = float(input("Masukkan angka untuk kenyamanan (dari 1 sampai 10): "))
        if validasiInput1sd10(kenyamanan):
            mobil.append(kenyamanan)
            break
    while True:
        irit = float(input("Masukkan angka untuk irit (dari 1 sampai 10): "))
        if validasiInput1sd10(irit):
            mobil.append(irit)
            break
    while True:
        kecepatan = float(input("Masukkan angka untuk kecepatan (dari 1 sampai 10): "))
        if validasiInput1sd10(kecepatan):
            mobil.append(kecepatan)
            break
    while True:
        harga = float(input("Masukkan angka untuk harga (lebih besar dari 0): "))
        if validasiInputHarga(harga):
            mobil.append(harga)
            break
    return mobil

#Rumus menghitung Euclidean Distance
def EuclideanDistance(train, test):
    jumlah = 0
    for i in range (0,len(test)):
        hasil = (train[i+1] - test[i]) ** 2
        jumlah += hasil
    return math.sqrt(jumlah)

#Tabel Klasifikasi menampung hasil Euclidean Distance
def tabelEuclidean(data_mobil, mobil):
    tbl_euclidean = []
    for i in range (0, len(data_mobil)):
        tampung = []
        nama_mobil = data_mobil[i][0]
        nilai = EuclideanDistance(data_mobil[i], mobil)
        tampung.append(nama_mobil)
        tampung.append(nilai)
        tbl_euclidean.append(tampung)
    return tbl_euclidean

#Algoritma Sorting
def SelectionSort(arr):
    for i in range(0,len(arr)):
        minimal = i
        for j in range(i+1,len(arr)):
            if (arr[minimal][1] > arr[j][1]):
                minimal = j
        arr[minimal], arr[i] = arr[i], arr[minimal]

#Memilih 3 nearest neighbour
def choose_3_nearest_neighbour(arr):
    three_neighbour = []
    for i in range(0,3):
        three_neighbour.append(arr[i][0])
    return three_neighbour

#Export Data ke Excel
def exportData(tbl_euclidean):
    df = pd.DataFrame(tbl_euclidean, columns = ["Nama Mobil"])
    df.to_excel(r'rekomendasi.xlsx', index=False, header=True)

#======================MAIN PROGRAM======================

#Melakukan import dara mobil.xls
data_mobil = importData()

#Menampung inputan dari User
mobil = inputDariUser()

#Tabel Klasifikasi menampung hasil menghitung jarak Euclidean
tbl_euclidean = tabelEuclidean(data_mobil, mobil)

#Mengurutkan tabel
SelectionSort(tbl_euclidean)

#Memilih 3 neighbour terdekat
three_neighbour = choose_3_nearest_neighbour(tbl_euclidean)

#Melakukan export data ke excel
exportData(three_neighbour)
