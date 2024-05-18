"""
Deskripsi
Matriks berukuran 3 × 3 adalah kumpulan 9 bilangan yang disusun dalam bentuk sebagai berikut. Karakter-karakter
'a' - 'i' menyatakan bilangan-bilangan bulat yang merupakan anggota-anggota dari matriks tersebut.
```
a b c
d e f
g h i
```
Transpos dari suatu matriks A yang berukuran 3 × 3, dilambangkan dengan AT, adalah matriks yang susunan
anggota-anggotanya diubah menjadi seperti berikut.
```
a d g
b e h
c f i
```
Pak Dengklek memberikan Anda sebuah matriks A yang berukuran 3 × 3. Tentukan transpos dari matriks A tersebut.

Format Masukan
Tiga buah baris berisi anggota-anggota matriks A sesuai format di atas.

Format Keluaran
Tiga buah baris berisi anggota-anggota transpos dari matriks A sesuai format di atas.
"""
ar = [input().split(), input().split(), input().split()]
for x in range(3):
    for y in range(3):
        print(f"{ar[y][x]}", end=" ")
    print("")
