import pefile

def analyze_pe(filepath):
    try:
        pe = pefile.PE(filepath)
        info = {
            "entrypoint": f"0x{pe.OPTIONAL_HEADER.AddressOfEntryPoint:X}",
            "sections": []
        }
        for section in pe.sections:
            info["sections"].append({
                "name": section.Name.decode(errors="ignore").rstrip('\x00'),
                "virtual_address": f"0x{section.VirtualAddress:X}",
                "raw_size": section.SizeOfRawData
            })

        if hasattr(pe, 'DIRECTORY_ENTRY_EXPORT'):
            exports = [e.name.decode() for e in pe.DIRECTORY_ENTRY_EXPORT.symbols if e.name]
            info["exports"] = exports

        return info
    except pefile.PEFormatError:
        return None
