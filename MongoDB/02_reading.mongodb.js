use("ecommerce");
// find specific product by name
db.products.find({ name: "Watch" });
// find all products in the Fashion category
db.products.find({ category: "Fashion" });
// price greater than 3000
db.products.find({ price: { $gt: 3000 } });
// price between 3000 and 6000
db.products.find({ price: { $gt: 3000, $lt: 6000 } });
// or operator
db.products.find({ $or: [{ category: "Fashion" }, { price: { $lt: 3000 } }] });
// specific fields
db.products.find({}, { name: 1, price: 1, _id: 0 });
// sorting and limiting results
db.products.find().sort({ price: -1 }).limit(2);
// pagination
db.products.find().sort({ price: -1 }).skip(1).limit(3);
