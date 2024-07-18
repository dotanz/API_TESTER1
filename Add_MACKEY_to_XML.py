def append_to_xml(xml_string, append_string):
    # Remove any trailing whitespace from the XML string
    xml_string = xml_string.rstrip()

    # Append the new string to the XML
    modified_xml_string = xml_string + append_string

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

    append_string = input("Enter the string to append: ")

    modified_xml_string = append_to_xml(xml_string, append_string)
    print("Modified XML:")
    print(modified_xml_string)
'''
