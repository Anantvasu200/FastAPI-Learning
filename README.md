# Pydantic Learning Notes

## What is Pydantic?

Pydantic is a Python library used for data validation, parsing, and serialization using Python type hints. It is widely used with FastAPI for request and response validation.

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

user = User(name="Anant", age=25)
print(user)
```

---

# BaseModel

`BaseModel` is the foundation of all Pydantic models.

```python
from pydantic import BaseModel

class User(BaseModel):
    username: str
    age: int
```

Benefits:

* Automatic type validation
* Data parsing
* Serialization support
* JSON schema generation

---

# Field Validator

`@field_validator` is used to validate a specific field.

```python
from pydantic import BaseModel, field_validator

class User(BaseModel):
    age: int

    @field_validator("age")
    @classmethod
    def age_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError("Age must be a positive integer")
        return value
```

### Key Points

* Validates a single field.
* Receives the field value.
* Must return the validated value.
* Raises `ValueError` when validation fails.

---

# Model Validator

`@model_validator` is used when validation depends on multiple fields.

```python
from pydantic import BaseModel, model_validator

class User(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def passwords_match(self):
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        return self
```

### Why `mode="after"`?

Because validation requires access to multiple fields after the model object has been created.

### Validator Modes

#### Before

```python
@model_validator(mode="before")
@classmethod
def validate_input(cls, data):
    return data
```

* Receives raw input data (dictionary).
* Runs before model creation.

#### After

```python
@model_validator(mode="after")
def validate_model(self):
    return self
```

* Receives the complete model object.
* Runs after model creation.

---

# Computed Field

`@computed_field` creates calculated fields based on existing fields.

```python
from pydantic import BaseModel, computed_field

class User(BaseModel):
    first_name: str
    last_name: str

    @computed_field
    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
```

Output:

```python
user.model_dump()
```

```json
{
  "first_name": "Anant",
  "last_name": "Awasthi",
  "full_name": "Anant Awasthi"
}
```

### Use Cases

* Full name generation
* Total price calculation
* Age category determination
* Derived fields

---

# Nested Models

A Pydantic model can contain another Pydantic model.

```python
from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str

class User(BaseModel):
    name: str
    address: Address
```

Example:

```python
user = User(
    name="Anant",
    address={
        "city": "Delhi",
        "state": "Delhi"
    }
)
```

Access nested data:

```python
print(user.address.city)
```

---

# Serialization

Serialization converts Python objects into dictionaries or JSON.

### Dictionary Serialization

```python
user.model_dump()
```

Output:

```python
{
    "name": "Anant",
    "age": 25
}
```

### JSON Serialization

```python
user.model_dump_json()
```

Output:

```json
{"name":"Anant","age":25}
```

---

# Deserialization

Deserialization converts JSON or dictionaries into Python objects.

### Dictionary to Object

```python
user = User.model_validate(data)
```

### JSON to Object

```python
user = User.model_validate_json(json_data)
```

---

# Dictionary Unpacking

```python
user_data = {
    "username": "Anant_Awasthi",
    "age": 25
}

user = User(**user_data)
```

Equivalent to:

```python
user = User(
    username="Anant_Awasthi",
    age=25
)
```

The `**` operator is called dictionary unpacking.

---

# Validation Errors

When validation fails, Pydantic raises a `ValidationError`.

```python
from pydantic import ValidationError

try:
    user = User(age=-5)
except ValidationError as e:
    print(e)
```

---

# Important Pydantic Methods

| Method                  | Purpose                        |
| ----------------------- | ------------------------------ |
| `model_dump()`          | Convert model to dictionary    |
| `model_dump_json()`     | Convert model to JSON          |
| `model_validate()`      | Create model from dictionary   |
| `model_validate_json()` | Create model from JSON         |
| `model_copy()`          | Create a copy of a model       |
| `model_fields`          | Access model field information |

---

# Quick Interview Notes

### What is Pydantic?

Pydantic is a Python data validation and settings management library that uses type hints to validate and parse data.

### What is BaseModel?

BaseModel is the parent class used to create Pydantic models.

### What is a Field Validator?

A field validator validates a single field and returns the validated value.

### What is a Model Validator?

A model validator validates the entire model and is useful when validation depends on multiple fields.

### What is a Computed Field?

A computed field generates a derived value from existing model fields.

### What is a Nested Model?

A nested model is a Pydantic model that contains another Pydantic model as a field.

### What is Serialization?

Serialization converts Python objects into JSON or dictionaries.

### What is Deserialization?

Deserialization converts JSON or dictionaries into Python objects.

---

# Summary

So far, I have learned:

* BaseModel
* Type Validation
* Field Validators
* Model Validators
* Computed Fields
* Nested Models
* Serialization
* Deserialization
* Dictionary Unpacking
* Validation Errors
* Common Pydantic Methods

These concepts form the foundation of using Pydantic effectively with FastAPI.
