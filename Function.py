# Function --> To make a code more organized and easy to remember
#              so taht we dont need to repeat the same code

# Function pada dasarnya memiliki input(parameter) --> Proses(code inside function) --> Output(untuk mengeluatkan pakai return)
# Example
def Pembatas():
    print("====================================")

# Function with parameter
# Ex:
def LuasSetiga(alas, tinggi):
    luas = 0.5 * alas * tinggi
    return luas # to get the output of LuasSetiga()

def HitungTotalratarata(listNilai):
    total = sum(listNilai)
    rata = total / len(listNilai)
    return rata # to get the output of HitungTotalratarata()


# Memanggil function
Pembatas()
Pembatas()
print(LuasSetiga(10, 20))
print(HitungTotalratarata([10, 20, 30, 40, 50]))
