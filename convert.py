import base64


def hex_string_to_bytes(hex_string):
    return bytes.fromhex(hex_string)


def bytes_to_base64(a_bytes):
    return base64.b64encode(a_bytes)


def hex_string_to_base64(a_string):
    a_bytes = hex_string_to_bytes(a_string)
    return bytes_to_base64(a_bytes)


def string_to_byte_array(a_string):
    output = bytearray()
    for letter in a_string:
        output.append(ord(letter))
    return output


def bytes_to_string(a_bytes):
    try:
        return a_bytes.decode("utf-8")
    except Exception:
        try:
            output = ""
            for aByte in a_bytes:
                output += chr(aByte)
            return output
        except Exception:
            return ""


def base64_to_byte_array(block):
    return base64.b64decode(block)
