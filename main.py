import sys
import json

class JsonTask():
    def __init__(self, file):
        self.file = file
        self.dane = None

    def json_validation(self):
        try:
            with open(sys.argv[1]) as json_file:
                self.dane = json.load(json_file)
            print("Dane zostały poprawnie załadowane i zweryfikowane!")
        except FileNotFoundError:
            print("Nie znaleziono takiego pliku")
        except json.decoder.JSONDecodeError:
            print("Plik json jest nieprawidłowy")
        except Exception as e:
            print(e)

    def json_save():
        try:
            with open(sys.argv[1], 'w') as json_file:
                json.dump(json_file)
        except json.decoder.JSONDecodeError:
            print("Plik json jest nieprawidłowy")
        except Exception as e:
            print(e)

if __name__ == '__main__':
    if ".json" in sys.argv[1]:
        json_task = JsonTask(sys.argv[1])
        json_task.json_validation()