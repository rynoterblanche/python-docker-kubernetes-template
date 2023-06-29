def test_returns_seed_product_given_id_1(client):
    response = client.get("/products/1")
    product = response.json

    assert response.status_code == 200
    assert product["name"] == "Product A"


def test_returns_not_found_given_id_0(client):
    response = client.get("/products/0")

    assert response.status_code == 404
