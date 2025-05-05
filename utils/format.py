def save_report(filepath, hex_lines, strings, pe_info, output_file="report.txt"):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"--- File Analysis: {filepath} ---\n\n")

        f.write("[Complete Hexdump]\n")
        f.writelines(line + "\n" for line in hex_lines)
        f.write("\n")

        f.write(f"[Strings] ({len(strings)} found)\n")
        for s in strings:
            f.write(f"- {s}\n")
        f.write("\n")

        if pe_info:
            f.write("[PE Info]\n")
            f.write(f"Entrypoint: {pe_info['entrypoint']}\n\n")
            f.write("Sections:\n")
            for sec in pe_info["sections"]:
                f.write(f" - {sec['name']} | VA: {sec['virtual_address']} | Size: {sec['raw_size']} bytes\n")
            f.write("\n")

            if "exports" in pe_info:
                f.write("Exports:\n")
                for exp in pe_info["exports"]:
                    f.write(f" - {exp}\n")

                f.write("\n[Header Style Export]\n")
                for exp in pe_info["exports"]:
                    f.write(f"extern void {exp}(void);\n")
        else:
            f.write("[PE Info] Not applicable (not a recognized .exe/.dll)\n")
