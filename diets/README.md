Diets
=====

This directory contains diet and religious dietary related data. Organised by creating a file for each diet type, and associating different data with them.

Reference https://en.wikipedia.org/wiki/Diet_(nutrition)#Diet_classification_table


Data
----

The TOML file itself contains attributes that should be applied to that diet.

The current list of attributes that are applied to the object itself:

* __translation__ - The current translations for the given item.


An example of this is (vegan.toml):

```toml
# https://en.wikipedia.org/wiki/Veganism

[translation]
  [translation.en]
    term = "vegan"
```

The above provides the translations for a vegan diet. For more information on how translations work see: [translations.md](../translations/README.md).
