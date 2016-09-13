Cuisines
========

This directory contains cuisine related data. Organised by grouping cuisines by regions (continents, subregions, countries, provinces).

Structure
---------

The data is organised into TOML files per region. Where attributes specified in parent folders applies to all children in that folder.

An example of this structure:

```
cuisines/
├── oceania.toml #contains info that is applied to oceanic regions
└── oceania/
    └── australasia.toml #contains info that is applied to the australasian region and inherits the attributes applied to oceania
        └── australia.toml #contains info that is applied to australia and inherits the attributes applied to australasia
```

Data
----

The TOML file itself contains attributes that should be applied to that region and attributes that should also be applied any child regions.

The current list of attributes that are applied to the object itself:

* __translation__ - The current translations for the given region.

The current list of attributes that are applied to the object and child objects:

* __cuisine__ - The cuisines that originate/associated with that region.


An example of this is (australia.toml):

```toml
[cuisine]
  [lamington.translation.en]
    term = "lamington"

[translation]
  [translation.en]
    term = "australia"
    adj = "australian"
```

The above indicates in the country Australia and any regions inside it (in the `australia/` directory), the cuisine `lamington` is available. For more information on how translations work see: [translations.md](../translations/README.md).
