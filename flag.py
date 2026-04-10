from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# Exemple 1 : Injection SQL (CodeQL détecte les requêtes SQL non sécurisées)
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Vulnérabilité : requête SQL avec concaténation de chaînes
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    if user:
        return "Login successful!"
    else:
        return "Login failed."

# Exemple 2 : Cross-Site Scripting (XSS) (CodeQL détecte les templates non sécurisés)
@app.route('/search')
def search():
    query = request.args.get('q', '')
    # Vulnérabilité : utilisation de render_template_string sans échappement
    return render_template_string(f"<h1>Résultats pour : {query}</h1>")

# Exemple 3 : Command Injection (CodeQL détecte les appels système non sécurisés)
@app.route('/ping')
def ping():
    host = request.args.get('host', '')
    # Vulnérabilité : utilisation de os.system avec une entrée utilisateur non validée
    import os
    os.system(f"ping -c 4 {host}")
    return f"Ping envoyé à {host}"

if __name__ == '__main__':
    app.run(debug=True)
