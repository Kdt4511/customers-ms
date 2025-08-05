from flask import Flask, request, jsonify
from flask_cors import CORS
from db_config import init_mysql

app = Flask(__name__)
CORS(app)
mysql = init_mysql(app)

@app.route('/customers', methods=['POST'])
def add_customer():
    data = request.json
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO customers (name, email, phone) VALUES (%s, %s, %s)",
                   (data['name'], data['email'], data['phone']))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': 'Customer added successfully'}), 201

@app.route('/customers', methods=['GET'])
def get_customers():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM customers")
    rows = cursor.fetchall()
    cursor.close()
    return jsonify(rows)

@app.route('/customers/<int:id>', methods=['PUT'])
def update_customer(id):
    data = request.json
    cursor = mysql.connection.cursor()
    cursor.execute("""
        UPDATE customers SET name=%s, email=%s, phone=%s WHERE id=%s
    """, (data['name'], data['email'], data['phone'], id))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': 'Customer updated successfully'})

@app.route('/customers/<int:id>', methods=['DELETE'])
def delete_customer(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM customers WHERE id=%s", (id,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': 'Customer deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
