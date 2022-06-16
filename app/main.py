import json
from services.middle_processor import middle_processor
from services.simple_processor import simple_processor

"""
Application for splitting concatenated street names and numbers into formatted json objects using different processors.
"""

task_1_e = ["Winterallee 3", "Musterstrasse 45", "Blaufeldweg 123B"]
task_1_t_0 = json.dumps({"street": "Winterallee", "housenumber": "3"}, ensure_ascii=False)
task_1_t_1 = json.dumps({"street": "Musterstrasse", "housenumber": "45"}, ensure_ascii=False)
task_1_t_2 = json.dumps({"street": "Blaufeldweg", "housenumber": "123B"}, ensure_ascii=False)
task_1_t = [task_1_t_0, task_1_t_1, task_1_t_2]

task_2_e = ["Am Bächle 23", "Auf der Vogelwiese 23 b"]
task_2_t_0 = json.dumps({"street": "Am Bächle", "housenumber": "23"},ensure_ascii=False)
task_2_t_1 = json.dumps({"street": "Auf der Vogelwiese", "housenumber": "23 b"},ensure_ascii=False)
task_2_t = [task_2_t_0, task_2_t_1]

if __name__ == "__main__":

    # for index in range(0,len(task_1_e)):
    #     simple_processor(task_1_e[index], task_1_t[index])

    for index in range(0,len(task_2_e)):
        middle_processor(task_2_e[index], task_2_t[index])
