def read_file_content(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()

def write_to_file(path, content):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)
