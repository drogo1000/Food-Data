Translations
============

This directory contains the translation files. These files have a different structure than the other data sources, in that the TOML files are simply structured as tables following this pattern: `lookup-name.culture-code`.

The lookup name should be a unique word or collection of words that reasonably convey what the object of the translations is. For the most part this will be the exact english name for the given object, however there will likely be certain things where there is no english name to represent it or it may use the same english name (might not differentiate between the two). In this case, a name should be chosen that best describes that particular object.

The culture codes follow the format of the 2 letter language code (ISO 639-1), the 2 letter country code (ISO 3166-1 alpha-2), and up to 3 letters country/province/subdivision code (ISO 3166-2). The precedence of these codes apply the top-level language code to all countries and provinces/subdivisions unless a specific country or province/subdivision alternative is specified too.

The term key contains the localised text itself.

Lastly to avoid confusion with the given translations (both lookup name and localised terms), liberal use of comments (highlighting external sources) is highly recommended.

An example of what this looks like is:

```toml
[greeting] # Source: link to definition of greeting
  [greeting.en]
    term = "hello"
    [greeting.en.AU] # Source: link to aussie variation
      term = "g'day"

  [greeting.fr]
    term = "bonjour"
```
