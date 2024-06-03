import sys
import json

def json_validation():
    try:
        with open(sys.argv[1]) as json_file:
            data = json.load(json_file)
    except TypeError as Type:
        print(Type)
    except FileNotFoundError as File:
        print(File)
    except json.decoder.JSONDecodeError as JSON:
        print(JSON)
    except Exception as e:
        print(e)

for x in sys.argv[1:]:
    print(f"Argument {x}")