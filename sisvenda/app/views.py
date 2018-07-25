# -*- coding: utf-8 -*-
import psycopg2
import psycopg2.extras
conn = psycopg2.connect('dbname=sisvenda user=postgres password=ifpb host=127.0.0.1')
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


from flask import render_template, request, session

from app import app


@app.route('/')
def home():
	if request.method == 'POST':
		session['name'] = request.form['email']
	if 'name' in session:
		name = session['name']
	else:
		name = None
	return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	return render_template('homelogin.html')

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

@app.route('/clientelogin', methods=['GET', 'POST'])
def clientelogin():
	if (request.method == 'POST'):
		cur.execute("SELECT * FROM cliente")
		x = cur.fetchall()
		email = request.form['email']
		senha = request.form['password']
		for i in x:
			if  i['email'] == email and i['senha'] == senha:
				return render_template('homecliente.html')
	return render_template('login.html')

@app.route('/estoque', methods=['GET'])
def estoque():
	if (request.method == 'GET'):
		cur.execute("SELECT * FROM estoque")
		lista_produtos = cur.fetchall()
		return render_template('historicoproduto.html', produtos=lista_produtos)

@app.route('/comprar', methods=['GET', 'POST'])
def comprar():
	if (request.method == 'POST'):
		cnpj_empresa = request.form['cnpj_empresa']
		codigo_produto = request.form['codigo_produto']
		quantidade = request.form['quantidade']
		cur.execute("UPDATE estoque SET quantidade = quantidade - 1 WHERE codigo = %s AND cnpj_empresa = %s;" %(codigo_produto,cnpj_empresa))
		cur.execute("INSERT INTO compra(cnpj_empresa,codigo_produto,quantidade) VALUES (%s,%s,%s)"%(cnpj_empresa,codigo_produto,quantidade))
		conn.commit()
	return render_template('produtocliente.html')

@app.route('/empresa', methods=['GET', 'POST'])
def empresa():
	if (request.method == 'POST'):
		nome_empresa = request.form['nome_empresa']
		email_empresa = request.form['email_empresa']
		senha_empresa = request.form['senha_empresa']
		cnpj = request.form['cnpj']
		session['name'] = request.form['email_empresa']
		cur.execute("INSERT INTO empresa (nome_empresa,email_empresa,senha_empresa,cnpj) VALUES ('%s','%s','%s', %s)"%(nome_empresa,email_empresa,senha_empresa,cnpj))
		conn.commit()
	return render_template('empresa.html')

@app.route('/empresalogin', methods=['GET', 'POST'])
def empresalogin():
	if (request.method == 'POST'):
		cur.execute("SELECT * FROM empresa")
		x = cur.fetchall()
		email = request.form['email']
		senha = request.form['password']
		for i in x:
			if  i['email_empresa'] == email and i['senha_empresa'] == senha:
				return render_template('homeempresa.html')
	return render_template('login.html')

@app.route('/historicoproduto', methods=['GET'])
def historicoproduto():
	if (request.method == 'GET'):
		cur.execute("SELECT * FROM estoque")
		lista_produtos = cur.fetchall()
		return render_template('historicoproduto.html', produtos=lista_produtos)

@app.route('/adicionarproduto', methods=['GET', 'POST'])
def adicionarproduto():
	if (request.method == 'POST'):
		cur.execute("SELECT cnpj FROM empresa WHERE email_empresa='%s' LIMIT 1;"%session['name'])
		ds = cur.fetchone()
		for d in ds:
			print(d)
		codigo = request.form['codigo']
		nome_produto = request.form['nome_produto']
		quantidade = request.form['quantidade']
		cur.execute("INSERT INTO estoque (cnpj_empresa, codigo,nome_produto,quantidade) VALUES (%s,%s,'%s',%s)"%(d, codigo,nome_produto,quantidade))
		conn.commit()
		return render_template('homeempresa.html')
	return render_template('produto.html')
