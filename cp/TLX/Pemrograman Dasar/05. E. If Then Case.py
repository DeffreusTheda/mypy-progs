"""
Deskripsi
Pak Dengklek meminta Anda membuat sebuah program sebagai berikut. Program akan menerima sebuah bilangan bulat N. Jika N
merupakan satuan, cetak satuan. Jika N merupakan puluhan, cetak puluhan. Jika N merupakan ratusan, cetak ratusan. Jika
N merupakan ribuan, cetak ribuan. Jika N merupakan puluh ribuan, cetak puluhribuan.

Format Masukan
Sebuah berisi sebuah bilangan bulat N.

Format Keluaran
Sebuah baris berisi keluaran sesuai permintaan soal.
"""
N = int(input())
if N >= 100000:
    print("ratusribuan")
elif N >= 10000:
    print("puluhribuan")
elif N >= 1000:
    print("ribuan")
elif N >= 100:
    print("ratusan")
elif N >= 10:
    print("puluhan")
else:
    print("satuan")
