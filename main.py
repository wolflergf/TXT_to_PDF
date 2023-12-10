import glob
from pathlib import Path
from fpdf import FPDF

# Create an instance of FPDF class with A4 paper size in portrait orientation
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Get all text files in the "Files" directory
filepaths = glob.glob("./Files/*.txt")

# Iterate over each text file
for filepath in filepaths:
    # Extract the filename (without extension) and capitalize it
    filename = Path(filepath).stem.capitalize()

    # Add a new page to the PDF and set the font for the title
    pdf.add_page()
    pdf.set_font("Times", size=18, style="B")

    # Add the title to the PDF
    pdf.cell(w=50, h=8, txt="{}".format(filename), ln=1) 

    # Open the text file and read its content
    with open(filepath, "r") as f:
        text = f.read()

        # Set the font for the text and add the text to the PDF
        pdf.set_font("Times", size=12)
        pdf.multi_cell(w=0, h=6, txt=text, align="J", border=0)

# Write the PDF document to a file
pdf.output("./PDF/animals.pdf")
