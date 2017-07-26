Cuisines
========

This directory contains cuisine related data. Organised by grouping cuisines by style. Style may be a geographical region (continents, subregions, countries, provinces), culture, or other.

Structure
---------

The data is organised into TOML files per style. Where attributes specified in parent folders applies to all children in that folder.

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

The TOML file itself contains attributes that should be applied to that style and attributes that should also be applied any child style.

The current list of attributes that are applied to the object itself:

* __type__ - The category it falls under. This may be geographical (`"continent"`, `"subregion"`, `"country"`, `"province"`), cultural (`"culture"`), or some other (`"other"`).

* __translation__ - The current translations for the given style.

The current list of attributes that are applied to the object and child objects:

* __cuisine__ - The cuisines that originate/associated with that style.


An example of this is (australia.toml):

```toml
[cuisine]
  [cuisine.lamington.translation.en]
    term = "lamington"

type = "country"

[translation]
  [translation.en]
    term = "australia"
    adj = "australian"
```

The above indicates in the country Australia and any styles inside it (in the `australia/` directory), the cuisine `lamington` is available. For more information on how translations work see: [translations.md](../translations/README.md).
