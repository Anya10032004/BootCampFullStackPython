from flask import Flask,jsonify

app = Flask(__name__)

# Pesan sambutan:
@app.route('/', methods = ['GET'])
def sambutan():
    return "welcome to my API"
# Biodata
@app.route('/biodata', methods = ['GET'])
def biodata():
    return jsonify(
        {"Nama": "Anya",
         "Kota": "Jakarta",
         "Hobi": ["membaca", "berenang"]
        })

# Sapaan Personal:
@app.route('/halo/<name>', methods = ['GET'])
def sapa(name):
    return f"Hello {name}! Welcome to my API"

# Hitung Tahun
@app.route('/umur/<int:tahun>', methods = ['GET'])
def hitung_umur(tahun):
    return f"Aku berumur {2026 - tahun}"


if __name__ == "__main__": 
    app.run(debug=True)

