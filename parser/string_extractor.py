import re

def extract_strings(filepath, min_length=4):
    with open(filepath, "rb") as f:
        data = f.read()
        pattern = re.compile(rb"[ -~]{%d,}" % min_length)
        strings = pattern.findall(data)
        result = []
        for s in strings:
            try:
                result.append(s.decode())
            except UnicodeDecodeError:
                continue
        return result
