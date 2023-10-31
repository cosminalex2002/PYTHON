# The build_xml_element function receives the following parameters: tag, content, and key-value elements given as name-parameters. Build and return a string that represents the corresponding XML element. Example: build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ") returns the string = "<a href="http://python.org \ "_class = " my-link \ "id = " someid \ "> Hello there "

def xml(tag, content, **kwargs):
    xml = f"<{tag}"
    for key, value in kwargs.items():
        xml += f" {key}=\"{value}\""
    xml += f"> {content} </{tag}>"
    
    return xml

result = xml("a", "Hello there", href="http://python.org", _class="my-link", id="someid")
print(result)
