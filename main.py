import sys
import json
import yaml

class JsonTask():
    def __init__(self, file):
        self.file = file
        self.dane = None

    def json_validation(self):
        try:
            with open(sys.argv[1]) as json_file:
                self.dane = json.load(json_file)
            print("Dane z pliku JSON zostały poprawnie załadowane i zweryfikowane!")
        except FileNotFoundError:
            print("Nie znaleziono takiego pliku")
        except json.decoder.JSONDecodeError:
            print("Plik json jest nieprawidłowy")
        except Exception as e:
            print(e)

    def json_save(self):
        try:
            with open("nowy_plik.json", 'w') as json_file:
                json.dump(self.dane, json_file)
        except json.decoder.JSONDecodeError:
            print("Plik json jest nieprawidłowy")
        except Exception as e:
            print(e)

class YamlTask():
    def __init__(self, file):
        self.file = file
        self.dane = None

    def yaml_validation(self):
        try:
            with open(sys.argv[1]) as yaml_file:
                self.dane = yaml.load(yaml_file, Loader=yaml.FullLoader)
            print("Dane z pliku YAML zostały poprawnie załadowane i zweryfikowane!")
        except FileNotFoundError:
            print("Nie znaleziono takiego pliku")
        except yaml.scanner.ScannerError:
            print("Plik yaml jest nieprawidłowy")
        except Exception as e:
            print(e)

if __name__ == '__main__':
    if ".json" in sys.argv[1]:
        json_task = JsonTask(sys.argv[1])
        json_task.json_validation()
        json_task.json_save()
    if ".yaml" in sys.argv[1]:
        yaml_task = YamlTask(sys.argv[1])
        yaml_task.yaml_validation()