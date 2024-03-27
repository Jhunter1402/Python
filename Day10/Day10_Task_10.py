def greet(**kwargs):
    print(f"Hello, {kwargs['name']}!")


info = {"name": "Alice"}
greet(**info)
