def test_returns_all_seed_products(client):
    response = client.get("/products")
    products = response.json

    assert response.status_code == 200
    assert len(products) == 3
