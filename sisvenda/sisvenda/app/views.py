# -*- coding: utf-8 -*-
import psycopg2
import psycopg2.extras
conn = psycopg2.connect('dbname=sisvenda user=postgres password=flasknao host=127.0.0.1')
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


from flask import render_template, request

from app import app


@app.route('/')
def home():
	return render_template('home.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
	return render_template('homecadastro.html')

@app.route('/cliente', methods=['GET', 'POST'])
def cliente():
	if (request.method == 'POST'):
		nome = request.form['nome']
		senha = request.form['senha']
		email = request.form['email']
		cpf = request.form['cpf']
		cur.execute("INSERT INTO cliente (nome,senha,email,cpf) VALUES ('%s','%s','%s', %s)"%(nome,senha,email,cpf))
		conn.commit()
		return render_template('cliente.html')
	return render_template('cliente.html')

@app.route('/empresa', methods=['GET', 'POST'])
def empresa():
	if (request.method == 'POST'):
		nome_empresa = request.form['nome_empresa']
		email_empresa = request.form['email_empresa']
		senha_empresa = request.form['senha_empresa']
		cnpj = request.form['cnpj']
		cur.execute("INSERT INTO empresa (nome_empresa,email_empresa,senha_empresa,cnpj) VALUES ('%s','%s','%s', %s)"%(nome_empresa,email_empresa,senha_empresa,cnpj))
		conn.commit()
	return render_template('empresa.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if (request.method == 'POST'):
		cur.execute("SELECT * FROM cliente, empresa")
		x = cur.fetchall()
		email = request.form['email']
		senha = request.form['password']
		for i in x:
			if (i['email'] == email and i['senha'] == senha) or (i['email_empresa'] == email and i['senha_empresa'] == int(senha)):
				return render_template('home.html')
	return render_template('login.html')
