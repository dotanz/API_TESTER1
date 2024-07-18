import xml.etree.ElementTree as ET


def add_base64_to_xml(xml_string, base64_string):
    # Parse the XML string
    root = ET.fromstring(xml_string)

    # Find or create the <MAC> element
    mac_element = root.find('.//MAC')
    if mac_element is None:
        mac_element = ET.SubElement(root, 'MAC')

    # Set the text of the <MAC> element to the Base64 string
    mac_element.text = base64_string

    # Convert the modified XML tree back to a string
    modified_xml_string = ET.tostring(root, encoding='unicode')

    return modified_xml_string


'''
# Example usage
if __name__ == "__main__":
    print("Enter the XML string (end with an empty line):")
    xml_lines = []
    while True:
        line = input()
        if line == "":
            break
        xml_lines.append(line)

    xml_string = "\n".join(xml_lines)

    base64_string = input("Enter the Base64 string: ")

    modified_xml_string = add_base64_to_xml(xml_string, base64_string)
    print("Modified XML with <MAC> field:")
    print(modified_xml_string)
'''
