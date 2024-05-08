const express = require('express');
const redis = require('redis');
const { promisify } = require('util');

const listProducts = [
  { Id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { Id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { Id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { Id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];

const app = express();
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

/**
 * Retrieves an item from the list of products based on its ID.
 * @param {number} id - The ID of the item to retrieve.
 * @returns {object|undefined} - The item object if found, or undefined if not found.
 */
const getItemById = id => {
  return listProducts.find(product => product.Id === id);
};

/**
 * Reserves stock for an item by its ID.
 * @param {string} itemId - The ID of the item.
 * @param {number} stock - The stock quantity to reserve.
 * @returns {Promise<void>} - A promise that resolves when the stock is reserved.
 */
async function reserveStockById(itemId, stock) {
  await setAsync(`item.${itemId}`, stock.toString()); // Convert stock to string before saving
}

listProducts.forEach(item => reserveStockById(item.Id, item.stock));

/**
 * Retrieves the current reserved stock for a given item ID.
 *
 * @param {string} itemId - The ID of the item.
 * @returns {Promise<number>} The current reserved stock for the item.
 */
async function getCurrentReservedStockById(itemId) {
  const reservedStock = await getAsync(`item.${itemId}`);
  return reservedStock ? parseInt(reservedStock) : 0;
}

app.use(express.json());

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const { itemId } = req.params;
  const product = getItemById(parseInt(itemId));

  if (!product) {
    res.json({ status: 'Product not found' });
  } else {
    const currentQuantity = await getCurrentReservedStockById(itemId);
    res.json({ ...product, currentQuantity });
  }
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const { itemId } = req.params;
  const product = getItemById(parseInt(itemId));

  if (!product) {
    res.json({ status: 'Product not found' });
  } else {
    const currentQuantity = await getCurrentReservedStockById(itemId);
    if (currentQuantity < 1) {
      res.json({ status: 'Not enough stock available', itemId: product.Id });
    } else {
      await reserveStockById(itemId, currentQuantity - 1);
      res.json({ status: 'Reservation confirmed', itemId: product.Id });
    }
  }
});

app.listen(1245, () => {
  console.log('Server started on port 1245');
});
