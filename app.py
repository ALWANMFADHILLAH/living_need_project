from flask import Flask, redirect, url_for, render_template, request, jsonify, session
from pymongo import MongoClient
import requests
from datetime import datetime
from bson import ObjectId
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME = os.environ.get("DB_NAME")

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]

app = Flask(__name__)

client=MongoClient('mongodb+srv://jaki:123@cluster0.2jeez0y.mongodb.net/?retryWrites=true&w=majority')
mydb = client.data
mycol = mydb.bas

app.secret_key = "iasjda8hd8qwhouhsaoduhoauihdouh"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == 'admin':
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')
    

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


@app.route('/dasboard')
def dashboard():
    return render_template('AdminDasboard.html')

@app.route('/adminproduk')
def adminproduk():
    return render_template('AdminProduk.html')

@app.route('/produk')
def produk():
    return render_template('Produk.html')

@app.route('/cemilan')
def cemilan():
    return render_template('Kategori1.html')

@app.route('/cereal')
def cereal():
    return render_template('Kategori2.html')

@app.route('/snack')
def snack():
    return render_template('Kategori.html')

@app.route('/minuman')
def minuman():
    return render_template('Kategori4.html')

@app.route('/cek')
def cek():
    return render_template('BagianDetail.html')

@app.route('/about')
def about():
    return render_template('Tentang.html')

@app.route('/kontak')
def kontak():
    return render_template('Kontak.html')

@app.route('/pesan')
def pesan():
    return render_template('AdminPesanan.html')

@app.route('/item')
def item():
    return render_template('AdminProduk.html')

@app.route('/pesanProduk')
def pesanProduk():
    return render_template('PesanProduk.html')

@app.route('/dasboardproduk',methods=['GET'])
def dasboardproduk():
    data = mydb.base.find({})

    return render_template('AdminProduk.html',data=data)

@app.route('/tambahProduk')
def tambahProduk():
    return render_template('TambahProduk.html')

@app.route('/dpesan')
def dpesan():
    return render_template('Detail_Pemesanan.html')

@app.route('/add', methods=['POST'])
def tambah():
    namaitempesan=request.form.get('namaitempesan')
    jumlahitempesan=request.form.get('jumlahitempesan')
    alamatpesan=request.form.get('alamatpesan')
    price=request.form.get('price')
    print(namaitempesan,jumlahitempesan,alamatpesan,price)

    my_dict = {'namaitempesan': namaitempesan,
               'jumlahitempesan': jumlahitempesan,
               'alamatpesan': alamatpesan,
                'price': price
                }
    
    mycol.insert_one(my_dict)
    return render_template('TambahProduk.html')

if __name__ == '__main__':  
    app.run('0.0.0.0', port=5000, debug=True)

