[![Stories in Ready](https://badge.waffle.io/ZURASTA/Food-Data.png?label=ready&title=Ready)](https://waffle.io/ZURASTA/Food-Data?utm_source=badge)
# Food-Data

A collection of different food related data sources. Aimed at categorising different groupings (connections) of data, and localised terminology.

The files are currently [TOML](https://github.com/toml-lang/toml) files, which have the basic form of nested groupings of data being done using tables, while the reserved `__info__` table is for attributes about that current table (libraries parsing the data can move data into that table).

### [/allergens](/diets)
Contains food allergy data.


### [/cuisines](/cuisines)
Contains the cuisine related data, such as grouping cuisines by style with localised cuisine and style names.


### [/diets](/diets)
Contains diet and religious dietary data.


### [/ingredients](/ingredients)
Contains the ingredient related data, such as grouping ingredients to types with localised ingredient and type names.


## Guidelines

* __Naming__ - All filenames, attributes, and values should be in lower case. Filenames should contain only letters and hyphens. Attributes should only contain letters, numbers, and hyphens.
