import json
import logging

import aws_lambda_logging
import requests

log = logging.getLogger()


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        Really simple event (name)

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    Polite Greeting: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    aws_lambda_logging.setup(level="INFO",
                             aws_request_id=context.aws_request_id)

    name = event['name']

    try:
        ip = requests.get("http://checkip.amazonaws.com/")
    except requests.RequestException as e:
        print(e)

        raise e

    message = json.dumps({
        "greeting": f"Hello, {name}.  So wonderful to see you!",
        "location": ip.text.replace("\n", "")
    })
    
    log.info(message)
    return message
