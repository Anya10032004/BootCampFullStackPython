# CARA KERJA WEB:

# 1. User meminta request ke server melalui browser
# 2. Server memproses permintaan dan mengirimkan respons
# 3. Browser menampilkan respons

# Bagaimana cara user dan server berkomunikasi ?
# Dengan API(Application Programming Interface, API adalah seperti pelayan di restoran
# Kita (User) memberi pesanan (request) kepada pelayan
# Pelayan (API) mengambil pesanan ke dapur (server)
# Dapur (server) menyiapkan pesanan (memproses request)
# Pelayan (API) membawa pesanan (response) ke kita (User)

# Request bisa berupa : GET, POST, PUT, DELETE(ini disebut dengan HTTP, jadi HTTP itu adalah metode atau cara user mengirimkan request ke server)
# GET : Mengambil data dari server (paling sering digunakan, untuk menampilkan data ke web)
# POST : Mengirim data ke server untuk dibuat (misal: membuat akun baru, mengirim formulir, register)
# PUT : Memperbarui data yang sudah ada di server (misal: edit profil)
# DELETE : Menghapus data di server (misal: hapus akun, hapus postingan)

# Status code umum : adalah sebuah kode yang digunakan untuk memberitahu apakah request berhasil atau tidak
# 200 OK : Request berhasil
# 404 Not Found : Request tidak ditemukan
# 500 Internal Server Error : Server error(jadi kalau ada status code 404 berarti data yang diminta tidak ada di server)

# Format pertukaran data yang paling umum digunakan adalah JSON(JavaScript Object Notation, jadi format pertukaran data yang paling umum digunakan)

# Ini adalah dasar untuk memahami REST API, 
# REST = principles for organizing that interface
# REST API = an API designed around REST principles

# Bagaimana cara mengetest API kita udah benar ?
# Kita pakai postman, postman adalah aplikasi yang digunakan untuk menguji API 

# The Flask library--> adalah sebuah framework python yang digunakan untuk membuat web dan REST API
# We will try using the flask library in Try_Flask.py 

