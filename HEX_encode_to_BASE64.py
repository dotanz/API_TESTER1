import base64


def hex_to_base64(hex_string):
    # Decode the HEX string to bytes
    byte_data = bytes.fromhex(hex_string)

    # Encode the bytes to Base64
    base64_encoded = base64.b64encode(byte_data)

    # Convert the Base64 bytes to a string
    base64_string = base64_encoded.decode()

    return base64_string


'''
# Example usage
if __name__ == "__main__":
    hex_string = input("Enter the HEX string: ")
    base64_string = hex_to_base64(hex_string)
    print(f"Base64 encoded string: {base64_string}")
'''
