from ast import Str
import os
import json
from prometheus_client import start_http_server
from services.fake_service import FakeService
from services.logger import logger

task_1_e = ["Winterallee 3" , "Musterstrasse 45", "Blaufeldweg 123B"  ]

task_1_t_0=  json.dumps({"street": "Winterallee", "housenumber": "3"})
task_1_t_1= json.dumps({"street": "Musterstrasse", "housenumber": "45"})
task_1_t_2 =  json.dumps({"street": "Blaufeldweg", "housenumber": "123B"})

task_1_t = [task_1_t_0, task_1_t_1, task_1_t_2]

"""
Application for splitting concatenated street names and numbers into formatted json objects using different processors.
"""


def simple_processor(concatenated_street: Str, test: json) -> json:

    [street, housenumber] = concatenated_street.split()
    x = {
    "street": street,
    "housenumber": housenumber
    }
    complete_street = json.dumps(x)

    print(complete_street==test)

if __name__ == "__main__":
    
    simple_processor(task_1_e[0], task_1_t_0)
    simple_processor(task_1_e[1], task_1_t_1)
    simple_processor(task_1_e[2], task_1_t_2)