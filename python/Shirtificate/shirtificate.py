from fpdf import FPDF


class Shirtificate(FPDF):
    def header(self):
        # Add a title to the PDF
        self.set_font("Arial", size=24, style="B")
        self.cell(0, 10, "CS50 Shirtificate", ln=True, align="C")
        self.ln(10)  # Space below header


def create_shirtificate(name):
    # Create a PDF instance
    pdf = Shirtificate()
    pdf.set_auto_page_break(auto=False)  # Disable automatic page breaks
    pdf.add_page(orientation="P", format="A4")  # Portrait, A4

    # Add the shirt image
    pdf.image("shirtificate.png", x=25, y=60, w=160)  # Adjust image position and size

    # Add the user's name on the shirt
    pdf.set_font("Arial", size=36, style="B")
    pdf.set_text_color(255, 255, 255)  # White text
    pdf.cell(0, 130, ln=True)  # Move to where the text should be
    pdf.cell(0, 10, f"{name} took CS50", align="C")  # Centered name text

    # Save the PDF
    pdf.output("shirtificate.pdf")
    print(f"Shirtificate for {name} created as 'shirtificate.pdf'.")


# Prompt for user's name
if __name__ == "__main__":
    name = input("What's your name? ")
    create_shirtificate(name)
