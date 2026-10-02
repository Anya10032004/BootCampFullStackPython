from flask import Flask, jsonify    

# Jadi Flask itu adalah framework untuk memudahkan kita membuat web dan REST API
# jsonify --> library untuk mengonversi dictionary ke JSON
# JSON adalah format pertukaran data yang paling umum digunakan

app = Flask(__name__) # Setingan utama web / object utama flask

# @app.route adalah syntax untuk memberi tahu kepada server bahwa ketika ada request 
#                   yang masuk dengan path tersebut, maka jalankan fungsi yang dibawahnya
# @app.route untuk per request 
# @app.route hanya bisa menerima satu HTTP method

@app.route('/') # '/' adalah root URL, atau alamat utama web 
                # jadi ketika user mengakses alamat http://127.0.0.1:5000/ --> maka akan menjalankan fungsi index()

def index(): 
    return "Hello World! Ini adalah REST API sederhana"


@app.route('/user/get-user') # '/user/get-user' adalah URL yang akan diakses 
                             # jadi ketika user mengakses alamat http://127.0.0.1:5000/user/get-user
                             # maka akan menjalankan fungsi getUser()
def getUser(): 
    return jsonify(
        {"statusCode": 200,
         "message": "sukses",
         "data":{
            "name": "Anya",
            "email": "[EMAIL_ADDRESS]"
         }
        })


# Dynamic Route --> variable di dalam url
# /user/<name> --> ini maksudnya adalah variable name yang bisa diisi apa saja 
# /user/<name> bisa menjadi /user/Anya, /user/Budi, /user/Cici
@app.route('/user/get-user/<name>')
def getUserName(name):
        return jsonify(
            {"statusCode": 200,
             "message": "sukses",
             "data":{
                "name": name,
                "email": "[EMAIL_ADDRESS]"
             }
            })



if __name__ == "__main__": # Menjalankan framework flask(menjalankan program)
    app.run(debug=True) # Menjalankan web (Debug mode akan menampilkan error di browser)


# GAMBARAN 
# app = Flask(__name__)  --> Beggining of the program
# if __name__ == "__main__": app.run(debug=True) --> The end of the program 
#                                                    jadi kalau program diakhiri dengan ini, 
#                                                    maka program tersebut sudah selesai 

