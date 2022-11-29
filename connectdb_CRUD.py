from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
import json
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PORT'] = 4306
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'data harga properti'
 
mysql = MySQL(app) #connect to db

@app.route("/")
def form():
    cursor = mysql.connection.cursor()
    cursor.execute("select * from rumah123_housing_data limit 2")
    result = cursor.fetchall()
    return jsonify(result)

#CRUD
@app.route("/CRUD", methods = ['POST', 'GET', 'PUT', 'DELETE'])
def CRUD():
    print(request.method)
    if(request.method=='GET'):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM rumah123_housing_data LIMIT 3") #get alias select
        result = cursor.fetchall()
        return jsonify(result)
    if(request.method=='POST'):
        cursor = mysql.connection.cursor()
        querys ="""INSERT INTO data_kost VALUES('Kost Berkah', 'Jalan Berkah No.28, Menteng, Jakarta', 'Menteng, Kota Jakarta Pusat', 'Menteng', 'Kota Jakarta Pusat', -6.2031310500000000, 106.82005333640619, 'Kost Putri', 'Standard', 20.0, 'Kursi, TV', 'Shower', True, 'CCTV, Dapur, Area Parkir', 3000000)"""
        cursor.execute(querys) #post alias insert into
        mysql.connection.commit()
        cursor.close()
        return f"Data Added!!"
    if(request.method=='PUT'):
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE rumah123_housing_data SET num_bedroom = 4 WHERE property_title = 'Rumah Mewah 2 Lantai Termurah Di Jabodetabek' ") #put alias update, set lalaala
        mysql.connection.commit()
        cursor.close()
        return f"Data Updated!!"
    if(request.method=='DELETE'):
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM data_kost WHERE nama_kost = 'Moona Kost & Homestay'") #delete alias delete from lalaala where
        mysql.connection.commit()
        cursor.close()
        return f"Data Deleted!!"

#(nama_kost, alamat, daerah, kecamatan, kota, latitude, longitude, tipe_kost, tipe_kamar, luas_kamar, fasilitas_kamar, fasilitas_kamar_mandi, isKamarMandiDalam, fasilitas_gedung, harga_per_bulan) 