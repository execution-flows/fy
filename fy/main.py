import re


def parse_file(file) -> [str]:
    tokens = None
    with open(file, 'r') as lines:
        for line in lines:
            tokens = re.findall(r'\w+|->|:', line)
        return tokens


def generate_python_script(tokens: [str], output_directory: str) -> None:
    open(output_directory, 'a').close()
    with open(output_directory, 'w') as file:
        for token in tokens:
            match token:
                case "flow":
                    file.write(f"class {write_next(tokens, tokens.index(token))}():\n")
                # This will be place where arguments get passed
                # case "default":
                #     file.write(f"(ExecutionFlow_Base[None]):\n")
                # : marks end of correct fy
                case ':':
                    file.write(f"\t def __call__(self) -> None:\n")
                    file.write(f"\t\tpass")


def write_next(tokens: [str], index: int) -> str:
    if tokens[index+1] is not None:
        return tokens[index+1]
    else:
        raise IndexError


if __name__ == '__main__':
    received = parse_file("/home/jere/fy/testing.fy")
    generate_python_script(received, "testing.py")
