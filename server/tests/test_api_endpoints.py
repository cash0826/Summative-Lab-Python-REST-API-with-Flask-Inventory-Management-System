from pathlib import Path
import sys
from unittest.mock import patch

import pytest


SERVER_DIR = Path(__file__).resolve().parents[1]
if str(SERVER_DIR) not in sys.path:
    sys.path.insert(0, str(SERVER_DIR))

import app as app_module
from models.inventory_item import Inventory_Item


@pytest.fixture
def client():
    app_module.app.config.update(TESTING=True)
    with app_module.app.test_client() as test_client:
        yield test_client


@pytest.fixture
def provider_mock():
    with patch.object(app_module, "_provider", autospec=True) as mock_provider:
        yield mock_provider


def test_get_inventory_returns_all_items(client, provider_mock):
    provider_mock.all_inventory.return_value = [
        Inventory_Item(id=1, name="Milk", quantity=3, barcode="111"),
        Inventory_Item(id=2, name="Eggs", quantity=12, barcode="222"),
    ]

    response = client.get("/inventory")

    assert response.status_code == 200
    assert response.get_json() == [
        {
            "id": 1,
            "name": "Milk",
            "description": "",
            "price": 0.0,
            "quantity": 3,
            "barcode": "111",
            "category": "",
            "product_details": {},
        },
        {
            "id": 2,
            "name": "Eggs",
            "description": "",
            "price": 0.0,
            "quantity": 12,
            "barcode": "222",
            "category": "",
            "product_details": {},
        },
    ]
    provider_mock.load.assert_called_once()


def test_get_inventory_filters_by_barcode(client, provider_mock):
    provider_mock.all_inventory.return_value = [
        Inventory_Item(id=1, name="Milk", quantity=3, barcode="111"),
        Inventory_Item(id=2, name="Eggs", quantity=12, barcode="222"),
    ]

    response = client.get("/inventory?barcode=222")

    assert response.status_code == 200
    assert response.get_json() == [
        {
            "id": 2,
            "name": "Eggs",
            "description": "",
            "price": 0.0,
            "quantity": 12,
            "barcode": "222",
            "category": "",
            "product_details": {},
        }
    ]


def test_post_inventory_creates_item_and_saves(client, provider_mock):
    payload = {
        "name": "Yogurt",
        "quantity": 4,
        "barcode": "333",
        "description": "Greek yogurt",
        "price": 5.25,
        "category": "Dairy",
    }
    parsed_item = Inventory_Item.from_dict(payload)
    created_item = Inventory_Item.from_dict({**payload, "id": 7})

    with patch.object(app_module.Inventory_Item, "from_dict", return_value=parsed_item) as from_dict_mock:
        provider_mock.add_item.return_value = created_item

        response = client.post("/inventory", json=payload)

    assert response.status_code == 201
    assert response.get_json()["id"] == 7
    assert response.get_json()["name"] == "Yogurt"
    provider_mock.load.assert_called_once()
    from_dict_mock.assert_called_once_with(payload)
    provider_mock.add_item.assert_called_once_with(parsed_item)
    provider_mock.save.assert_called_once()


def test_put_inventory_updates_item_and_saves(client, provider_mock):
    payload = {
        "id": 2,
        "name": "Eggs",
        "quantity": 18,
        "barcode": "222",
        "description": "Large eggs",
        "price": 6.0,
        "category": "Dairy",
    }
    parsed_item = Inventory_Item.from_dict(payload)

    with patch.object(app_module.Inventory_Item, "from_dict", return_value=parsed_item) as from_dict_mock:
        provider_mock.update.return_value = parsed_item

        response = client.put("/inventory/2", json=payload)

    assert response.status_code == 200
    assert response.get_json()["quantity"] == 18
    provider_mock.load.assert_called_once()
    from_dict_mock.assert_called_once_with(payload)
    provider_mock.update.assert_called_once_with(2, parsed_item)
    provider_mock.save.assert_called_once()


def test_delete_inventory_removes_item_and_saves(client, provider_mock):
    provider_mock.delete.return_value = True

    response = client.delete("/inventory/9")

    assert response.status_code == 204
    provider_mock.load.assert_called_once()
    provider_mock.delete.assert_called_once_with(9)
    provider_mock.save.assert_called_once()


def test_get_inventory_item_returns_404_when_missing(client, provider_mock):
    provider_mock.inventory_item_id.return_value = None

    response = client.get("/inventory/999")

    assert response.status_code == 404
    assert response.get_json() == {"error": "Item not found for requested id"}
    provider_mock.load.assert_called_once()
