from services.simple_processor import simple_processor

"""
Application for splitting concatenated street names and numbers into
formatted json objects using different processors.
"""

simple_data = ["Winterallee 3", "Musterstrasse 45", "Blaufeldweg 123B"]

if __name__ == "__main__":
    print("This is the main app")
    simple_processor(simple_data)
