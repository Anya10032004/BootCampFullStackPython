import requests
from enum import unique
from datetime import datetime
import os
from flask import Flask, jsonify, request 
from sqlalchemy import create_engine, String, DateTime, select, text, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, mapped_column, Session, Mapped

#Membuat Flask App
app = Flask(__name__)

# Connect The database
# user: root
# password: no password
# host: localhost(our computer,, kalau berjalan di server, ganti localhost menjadi IP server)
# port: 3306(ini adalah port default, bisa juga diubah sesuai dengan port mysql di komputer anda)
# database:  perpustakaan

#format: mysql+pymysql://user:password@host:port/nama_database
database_url = os.getenv("DATABASE_URL", "mysql+pymysql://root:@localhost:3306/perpustakaan")
engine = create_engine(database_url, pool_pre_ping=True)

# Cek Koneksi database
try:
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
        print("Database connection successful!")

except Exception as error:
    print("Database connection failed:")
    print(error)

# Pembuatan model (Table) NOTES 
class Base(DeclarativeBase): # Ini adalah base class, base class digunakan untuk memberitahu ke sqlalchemy bahwa ini adalah sebuah table/model
    pass

class Penulis(Base): # Ini adalah model untuk tabel notes
    __tablename__ = "Penulis" # name of the table

    # define the columns 
    id_penulis: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nama_penulis: Mapped[str] = mapped_column(String(255))
    email : Mapped[str] = mapped_column(String(255), unique=True)
    create_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)


    def info_penulis(self):
        return {
            "id_penulis": self.id_penulis,
            "nama_penulis": self.nama_penulis,
            "email": self.email,
            "create_at": self.create_at.isoformat() if self.create_at else None,
        }


class Kategori(Base): # Ini adalah model untuk tabel notes
    __tablename__ = "Kategori" # name of the table

    # define the columns 
    id_kategori: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nama_kategori: Mapped[str] = mapped_column(String(255), unique=True)
    deskripsi: Mapped[str] = mapped_column(String(255))

    def info_kategori(self):
        return {
            "id_kategori": self.id_kategori,
            "nama_kategori": self.nama_kategori,
            "deskripsi": self.deskripsi,
        }

class Buku(Base): # Ini adalah model untuk tabel notes
    __tablename__ = "Buku" # name of the table

    # define the columns 
    id_buku: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    judul: Mapped[str] = mapped_column(String(255))
    isbn : Mapped[str] = mapped_column(String(255), unique = True)
    tahun_terbit: Mapped[int] = mapped_column(Integer)
    harga: Mapped[int] = mapped_column(Integer)
    id_penulis: Mapped[int] = mapped_column(ForeignKey('Penulis.id_penulis'))
    id_kategori: Mapped[int] = mapped_column(ForeignKey('Kategori.id_kategori'))
    

    def info_buku(self):
        return {
            "id_buku" : self.id_buku,
            "judul" : self.judul,
            "isbn" : self.isbn,
            "tahun_terbit" : self.tahun_terbit,
            "harga" : self.harga,
            "id_penulis" : self.id_penulis,
            "id_kategori" : self.id_kategori,
        }


Base.metadata.create_all(engine) #Ini adalah perintah untuk membuat tabel di database



@app.route("/", methods=['GET'])
def index():
    return jsonify({
        "message": "Welcome to the API",
        "status": 200,
        "data": None
    })
# -------------------------------------------------------- Penulis ----------------------------------------
# Create
@app.route("/create/penulis", methods = ["POST"])
def create_penulis():

    # Gettting the input from user
    input_data = request.get_json(silent=True) or {}
    nama = input_data.get("nama_penulis")
    email = input_data.get("email")

    # if there is an input that missing, return an error
    if not nama or not email:
        return jsonify({
            "message": "Input data missing",
            "status": 400,
            "data": None
        }), 400

    # Access the database
    with Session(engine) as session:
        # Create the object based on the class note that we created
        lists = session.scalars(select(Penulis).order_by(Penulis.id_penulis)).all()
        
        # check if the email is already exist
        for e in lists:
            if e.email == email:
                return jsonify({
                    "message": "Email already exist",
                    "status": 400,
                    "data": None
                }), 400
        new_note = Penulis(nama_penulis=nama, email=email)
        session.add(new_note)
        session.commit()
        
        return jsonify({
            "message": "Data berhasil ditambahkan",
            "status": 200,
            "data": new_note.info_penulis()
        }), 200

# Read all
@app.route("/read/penulis", methods = ["GET"])
def read_penulis():
    with Session(engine) as session:
        lists = session.scalars(select(Penulis).order_by(Penulis.id_penulis)).all()
        if lists != []:
            return jsonify({
                "message": "Data berhasil diambil",
                "status": 200,
                "data": [note.info_penulis() for note in lists]
            }), 200 
        else:
            return jsonify({
                "message": "Data is empty",
                "status": 200,
                "data": None
            }), 200
    
        
# Read by id
@app.route("/read/penulis/<int:id_penulis>", methods = ["GET"])
def read_penulis_id(id_penulis):
    with Session(engine) as session:
        lists = session.scalars(select(Penulis).order_by(Penulis.id_penulis)).all()
        for note in lists:
            if note.id_penulis == id_penulis:
                return jsonify({
                    "message": "Data berhasil diambil",
                    "status": 200,
                    "data": note.info_penulis()
                }), 200 
        return jsonify({
            "message": "Data tidak ditemukan",
            "status": 404,
            "data": None
        }), 404 
    
    
# Update
@app.route("/update/penulis/<int:id_penulis>", methods = ["PUT"])
def update_penulis(id_penulis):
    new_input = request.get_json(silent = True) or {}
    nama = new_input.get("nama_penulis")
    email = new_input.get("email")
    
    # If there is an input that missing, return an error
    if not nama and not email:
        return jsonify({
            "message": "Input data missing",
            "status": 400,
            "data": None
        }), 400
    
    with Session(engine) as session:
        lists = session.scalars(select(Penulis).order_by(Penulis.id_penulis)).all()
        for note in lists:
            if note.id_penulis == id_penulis:
                if "nama_penulis" in new_input:
                    note.nama_penulis = new_input["nama_penulis"]
                if "email" in new_input:
                    note.email = new_input["email"]
                session.commit()
                return jsonify({
                    "message": "Data berhasil diupdate",
                    "status": 200,
                    "data": note.info_penulis()
                }), 200 
    
        return jsonify({
            "message": "Data tidak ditemukan",
            "status": 404,
            "data": None
        }), 404 
    
# Delete
@app.route("/delete/penulis/<int:id_penulis>", methods = ["DELETE"])
def delete_penulis(id_penulis):
    with Session(engine) as session:
        lists = session.scalars(select(Penulis).order_by(Penulis.id_penulis)).all()
        for note in lists:
            if note.id_penulis == id_penulis:
                session.delete(note)
                session.commit()
                return jsonify({
                    "message": "Data berhasil dihapus",
                    "status": 200,
                    "data": note.info_penulis()
                }), 200 
    
        return jsonify({
            "message": "Data tidak ditemukan",
            "status": 404,
            "data": None
        }), 404 

# -------------------------------------------------------- Kategori ----------------------------------------
# Create
@app.route("/create/kategori", methods = ["POST"])
def create_kategori():
    input_data = request.get_json(silent = True) or {}
    nama = input_data.get("nama_kategori")
    deskripsi = input_data.get("deskripsi")
    
    # If there is an input that missing, return an error
    if not nama and not deskripsi:
        return jsonify({
            "message": "Input data missing",
            "status": 400,
            "data": None
        }), 400
    
    with Session(engine) as session:
        # Create the object based on the class note that we created
        lists = session.scalars(select(Kategori).order_by(Kategori.id_kategori)).all()
        
        # check if the nama is already exist
        for n in lists:
            if n.nama_kategori == nama:
                return jsonify({
                    "message": "Nama already exist",
                    "status": 400,
                    "data": None
                }), 400
        new_note = Kategori(nama_kategori=nama, deskripsi=deskripsi)
        session.add(new_note)
        session.commit()
        
        return jsonify({
            "message": "Data successfully added",
            "status": 200,
            "data": new_note.info_kategori()
        }), 200

# Read all
@app.route("/read/kategori", methods = ["GET"])
def read_kategori():
    with Session(engine) as session:
        lists = session.scalars(select(Kategori).order_by(Kategori.id_kategori)).all()
        return jsonify({
            "message": "Data berhasil diambil",
            "status": 200,
            "data": [note.info_kategori() for note in lists]
        }), 200
# Read by id
@app.route("/read/kategori/<int:id_kategori>", methods = ["GET"])
def read_kategori_id(id_kategori):
    with Session(engine) as session:
        lists = session.scalars(select(Kategori).order_by(Kategori.id_kategori)).all()
        for note in lists:
            if note.id_kategori == id_kategori:
                return jsonify({
                    "message": "Data berhasil diambil",
                    "status": 200,
                    "data": note.info_kategori()
                }), 200 
        return jsonify({
            "message": "Data tidak ditemukan",
            "status": 404,
            "data": None
        }), 404 
# Update
@app.route("/update/kategori/<int:id_kategori>", methods = ["PUT"])
def update_kategori(id_kategori):
    input_data = request.get_json(silent = True) or {}
    name = input_data.get("nama_kategori")
    description = input_data.get("deskripsi")
    
    if not name and not description:
        return jsonify({
            "message": "Input data missing",
            "status": 400,
            "data": None
        }), 400
    
    with Session(engine) as session:
        lists = session.scalars(select(Kategori).order_by(Kategori.id_kategori)).all()
        for note in lists:
            if note.id_kategori == id_kategori:
                if "nama_kategori" in input_data:
                    note.nama_kategori = input_data["nama_kategori"]
                if "deskripsi" in input_data:
                    note.deskripsi = input_data["deskripsi"]
                session.commit()
                return jsonify({
                    "message": "Data berhasil diupdate",
                    "status": 200,
                    "data": note.info_kategori()
                }), 200 
        return jsonify({
            "message": "Data tidak ditemukan",
            "status": 404,
            "data": None
        }), 404 
# Delete
@app.route("/delete/kategori/<int:id_kategori>", methods = ["DELETE"])
def delete_kategori(id_kategori):
    with Session(engine) as session:
        lists = session.scalars(select(Kategori).order_by(Kategori.id_kategori)).all()
        for note in lists:
            if note.id_kategori == id_kategori:
                session.delete(note)
                session.commit()
                return jsonify({
                    "message": "Data berhasil dihapus",
                    "status": 200,
                    "data": note.info_kategori()
                }), 200 
        return jsonify({
            "message": "Data tidak ditemukan",
            "status": 404,
            "data": None
        }), 404 

# -------------------------------------------------------- Buku ----------------------------------------
# Create
@app.route("/create/buku", methods = ["POST"])
def create_buku():
    input_data = request.get_json(silent = True) or {}
    judul = input_data.get("judul")
    isbn = input_data.get("isbn")
    harga_buku = input_data.get("harga")
    tahun_terbit = input_data.get("tahun_terbit")
    id_penulis = input_data.get("id_penulis")
    id_kategori = input_data.get("id_kategori")

    if not judul and not isbn and not harga_buku and not id_penulis and not id_kategori:
        return jsonify({
            "message": "Input data missing",
            "status": 400,
            "data": None
        }), 400
    
    with Session(engine) as session:
        # Create the object based on the class note that we created
        lists = session.scalars(select(Buku).order_by(Buku.id_buku)).all()
        for a in lists:
            if a.judul == judul:
                return jsonify({
                    "message": "Judul sudah terdaftar",
                    "status": 400,
                    "data": None
                }), 400
            if a.isbn == isbn:
                return jsonify({
                    "message": "ISBN already exist",
                    "status": 400,
                    "data": None
                }), 400
        new_buku = Buku(judul=judul, id_penulis=id_penulis, id_kategori=id_kategori, isbn=isbn, harga=harga_buku, tahun_terbit = tahun_terbit)
        session.add(new_buku)
        session.commit()
        return jsonify({
            "message": "Data successfully added",
            "status": 200,
            "data": new_buku.info_buku()
        }), 200

# Read all
@app.route("/read/buku", methods = ["GET"])
def read_buku():
    penulis_id = request.args.get("penulis_id", type = int)
    kategori_id = request.args.get("kategori_id", type = int)
    judul = request.args.get("q")

    with Session(engine) as session:
        lists = session.scalars(select(Buku).order_by(Buku.id_buku)).all()
        if penulis_id is not None:
            for note in lists:
                if note.id_penulis == penulis_id:
                    return jsonify({
                        "message": "Data successfully retrived",
                        "status": 200,
                        "data": [note.info_buku() for note in lists if note.id_penulis == penulis_id]
                    }), 200
            return jsonify({
                "message": f"Data not found with the penulis id = {penulis_id}",
                "status": 404,
                 "data": None
            }), 404
        elif kategori_id is not None:
            for note in lists:
                if note.id_kategori == kategori_id:
                    return jsonify({
                        "message": "Data successfully retrived",
                        "status": 200,
                        "data": [note.info_buku() for note in lists if note.id_kategori == kategori_id]
                    }), 200
            return jsonify({
                "message": f"Data not found with the kategori_id = {kategori_id}",
                "status": 404,
                "data": None
            }), 404
        elif judul is not None:
            for note in lists:
                if note.judul == judul:
                    return jsonify({
                        "message": "Data successfully retrived",
                        "status": 200,
                        "data": [note.info_buku() for note in lists if note.judul.lower() == judul.lower()]
                    }), 200
            return jsonify({
                "message": f"Data not found with the judul = {judul}",
                "status": 404,
                "data": None
            }), 404
            
        else:
            return jsonify({
                "message": "Data successfully retrived",
                "status": 200,
                "data": [note.info_buku() for note in lists]
                }), 200
    return jsonify({
            "message": "Data not found",
            "status": 404,
            "data": None
        }), 404 
# Read by id
@app.route("/read/buku/<int:id_buku>", methods = ["GET"])
def read_buku_id(id_buku):
    with Session(engine) as session:
        lists = session.scalars(select(Buku).order_by(Buku.id_buku)).all()
        for a in lists:
            if a.id_buku == id_buku:
                return jsonify({
                    "message": "Data successfully retrived",
                    "status": 200,
                    "data": a.info_buku()
                }), 200 
        return jsonify({
            "message": "Data not found",
            "status": 404,
            "data": None
        }), 404 
# Update
@app.route("/update/buku/<int:id_buku>", methods = ["PUT"])
def update_buku(id_buku):
    input_data = request.get_json(silent = True) or {}
    judul = input_data.get("judul")
    penulis = input_data.get("penulis")
    kategori = input_data.get("kategori")
    isbn = input_data.get("isbn")
    jumlah_buku = input_data.get("jumlah_buku")
    tahun_terbit = input_data.get("tahun_terbit")
    
    if not judul and not penulis and not kategori and not isbn and not jumlah_buku:
        return jsonify({
            "message": "Input data missing",
            "status": 400,
            "data": None
        }), 400
    
    with Session(engine) as session:
        # Create the object based on the class note that we created
        lists = session.scalars(select(Buku).order_by(Buku.id_buku)).all()
        for a in lists:
            if a.id_buku == id_buku:
                if "judul" in input_data:
                    a.judul = input_data["judul"]
                if "penulis" in input_data:
                    a.penulis = input_data["penulis"]
                if "kategori" in input_data:
                    a.kategori = input_data["kategori"]
                if "isbn" in input_data:
                    a.isbn = input_data["isbn"]
                if "jumlah_buku" in input_data:
                    a.jumlah_buku = input_data["jumlah_buku"]
                if "tahun_terbit" in input_data:
                    a.tahun_tebrit = input_data["tahun_terbit"]
                session.commit()
                return jsonify({
                    "message": "Data successfully updated",
                    "status": 200,
                    "data": a.info_buku()
                }), 200 
        return jsonify({
            "message": "Data not found",
            "status": 404,
            "data": None
        }), 404 
# Delete
@app.route("/delete/buku/<int:id_buku>", methods = ["DELETE"])
def delete_buku(id_buku):
    with Session(engine) as session:
        lists = session.scalars(select(Buku).order_by(Buku.id_buku)).all()
        for a in lists:
            if a.id_buku == id_buku:
                session.delete(a)
                session.commit()
                return jsonify({
                    "message": "Data successfully deleted",
                    "status": 200,
                    "data": a.info_buku()
                }), 200 
        return jsonify({
            "message": "Data not found",
            "status": 404,
            "data": None
        }), 404 


if __name__ == "__main__":
    app.run(debug=True)

