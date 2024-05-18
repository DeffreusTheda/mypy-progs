"""
Deskripsi
Pak Dengklek menggambar sebuah segitiga yang alasnya berukuran A cm dan tingginya berukuran T cm. Ia ingin menghitung
luas dari segitiga tersebut, tetapi ia lupa caranya. Bantulah dia.

Format Masukan
Sebuah baris berisi dua buah bilangan bulat A dan T.

Format Keluaran
Sebuah baris berisi sebuah bilangan riil yang menyatakan luas dari segitiga tersebut dalam cm persegi, dengan tepat dua
angka di belakang koma.
"""
tmp = input().split()
A = int(tmp[0])
T = int(tmp[1])
res = 0.5 * A * T
print(f"{res:.2f}")
