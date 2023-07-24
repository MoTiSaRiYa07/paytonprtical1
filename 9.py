import sys

def display_size(data, data_type):
    size = sys.getsizeof(data)
    print(f"Size of {data_type}: {size} bytes")

if __name__ == "__main__":
    data_types = [
        10,           # int
        3.14,         # float
        "Hello",      # string
        [1, 2, 3],    # list
        (1, 2, 3),    # tuple
        {1: 'one', 2: 'two'},  # dictionary
        True,         # bool
        None          # NoneType
    ]

    for i, data in enumerate(data_types, start=1):
        data_type = type(data).__name__
        display_size(data, data_type)
