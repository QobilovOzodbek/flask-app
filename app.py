from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Bu yerda formadan ma'lumotlarni olib, email jo'natish yoki bazaga yozish mumkin
        return "<h1>Thanks for getting in touch!</h1> "
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
