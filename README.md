# BinExplorer

A simple, terminal‑based binary analysis tool written in Python.  
BinExplorer lets you inspect any binary file (PE, raw `.bin`, etc.) by dumping its bytes, extracting printable strings, and—when applicable—parsing PE headers (entrypoint, sections, exports). Results are saved in a clean, detailed report.

---

## 🚀 Features

- **Hexdump**  
  Full hexadecimal + ASCII dump of the entire file.

- **Strings Extraction**  
  Finds all printable ASCII sequences (minimum length configurable).

- **PE Analysis**  
  - Detects Windows Portable Executable files (`.exe`, `.dll`).  
  - Reports entrypoint address.  
  - Lists all sections (name, virtual address, raw size).  
  - Extracts exported symbols (functions) and generates C‑style `extern` declarations.

- **Custom Report**  
  - Save analysis to a custom‑named `.txt` report.  
  - Organized sections: raw hexdump, strings list, PE info, exports, C headers.

---

## 📦 Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your‑username/binexplorer.git
   cd binexplorer
   pip install -r requirements.txt
   python explorer.py <path/to/file> [--output report_name.txt]
   ```

## 👀 Examples
   ```bash
   # Analyze notepad.exe and save as notepad_report.txt
   python explorer.py C:/Windows/System32/notepad.exe

   # Analyze a DLL and save custom report
   python explorer.py myplugin.dll --output plugin_analysis.txt
   ```

- **BinExplorer will**
  Print a progress message.
  Extract all printable strings.
  If it’s a PE file, parse headers and exports.
  Save a structured, human‑readable report.

## 📄 Sample Report
   ```csharp
   --- Analysis of file: myplugin.dll ---
   
   [Hexdump Complete]
   00000000  4D 5A 90 00 03 00 00 00 …  
   00000010  …  
   …
   
   [Strings] (123 found)
   - Hello, World!
   - MSVCRT.dll
   - myplugin_init
   …
   
   [PE Info]
   Entrypoint : 0x1000
   
   Sections :
    - .text | VA: 0x1000 | Size: 1536 bytes
    - .rdata | VA: 0x2000 | Size: 512 bytes
    - .data | VA: 0x3000 | Size: 256 bytes
   
   Exports :
    - initialize
    - process_data
    - shutdown
   
   [Header Style Export]
   extern void initialize(void);
   extern void process_data(void);
   extern void shutdown(void);

