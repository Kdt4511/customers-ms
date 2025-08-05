from flask import Blueprint, request, jsonify
from app.models import Customer
from app import db

main = Blueprint('main', __name__)

@main.route('/customers', methods=['POST'])
def add_customer():
    data = request.json
    customer = Customer(name=data['name'], email=data['email'], phone=data['phone'])
    db.session.add(customer)
    db.session.commit()
    return jsonify({'message': 'Customer added'}), 201

@main.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return jsonify([{'id': c.id, 'name': c.name, 'email': c.email, 'phone': c.phone} for c in customers])

@main.route('/customers/<int:id>', methods=['PUT'])
def update_customer(id):
    data = request.json
    customer = Customer.query.get_or_404(id)
    customer.name = data['name']
    customer.email = data['email']
    customer.phone = data['phone']
    db.session.commit()
    return jsonify({'message': 'Customer updated'})

@main.route('/customers/<int:id>', methods=['DELETE'])
def delete_customer(id):
    customer = Customer.query.get_or_404(id)
    db.session.delete(customer)
    db.session.commit()
    return jsonify({'message': 'Customer deleted'})