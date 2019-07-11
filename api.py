from __future__ import print_function
import mysql.connector
from flask import Flask, render_template,request,redirect,url_for,send_file



app = Flask(__name__)
app.secret_key = "sysall14"

@app.route("/")
def main():
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="ade",
        passwd="Jenkins0",
        database="achat_credit"
    )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM `produits`")
    data = mycursor.fetchall()

    return render_template('index.html',data=data)

@app.route("/television")
def mainTv():
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="ade",
        passwd="Jenkins0",
        database="achat_credit"
    )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM `produits` WHERE `categorie`='tv' ")
    data = mycursor.fetchall()

    return render_template('index.html',data=data)

@app.route("/frigos")
def mainFrigos():
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="ade",
        passwd="Jenkins0",
        database="achat_credit"
    )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM `produits` WHERE `categorie`='frigos'")
    data = mycursor.fetchall()

    return render_template('index.html',data=data)

@app.route("/climatiseur")
def mainClimatiseur():
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="ade",
        passwd="Jenkins0",
        database="achat_credit"
    )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM `produits` WHERE `categorie` = 'climatiseur'")
    data = mycursor.fetchall()

    return render_template('index.html',data=data)

@app.route("/cuisiniere")
def mainCuisinere():
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="ade",
        passwd="Jenkins0",
        database="achat_credit"
    )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM `produits` WHERE `categorie`='cuisiniere'")
    data = mycursor.fetchall()

    return render_template('index.html',data=data)


@app.route('/index/')
def index():
    productId = request.args.get('productId')
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="ade",
        passwd="Jenkins0",
        database="achat_credit"
    )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM `produits` WHERE id="+productId)
    data = mycursor.fetchone()

    return render_template('product.html', data=data)

@app.route('/download')
def down():
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="ade",
        passwd="Jenkins0",
        database="achat_credit"
    )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM `produits`")
    data = mycursor.fetchall()

    return render_template('download.html', data=data)

@app.route('/upload1', methods=['POST','GET'])
def upload1():
    if request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        profession = request.form['profession']
        email = request.form['email']
        telephone = request.form['telephone']
        proName = request.form['prodName']
        salaire = request.form.getlist("exampleRadios")

        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="ade",
            passwd="Jenkins0",
            database="achat_credit"
        )
        mycursor = mydb.cursor()

        sql = "INSERT INTO clients (nom,prenom,profession,salaire,email,telephone,produitCommande) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (nom, prenom, profession, salaire[0], email, telephone, proName)
        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")

    return redirect(url_for('down'))


@app.route('/return-files/')
def return_files_tut():
    try:
        return send_file('static/form.pdf', attachment_filename='form.pdf')
    except Exception as e:
        return str(e)



if __name__ == "__main__":
    app.run(debug=True)



