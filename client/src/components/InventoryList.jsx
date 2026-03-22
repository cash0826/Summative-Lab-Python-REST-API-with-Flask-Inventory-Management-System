// td = table data
// th = table header

import { deleteItem } from "../services/InventoryService.js";

export default function InventoryList({inventory, setInventory, ...props}) {

  async function handleDelete(itemId) {
    await deleteItem(itemId);
    setInventory((previous) => previous.filter(item => item.id !== itemId))
  }

  let rows = inventory?.map((item, index) =>{
    return(
      <tr key={item.id}>
        <td>{ item.barcode }</td>
        <td>{ item.name }</td>
        <td>{ item.price }</td>
        <td>{ item.quantity } </td>
        <td>{ item.category }</td>
        <td><button onClick={() => handleDelete(item.id)}>Delete</button> </td>
      </tr>
    )
  })

  return(
    <table>
      <thead>
        <tr>
          <th>Barcode</th>
          <th>Name</th>
          <th>Price</th>
          <th>Quantity</th>
          <th>Category</th>
          <th>Actions</th>
        </tr>
      </thead>

      <tbody> 
        { rows }
      </tbody>

      <tfoot>
        <tr>
          <td colSpan={6}>Total Items: { inventory?.length || 0 } </td>
        </tr>
      </tfoot>

    </table>
  );
}