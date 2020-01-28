from fpdf import FPDF
import os
import json
import dicttoxml
from xml.dom.minidom import parseString

FILE_ROOT = "suade_app/reports"
PDF_ROOT = os.path.join(FILE_ROOT, "pdf")
XML_ROOT = os.path.join(FILE_ROOT, "xml")

class PDF_Generator():
    def __init__(self):
        self.pdf = FPDF()

    def create_report(self, data):
        """
        Generates report for a given data row. The data is provided as a tuple.
        param data: tuple of data from database
        return: file_name
        """
        # Set up
        self.pdf.add_page()
        self.pdf.set_font("Arial", size=32)
        # Convert data to be accessible and set up vars
        [id, entry] = list(data)
        filename = "report_"+str(id)+".pdf"
        entry = json.loads(entry)
        # Heading
        self.pdf.cell(200, 10, txt="The Report", ln=1, align="C")

        # Data
        self.pdf.set_font("Arial", size=12)
        self.pdf.cell(200, 10, txt=entry["organization"], ln=1, align="C")
        self.pdf.cell(200, 10, txt=entry['reported_at'], ln=1, align="C")
        self.pdf.cell(200, 10, txt=entry['created_at'], ln=1, align="C")
        self.pdf.cell(200, 10, txt="Inventory", ln=1, align="C")
        for row in entry['inventory']:
            self.pdf.cell(200, 10, txt=row['name'], ln=1, align="C")
            self.pdf.cell(200, 10, txt=row['price'], ln=1, align="C")
        output_location = os.path.join(PDF_ROOT, filename)
        self.pdf.output(output_location)
        return output_location

class XML_Generator():

        def __init__(self):
            pass

        def create_report(self, data):
            """
            Generates an xml report for a given data entry. Data is supplied as a tuple string.
            param data: string tuple
            return: file_name
            """
            [id, entry] = list(data)
            filename = "report_"+str(id)+".xml"
            entry = json.loads(entry)

            xml = dicttoxml.dicttoxml(entry)
            dom = parseString(xml)
            output_location = os.path.join(XML_ROOT, filename)
            with open(output_location, "w+") as fp:
                fp.write(dom.toprettyxml())
                fp.close()
            return output_location
