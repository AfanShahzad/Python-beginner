use("ecommerce");

// delete one product by name
db.contacts.deleteOne({ name: "Alice Johnson" });

// delete many orders with status "delivered"
db.orders.deleteMany({ status: "Delivered" });