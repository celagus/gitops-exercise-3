from hello_world.app.app import hello_world


def test_get_hello():
    response = hello_world()
    assert response["message"] == "Hello world!"


if __name__ == "__main__":
    test_get_hello()
