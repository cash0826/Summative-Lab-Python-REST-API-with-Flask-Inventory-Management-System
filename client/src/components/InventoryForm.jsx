import { useState } from "react";
import { addItem } from "../services/InventoryService";

export default function InventoryForm({inventory, setInventory, ...props}) {

  const [formData, setFormData] = useState({
    barcode: "",
    name: "",
    quantity: "",
    price: "",
    category: ""
  });

  function handleChange(e) {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value
    }));
  }

  async function handleSubmit(e) {
    e.preventDefault();
    const newItem = {
      barcode: formData.barcode,
      name: formData.name,
      quantity: formData.quantity,
      price: formData.price,
      category: formData.category
    }
    const createdItem = await addItem(newItem);
    setInventory((prevInventory) => [...prevInventory, createdItem]);
    setFormData({
      barcode: "",
      name: "",
      quantity: "",
      price: "",
      category: ""
    });
  }

  return(
    <>
      <h2>Add New Product:</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="barcode"
          required
          value={formData.barcode}
          onChange={handleChange}
          placeholder="Barcode"
        />
        <input
          type="text"
          name="name"
          value={formData.name}
          onChange={handleChange}
          placeholder="Name"
        />
        <input
          type="number"
          name="quantity"
          required
          value={formData.quantity}
          onChange={handleChange}
          placeholder="Quantity"
        />
        <input
          type="number"
          name="price"
          required
          value={formData.price}
          onChange={handleChange}
          placeholder="Price"
        />
        <input
          type="text"
          name="category"
          value={formData.category}
          onChange={handleChange}
          placeholder="Category"
        />
        <div></div>
        <button type="submit">Create Product</button>
      </form>
    </>
  );
}