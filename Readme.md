# Text to PDF Converter

This is a Python script that converts text files into a PDF document. It uses the `glob`, `pathlib`, and `fpdf` libraries.

## How it works

1. The script creates an instance of the `FPDF` class with A4 paper size in portrait orientation.
2. It then finds all text files in the "Files" directory.
3. For each text file, it extracts the filename (without the extension) and capitalizes it.
4. This filename is then added to the PDF as a new page with a title. The title is set in bold Times font, size 18.
5. The script then opens the text file, reads the entire content of the file into a string, and adds this text to the PDF. The text is set in Times font, size 12.
6. After all the text files have been processed and their content added to the PDF, the script writes the PDF document to a file named "animals.pdf" in the "PDF" directory.

## Usage

To use this script, simply place your text files in the "Files" directory and run the script. The resulting PDF will be saved in the "PDF" directory.

## Dependencies

This script requires the `glob`, `pathlib`, and `fpdf` libraries. You can install them using pip:

```bash
pip install glob2 pathlib fpdf