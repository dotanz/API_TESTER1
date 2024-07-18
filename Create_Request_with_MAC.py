import Add_MACKEY_to_XML
import SHA256_converter
import HEX_encode_to_BASE64
import Add_MAC_to_XML

MAC_Key = "FjhHHd7gHzEOoEnL"
print("Enter the XML string (end with an empty line):")
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

xml_string = "\n".join(lines)

mackey_appended_to_xml = Add_MACKEY_to_XML.append_to_xml(xml_string, MAC_Key)
hex_string = SHA256_converter.sha256_encode_xml(mackey_appended_to_xml)
base64_string = HEX_encode_to_BASE64.hex_to_base64(hex_string)

final_XML = Add_MAC_to_XML.add_base64_to_xml(xml_string, base64_string)

print(final_XML)
