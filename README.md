# AntiGravity SCM 🚚📦

AntiGravity SCM is a Smart Supply Chain Management System developed to streamline and automate supply chain operations including inventory management, warehouse monitoring, order processing, shipment tracking, analytics, and AI-based demand forecasting.

The project provides a centralized platform for managing products, suppliers, warehouses, customers, and logistics efficiently.

---

# Features

## User Management
- User Registration & Login
- Role-Based Access Control
- Roles:
  - Admin
  - Supplier
  - Warehouse Manager
  - Customer/Retailer

---

## Supplier Management
- Add and update suppliers
- Supplier performance tracking
- Supplier-product mapping

---

## Product Management
- Add/Edit/Delete products
- Product categorization
- Pricing management
- Stock monitoring

---

## Warehouse Management
- Multiple warehouse support
- Warehouse stock tracking
- Capacity monitoring

---

## Inventory Management
- Real-time inventory updates
- Automated stock deduction
- Low-stock alerts
- Warehouse stock transfer

---

## Order Management
- Create customer orders
- Order status tracking
- Automatic inventory deduction

### Order Status
- Pending
- Processed
- Shipped
- Delivered

---

## Shipment & Logistics
- Shipment tracking
- Delivery status monitoring
- Delay detection

---

## Analytics & Reports
- Monthly sales reports
- Revenue analysis
- Top-selling products
- Supplier performance analysis
- Inventory turnover reports
- Delayed shipment reports

---

## AI Features 🤖
- Demand forecasting
- Reorder recommendations
- Delivery delay prediction

### ML Techniques Used
- Moving Average
- Linear Regression

---

# Tech Stack

## Frontend
- HTML
- CSS
- JavaScript
- Bootstrap

## Backend
- Python Flask

## Database
- MySQL

## AI / Analytics
- Python
- Pandas
- Scikit-learn

---

# Database Concepts Used

| Concept | Usage |
|----------|---------------------------|
| Primary Keys | Unique Identification |
| Foreign Keys | Table Relationships |
| Joins | Report Generation |
| Views | Dashboard Reports |
| Triggers | Auto Stock Updates |
| Stored Procedures | Order Processing |
| Transactions | Safe Inventory Changes |
| Indexes | Faster Searches |
| Constraints | Data Integrity |
| Normalization | Efficient Database Design |

---

# Project Workflow

```plaintext
Customer Places Order
        ↓
System Checks Inventory
        ↓
Stock Available?
   ↓             ↓
 YES             NO
 ↓               ↓
Create Order     Generate Alert
Deduct Stock     Reorder Suggestion
Generate Shipment
        ↓
Track Delivery
        ↓
Order Delivered
```

---

# Folder Structure

```plaintext
antigravity-scm/
│
├── app.py
├── routes/
├── templates/
├── static/
├── database/
├── models/
├── ml/
├── requirements.txt
└── README.md
```

---


# Future Enhancements

- Blockchain integration for secure supply chain tracking
- IoT-based warehouse monitoring
- GPS shipment tracking
- Mobile application support
- Cloud deployment
- AI chatbot integration

---

# Expected Outcomes

- Efficient inventory management
- Reduced manual work
- Smart warehouse monitoring
- Automated supply chain operations
- Better demand prediction
- Improved business decision-making

---

# Conclusion

AntiGravity SCM combines database management, automation, analytics, and AI technologies to provide an intelligent and scalable supply chain management solution. The system improves operational efficiency, minimizes stock-related issues, and supports smarter business decisions.

---

# Contributors

- Navya BV

---

# License

This project is developed for educational and academic purposes.
