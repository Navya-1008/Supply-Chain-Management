from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from models import db, Product, Inventory, Order, Warehouse, Supplier, SalesHistory
from ml.predictor import predict_future_demand

routes = Blueprint('routes', __name__)

def register_routes(app):
    app.register_blueprint(routes)

@routes.route('/')
def dashboard():
    products_count = Product.query.count()
    low_stock_items = Inventory.query.filter(Inventory.quantity <= Inventory.low_stock_threshold).all()
    pending_orders = Order.query.filter_by(status='Pending').count()
    return render_template('dashboard.html', 
                           products_count=products_count, 
                           low_stock_items=low_stock_items,
                           pending_orders=pending_orders)

@routes.route('/inventory')
def inventory():
    items = Inventory.query.all()
    return render_template('inventory.html', items=items)

@routes.route('/orders')
def orders():
    all_orders = Order.query.order_by(Order.date.desc()).all()
    return render_template('orders.html', orders=all_orders)

@routes.route('/analytics')
def analytics():
    return render_template('analytics.html')

@routes.route('/api/predict')
def api_predict():
    products = Product.query.all()
    results = []
    
    for product in products:
        sales_records = SalesHistory.query.filter_by(product_id=product.id).all()
        # format data for predictor
        data = [{'date': str(r.date), 'quantity_sold': r.quantity_sold} for r in sales_records]
        
        predicted_demand = predict_future_demand(data)
        
        # Get current stock
        inventory_items = Inventory.query.filter_by(product_id=product.id).all()
        current_stock = sum(item.quantity for item in inventory_items)
        
        results.append({
            'product_name': product.name,
            'current_stock': current_stock,
            'predicted': predicted_demand
        })
        
    return jsonify(results)
