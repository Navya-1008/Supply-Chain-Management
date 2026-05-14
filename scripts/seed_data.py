import os
import sys
from datetime import datetime, timedelta
import random

# Add parent directory to path so we can import app and models
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from models import db, Supplier, Warehouse, Product, Inventory, Order, SalesHistory

app = create_app()

def seed_database():
    with app.app_context():
        print("Dropping all tables...")
        db.drop_all()
        print("Creating all tables...")
        db.create_all()

        print("Seeding Suppliers...")
        s1 = Supplier(name="AEKI Manufacturing", contact_email="contact@aeki.com")
        s2 = Supplier(name="Nordic Wood Supplies", contact_email="sales@nordicwood.com")
        db.session.add_all([s1, s2])
        db.session.commit()

        print("Seeding Warehouses...")
        w1 = Warehouse(name="East Coast Mega Hub", location="New Jersey", capacity=50000)
        w2 = Warehouse(name="West Coast Depot", location="California", capacity=45000)
        db.session.add_all([w1, w2])
        db.session.commit()

        print("Seeding Products...")
        p1 = Product(name="KIVIK Sofa", supplier_id=s1.id, price=499.00)
        p2 = Product(name="BILLY Bookcase", supplier_id=s1.id, price=89.00)
        p3 = Product(name="MALM Bed Frame", supplier_id=s2.id, price=249.00)
        p4 = Product(name="POÄNG Chair", supplier_id=s2.id, price=149.00)
        db.session.add_all([p1, p2, p3, p4])
        db.session.commit()

        print("Seeding Inventory...")
        i1 = Inventory(product_id=p1.id, warehouse_id=w1.id, quantity=150, low_stock_threshold=20)
        i2 = Inventory(product_id=p2.id, warehouse_id=w1.id, quantity=15, low_stock_threshold=30) # Low stock
        i3 = Inventory(product_id=p3.id, warehouse_id=w2.id, quantity=40, low_stock_threshold=10)
        i4 = Inventory(product_id=p4.id, warehouse_id=w2.id, quantity=5, low_stock_threshold=20) # Low stock
        db.session.add_all([i1, i2, i3, i4])
        db.session.commit()

        print("Seeding Orders...")
        o1 = Order(product_id=p2.id, quantity=50, status="Pending")
        o2 = Order(product_id=p4.id, quantity=100, status="Shipped")
        db.session.add_all([o1, o2])
        db.session.commit()

        print("Seeding Sales History for ML...")
        # Generate 60 days of sales data for each product
        start_date = datetime.now() - timedelta(days=60)
        sales_records = []
        for p in [p1, p2, p3, p4]:
            base_sales = random.randint(5, 20)
            for i in range(60):
                current_date = start_date + timedelta(days=i)
                # Add some random noise
                qty_sold = max(0, base_sales + random.randint(-5, 10))
                sales_records.append(SalesHistory(product_id=p.id, date=current_date.date(), quantity_sold=qty_sold))
        
        db.session.add_all(sales_records)
        db.session.commit()

        print("Database seeding completed successfully!")

if __name__ == "__main__":
    seed_database()
