use("ecommerce");

db.dropDatabase();

// create sales collection and insert documents
db.sales.insertMany([
  {
    _id: 1,
    item: "Apple",
    price: 20,
    quantity: 2,
    category: "Fruits",
    timestamp: new Date(),
  },
  {
    _id: 2,
    item: "Banana",
    price: 15,
    quantity: 3,
    category: "Fruits",
    timestamp: new Date(),
  },
  {
    _id: 3,
    item: "Orange",
    price: 25,
    quantity: 1,
    category: "Fruits",
    timestamp: new Date(),
  },
  {
    _id: 4,
    item: "Carrot",
    price: 10,
    quantity: 5,
    category: "Vegetables",
    timestamp: new Date(),
  },
  {
    _id: 5,
    item: "Broccoli",
    price: 12,
    quantity: 3,
    category: "Vegetables",
    timestamp: new Date(),
  },
]);

// aggregation
db.sales.aggregate([
  { $match: { category: "Fruits" } },
  { $project: { _id: 1, item: 1, quantity: 1 } },
]);
// group sales by category and calculate total price
db.sales.aggregate([
  {
    $group: {
      _id: "$category",
      totalPrice: { $sum: { $multiply: ["$price", "$quantity"] } },
    },
  },
]);
