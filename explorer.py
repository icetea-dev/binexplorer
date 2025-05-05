from parser.hex_view import hexdump
from parser.string_extractor import extract_strings
from parser.pe_parser import analyze_pe
from utils.format import save_report
import argparse
from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            "Binary analysis tool (hexdump, strings, PE)\n\n"
            "Example usage:\n"
            "  python explorer.py /path/to/file.exe --output report.txt\n"
            "  python explorer.py /path/to/file.dll"
        ),
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("filepath", help="File to analyze (.exe, .dll, etc.)")
    parser.add_argument("--output", help="Name of the report file (e.g., myreport.txt)")
    return parser.parse_args()

def main():
    args = parse_args()
    filepath = args.filepath
    report_name = args.output or f"{Path(filepath).stem}_report.txt"

    print("[*] Analysis in progress...")

    hex_lines = hexdump(filepath)
    strings = extract_strings(filepath)
    pe_info = analyze_pe(filepath)

    save_report(filepath, hex_lines, strings, pe_info, output_file=report_name)
    print(f"[+] Report generated in {report_name}")


if __name__ == "__main__":
    main()
