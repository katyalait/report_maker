import pytest
import os
import tempfile
import json
from suade_app import app

@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])

def test_file_generation(client):
    """
    Test that file is created
    """
    rv = client.get("/report/xml/2", follow_redirects=True)
    print(rv)
    pv = client.get("/report/pdf/2", follow_redirects=True)
    assert os.path.exists("suade_app/reports/xml/report_2.xml")

def test_index(client):
    """
    Test the index view works
    """
    resp = client.get("/index", data=dict(title="Home", rows="[[1],[\'Org Test\']]"), follow_redirects=True)
    assert resp.status_code == 200
