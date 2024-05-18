"""
Deskripsi
Pak Dengklek memiliki N ekor bebek. Ia ingin membagi-bagikan bebek-bebeknya tersebut sama rata kepada M orang temannya.
Pak Dengklek juga menyadari bahwa bisa saja terdapat sisa bebek karena banyaknya bebek tidak habis dibagi banyaknya
temannya.

Bantulah Pak Dengklek untuk menentukan berapa ekor bebek yang harus dia berikan kepada masing-masing temannya, dan
berapa sisanya.

Format Masukan
Sebuah baris berisi dua buah bilangan bulat N dan M.

Format Keluaran
Baris pertama berisi masing-masing A, dengan A adalah banyaknya bebek yang diberikan kepada masing-masing temannya.
Baris kedua berisi bersisa B, dengan B adalah banyaknya sisa bebek Pak Dengklek.
"""
tmp = input().split()
N = int(tmp[0])
M = int(tmp[1])
print("masing-masing " + str(int(N/M)))
print("bersisa " + str(N % M))
