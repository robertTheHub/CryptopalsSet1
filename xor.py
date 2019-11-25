import convert


def two_bytes(bytes_a, bytes_b):
    output = bytearray()
    for a, b in zip(bytes_a, bytes_b):
        output.append(a ^ b)
    return output


def two_hex_strings(string_a, string_b):
    bytes_a = convert.hex_string_to_bytes(string_a)
    bytes_b = convert.hex_string_to_bytes(string_b)
    output = two_bytes(bytes_a, bytes_b)
    return output


def byte_array_with_string(byte_array, string):
    temp_byte_array = convert.string_to_byte_array(string)
    remainder = len(byte_array) % len(string)
    divisor = len(byte_array) // len(string)
    other_byte_array = temp_byte_array[:] * divisor + temp_byte_array[:remainder]
    return two_bytes(byte_array, other_byte_array)
