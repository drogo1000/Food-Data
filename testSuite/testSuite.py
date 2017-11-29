import toml
import re
from pathlib import Path


# A valid filename should only contain lowercase letters
# and hyphens
def validFilename(filename):
    result = re.findall('[^a-z\-\.]', filename)
    if not len(result) == 0:
        raise ValueError('invalid filename')


# A valid attribute should only contain lowercase letters,
# hyphens and numbers, except attributes under translation
def validAttribute(attribute):
    result = re.findall('[^a-z1-9\-]', attribute)
    if not len(result) == 0:
        raise ValueError('invalid attribute')


# A valid value should only contain lowercase letters (any
# characters in different languages)
def validValue(value):
    result = re.findall('[^a-z]', value)
    if not len(result) == 0:
        # raise ValueError()
        # Tests:
        print("not valid: ",value)


# Traverse a dictionary parsed from a .toml file with many
# layers to exam the validation for attribute names and
# values on each layer
def traverseDictionary(element):
    if type(element) == str:
        # Test:
        print(element)
        validValue(element)
    elif type(element) == dict:
        # traverse items
        for item in element.items():
            key = item[0]
            value = item[1]
            # Test:
            print(key)
            validAttribute(key)

            # apply different validation rules based on key
            if key == 'translation':
                validTranslation(value, 1)
            elif key == 'exclude-diet':
                validExDiet(value)
            elif key == 'exclude-allergens':
                validExAllergens(value)
            elif key == 'type':
                validCuisineType(value)
            elif key == 'cuisine':
                validCuisine(value)
            else:
                traverseDictionary(value)


# A vaild translation dictionary can have three levels:
#  - The first level should be 2 lowercase letters
#  - The second level should be 2 uppercase letters
#  - The third level should be 3 uppercase letters
def validTranslation(dictionary, level):
    # verify data type of argument
    if not type(dictionary) == dict:
        raise ValueError('invalid translation')

    # declare naming pattern for certain layer
    lowest = False
    match = ''
    if level == 1:
        match = '[a-z]{2}'
    elif level == 2:
        match = '[A-Z]{2}'
    elif level == 3:
        match = '[A-Z]{3}'
    elif level == 4:
        lowest = True
    else:
        raise ValueError('invalid translation')

    if not lowest:
        for item in dictionary.items():
            key = item[0]
            val = item[1]
            if type(val) == str:
                # Test:
                print(val)
                validValue(val)
            elif type(val) == dict:
                result = re.fullmatch(match, key)
                if result == None:
                    raise ValueError('invalid translation')
                validTranslation(val, level + 1)
    else:
        for item in dictionary.items():
            key = item[0]
            val = item[1]
            if type(val) == str:
                # Test:
                print(val)
                validValue(val)
                validAttribute(key)
            else:
                raise ValueError('invalid translation')


# The value shoud be one of `"continent", "subregion", "country",
# "province" or "culture".
def validCuisineType(value):
    if type(value) == str:
        if (value == 'continent'
        or value == 'subregion'
        or value == 'country'
        or value == 'province'
        or value == 'culture'):
            return
    raise ValueError('invalid cuisine type')


# should have a list of strings as its value (may be an empty
# list). These strings should reference the filenames of diets
# that exists in diets/
def validExDiet(value):
    # get the path to diets/
    path = Path('../diets')
    # exam the reference
    if type(value) == list:
        for ele in value:
            filename = ele + '.toml'
            pathToFile = path / filename
            if not pathToFile.is_file():
                raise ValueError('invalid exclude-diet')
    else:
        raise ValueError('invalid exclude-diet')


# should have a list of strings as its value (may be an empty
# list). These strings should reference the filenames of allergens
# that exists in allergens/
def validExAllergens(value):
    # get the path to diets/
    path = Path('../allergens')
    # exam the reference
    if type(value) == list:
        for ele in value:
            filename = ele + '.toml'
            pathToFile = path / filename
            if not pathToFile.is_file():
                raise ValueError('invalid exclude-allergens')
    else:
        raise ValueError('invalid exclude-allergens')


# A cuisine attri should be of the format cuisine.<name>.translation,
# where name is a custom name.
def validCuisine(value):
    if type(value) == dict:
        for item in value.items():
            key = item[0]
            val = item[1]
            validAttribute(key)
            if (type(val) == dict
            and len(val.keys()) == 1
            and 'translation' in val):
                validTranslation(val['translation'], 1)
            else:
                raise ValueError('invalid cusine')
    else:
        raise ValueError('invalid cusine')


# If a folder exists inside there must be a file with the
# same name (in the same level).
# Excludes folders that have the prefix __
def validDirectory(folder):
    path = Path(folder)
    for child in path.iterdir():
        if child.is_dir() and child.stem[:2] != '__':
            filename = child.with_suffix('.toml')
            if not filename.is_file():
                raise ValueError('invalid folder')


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

    # traverse sub-folder
    for child in path.iterdir():
        if child.is_dir() and child.stem[:2] != '__':
            validFile(child)
