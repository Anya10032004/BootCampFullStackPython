jam_masuk = int(input("Jam masuk : "))
menit_masuk = int(input("Menit masuk : "))
jam_keluar = int(input("Jam keluar : "))
menit_keluar = int(input("Menit keluar : "))

jam = jam_keluar > jam_masuk and jam_keluar - jam_masuk or (24+jam_keluar) - jam_masuk
menit = menit_keluar > menit_masuk and menit_keluar - menit_masuk or (60+menit_keluar) - menit_masuk
print(f"Lama parkir : {jam} jam {menit} menit")
jam_ditagih = menit > 0 and jam+1 or jam
print(f"Jam ditagih : {jam_ditagih}")
print(f"Total tarif : Rp {(jam_ditagih-1)*2000 + 3000}")
