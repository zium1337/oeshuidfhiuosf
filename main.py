import sys
import json
import yaml
import xml.etree.ElementTree as ET
import xmltodict

class JsonTask():
    def __init__(self, from_file, to_file = None):
        self.file = from_file
        self.file2 = to_file
        self.dane = None
    
    def yaml_to_json_convert(self):
        try:
            self.dane = json.dumps(self.file)
            print("Dane zostały poprawnie skonwertowane")
        except FileNotFoundError:
            print("Nie znaleziono takiego pliku")
        except json.decoder.JSONDecodeError:
            print("Plik json jest nieprawidłowy")
        except Exception as e:
            print(e)

    def xml_to_json_convert(self):
        try:
            with open(self.file) as xml_file:
                self.dane = json.dumps(xmltodict.parse(xml_file.read()))
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

    def xml_to_yaml_convert(self):
        try:
            with open(self.file) as xml_file:
                self.dane = yaml.load(xml_file, Loader=yaml.FullLoader)
            print("Dane zostały poprawnie skonwertowane")
        except FileNotFoundError:
            print("Nie znaleziono takiego pliku")
        except yaml.scanner.ScannerError:
            print("Plik yaml jest nieprawidłowy")
        except Exception as e:
            print(e)

    def json_to_yaml_convert(self):
        try:
            self.dane = yaml.safe_dump(self.file)
            print("Dane zostały poprawnie skonwertowane")
        except FileNotFoundError:
            print("Nie znaleziono takiego pliku")
        except yaml.scanner.ScannerError:
            print("Plik yaml jest nieprawidłowy")
        except Exception as e:
            print(e)

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

class XmlTask():
    def __init__(self, from_file, to_file = None):
        self.file = from_file
        self.file2 = to_file
        self.dane = None

    def xml_convert(self):
        try:
            self.dane = xmltodict.unparse(self.file)
            print("Dane zostały poprawnie skonwertowane")
        except FileNotFoundError:
            print("Nie znaleziono takiego pliku")
        except yaml.scanner.ScannerError:
            print("Plik yaml jest nieprawidłowy")
        except Exception as e:
            print(e)

    def xml_validation(self):
        try:
            with open(self.file) as xml_file:
                self.dane = ET.parse(xml_file)
            print("Dane z pliku XML zostały poprawnie załadowane i zweryfikowane!")
        except FileNotFoundError:
            print("Nie znaleziono takiego pliku")
        except ET.ParseError:
            print("Plik xml jest nieprawidłowy")
        except Exception as e:
            print(e)

    def xml_save(self):
        try:
            with open(self.file2, 'w') as xml_file:
                xml_file.write(self.dane)
        except ET.ParseError:
            print("Plik xml jest nieprawidłowy")
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
        if ".xml" in sys.argv[2]:
            xml_task = XmlTask(json_task.dane, sys.argv[2])
            xml_task.xml_convert()
            xml_task.xml_save()
    if ".yaml" in sys.argv[1]:
        yaml_task = YamlTask(sys.argv[1])
        yaml_task.yaml_validation()
        if ".json" in sys.argv[2]:
            json_task = JsonTask(yaml_task.dane, sys.argv[2])
            json_task.yaml_to_json_convert()
            json_task.json_save()
        if ".xml" in sys.argv[2]:
            xml_task = XmlTask(yaml_task.dane, sys.argv[2])
            xml_task.xml_convert()
            xml_task.xml_save()
    if ".xml" in sys.argv[1]:
        xml_task = XmlTask(sys.argv[1])
        xml_task.xml_validation()
        if ".json" in sys.argv[2]:
            json_task = JsonTask(sys.argv[1], sys.argv[2])
            json_task.xml_to_json_convert()
            json_task.json_save()
        if ".yaml" in sys.argv[2]:
            json_task = JsonTask(sys.argv[1], sys.argv[2])
            json_task.xml_to_json_convert()
            yaml_task = YamlTask(json_task.dane, sys.argv[2])
            yaml_task.json_to_yaml_convert()
            yaml_task.yaml_save()