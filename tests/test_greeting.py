from my_app.main import greeting


def test_greeting() -> None:
    result = greeting("World")
    assert result == "Hello, World!"
