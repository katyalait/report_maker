from suade_app import app, con
from flask import render_template, send_from_directory, send_file
from .generator import PDF_Generator, XML_Generator, XML_ROOT, PDF_ROOT
import json

@app.route('/')
@app.route('/index')
def index():
    """
    Home page view. Lists all files found in remote database.
    """
    rows = []
    for row in con.execute("select * from reports"):
        [id, entry] = list(row)
        entry = json.loads(entry)
        rows.append([id,entry["organization"]])
    return render_template('index.html', title='Home', rows=rows)

@app.route('/report/xml/<id>')
def create_xml(id):
    """
    XML generator for requested file.
    """
    query = "select * from reports where id=" + str(id)
    [id, data] = list(con.execute(query).first())
    data = json.loads(data)
    xml_gen = XML_Generator()
    filepath = xml_gen.create_report([id, data])

    return send_file(filepath, as_attachment=True)

@app.route('/report/pdf/<id>')
def create_pdf(id):
    """
    PDF Generator for requested file.
    """
    query = "select * from reports where id=" + str(id)
    [id, data] = list(con.execute(query).first())
    data = json.loads(data)
    pdf_gen = PDF_Generator()
    filepath = pdf_gen.create_report([id, data])

    return send_file(filepath, as_attachment=True)
