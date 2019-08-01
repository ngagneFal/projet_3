from flask import Flask,render_template,request,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:ngagne03@localhost/isi2'
db = SQLAlchemy(app)
############################################  creation des tables#####################s#####################s#####################
                    ####################### etudiant#####################
class Etudiant(db.Model):
    __tablename__ = 'Etudiant'
    id= db.Column(db.Integer, primary_key=True)
    matricule = db.Column(db.String(100), unique=True,nullable = False)
    prenom = db.Column(db.String(200),nullable = False)
    nom = db.Column(db.String(200),nullable = False)
    email = db.Column(db.String(200),nullable = False)
    date_naiss = db.Column(db.Date)
    # id_etudiant=db.relationship('inscription',backref='Etudiant')
    
    def __init__(self,matricule,prenom,nom,email,date_naiss):
        self.matricule =  matricule
        self.prenom = prenom
        self.nom = nom
        self.email = email
        self.date_naiss = date_naiss

    def __repr__(self):
        return '<Etudiant %r>'  
####################### filiere#####################
class filiere(db.Model):
    __tablename__ = 'filiere'
    id= db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.String(200))

    def __init__(self,libelle):
        self.libelle =   libelle


    def __repr__(self):
        return '<filiere %r>'% self.libelle     
#######################classe#####################       
class classe(db.Model):
    __tablename__ = 'classe'
    id= db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.String(200))
    montant_ins = db.Column(db.String(200))
    mensualite = db.Column(db.String(200))
    filiere_id=db.Column(db.Integer, db.ForeignKey('filiere.id'))
    

    def __init__(self,libelle,montant_ins, mensualite,filiere_id):
        self.libelle = libelle
        self.montant_ins = montant_ins
        self.mensualite =  mensualite
        self.filiere_id =  filiere_id
        

    def __repr__(self):
        return '<classe %r>'% self.libelle  

#######################inscription#####################       
class inscription(db.Model):
    __tablename__ = 'inscription'
    id= db.Column(db.Integer, primary_key=True)
    annee_acade = db.Column(db.String(200))
    date_ins = db.Column(db.Date)
    classe_id=db.Column(db.Integer, db.ForeignKey('classe.id'))
    Etudiant_id=db.Column(db.Integer, db.ForeignKey('Etudiant.id')) 
    

    def __init__(self,annee_acade,date_ins,classe_id,etudiant_id):
        self.annee_acade = annee_acade
        self.date_ins = date_ins
        self.classe_id =  classe_id
        self.etudiant_id =etudiant_id
        

    def __repr__(self):
        return '<inscription %r>'% self.annee_acade         
############################################ formulaire ###############################################################


if __name__ == '__main__':
    app.run(debug=True)