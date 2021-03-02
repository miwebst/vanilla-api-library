import json
import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    response = {"text": "Python GetMessage 2020-10-2 15:08"}
    return func.HttpResponse(
        json.dumps(response),
        mimetype="application/json")
