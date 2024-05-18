"""
Deskripsi
Pak Dengklek memiliki N buah kandang bebek, dinomori dari 1 sampai dengan N. Kandang ke-i berisi Bi ekor bebek. Berapa
banyaknya total bebek yang Pak Dengklek miliki?

Format Masukan
Baris pertama berisi sebuah bilangan bulat N. Baris kedua berisi N buah bilangan bulat B1, B2, ..., BN.

Format Keluaran
Sebuah baris berisi sebuah bilangan bulat yang merupakan banyaknya total bebek.
"""
N = input()
ar = input().split()
sum = 0
for i in ar:
    sum += int(i)
print(sum)
