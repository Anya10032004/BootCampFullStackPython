from datetime import datetime
from flask import Flask, jsonify, request
from sqlalchemy import create_engine, String, DateTime, text
from sqlalchemy.orm import DeclarativeBase, mapped_column, Session, Mapped
from sqlalchemy.exc import IntegrityError

# app setup
app = Flask(__name__)

# database connection string
DATABASE_URL = "mysql+pymysql://root:@localhost:3306/perpustakaan_orm"  # → database harus sudah ada
engine = create_engine(DATABASE_URL, pool_pre_ping=True)


# =========================================================================
#             MODEL (TABLE SCHEMA) — PENULIS
# =========================================================================

class Base(DeclarativeBase):
    pass

class Penulis(Base):
    __tablename__ = "penulis"

    id_penulis: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nama_penulis: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255), unique=True)
    create_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    def info(self):
        return {
            "id_penulis": self.id_penulis,
            "nama_penulis": self.nama_penulis,
            "email": self.email,
            "create_at": self.create_at.isoformat() if self.create_at else None,
        }


# =========================================================================
#       TUTORIAL: CREATE DATABASE & TABLE (satu kali jalan)
# =========================================================================

@app.route("/buat-tabel-penulis", methods=["GET"])
def buat_tabel():
    try:
        Base.metadata.create_all(engine)  # → bikin tabel penulis
        return jsonify({
            "status": 200,
            "message": "Tabel penulis berhasil dibuat/sudah ada.",
            "data": None
        })
    except Exception as e:
        return jsonify({
            "status": 500,
            "message": f"Error saat membuat tabel: {str(e)}",
            "data": None
        }), 500


# =========================================================================
#                    API: CREATE PENULIS (POST)
# =========================================================================

@app.route("/api/penulis", methods=["POST"])
def create_penulis():
    data = request.get_json(silent=True) or {}
    nama_penulis = data.get("nama_penulis")
    email = data.get("email")

    if not nama_penulis or not email:
        return jsonify({
            "status": 400,
            "message": "nama_penulis dan email wajib diisi.",
            "data": None
        }), 400

    with Session(engine) as session:
        try:
            # 1. Cek apakah email sudah ada (supaya sesuai unique constraint)
            stmt = select(Penulis).where(Penulis.email == email)
            if session.execute(stmt).scalar_one_or_none():
                return jsonify({
                    "status": 409,  # Conflict
                    "message": "Email sudah terdaftar.",
                    "data": None
                }), 409

            # 2. Buat object baru lalu simpan
            new_penulis = Penulis(
                nama_penulis=nama_penulis,
                email=email
            )
            session.add(new_penulis)
            session.commit()

            return jsonify({
                "status": 200,
                "message": "Penulis berhasil ditambahkan.",
                "data": new_penulis.info()
            })

        except IntegrityError:
            session.rollback()
            return jsonify({
                "status": 409,
                "message": "Email sudah digunakan ( IntegrityError ).",
                "data": None
            }), 409
        except Exception as e:
            session.rollback()
            return jsonify({
                "status": 500,
                "message": f"Error internal: {str(e)}",
                "data": None
            }), 500


if __name__ == "__main__":
    # Saat run pertama kali, lebih baik hapus dulu baris app.run
    # Lalu jalankan di terminal: python nama_file.py
    # Lalu akses: http://[IP_ADDRESS]/buat-tabel-penulis
    # Setelah tabel muncul, baru uncomment app.run()
    # app.run(debug=True)
    pas
