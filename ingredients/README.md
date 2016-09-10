Ingredients
===========

This directory contains ingredient related data.

ingredients.toml
----------------

This file contains structured ingredient data grouped by the culinary types and names, and miscellaneous details associated with that group or ingredient.

The structure of this file is as follows:

The `__info__` field provides miscellaneous details about the current group and child groups. In addition the root `__info__` contains file references to the different keyword lookups (to handle translations).

The current fields that may be found in an `__info__` table are:

    * __groups__ - The group names.
    * __names__ - The ingredient names.
    * __diets__ - The dietary names.
    * __exclude-diet__ - The diets that do not allow consumption of this ingredient or type of ingredient. By default all diets are allowed to consume the ingredient unless specifically excluded.
    * __exclude-allergen__ - The allergies that are triggered by consumption of this ingredient or type of ingredient. By default all allergy types are allowed to consume the ingredient unless specifically excluded.

Groups are defined as tables or nested tables that are either a keyword to a culinary type (group), or an ingredient (culinary name).

An example of this is:

```toml
[__info__]
  groups = "../translations/culinary-groups.toml"
  names = "../translations/culinary-names.toml"
  diets = "../translations/diet-names.toml"

[vegetable]
  [vegetable.__info__]
    exclude-diet = ["carnivorous", "ketogenic"]

  [vegetable.spring-onion]

  [vegetable.tuber]
    [vegetable.tuber.__info__]
      exclude-diet = ["fruitarian"]

    [vegetable.tuber.potato]
```

The above indicates a vegetable (culinary-groups.toml) is excluded from the carnivorous and ketogenic diets (diet-names.toml). While the ingredient spring-onion (culinary-names.toml) is a type of vegetable, and inherits all of vegetable's info. And a tuber (culinary-groups.toml) is a type of vegetable, that is also excluded from fruitarian diets (diet-names.toml). Lastly the ingredient potato (culinary-names.toml) belongs to the tuber vegetable type.
