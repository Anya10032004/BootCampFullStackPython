# Things we need to know:
# - Class --> Like a blueprint it will contain the summarize behavior(methods) and features(property)
# - Object --> Specific examples from the blueprint(class)

# Example:
# Class: Car
# Objects: Toyota, Honda, Suzuki

# Class: animal
# Objects: Cat, Dog, Rabbit

# Example class:
class Mobil():
    def __init__(self, merkk, warnaa, tahunn): # __init__ is a function that will run when we create an object.
                                            # In this function we define properties of the object.
        self.merk = merkk # self.merk is a property
        self.warna = warnaa # self.warna is a property
        self.tahun = tahunn # self.tahun is a property

    def info(self): 
        print(f"Mobil {self.merk} berwarna {self.warna} tahun {self.tahun}")

    # self is used to refer to the object itself and info() is a method
    # NOTEE: self needs to be the first parameter in every method

    def drive(self): # drive() is a method
        print(f"Mobil {self.merk} sedang melaju")
    
    def stop(self): # stop() is a method
        print(f"Mobil {self.merk} berhenti")
    
    def hitungBahanBakar(self, jarak_tempuh):
        return (jarak_tempuh/10) * 10000


# To create an object
mobil1 = Mobil("Toyota", "Merah", 2022)
mobil2 = Mobil("Honda", "Biru", 2023)

# Too look at the property
print(f"The first's name: {mobil1.merk}")
print(f"The second's name: {mobil2.merk}")
print(f"The first's color: {mobil1.warna}")
print(f"The second's color: {mobil2.warna}")
print(f"The first's year: {mobil1.tahun}")
print(f"The second's year: {mobil2.tahun}")

print(" ")
print(" ")

# To call a method
mobil1.info()
mobil2.info()
mobil1.drive()
mobil2.stop()
bahanbakar_mobil1 = mobil1.hitungBahanBakar(10)
bahanbakar_mobil2 = mobil2.hitungBahanBakar(20)
print(f"The first's fuel needed: {bahanbakar_mobil1}")
print(f"The second's fuel needed: {bahanbakar_mobil2}")

# IMPORTANT NOTEE FOR PROJECT:
# OOP will be used to get the data from the database
# and the data we get from teh database will be put on an object
# and the object will be used to display the data in the GUI