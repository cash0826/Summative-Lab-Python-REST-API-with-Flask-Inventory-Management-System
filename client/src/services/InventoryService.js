const baseUrl = "http://127.0.0.1:5555";

export async function getInventory() {
  const url = `${baseUrl}/inventory`;
  const response = await fetch(url);
  if (response.ok) {
    let json = await response.json(); 
    return json
  }
  throw new Error(`Error fetching inventory: ${ response.statusText }`);
  return [];   
}

export async function addItem(newItemData) {
  const url = `${baseUrl}/inventory`;
  if (newItemData) {
    const response = await fetch (url, {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(newItemData)
    });
    if (response.ok) {
      const data = await response.json()
      return data;
    }
    throw new Error(`Error adding new item: ${ response.statusText }`);
    return null;
  }
}

export async function updateItem(itemId, updatedItemData) {
  const url = `${baseUrl}/inventory/${itemId}`;
  const response = await fetch(url, {
    method: "PATCH",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(updatedItemData) // Come back later and update the logic as needed to PATCH update
  });
  if (response.ok) {
    const data = await response.json();
    return data;
  }
  throw new Error(`Error updating item to the inventory: ${ response.statusText}`)
}

export async function deleteItem(itemId) {
  const url = `${baseUrl}/inventory/${itemId}`;
  const response = await fetch(url, {
    method: "DELETE"
  });
  if (response.ok) {
    return response;
  }
  throw new Error(`Error deleting item: ${ response.statusText }`);  
}

// useEffect(() => {
//   (async () => {



//     setInventory((previous) => json) // if this were local, ensure use ... array method
//   })();
// }, [])