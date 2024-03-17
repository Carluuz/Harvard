from fpdf import FPDF
from fpdf.enums import XPos


pdf = FPDF()


def main():
    name = input("Name: ")
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 40)
    pdf.set_text_color(200, 0, 0)
    pdf.cell(0, 50, "CS50 Shirtificate", align='C')
    pdf.ln(50)
    pdf.image("shirtificate.png", 5, 80, 200)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 180, f'{name} took CS50', align='C')
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()


pdf = FPDF(orientation="P", unit="mm", format="A4")
