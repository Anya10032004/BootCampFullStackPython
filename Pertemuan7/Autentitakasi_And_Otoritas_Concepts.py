# Authentication vs Authorization:
# - Authentication (Autentikasi): Proses untuk membuktikan siapa kamu.
# Contoh: Login menggunakan username dan password.

# - Authorization (Otorisasi): Proses untuk menentukan apa yang boleh kamu lakukan.
# Contoh: Admin boleh menghapus data, tetapi user biasa hanya boleh melihat data.

# Examples of Techniques:
# - Hashing: Mengubah password menjadi bentuk hash agar password asli tidak disimpan secara langsung di database. Contoh: SHA-256. Note: Passwords should generally use password-specific hashing algorithms, such as Argon2 or bcrypt.

# - RBAC (Role-Based Access Control): Mengatur hak akses berdasarkan role atau peran, seperti Admin, Staff, dan User.

# - Token: Bukti digital yang digunakan untuk menunjukkan bahwa pengguna telah berhasil login.

# - JWT (JSON Web Token): Salah satu jenis token yang berisi informasi atau klaim yang dapat diverifikasi untuk membantu mengidentifikasi pengguna dan memproses aksesnya.

# Easy Example
# Bayangkan kamu masuk ke perpustakaan:
# 1. Authentication: Petugas memeriksa kartu anggota untuk memastikan siapa kamu.
# 2. Authorization: Petugas menentukan apakah kamu boleh meminjam atau hanya membaca buku di tempat.
# Remember: Authentication = Who are you?
# Authorization = What are you allowed to do?

# @jwt_requiered --> @jwt_required() connects to Authentication because it checks whether the user has a valid JWT token before 
#                    allowing them to access an endpoint.

# CORS and Enviroment Variable
# CORS (Cross-Origin Resource Sharing): Controls which websites are allowed
# to access your API through a browser.

# Environment Variables: Store configuration values outside the source code,
# such as secret keys and database credentials.

# Register → Login → Access works using a token and JWT

# Step 1 — Register (POST /register)

# The user creates an account with a username and password.
# - The server hashes the password before storing it in the database.
# - The original password should not be stored directly.
# - Use a password-hashing algorithm such as Argon2 or bcrypt.

# Step 2 — Login (POST /login)

# The user sends their username and password to the server.
# - The server checks whether the account exists.
# - It verifies the submitted password against the stored password hash.
# - If the credentials are correct, the server generates a JWT token and sends it back.
# This is Authentication, because the server verifies who the user is.

# Step 3 — Access a protected endpoint (GET /profil)

# The user sends the JWT token along with the request.
# - The server validates the token.
# - If the token is valid, @jwt_required() allows the request to proceed.
# - The server can then check the user's role and permissions before allowing a particular action.


# Authentication: Is the token valid, and who is the user?
# Authorization: Is this user allowed to perform this action?

# We will learn how to do this process in meeting7.py