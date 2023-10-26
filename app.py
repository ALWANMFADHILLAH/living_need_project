from flask import Flask, redirect, url_for, render_template, request, jsonify, session
from pymongo import MongoClient
import requests
from datetime import datetime
from bson import ObjectId

app = Flask(__name__)

client=MongoClient('mongodb+srv://jaki:123@cluster0.2jeez0y.mongodb.net/?retryWrites=true&w=majority')
mydb = client.data
mycol = mydb.base

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


@app.route('/dasboard',methods=['GET'])
def dashboard():
    data = mydb.base.find({})

    return render_template('AdminDasboard.html',data=data)

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

@app.route('/pesanProduk')
def pesanProduk():
    return render_template('PesanProduk.html')

@app.route('/kontak')
def kontak():
    return render_template('Kontak.html')

@app.route('/delete', methods=['GET'])
def delete():
    id=request.args.get('_id')
    mycol.delete_one({'_id':ObjectId(id)})
    data=list(mydb.base.find({}))
    return render_template('AdminDasboard.html',data=data)

@app.route('/pesanProduk', methods=['POST'])
def tambah():
    nama_pemesan=request.form.get('nama_pemesan')
    namaitempesan=request.form.get('namaitempesan')
    jumlahitempesan=request.form.get('jumlahitempesan')
    alamatpesan=request.form.get('alamatpesan')
    print(nama_pemesan,namaitempesan,jumlahitempesan,alamatpesan)

    my_dict = {'nama_pemesan': nama_pemesan,
               'namaitempesan': namaitempesan,
               'jumlahitempesan': jumlahitempesan,
               'alamatpesan':alamatpesan}
    
    mycol.insert_one(my_dict)
    return render_template('PesanProduk.html')

if __name__ == '__main__':  
    app.run('0.0.0.0', port=5000, debug=True)

