import { useState, useEffect, useContext } from "react";
import { ThemeContext } from "../context/ThemeContext.jsx";
import { addItem } from "../services/InventoryService.js";

export default function ItemForm({inventory, setInventory, ...props}) {
  const { theme } = useContext(ThemeContext);
  const [formData, setFormData] = useState({
    name: "",
    description: "",
    price: 0.0,
    quantity: 0,
    barcode: "",
    category: "",
  });

  async function handleSubmit(e) {
    e.preventDefault();
    const newItem = {
      name: formData.name,
      description: formData.description,
      price: parseFloat(formData.price),
      quantity: parseInt(formData.quantity, 10),
      barcode: formData.barcode,
      category: formData.category,
    };
    
    const updated = await addItem(newItem);
    setInventory(previous => inventory.map(item => item.id === updated.id ? updated : item).concat(updated));
    setFormData({
      name: "",
      description: "",
      price: 0.0,
      quantity: 0,
      barcode: "",
      category: "",
    });
  }

  return(
    <div>
      <h2> Add New Product </h2>
      <form onSubmit={handleSubmit}>
        <label htmlFor="name"> Name: </label>
        <input id="name" type="text" name="name" value={formData.name} onChange={(e) => setFormData({ ...formData, name: e.target.value })} />
        <br />

        <label htmlFor="description"> Description: </label>
        <input id="description" type="text" name="description" value={formData.description} onChange={(e) => setFormData({ ...formData, description: e.target.value })} />
        <br />

        <label htmlFor="price"> Price: </label>
        <input id="price" type="number" name="price" step="0.01" required value={formData.price} onChange={(e) => setFormData({ ...formData, price: e.target.value })} />
        <br />

        <label htmlFor="quantity"> Quantity: </label>
        <input id="quantity" type="number" name="quantity" required value={formData.quantity} onChange={(e) => setFormData({ ...formData, quantity: e.target.value })} />
        <br />

        <label htmlFor="barcode"> Barcode: </label>
        <input id="barcode" type="text" name="barcode" required value={formData.barcode} onChange={(e) => setFormData({ ...formData, barcode: e.target.value })} />
        <br />

        <label htmlFor="category"> Category: </label>
        <input id="category" type="text" name="category" value={formData.category} onChange={(e) => setFormData({ ...formData, category: e.target.value })} />
        <br />
        <button type="submit"> Submit </button>
      </form>
    </div>
  )
}