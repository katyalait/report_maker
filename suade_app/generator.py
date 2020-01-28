from fpdf import FPDF
import os
import json
import dicttoxml
from xml.dom.minidom import parseString

FILE_ROOT = "suade_app"
PDF_ROOT = "reports/pdf"
XML_ROOT = "reports/xml"

class PDF_Generator():
    def __init__(self):
        self.pdf = FPDF()

    def create_report(self, data):
        """
        Generates report for a given data row. The data is provided as a tuple.
        param data: tuple of data from database
        return: filename
        """
        # Set up
        self.pdf.add_page()
        self.pdf.set_font("Arial", size=32)
        # Convert data to be accessible and set up vars
        [id, entry] = data
        filename = "report_"+str(id)+".pdf"

        # Border
        self.pdf.set_line_width(1)
        self.pdf.set_fill_color(0, 255, 0)
        self.pdf.rect(10, 10, 190, 270)

        # Heading
        self.pdf.cell(190, 20, txt="The Report", ln=3, align="C")

        # Data
        self.pdf.set_font("Arial", size=12)
        self.pdf.cell(130)
        self.pdf.cell(0, 10, txt="Organization: " + entry["organization"], ln=1)
        self.pdf.cell(130)
        self.pdf.cell(0, 10, txt="Reported at: " + entry['reported_at'], ln=1)
        self.pdf.cell(130)
        self.pdf.cell(0, 10, txt="Created at: " + entry['created_at'], ln=1)
        self.pdf.cell(190, 10, txt="Inventory", ln=1, align="C")
        for row in entry['inventory']:
            self.pdf.cell(200, 10, txt= row['name'] + ": " + row['price'], ln=1, align="C")
        output_location = os.path.join(FILE_ROOT, os.path.join(PDF_ROOT, filename))
        self.pdf.output(output_location)
        return os.path.join(PDF_ROOT, filename)

class XML_Generator():

        def __init__(self):
            pass

        def create_report(self, data):
            """
            Generates an xml report for a given data entry. Data is supplied as a tuple string.
            param data: string tuple
            return: filename
            """
            [id, entry] = data
            filename = "report_"+str(id)+".xml"
            xml = dicttoxml.dicttoxml(entry)
            dom = parseString(xml)
            output_location = os.path.join(FILE_ROOT, os.path.join(XML_ROOT, filename))
            with open(output_location, "w+") as fp:
                fp.write(dom.toprettyxml())
                fp.close()
            return os.path.join(XML_ROOT, filename)
