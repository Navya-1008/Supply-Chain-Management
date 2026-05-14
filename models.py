from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact_email = db.Column(db.String(100), nullable=True)

class Warehouse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'), nullable=False)
    price = db.Column(db.Float, nullable=False)
    supplier = db.relationship('Supplier', backref=db.backref('products', lazy=True))

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    warehouse_id = db.Column(db.Integer, db.ForeignKey('warehouse.id'), nullable=False)
    quantity = db.Column(db.Integer, default=0)
    low_stock_threshold = db.Column(db.Integer, default=10)
    product = db.relationship('Product', backref=db.backref('inventory_items', lazy=True))
    warehouse = db.relationship('Warehouse', backref=db.backref('inventory_items', lazy=True))

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), default='Pending')
    date = db.Column(db.DateTime, default=datetime.utcnow)
    product = db.relationship('Product', backref=db.backref('orders', lazy=True))

class SalesHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    quantity_sold = db.Column(db.Integer, nullable=False)
    product = db.relationship('Product', backref=db.backref('sales_history', lazy=True))
