# ============================================================
#  PRAKTIK PERTEMUAN 7 — Autentikasi & Keamanan API
#  Register, Login (JWT), & Protected Route
#  Course : Python Fullstack AI Engineer — Kelas Santai
#  Cara menjalankan :
#    1) Aktifkan venv
#    2) pip install flask flask-sqlalchemy flask-jwt-extended werkzeug flask-cors python-dotenv PyMsql
#    3) python praktik_pertemuan_07.py
#    4) Uji dengan Postman / Thunder Client (base: http://127.0.0.1:5000)
# ------------------------------------------------------------
#  IDE INTI:
#   - Password TIDAK PERNAH disimpan polos -> disimpan sebagai HASH.
#   - Setelah login benar, server memberi TOKEN (JWT).
#   - Endpoint rahasia hanya bisa diakses jika membawa token valid.
# ------------------------------------------------------------
#  ALUR:  register -> login (dapat token) -> akses /profil pakai token
# ============================================================

from datetime import datetime
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase # Untuk Mengenerate Sebuah Database dari Code 
import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
)
from flask_cors import CORS


#Libdary Untuk Membaca Data .env nya 
from dotenv import load_dotenv

# Memuat konfigurasi rahasia dari file .env (JANGAN commit .env ke GitHub!)
load_dotenv()

app = Flask(__name__)
CORS(app)   # izinkan frontend (domain lain) mengakses API ini

app.json.sort_keys = False  # Agar urutan key JSON sesuai dengan urutan dictionary
# Koneksi ke MySQL (port: 3306) menggunakan driver PyMySQL
# Format : mysql+pymysql://user:password@host:port/nama_database

#DATABASE_URL = os.getenv(
#    "DATABASE_URL","mysql+pymysql://root:@localhost:3306/fullstack" 
#)

# String koneksi gabungan (cara paling aman agar .env terbaca)
database_url = f"mysql+pymysql://{os.getenv('DBUSER')}:@{os.getenv('DBHOST')}:{os.getenv('DBPORT')}/{os.getenv('DBNAME')}"
#Mengambil data dari .env
#koneksi ke Databae
app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {"pool_pre_ping": True}

# Config Model Database SQLAlchemy
class Base(DeclarativeBase):
    pass

# Kunci rahasia untuk menandatangani token. Diambil dari .env.
# Nilai default hanya untuk jaga-jaga saat belajar.
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "rahasia-kelas-santai")


db = SQLAlchemy(app, model_class=Base) #Membuat Databas dari Class Base
jwt = JWTManager(app) #Inisialisasi Library

# ------------------------------------------------------------
# MODEL — User
# ------------------------------------------------------------
class User(db.Model):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    # PENTING: kolom ini menyimpan HASH, bukan password asli.
    password_hash: Mapped[str] = mapped_column(String(256), nullable=False)
    nama_lengkap: Mapped[str] = mapped_column(String(100), nullable=False)
    nomor_hp: Mapped[str] = mapped_column(String(15), nullable=False)
    alamat: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    # Role == "Admin", "Staff"
    

    def info(self):
        return {
            "id": self.id,
            "username": self.username,
            "nama_lengkap": self.nama_lengkap,
            "nomor_hp": self.nomor_hp,
            "alamat": self.alamat,
            "email": self.email,
            
        }

class Kategori(db.Model):
    __tablename__ = "kategori"
    idKategori: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    namaKategori: Mapped[str] = mapped_column(String(100))
    deskripsi: Mapped[str] = mapped_column(String(255))
    createdAt: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updatedAt: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)

    def info(self):
        return {
            "idKategori": self.idKategori,
            "namaKategori": self.namaKategori,
            "deskripsi": self.deskripsi,
            "createdAt": self.createdAt.isoformat() if self.createdAt else None,
            "updatedAt": self.updatedAt.isoformat() if self.updatedAt else None,
        }


# ------------------------------------------------------------
# REGISTER — membuat akun baru   (POST /register)
# ------------------------------------------------------------
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json() or {}  # MEnyimoan data inputan menjadi dixctionary 
    username = data.get("username") #Mengambil Data Username 
    password = data.get("password") #Mengambil Data Password
    alamat = data.get("alamat")
    nomor_hp = data.get("nomor_hp")
    email = data.get("email")
    nama_lengkap = data.get("nama_lengkap")

    # Role ==

    if not username or not password or not alamat or not nomor_hp or not email or not nama_lengkap: #Memastikan Data Ada
        return jsonify({"error": "username & password wajib diisi"}), 400

    # Cek apakah username sudah dipakai
    if User.query.filter_by(username=username).first():
        return jsonify({"error": "username sudah terpakai"}), 409

    # HASH password sebelum disimpan -> tidak bisa dibaca balik.
    hashed = generate_password_hash(password)  # String Hash --> Untuk Menyimpan Password
    print("Password Hash : "+hashed)   

    # ada beberapa conflix antara pengecekan variabel
    user = User(username=username, password_hash=hashed, nama_lengkap=nama_lengkap, nomor_hp=nomor_hp, alamat=alamat, email=email) #Menyimpan Data ke Database
    db.session.add(user) #Menambahkan Data ke Database
    db.session.commit() #Menyimpan Data ke Database
    return jsonify({"pesan": f"User {username} berhasil dibuat"}), 201


# ------------------------------------------------------------
# LOGIN — verifikasi & beri token   (POST /login)
# ------------------------------------------------------------
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json() or {}
    username = data.get("username")
    password = data.get("password")

    #Query untuk mengambil berdasarkan user 
    user = User.query.filter_by(username=username).first()
    print(user)

    # Bentuk qouerynya yaitu : Select * from User Where username = ? AND password_hash = ?
    #user = User.query.filter_by(username=username, password_hash=password).first()
    
    # check_password_hash membandingkan password polos dengan hash
    if user is None or not check_password_hash(user.password_hash, password):
        # Sengaja pesan umum: jangan bocorkan mana yang salah.
        return jsonify({"error": "username atau password salah"}), 401


    # Login benar -> buat token yang menyimpan identitas user.
    token = create_access_token(
        identity=str(user.id),
        additional_claims={
            "id_user" : user.id,
            "username" : user.username,
            "nama_lengkap" : user.nama_lengkap,
            "nomor_hp" : user.nomor_hp,
            "alamat" : user.alamat,
            "email" : user.email,
            #"role" : user.role,
        }, 
        )
    return jsonify({"access_token": token}), 200


# ------------------------------------------------------------
# PROTECTED — hanya untuk yang membawa token valid  (GET /profil)
# ------------------------------------------------------------
# @jwt_required() memaksa request menyertakan header:
#   Authorization: Bearer <token> 
@app.route("/create_book", methods=["POST"])
@jwt_required()
def create_book():
    tokenAkses = get_jwt()
    print(tokenAkses)
    role = tokenAkses.get("role")
    if role != "Admin":
        return jsonify({"error": "Anda tidak memiliki akses"}), 401

    # Lanjutkan untuk mengisi 
    data = request.get_json() or {}
    return jsonify({"pesan": "Buku berhasil dibuat"}), 201

@app.route("/profil", methods=["GET"])
@jwt_required()  #Fungsi Untuk Mengaktifkan JWT atau sebagai verifikasi token / Middleware 
def profil():
  
    tokenAkses = get_jwt()   # Mengambil Semua JWT

    print(tokenAkses) 

    nama_lengkap = tokenAkses.get("nama_lengkap")
    nomor_hp = tokenAkses.get("nomor_hp")
    alamat = tokenAkses.get("alamat")
    email = tokenAkses.get("email")

    id_user = tokenAkses.get("id_user")
    print("Nama Lengkap : "+nama_lengkap)
    print("Nomor HP : "+nomor_hp)
    print("Alamat : "+alamat)
    print("Email : "+email)
    # Ambil Data dari Token JWT
    user = db.session.get(User, int(id_user))   
    return jsonify({"id": user.id, "username": user.username, "nama_lengkap": user.nama_lengkap, "nomor_hp": user.nomor_hp, "alamat": user.alamat, "email": user.email}), 200


# ------------------------------------------------------------
# PUBLIC — bebas diakses siapa saja (pembanding)  (GET /)
# ------------------------------------------------------------
@app.route("/")
def beranda():
    return jsonify({
        "pesan": "API Auth Kelas Santai",
        "alur": ["POST /register", "POST /login -> token",
                 "GET /profil (pakai token)"],
    })


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)


# ============================================================
# CARA MENGUJI (Postman / Thunder Client)
# ------------------------------------------------------------
#  1) REGISTER
#     POST /register
#     Body (JSON): {"username": "budi", "password": "rahasia123"}
#     -> 201 Created
#
#  2) LOGIN
#     POST /login
#     Body (JSON): {"username": "budi", "password": "rahasia123"}
#     -> 200 + {"access_token": "eyJhbGciOi..."}
#        SALIN token tersebut.
#
#  3) AKSES PROTECTED ROUTE
#     GET /profil
#     Header: Authorization: Bearer <token yang tadi disalin>
#     -> 200 + data user
#     (Tanpa token / token salah -> 401 Unauthorized)
# ------------------------------------------------------------
# CONTOH FILE .env (buat file bernama ".env", JANGAN di-commit):
#     JWT_SECRET_KEY=ganti-dengan-kunci-acak-yang-panjang
# Dan tambahkan ke .gitignore:
#     .env
#     *.db
#     venv/
# ------------------------------------------------------------
# TUGAS MANDIRI (kembangkan api_buku_db.py -> api_buku_auth.py)
# ------------------------------------------------------------
#  Amankan CRUD buku (Pertemuan 6) dengan autentikasi:
#    - Tambah model User + endpoint /register & /login (JWT)
#    - Lindungi endpoint yang MENGUBAH data (POST/PUT/DELETE /buku)
#      dengan @jwt_required(); GET boleh tetap publik
#    - Simpan JWT_SECRET_KEY di .env (pakai python-dotenv)
#    - Aktifkan CORS
#    - requirements.txt: flask, flask-sqlalchemy, flask-jwt-extended,
#      werkzeug, flask-cors, python-dotenv
#  Kumpulkan folder/zip atau link GitHub via LMS sebelum Pertemuan 8.
#  (JANGAN sertakan file .env di dalam kumpulan!)
# ============================================================
