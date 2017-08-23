Allergens
=========

This directory contains allergy related data. Organised by creating a file for each allergen type, and associating different data with them.

Reference https://en.wikipedia.org/wiki/List_of_allergens#Food


Data
----

The TOML file itself contains attributes that should be applied to that diet.

The current list of attributes that are applied to the object itself:

* __translation__ - The current translations for the given item.


An example of this is (peanut.toml):

```toml
# https://en.wikipedia.org/wiki/Peanut_allergy

[translation]
  [translation.en]
    term = "peanut allergy"
```

The above provides the translations for a peanut allergy. For more information on how translations work see: [translations.md](../translations.md).
