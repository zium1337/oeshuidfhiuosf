import subprocess

dependencies = [
    "PyYAML"
    "xmltodict"
]

def install_packages():
    for package in dependencies:
        subprocess.check_call(['python', '-m', 'pip', 'install', package])

install_packages()
