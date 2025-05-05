def hexdump(filepath, width=16):
    lines = []
    with open(filepath, "rb") as f:
        offset = 0
        while chunk := f.read(width):
            hex_bytes = " ".join(f"{b:02X}" for b in chunk)
            ascii_bytes = "".join(chr(b) if 32 <= b < 127 else '.' for b in chunk)
            line = f"{offset:08X}  {hex_bytes:<48}  {ascii_bytes}"
            lines.append(line)
            offset += width
    return lines
