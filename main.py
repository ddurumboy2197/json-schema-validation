import jsonschema

# Oddiy schema
schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"},
        "city": {"type": "string"}
    },
    "required": ["name", "age", "city"]
}

# Berilgan JSON
json_data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

try:
    jsonschema.validate(instance=json_data, schema=schema)
    print("JSON valid")
except jsonschema.exceptions.ValidationError as err:
    print("JSON invalid:", err)
```

```python
import jsonschema

# Oddiy schema
schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"},
        "city": {"type": "string"}
    },
    "required": ["name", "age", "city"]
}

# Berilgan JSON
json_data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

try:
    jsonschema.validate(instance=json_data, schema=schema)
    print("JSON valid")
except jsonschema.exceptions.ValidationError as err:
    print("JSON invalid:", err)
```

```python
import jsonschema

# Oddiy schema
schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"},
        "city": {"type": "string"}
    },
    "required": ["name", "age", "city"]
}

# Berilgan JSON
json_data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

try:
    jsonschema.validate(instance=json_data, schema=schema)
    print("JSON valid")
except jsonschema.exceptions.ValidationError as err:
    print("JSON invalid:", err)
