---
layout: default
title: Release notes
description: Latest release notes for the Firebolt data warehouse.
parent: General reference
nav_order: 1
has_toc: false
has_children: false
---

# Release notes

Firebolt continuously releases updates so that you can benefit from the latest and most stable service. These updates might happen daily, but we aggregate release notes to cover a longer time period for easier reference. The most recent release notes from the latest version are below. 

- See the [Release notes archive](../release-notes/release-notes-archive.md) for earlier-version release notes.

{: .note}
Firebolt might roll out releases in phases. New features and changes may not yet be available to all accounts on the release date shown.

## DB version 4.2
**July 2024**

- [Release notes](#release-notes)
  - [DB version 4.2](#db-version-42)
    - [Breaking Changes](#breaking-changes)
    - [Enhancements, changes and new integrations](#enhancements-changes-and-new-integrations)

### Breaking Changes 

<!--- FIR-33028 --->**Improved rounding precision for floating point to integer casting**
{: style="color:red;"}

Casting from floating point to integers now uses Banker's Rounding, matching PostgreSQL's behavior. This means that numbers that are equidistant from the two nearest integers are rounded to the nearest even integer:  

Examples:
```sql
SELECT 0.5::real::int
``` 
This returns 0. 

```sql
SELECT 1.5::real::int
``` 
This returns 2. 

 Rounding behavior has not changed for numbers that are strictly closer to one integer than to all others.
 
<!--- FIR-33869---> **JSON functions update**
{: style="color:red;"}

Removed support for `json_extract_raw`, `json_extract_array_raw`, `json_extract_values`, and `json_extract_keys`. Updated `json_extract` function: the third argument is now `path_syntax`, which is a JSON pointer expression. See [JSON_EXTRACT](../sql_reference/../../sql_reference/functions-reference/JSON/json-extract.md) for examples and usage. 

<!--- FIR-32486---> **Cluster ordinal update**
{: style="color:red;"}

Replaced `engine_cluster` with [`cluster_ordinal`](../sql_reference/../../sql_reference/information-schema/engine-metrics-history.md) in `information_schema.engine_metrics_history`. The new column is an integer representing the cluster number.

<!--- FIR-34090 ---> **Configurable cancellation behavior on connection drop**
{: style="color:red;"}

Introduced the `cancel_query_on_connection_drop` setting, allowing clients to control query cancellation on HTTP connection drop. Options include `NONE`, `ALL`, and `TYPE_DEPENDENT`. Refer to [system settings](../system-settings.md#query-cancellation-mode-on-connection-drop) for examples and usage. 

<!--- FIR-33925 ---> **JSON format as default for error output**
{: style="color:red;"}

The HTTP API now returns query execution errors in JSON format by default. This change allows for the inclusion of meta information such as error codes and the location of failing expressions in SQL scripts.

<!--- FIR-33857---> **Updated table-level RBAC and ownership management**
{: style="color:red;"}

1. Table level RBAC will be enabled for new accounts, which means that RBAC checks also covers schema, table, view and aggregating indexes. Refer to our [RBAC](./../../Guides/security/rbac.md) docs for the full new spec. Newly created accounts will have this version enabled immediately, but this introduces changes to existing accounts that will be migrated to the new version:
   * System built-in roles will be migrated to promote the account to table level RBAC. This means that new privileges will be added to `account_admin`, `system_admin` and `public` roles. The effect is transparent— any user assigned with those roles will not be affected.
   * `Security_admin` role will be removed temporarily and re-introduced in a later release.
   * `Information_object_privileges` will include more privileges and switching to to a specific user db (e.g by executing `use database db`) will only show privileges relevant for that database.
   * Every newly created user is granted with a `public` role. This grant can be revoked.

2. Ownership has been introduced. This means that the user creator of an object is it's owner. Owners of objects cannot be dropped until their ownership is transferred. 

3. On new accounts, roles cannot be dropped if there are privileges granted on them.

### Enhancements, changes and new integrations

<!--- FIR-33699---> **Improved query performance**

Queries with "`SELECT [project_list] FROM [table] LIMIT [limit]`" on large tables are now significantly faster.

<!--- FIR-32118---> **Updated `ntile` return type**

The `ntile` function now returns the same type as its input argument: For `INTEGER`/`BIGINT` arguments. It now returns `INTEGER`/`BIGINT` respectively, making it consistent with PostgreSQL. See [NTILE](../sql_reference/../../sql_reference/functions-reference/window/ntile.md) for examples and usage. 

<!--- FIR-32882---> **Multi-node query performance**

Improved the performance for data transfer between nodes, resulting in faster overall query execution times. 


