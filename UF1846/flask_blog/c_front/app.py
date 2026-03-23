
from flask import Flask,render_template,abort,request,session,redirect,flash
import requests

app = Flask(__name__)
app.secret_key="supersecreto"

API = "http://127.0.0.1:5002/api"

def get_posts():
    return requests.get(f"{API}/posts").json()
    
def get_posts_all():
    return requests.get(f"{API}/posts_all").json()

def get_post(post_id):
    resp = requests.get(f"{API}/post/{post_id}")
    if resp.status_code == 404:
        return None
    return resp.json()

def is_admin():
    return session.get('rol') == 'admin'

# ------------------------------------------

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def home():
    entradas = get_posts()
    return render_template('home.html',posts=entradas)

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    if post is None:
        abort(404)
    
    return render_template('post.html',post=post)


@app.route('/login', method=['GET','POST'])
def login():
    if request.method == "POST":
        data = {
            'email': request.form['email'],
            'password': request.form['password']
        }
        resp = requests.post(f"{API}/login", json=data)
        if resp.status_code == 200:
            user = resp.json()
            session['user_id'] = user['user_id']
            session['user_role'] = user['rol']
            return redirect('/admin')
        else:
            flash('Error: Usuario no válido.')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/admin')
def admin():
    if not is_admin():
        return redirect('/login')
    
    posts = get_posts_all()
    return render_template('admin.html', posts = posts)

@app.route('/admin/create', methods=['POST','GET'])
def create_post():
    if not is_admin():
        return redirect('/login')
    
    if request.method == 'POST':
        data = {
            'titulo': request.form['titulo'],
            'contenido': request.form['contenido'],
            'id_autor': session.get('user_id'),
            'estado': request.form['estado']
        }
        requests.post(f'{API}/posts', json=data)
        flash('Post creado con éxito.')
        return redirect('/admin')
    return render_template('from_post.html', post=None)

@app.route('/admin/edit/<int:post_id>', methods=['POST', 'GET'])
def edit_post(post_id):
    if not is_admin():
        return redirect('/login')
    
    if request.method == 'POST':
        data = {
            'titulo': request.form['titulo'],
            'contenido': request.form['contenido'],
            'estado': request.form['estado']
        }
        requests.put(f'{API}/post/{post_id}', json=data)
        flash('Post actualizado con éxito.')
        return redirect('/admin')
    
    post = get_post(post_id)
    return render_template('from_post.html', post=post)

@app.route('/admin/delete/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    if not is_admin():
        return redirect('/login')
    
    requests.delete(f"{API}/post/{post_id}")
    flash('Post eliminado con éxito.')
    return redirect('/admin')
        

# --------------------------------------------
if __name__ == '__main__':
    app.run(port=5000,debug=True)
