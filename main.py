from flask import render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required

from app import app, db
from app.models.model import Lider

login_manager = LoginManager(app)


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome_lider = request.form.get('nome')
        departamento_lider = request.form.get('departamento')
        email_lider = request.form.get('email')
        password_lider = request.form.get('senha')
        password_hashed = Lider.hash_password(password_lider)
        
        if nome_lider and departamento_lider and email_lider and password_hashed:
            lider = Lider(nome_lider, departamento_lider, email_lider, password_hashed)
            db.session.add(lider)
            db.session.commit()
            
            return redirect(url_for('login'))
        
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
        if request.method == 'POST':
            email_lider = request.form.get('email')
            pwd = request.form.get('senha')
            
            user = Lider.query.filter_by(email_lider=email_lider).first()
                        
            if not user or not user.verify_password(pwd):
                print('Usuário ou senha inválido')
                return redirect(url_for('login'))
            else:
                login_user(user)
                return redirect(url_for('index'))
            
        return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@login_manager.user_loader
def load_user(user_id):
    return Lider.query.get(int(user_id))

# END LOGIN

# Lider
@app.route('/lider', methods=['GET', 'POST'])
@login_required
def lider():
    if request.method == 'GET':
        lideres = Lider.query.all()
        print(lideres)
        return render_template('lider.html', lideres=lideres)
    
    elif request.method == 'POST':
        
        return render_template('lider.html')
    
# Colaborador

@app.route('/colaborador', methods=['GET', 'POST'])
@login_required
def colaborador():
    if request.method == 'GET':
        return render_template('colaborador.html')

    elif request.method == 'POST':
        return render_template('colaborador.html')
    
# Reunão
@app.route('/reuniao', methods=['GET', 'POST'])
@login_required
def reuniao():
    if request.method == 'GET':
        return render_template('reuniao.html')
    
    elif request.method == 'POST':
        return render_template('reuniao.html')
    


app.run(debug=True)