from functools import singledispatch


@singledispatch
def process(data):
    """Default behavior for unrecognized types."""
    print(f"Received data: {data}")


@process.register(str)
def _(data):
    """Handle string objects."""
    print(f"Processing a string: {data}")


@process.register(int)
def _(data):
    """Handle integer objects."""
    print(f"Processing an integer: {data}")


@process.register(list)
def _(data):
    """Handle list objects."""
    print(f"Processing a list of length: {len(data)}")


# Testing the generic function
process(42)        # Outputs: Processing an integer: 42
process("hello")   # Outputs: Processing a string: hello
process([1, 2, 3]) # Outputs: Processing a list of length: 3
process(2.5)       # Outputs: Received data: 2.5
