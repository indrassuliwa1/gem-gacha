from api.index import app
from flask import send_from_directory
import os

# Override route '/' khusus untuk testing lokal
# Agar bisa membuka index.html
@app.route('/')
def serve_frontend():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    print("Game berjalan di: http://127.0.0.1:5000")
    app.run(debug=True, port=5000)