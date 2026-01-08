"""
Example consumer script for demo-elt-framework.

Before running:
pip install demo-elt-framework @ <WHEEL_URL>

Then run:
python consumer_example.py
"""

from demo_elt_framework.math_ops import add, subtract, divide
from demo_elt_framework.transforms import clean_columns, dedupe

def main():
    print("Math operations:")
    print("Add:", add(10, 5))
    print("Subtract:", subtract(10, 5))
    print("Divide:", divide(10, 2))

    print("\nTransformations:")
    cols = ["First Name", " Last Name ", "City"]
    print("Clean columns:", clean_columns(cols))

    data = [
        {"id": 1, "name": "Alice"},
        {"id": 1, "name": "Alice Duplicate"},
        {"id": 2, "name": "Bob"},
    ]
    print("Deduped records:", dedupe(data, ["id"]))

if __name__ == "__main__":
    main()
