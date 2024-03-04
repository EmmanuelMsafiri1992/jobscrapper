import os
from dotenv import load_dotenv, find_dotenv
import json
import base64


def get_service_account_key(forMainDB: bool = False) -> dict:
    """
    Returns service account key for firestore

    Args:
        forMainDB (bool, optional): If false, service account key for database
        containing only statistics is returned. If true, service account
        key for database containing all jobs is returned. Defaults to False.

    Returns:
        dict: Service account key
    """
    load_dotenv(find_dotenv())
    var_name = ""
    if forMainDB:
        var_name = 'SAK_MAIN_DB'
    else:
        var_name = 'SAK_STATS_DB'

    encoded_key = os.getenv(var_name)

    # https://stackoverflow.com/questions/50693871/error-in-json-loads-for-data-that-has-base64-decoding-applied
    dic = base64.b64decode(str(encoded_key)[2:-1]).decode('utf-8')
    return json.loads(dic)


def service_key_to_base64(service_key: dict) -> bytes:
    """
    Converts firebase service key to base64.

    Args:
        service_key (dict): Service account key generated in firebase project
        settings. Check docs for an example of a service key.

    Returns:
        bytes: base64 string. String begins with `b'` and ends with `'`
    """

    # convert json to a string
    str_service_key = json.dumps(service_key)

    # encode service key
    encoded_service_key = base64.b64encode(str_service_key.encode('utf-8'))

    # Format of encoded_service_key: b'a_lot_of_chars'
    return encoded_service_key


if __name__ == "__main__":
    service_key = {
        "type": "service_account",
        "project_id": "emphx-innovative-solutions",
        "private_key_id": "600c3c8cea887c709b24244db29b8146b6dd2170",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCmIUNMcVQgyYfD\njX0JabdNHEs+PLlKGHaS7vR5wYXOdvy71S/yS5TV1CE6AkU59qPOlOEdux91leCh\nPzigoGlCUSDHVyRwZSuym03KorNexsVrDc9eQ8/mm2qUbtUEXq66JQ/Q25cZiVoF\nJZD8YUnQIz9vWK1p+aI1pg6xDhStY13mrQiFzl2hwJVACg7WcikAWioGBnRfAQCS\ntz0ISPU3kqgRUI8funZcF7ct5geYJtBp7baS4q1hMbC+H/V+iKjxhjwLJjevbM/2\nwI5qANcRb/4ikZMxtKNExFJMrHbL9hdwov6WB8FPNyw48gV+cAUuzMl+LgLSlRI1\nCQNWv95bAgMBAAECggEAAPCWeW99DVTqZ+VykdRKIjcJ7WJAOUy72vyKndgyXzwp\nx+EW6B6zTsTYspslE3Ftk8TauAKYdAo+mvYQ6it23fFe+NeIjkDSkQWIhxw4Lnx0\nImOlHFHf6rW7q0THPWHkSJMU4v1jBgdWaoAZIYYQ4rmWYcek3wLr65VR41ICmhYg\n1TGKr0QTs7YMEgiFF+/NZRaZ6i6e7jNpDTDeFTmcvfBi4pRjwOuRJOq8c11kDJ8/\nq2kfjib78PmsRa5NkJjGxWyQk11dy0I1okK/saTPGzxzUNWo6It06ahoby+/111X\no7/YhWRg7bEOb2Qe20IN/jbdweUl7nlTzNzHHqgI1QKBgQDRLLcn0DHHDMC/qxnE\nhWs9U0Ml2KvEKsLmSeoUPTDvcc/QMhq9am0ts4YKpZ2kDKU24hjkxHpNM6rWbvLP\nuODLCi2TrdOWle5fUUqqgDItl1F8lLWk9hGz97CW/9EYI0prvviE4RXlECCUVTzq\nx7mO4juwkCjY2hCkRzxYi5Iw7QKBgQDLUcJ84DCr8hvDJ5PU8y38234WhUO9em2t\nkHift1pVfZaAE1o/qVItcmeyYl9e8XFu2YxcYFwctCDE+SABNoxLvnqmTMUMs2wP\nFfVEiGbpzzYCnjUe4IUgOh4pXunUjVeP3Srb3dER8T0nOguKJZ8NWuyJJ8YnlbNk\nr26/66QLZwKBgB+TVW6gIfN/PFVymagtz7tpJzi+VWd+YP9sZvZ5Kjrq/kjaV2kC\neMquT+yphXtvIT2AsetOsXuX8hD+nI64xM5BkhG56rfPmDUxS0kjou946ScaN7VY\nI+H74N9abJDtOt267T75z1lNru1VVKXIUn18LzB/AnuBp4N08WoYX5AdAoGAXpWy\nfJVvDw6ai7cltrNKeY9CoQdt8/+4dj33X5XUmGDMWtil62fBqxLF2t6Yr3py4rah\n7XeGYnQJqpiaovXVXodGV4bvRHFTm9EDQNaTycFzxtQCslKQm+VtkqFs9kyqp2qk\nPZR7ZnVrlYwTQjkuPPBHiabPMCscQYK7at0ce5ECgYBN9Tr7s53ZiF2StpZSeLKC\n+yis8YJ4K6KgDVmaJLhtGSo6fDU8BT5P9pXmwp1uHb2TvNUVvu/uCdzJFpzjYNnd\nQE3Ykr/NkTguBfLnBt2jzUPQsoUHdUaH+AFzt3InLs4hDM2UO+c8EuusUJbl+4Vz\n0tVTD0Qbkg6f9MXXS1KRFw==\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-ugrdo@emphx-innovative-solutions.iam.gserviceaccount.com",
        "client_id": "104427152935865542227",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-ugrdo%40emphx-innovative-solutions.iam.gserviceaccount.com"
    }
    print(service_key_to_base64(service_key))
    # b'eyJ0eXBlIjogInNlcnZpY2VfYWNjb3VudCIsICJwcm9qZWN0X2lkIjogInh4eCIsICJwcml2YXRlX2tleV9pZCI6ICJ4eHgiLCAicHJpdmF0Z
    # V9rZXkiOiAieHh4eCIsICJjbGllbnRfZW1haWwiOiAieHh4eC5jb20iLCAiY2xpZW50X2lkIjogInh4eHgiLCAiYXV0aF91cmkiOiAieHh4eCIsI
    # CJ0b2tlbl91cmkiOiAieHh4eCIsICJhdXRoX3Byb3ZpZGVyX3g1MDlfY2VydF91cmwiOiAieHh4eCIsICJjbGllbnRfeDUwOV9jZXJ0X3VybCI6ICJ4eHh4In0='
