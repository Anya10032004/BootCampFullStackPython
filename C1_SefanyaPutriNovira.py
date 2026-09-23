
total_belanja = int(input("Total Belanja : "))
total_dibayar = int(input("Uang Dibayar : "))
print(f"Uang cukup {total_dibayar>=total_belanja}")
print(f"Kekurangan : {total_belanja-total_dibayar}")
kembalian = total_dibayar>=total_belanja and total_dibayar-total_belanja or 0
print(f"Kembalian : {kembalian or 0}")
lem1 = kembalian//100000
print(f"Rp100.000 {lem1}")
kembalian -= lem1*100000
lem2 = kembalian//50000
print(f"Rp50.000 {lem2}")
kembalian -= lem2*50000
lem3 = kembalian//20000
print(f"Rp20.000 {lem3}")
kembalian -= lem3*20000
lem4 = kembalian//10000
print(f"Rp10.000 {lem4}")
kembalian -= lem4*10000
lem5 = kembalian//5000
print(f"Rp5.000 {lem5}")
kembalian -= lem5*5000
lem6 = kembalian//2000
print(f"Rp2.000 {lem6}")
kembalian -= lem6*2000
lem7 = kembalian//1000
print(f"Rp1.000 {lem7}")
kembalian -= lem7*1000
lem8 = kembalian//500
print(f"Rp500 {lem8}")
print(f"Total lembar/keping : {lem1+lem2+lem3+lem4+lem5+lem6+lem7+lem8}")
