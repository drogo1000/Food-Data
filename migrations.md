Migrations
============

Migrations are files denoting the changes made since the last recorded migration. These migration files can be used to understand what data needs to be acted on.

A property of these files are that they can be merged to further reduce the amount of operations needed to be performed. An example of this being done can be seen in the [yum](https://github.com/ZURASTA/yum/blob/132cb79ab328d2e4063d581f79fde0ff4243eb02/lib/yum/migration.ex#L65-L130) library.

## Structure

Each resource type (ingredients, cuisines, diets, allergens, etc.) contains migration files (`[type]/__migrations__/[timestamp].yml`) which include a list of changes that were made since the previous migration.

### Timestamp

The file timestamp is formatted as `Y*MMDDhhmmss` or `YYYYMMDDhhmmss`.

* `Y*` or `YYYY` is the current year (AD), e.g. `2018`.
* `MM` is the month (`00` to `12`), e.g. `03`.
* `DD` is the day (`00` to max day for that given month), e.g. `15`.
* `hh` is the 24-hour (`00` to `23`), e.g. `22`.
* `mm` is the minute (`00` to `59`), e.g `17`.
* `ss` is the second (`00` to `59`), e.g `00`.

e.g. `20180315221700.yml`

The higher the timestamp the more recent the migration.

### Actions

The actions tracked in a migration are:

* `A` - `Added` a file: `A: [file]`
* `U` - `Updated` a file (its contents were changed): `U: [file]`
* `M` - `Moved` a file: `M: [old_file] [new_file]`
* `D` - `Deleted` a file: `D: [file]`

These actions will be listed in a migration file with the current timestamp it was created at. So each migration will be able to be run in order.

The actions will appear in the order: `M > D > A > U`

#### Adding a file

When a new file is added (as in a new resource to track) since the last migration, the current migration file should contain an `A` action, with the name of the file as its argument.

#### Updating a file

When the contents of a tracked file has been changed since the last migration, the current migration file should contain an `U` action, with the name of the file as its argument.

#### Moving a file

When the tracked file has moved or been renamed since the last migration, the current migration should contain a `M` action, with the old file and new file as its arguments.

#### Deleting a file

When deleting a tracked file since the last migration, the current migration should contain a `D` action, with the file as its argument.

### Example

#### Changes (`ingredients/__migrations__/01.yml`):
1. Added a `meats/lamb-cutlets.toml` file
2. Added a `fruits/orange.toml` file

```yaml
- A: meats/lamb-cutlets
- A: fruits/orange
```

#### Changes (`ingredients/__migrations__/02.yml`):
1. Updated the contents of the `meats/lamb-cutlets.toml` file (note: how this references the final file name)
2. Moved the `meats/lamb-cutlets.toml` file is from the `meats/` directory into `meats/lamb/` and renamed it to `cutlets.toml`

```yaml
- M: meats/lamb-cutlets meats/lamb/cutlets
- U: meats/lamb/cutlets
```

#### Changes (`ingredients/__migrations__/03.yml`):
1. Deleted the `meats/lamb/cutlets.toml`
2. Replace the `fruits/orange.toml` (creating a new trackable resource)

```yaml
- D: meats/lamb/cutlets
- D: fruits/orange
- A: fruits/orange
```
