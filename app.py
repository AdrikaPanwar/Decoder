from flask import Flask, render_template, request, flash
import qrcode
from io import BytesIO
from base64 import b64encode

app = Flask(__name__, static_folder='static')  
app.secret_key = 'uper secret key'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        memory = BytesIO()
        data = request.form.get('link')
        img = qrcode.make(data)
        img.save(memory)
        memory.seek(0)
        base64_img ='data:img.png;base64,' + b64encode(memory.getvalue()).decode('ascii')
        flash(base64_img)
        flash('Here is the QR Code we generated for you ')
        return render_template('index.html')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)