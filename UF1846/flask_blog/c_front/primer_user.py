from werkzeug.security import generate_password_hash

email = "user@mail.com"
password = "A1234b"
rol = 'admin'

hashed = generate_password_hash(password)

print(f"INSERT INTO usauario (email,pw_hash,rol,nombre) VALUES ('{email}','{hashed}','{rol}','administrador')")