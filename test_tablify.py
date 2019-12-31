from tablify import tablify


def test_can_call_without_crashing():
    header = ["name", "surname", "age"]
    rows = [
        ("John", "Johnsson", 49),
        ("Old", "Oldsson", 34_000_000),
    ]
    print()
    print(tablify([header] + rows))
