from flask import render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required

from app import app, db
from app.models.model import Users, Employees

login_manager = LoginManager(app)


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
    return render_template('employees.html')

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
                return redirect(url_for('employees'))
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

# Employees
@login_required
@app.route('/employees', methods=['GET', 'POST'])
def employees():
    if request.method == 'GET':
        employees = Employees.query.all()
        print(employees)
        return render_template('employees.html', employees=employees)
    
    
@app.route('/employees/new', methods=['GET', 'POST'])
@login_required
def new_employee():
    if request.method == 'GET':
        return render_template('new_employee.html')
    
    elif request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        role = request.form.get('role')
        department = request.form.get('department')
        gender_id = request.form.get('gender')
        birth_date = request.form.get('birth_date')
        admission_date = request.form.get('admission_date')
        resignation_date = request.form.get('resignation_date')
        #address_id = request.form.get('address')
        marital_status_id = request.form.get('marital-status')
        status_id = request.form.get('status')        

        print(name, phone, email, role, department, gender_id, birth_date, admission_date, resignation_date, marital_status_id, status_id)
        
        try:
            # retirei o address
            employees = Employees(name=name, phone=phone, email=email, role=role, department=department, gender_id=gender_id, birth_date=birth_date, admission_date=admission_date, resignation_date=resignation_date, marital_status_id=marital_status_id, status_id=status_id)
            db.session.add(employees)
            db.session.commit()
            print('Funcionário cadastrado com sucesso')
            return redirect(url_for('employees'))
        except Exception as e:
            print(f'Erro ao cadastrar funcionário: {str(e)}') 
    
    
app.run(debug=True)