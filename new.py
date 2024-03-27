from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

dummy_data = [
    {'id': 1, 'name': 'sagar', 'email': 'sagar@gmail.com', 'address': '20-3'},
    {'id': 2, 'name': 'sar', 'email': 'sar@gmail.com', 'address': 'sdf3'},
]

def generate_id():
    return max(item['id'] for item in dummy_data) + 1 if dummy_data else 1

@app.route('/')
def index():
    return render_template('new.html', items=dummy_data)

@app.route('/add', methods=['GET'])
def add():
    return render_template('update.html', item='')

@app.route('/add_data', methods=['POST'])
def add_data():
    if request.method == 'POST':
        new_item = {'id': generate_id(), 'name': request.form['name'], 'email': request.form['email'], 'address': request.form['address']}
        dummy_data.append(new_item)
    return redirect(url_for('index')) 

@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit(item_id):
    item = next((item for item in dummy_data if item['id'] == item_id), None)
    if request.method == 'POST':
        item['name'] = request.form['name']
        item['email'] = request.form['email']
        item['address'] = request.form['address']
        return redirect(url_for('index'))
    return render_template('edit.html', item=item)

@app.route('/delete/<int:item_id>')
def delete(item_id):
    global dummy_data
    dummy_data = [item for item in dummy_data if item['id'] != item_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
