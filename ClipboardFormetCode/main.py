import re
import pyperclip

def compress_code(code: str) -> str:
    lines = code.split('\n')
    compressed_lines = []
    for line in lines:
        line = line.strip() # Remove leading and trailing whitespace
        line = re.sub(r'\s*([=+\-*/(,)])\s*', r'\1', line) # Remove spaces around operators and brackets
        compressed_lines.append(line)
    compressed_code = ' '.join(compressed_lines)
    return compressed_code

if __name__ == "__main__":
    code = pyperclip.paste()
    compressed = compress_code(code)
    pyperclip.copy(compressed)