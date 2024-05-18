"""
Deskripsi
Jarak Manhattan adalah jarak dari suatu titik menuju suatu titik lainnya pada suatu sistem koordinat Kartesius dengan
menyusuri bagian vertikal dan horizontal, tanpa pernah kembali. Secara sederhana, sama dengan jumlah dari selisih absis
dan selisih ordinat. Dengan kata lain, jarak Manhattan = |x1 - x2| + |y1 - y2|.

Pak Dengklek ingin pergi dari koordinat (x1, y1) menuju (x2, y2). Tentukan jarak Manhattan yang harus ditempuh Pak
Dengklek.

Format Masukan
Sebuah baris berisi empat buah bilangan bulat x1, y1, x2, dan y2.

Format Keluaran
Sebuah baris berisi sebuah bilangan bulat yang merupakan jarak Manhattan dari kedua titik tersebut.
"""
s = input().split()
print(f"{abs(int(s[0]) - int(s[2])) + abs(int(s[1]) - int(s[3]))}")
