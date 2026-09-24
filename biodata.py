# Pertemuan 1 
nama = input("What is your name? ")
kota_asal = input("Where are you from? ")
tahun_lahir = int(input("What year were you born? "))
hobi = input("What are your hobbies? ")

print("===================================")
print("            BIODATA                ")
print("===================================")
print(f"Name: {nama}")
print(f"City: {kota_asal}")
print(f"Year of Birth: {tahun_lahir}")
print(f"Age: {2026 - tahun_lahir}")
print(f"Hobbies: {hobi}")
print(f"Age (in months): {12 * (2026 - tahun_lahir)}")
print("===================================")

