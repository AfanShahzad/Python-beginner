use("ecommerce");

// update one
db.products.updateOne(
  { name: "Watch" },
  { $set: { price: 3000, stocks: 100 } }
);

// update many
db.products.updateMany(
  { category: "Fashion" },
  { $inc: { stocks: -1 } }
);
// push to array
db.products.updateOne(
  { name: "Laptop" },
  { $push: { tags: "new" } }
);