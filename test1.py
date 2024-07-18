import hashlib

def sha256_encode_xml(xml_string):
    # Encode the XML string to bytes
    encoded_xml = xml_string.encode()

    # Create a SHA-256 hash object
    sha256_hash = hashlib.sha256()

    # Update the hash object with the encoded XML content
    sha256_hash.update(encoded_xml)

    # Get the hexadecimal representation of the hash
    hex_digest = sha256_hash.hexdigest()

    return hex_digest

# Example usage
if __name__ == "__main__":
    print("Paste the XML string and type 'END' on a new line to finish:")
    lines = []
    while True:
        line = input()
        if line.strip() == "</TRANSACTION>":
            break
        lines.append(line)

    xml_string = "\n".join(lines)
    encoded_string = sha256_encode_xml(xml_string)
    print(f"SHA-256 encoded XML content: {encoded_string}")
