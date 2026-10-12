from datetime import datetime # Ini digunakan untuk mengambil waktu sekarang atau memanipulasiwaktu 
import os # Untuk membaca enviroment

from flask import Flask, jsonify, request # Ini gunanya untuk framework Web untuk membuat API REST

# Ini adalah sebuah ORM untuk terhubung ke database
# pyrefly: ignore [missing-import]
from sqlalchemy import create_engine, String, DateTime, select, text
from sqlalchemy.orm import DeclarativeBase, mapped_column, Session, Mapped

# Pembuatan Flask App
app = Flask(__name__)

# Koneksi mySQL(port 3307) menggunakan driver PyMySQL
# format: mysql +pymysql://user:password@host:port/nama_database
# user: root
# password: no password
# host: localhost(our computer,, kalau berjalan di server, ganti localhost menjadi IP server)
# port: 3307(ini adalah port default, bisa juga diubah sesuai dengan port mysql di komputer anda)
# database:  testing-db (nama databasenya adalah testing-db)
# ------------------------------------------------------------------------
DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:@localhost:3306/testing-db") # Ini untuk menghubungkan ke database mysql 
engine = create_engine(DATABASE_URL, pool_pre_ping=True) # Ini gunanya untuk mengecek apakah database sudah terhubung atau belum

# Cek Koneksi database
try:
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
        print("Database connection successful!")

except Exception as error:
    print("Database connection failed:")
    print(error)

# Pembuatan model (Table) NOTES 
class Base(DeclarativeBase): # Ini adalah base class untuk membuat model 
    pass

class Note(Base): # Ini adalah model untuk tabel notes
    __tablename__ = "notes" # name of the table

    # define the columns 
    id_note: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    deskripsi: Mapped[str] = mapped_column(String(255))
    status: Mapped[str] = mapped_column(String(20), default="TODO")
    create_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    update_at: Mapped[datetime | None] = mapped_column(
        DateTime, onupdate=datetime.now
    )

    def info(self):
        return {
            "id_note": self.id_note,
            "deskripsi": self.deskripsi,
            "status": self.status,
            "create_at": self.create_at.isoformat() if self.create_at else None,
            "update_at": self.update_at.isoformat() if self.update_at else None,
        }
# Let's try to make the user table, first define the class
class User(Base): # Ini adalah model untuk tabel user
    __tablename__ = "users_buatanORM"

    # define the column
    id_user : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username : Mapped[str] = mapped_column(String(255))
    email : Mapped[str] = mapped_column(String(255))
    password : Mapped[str] = mapped_column(String(255))
    create_at : Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    update_at : Mapped[datetime | None] = mapped_column(DateTime, onupdate=datetime.now)

    def info(self):
        return {
            "id_user": self.id_user,
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "create_at": self.create_at.isoformat() if self.create_at else None,
            "update_at": self.update_at.isoformat() if self.update_at else None,
        }   

# Membuat tabel otomatis apabila belum ada(membuat object from Noet class)
Base.metadata.create_all(engine) # Ini adalah perintah untuk membuat tabel di database


# ==================================== API(For the Note Table, for the user table we need to make another REST API ) ====================================

@app.route("/", methods=["GET"]) # Ini adalah perintah untuk menampilkan halaman utama
def main(): # Ini adalah fungsi untuk menampilkan halaman utama
    return "Ini Untuk API Note"

# CREATE DATA
# CREATE NOTE ->POST /create_note

@app.route("/create_note", methods=["POST"]) # Ini adalah perintah untuk membuat data
def create_note():
    # ambil data dari user
    data = request.get_json(silent=True) or {}
    deskripsi = data.get("deskripsi")
    status = data.get("status", "TODO")
    
    # validasi input
    if not deskripsi:
        return jsonify(
            {
                "status": 400,
                "message": "Deskripsi harus diisi!",
                "data": None,
            }
        ), 400
        
    # simpan data ke database (menggunakan Session)
    with Session(engine) as session:
        new_note = Note(deskripsi=deskripsi, status=data.get("status", "TODO"))
        session.add(new_note)
        session.commit()
        
        return jsonify(
            {
                "status": 200,
                "message": "Data berhasil ditambahkan",
                "data": new_note.info(),
            }
        ), 200


# READ DATA
# GET BY ID -> GET /read_note/<int:note_id>

@app.route("/read_note/<int:note_id>", methods=["GET"]) # Ini adalah perintah untuk mengambil data berdasarkan primary key
def read_note(note_id): # Ini adalah fungsi untuk mengambil data berdasarkan primary key
    with Session(engine) as session:
        # ambil data berdasarkan primary key
        note = session.get(Note, note_id)
        
        if not note:
            return jsonify(
                {
                    "status": 404,
                    "message": "Data tidak ditemukan",
                    "data": None,
                }
            ), 404
        
        return jsonify(
            {
                "status": 200,
                "message": "Data berhasil diambil",
                "data": note.info(),
            }
        ), 200


# GET ALL DATA -> GET /read_note_list
@app.route("/read_note_list", methods=["GET"]) # Ini adalah perintah untuk mengambil data berdasarkan primary key
def read_note_list(): # Ini adalah fungsi untuk mengambil data berdasarkan primary key
    with Session(engine) as session:
        # select data menggunakan SQLAlchemy core
        notes = session.scalars(select(Note).order_by(Note.id_note)).all()
        
        return jsonify(
            {
                "status": 200,
                "message": "Data berhasil diambil",
                "data": [note.info() for note in notes],
            }
        ), 200


# UPDATE DATA
# UPDATE NOTE -> PUT /update_note/<int:note_id>

@app.route("/update_note/<int:note_id>", methods=["PUT"]) # Ini adalah perintah untuk mengupdate data berdasarkan primary key
def update_note(note_id): # Ini adalah fungsi untuk mengupdate data berdasarkan primary key
    # ambil data yang diupdate
    new_input = request.get_json() or {}
    
    with Session(engine) as session:
        note = session.get(Note, note_id)
        
        if not note:
            return jsonify(
                {
                    "status": 404,
                    "message": "Data tidak ditemukan",
                    "data": None,
                }
            ), 404
        
        # update field jika dikirim
        if "deskripsi" in new_input:
            note.deskripsi = new_input["deskripsi"]
        if "status" in new_input:
            note.status = new_input["status"]
        
        session.commit()
        
        return jsonify(
            {
                "status": 200,
                "message": "Data berhasil diupdate",
                "data": note.info(),
            }
        ), 200


# DELETE DATA
# DELETE NOTE -> DELETE /delete_note/<int:note_id>

@app.route("/delete_note/<int:note_id>", methods=["DELETE"]) # Ini adalah perintah untuk menghapus data berdasarkan primary key
def delete_note(note_id): # Ini adalah fungsi untuk menghapus data berdasarkan primary key
    with Session(engine) as session:
        note = session.get(Note, note_id)
        
        if not note:
            return jsonify(
                {
                    "status": 404,
                    "message": "Data tidak ditemukan",
                    "data": None,
                }
            ), 404
        
        # delete data
        session.delete(note)
        session.commit()
        
        return jsonify(
            {
                "status": 200,
                "message": "Data berhasil dihapus",
                "data": note.info(),
            }
        ), 200


if __name__ == "__main__":
    app.run(debug=True)


# NOTEEE PENTING:
# Jadi kalau sesi kemaren kita belajar REST API lalu masukin datanya ke json sekarang kita belajar database 
# jadi di sesi ini, kita belajar cara melakukan hal yang sama, tetapi kita tidak akan masukin datanya ke json file tetapi
# ke mysql file.
# Kita juga akan belajar cara:
#  - set up database dan tabble di mysql
#  - membuat tabble lalu masukin ke mysql lewat python(pakai ORM)

# Struktur folder yang disarankan:
# my_project/
#   app.py
#       Menjalankan Flask app dan mendaftarkan endpoint.
#   database.py
#       Mengatur koneksi database, engine, dan Base SQLAlchemy.
#   models/
#       Menyimpan definisi tabel database.
#       note.py — model Note
#       user.py — model User
#   routes/
#       Menyimpan endpoint REST API.
#       note_routes.py — API Note
#       user_routes.py — API User
#   requirements.txt — daftar library Python