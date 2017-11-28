import toml
import re
from pathlib import Path


# A valid filename should only contain lowercase letters
# and hyphens
def validFilename(filename):
    result = re.findall('[^a-z\-\.]', filename)
    if not len(result) == 0:
        # Test:
        print(key)
        raise ValueError()


# A valid attribute should only contain lowercase letters,
# hyphens and numbers, except attributes under translation
def validAttribute(attribute):
    result = re.findall('[^a-z1-9\-]', attribute)
    if not len(result) == 0:
        raise ValueError()


# A valid value should only contain lowercase letters (any
# characters in different languages)
def validValue(value):
    result = re.findall('[^a-z]', value)
    if not len(result) == 0:
        raise ValueError()


# Traverse a dictionary parsed from a .toml file with many
# layers to exam the validation for attribute names and
# values on each layer
def traverseDictionary(element):
    if type(element) == str:
        # Test:
        # validValue(element)
        print(element)
    elif type(element) == dict:
        for key in element.keys():
            # Test:
            # validAttribute(key)
            print(key)
        for value in element.values():
            traverseDic(value)


# A vaild translation dictionary can have three levels:
#  - The first level should be 2 lowercase letters
#  - The second level should be 2 uppercase letters
#  - The third level should be 3 uppercase letters
def validTranslation(dictionary, level):
    # verify data type of argument
    if not type(dictionary) == dict:
        raise ValueError()

    # the second and third levels are optional.
    # it could be the value
    if not level == 1:
        isValue = False
        for value in dictionary.values():
            if type(value) == str:
                isValue = True
                # Test:
                print(value)
                # validValue(value)
        if isValue:
            for key in dictionary.keys():
                # Test:
                print(key)
                # validAttribute(key)
            return

    # declare naming pattern for certain layer
    match = ''
    if level == 1:
        match = '[a-z]{2}'
    elif level == 2:
        match = '[A-Z]{2}'
    elif level == 3:
        match = '[A-Z]{3}'
    else:
        raise ValueError()

    # exam the validation of certain layer
    for key in dictionary.keys():
        # Test:
        print(key)
        result = re.fullmatch(match, key)
        if result == None:
            raise ValueError()

    # exam the validation of the next layer
    for value in dictionary.values():
        if type(value) == dict:
            validTranslation(value, level + 1)
        else:
            raise ValueError()


# If a folder exists inside there must be a file with the
# same name (in the same level).
# Excludes folders that have the prefix __
def validDirectory(folder):
    path = Path(folder)
    for child in path.iterdir():
        if child.is_dir() and child.stem[:2] != '__':
            if not child.with_suffix('.toml').is_file():
                raise ValueError()


# Parse a .toml file into a dictionary and exam its validation
def validFile(folder):
    # exam the validation of the folder structure
    validDirectory(folder)

    # read .toml in the folder
    path = Path(folder)
    tomlFileList = list(path.glob('*.toml'))
    for f in tomlFileList:
        # exam the validation of filename
        validFilename(f.stem)

        # parse .toml file into a dictionary and traverse it
        fs = f.open()
        tomlString = fs.read()
        fs.close()
        parsedData = toml.loads(tomlString)
        traverseDictionary(parsedData)
