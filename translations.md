Translations
============

Translation data is represented in the TOML files as a translation table (`[translation]`), they appear in the format of: `translation.culture-code`.

The culture codes follow the format of the 2 letter language code (ISO 639-1), the 2 letter country code (ISO 3166-1 alpha-2), and up to 3 letters country/province/subdivision code (ISO 3166-2). The precedence of these codes apply the top-level language code to all countries and provinces/subdivisions unless a specific country or province/subdivision alternative is specified too.

The term key contains the localised text itself.

Lastly to avoid confusion with the given translations (localised terms), liberal use of comments (highlighting external sources) is highly recommended.

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
