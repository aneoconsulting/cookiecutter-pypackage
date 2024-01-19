from {{ cookiecutter.project_slug }}.hello import hello


def test_hello():
    assert hello() == "Hello, World!"
