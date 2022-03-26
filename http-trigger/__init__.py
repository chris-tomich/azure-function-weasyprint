import logging
import azure.functions as func
from weasyprint import HTML
import hashlib


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    logging.info(list(req.headers.keys()))
    logging.info(list(req.headers.values()))
    logging.info('request body hash ' + hashlib.md5(req.get_body()).hexdigest())

    # name = req.params.get('name')
    pdf = HTML(string=req.get_body().decode('utf-8')).write_pdf()

    logging.info('response body hash ' + hashlib.md5(pdf).hexdigest())

    return func.HttpResponse(pdf, mimetype='application/pdf')
