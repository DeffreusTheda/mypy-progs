"""
Deskripsi
Nilai floor dari sebuah bilangan riil adalah bilangan bulat terbesar yang masih lebih kecil daripada atau sama dengan
bilangan tersebut. Sebaliknya, nilai ceiling dari sebuah bilangan riil adalah bilangan bulat terkecil yang masih lebih
besar daripada atau sama dengan bilangan tersebut.

Pak Dengklek memberikan Anda sebuah bilangan riil N. Tentukan nilai floor dan ceiling dari N.

Format Masukan
Sebuah baris berisi sebuah bilangan riil N.

Format Keluaran
Sebuah baris berisi F C, dengan F adalah floor dari N dan C adalah ceiling dari N.
"""
N = float(input())
if N % 1 == 0:
    print(f"{int(N)} {int(N)}")
elif N >= 0:
    print(f"{int(N)} {int(N+1)}")
else:
    print(f"{int(N-1)} {int(N)}")
