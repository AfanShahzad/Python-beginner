use("ecommerce");

db.dropDatabase();

db.products.insertMany([
  {
    name: "Watch",
    price: 2500,
    category: "Fashion",
    stocks: 120,
    rating: 4.5,
    tags: ["accessory", "fashion", "luxury"],
    timestamp: new Date(),
  },
  {
    name: "Shoes",
    price: 5000,
    category: "Fashion",
    stocks: 80,
    rating: 4.7,
    tags: ["footwear", "fashion", "luxury"],
    timestamp: new Date(),
  },
  {
    name: "Laptop",
    price: 75000,
    category: "Electronics",
    stocks: 50,
    rating: 4.8,
    tags: ["computer", "electronics", "luxury"],
    timestamp: new Date(),
  },
]);

db.contacts.insertMany([
  {
    name: "John Doe",
    email: "john.doe@example.com",
    phone: "123-456-7890",
    message: "I have a question about my order.",
    timestamp: new Date(),
  },
  {
    name: "Jane Smith",
    email: "jane.smith@example.com",
    phone: "098-765-4321",
    message: "I would like to inquire about a product.",
    timestamp: new Date(),
  },
  {
    name: "Alice Johnson",
    email: "alice.johnson@example.com",
    phone: "555-1234",
    message: "I'm interested.",
    timestamp: new Date(),
  },
]);

db.orders.insertMany([
  {
    productId: "ORD001",
    customerName: "John Doe",
    products: [
      { name: "Watch", price: 2500, quantity: 2 },
      { name: "Shoes", price: 5000, quantity: 1 }
    ],
    totalPrice: 10000,
    status: "Pending",
    timestamp: new Date(),
  },
  {
    productId: "ORD002",
    customerName: "Jane Smith",
    products: [{ name: "Laptop", price: 75000, quantity: 1 }],
    totalPrice: 75000,
    status: "Pending",
    timestamp: new Date(),
  },
]);
