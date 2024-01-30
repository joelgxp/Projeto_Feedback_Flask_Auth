from flask import render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required

from app import app, db
from app.models.model import Users

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
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        access_level = 'admin'
        
        if name and email and password:
                        
            users = Users(name, email, password, access_level)
            db.session.add(users)
            db.session.commit()
            
            return redirect(url_for('login'))
        
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
        if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('password')
            
            user = Users.query.filter_by(email=email).first()
                        
            if user and user.verify_password(password):
                login_user(user)
                return redirect(url_for('index'))
            else:
                print('Usuário ou senha inválido')
                return redirect(url_for('login'))
            
        return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

# END LOGIN

# Lider
@app.route('/lider', methods=['GET', 'POST'])
@login_required
def lider():
    if request.method == 'GET':
        lideres = Users.query.all()
        print(lideres)
        return render_template('lider.html', lideres=lideres)
    
    elif request.method == 'POST':
        
        return render_template('lider.html')
    
   


app.run(debug=True)