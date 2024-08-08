import os
import re
from jinja2 import Environment, FileSystemLoader


def parse_file(file) -> [str]:
    file_path = os.path.join('..', file)
    tokens = []
    with open(file_path, 'r') as lines:
        for line in lines:
            token = re.split('\\s', line)
            tokens.append(token)
        return tokens


def generate_python_script(tokens: [[str]]) -> [str]:
    template_info = {}
    for token in tokens:
        for lexeme in token:
            match lexeme:
                case "flow":
                    template_info["flow_name"] = write_next(token, token.index(lexeme))
                case 'def':
                    template_info["call_method_definition"] = "pass\n"
    return template_info


def write_next(token: [str], index: int) -> str:
    if token[index + 1] is not None:
        lexeme = re.split(':', token[index + 1])
        return lexeme[0]
    else:
        raise IndexError


def find_fy_files(root: str = '..') -> str:
    for fy_file in os.listdir('..'):
        if fy_file.endswith('.fy'):
            return fy_file


def create_dir(output_directory: str) -> None:
    open(output_directory, 'a').close()


def write_to_jinja2_template(content: str, dir_to_write: str) -> None:
    with open(dir_to_write, "w", encoding="UTF-8") as fy_to_py:
        fy_to_py.write(content)


if __name__ == '__main__':
    py_file = "testing.py"
    file = find_fy_files()
    tok = parse_file(file)
    temp_info = generate_python_script(tok)
    create_dir(py_file)
    env = Environment(loader=FileSystemLoader("../templates/"))
    template = env.get_template("test.jinja2")
    content = template.render(temp_info)
    write_to_jinja2_template(content, py_file)
