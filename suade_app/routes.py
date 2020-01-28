from suade_app import app, con
from flask import render_template
from .generator import PDF_Generator, XML_Generator

@app.route('/')
@app.route('/index')
def index():
    rows = []
    for row in con.execute("select * from reports"):
        rows.append(row)
    
    pdf_gen = PDF_Generator()
    pdf_gen.create_report(rows[0])
    xml_gen = XML_Generator()
    xml_gen.create_report(rows[0])
    return render_template('index.html', title='Home', rows=rows)
