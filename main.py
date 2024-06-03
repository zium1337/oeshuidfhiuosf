import sys
import json
import yaml

class JsonTask():
    def __init__(self, from_file, to_file = None):
        self.file = from_file
        self.file2 = to_file
        self.dane = None
    
    def json_convert(self):
        try:
            self.dane = json.dumps(self.file)
            print("Dane zostały poprawnie skonwertowane")
        except FileNotFoundError:
            print("Nie znaleziono takiego pliku")
        except json.decoder.JSONDecodeError:
            print("Plik json jest nieprawidłowy")
        except Exception as e:
            print(e)

    def json_validation(self):
        try:
            with open(self.file) as json_file:
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
            with open(self.file2, 'w') as json_file:
                json_file.write(self.dane)
        except json.decoder.JSONDecodeError:
            print("Plik json jest nieprawidłowy")
        except Exception as e:
            print(e)

class YamlTask():
    def __init__(self, from_file, to_file = None):
        self.file = from_file
        self.file2 = to_file
        self.dane = None

    def yaml_validation(self):
        try:
            with open(self.file) as yaml_file:
                self.dane = yaml.load(yaml_file, Loader=yaml.FullLoader)
            print("Dane z pliku YAML zostały poprawnie załadowane i zweryfikowane!")
        except FileNotFoundError:
            print("Nie znaleziono takiego pliku")
        except yaml.scanner.ScannerError:
            print("Plik yaml jest nieprawidłowy")
        except Exception as e:
            print(e)
    
    def yaml_save(self):
        try:
            with open(self.file2, 'w') as yaml_file:
                yaml.dump(self.dane, yaml_file)
        except yaml.scanner.ScannerError:
            print("Plik yaml jest nieprawidłowy")
        except Exception as e:
            print(e)

if __name__ == '__main__':
    if ".json" in sys.argv[1]:
        json_task = JsonTask(sys.argv[1])
        json_task.json_validation()
        if ".yaml" in sys.argv[2]:
            yaml_task = YamlTask(sys.argv[1], sys.argv[2])
            yaml_task.yaml_validation()
            yaml_task.yaml_save()
    if ".yaml" in sys.argv[1]:
        yaml_task = YamlTask(sys.argv[1])
        yaml_task.yaml_validation()
        if ".json" in sys.argv[2]:
            json_task = JsonTask(yaml_task.dane, sys.argv[2])
            json_task.json_convert()
            json_task.json_save()