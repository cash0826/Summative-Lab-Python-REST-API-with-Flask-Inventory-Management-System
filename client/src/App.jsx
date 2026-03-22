import './App.css'
import { useContext, useState, useEffect } from "react";
import { ThemeContext } from "./context/ThemeContext.jsx";
import { getInventory } from "./services/InventoryService";
import InventoryList from "./components/InventoryList.jsx";
import ItemForm from "./components/ItemForm.jsx";

function App() {
  const { theme, setTheme } = useContext(ThemeContext);
  const [inventory, setInventory] = useState([])
  const [allItems, setAllItems] = useState([])
  const [query, setQuery] = useState("");
  const [showForm, setShowForm] = useState(false)

  useEffect(() => {
    getInventory().then((data) =>{
      setAllItems(data);
      setInventory(data);
    }).catch((error) => {
      console.error("Error fetching inventory:", error)
    });
  }, [])

  function handleSearch (e) {
    const q = e.target.value;
    setQuery(q);
  
    if (!q) {
      setInventory(allItems)
      return;
    }
    const filteredItems = allItems.filter(item =>
      item.name.toLowerCase().includes(q.toLowerCase())
    )
    setInventory(filteredItems)
  }

  const searchBar = (
    <div>
      <input
        id="search-bar"
        type="text" 
        placeholder="Search item by name..."
        value = {query}
        onChange={handleSearch}
      />
    </div>
  )

  function handleClick() {
    setShowForm((showForm) => !showForm)
  }

  return(
    <div className={`app-container ${theme === "dark" ? "dark" : "" }`}>
      <nav className="navbar"> {searchBar} </nav>
      <main>
        <h2>This is the Inventory:</h2>
        <InventoryList inventory={inventory} setInventory={setInventory} />

      </main>

      
      {showForm && <ItemForm inventory={inventory} setInventory={setInventory} />}

      <button onClick={handleClick}> {showForm ? "Hide Form" : "Add Product"} </button>

      <div></div>

      <button onClick={() => {setTheme(theme === "light" ? "dark" : "light")}}>Toggle Theme</button>
    </div>
  )
}

export default App
