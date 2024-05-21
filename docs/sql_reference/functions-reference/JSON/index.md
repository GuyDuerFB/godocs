---
layout: default
title: JSON functions
description: Reference for JSON functions
nav_order: 7
parent: SQL functions
grand_parent: SQL reference
has_children: true
---

## JSON functions

The reference for each JSON function uses common syntax and conventions as outlined below.

### JSON pointer expression syntax

The placeholder `<json_pointer_expression>` indicates where you should use a JSON pointer, which is a way to access specific elements in a JSON document. For a formal specification, see [RFC6901](https://tools.ietf.org/html/rfc6901).

A JSON pointer starts with a forward slash (`/`), which denotes the root of the JSON document. This is followed by a sequence of property (key) names or zero-based ordinal numbers separated by slashes. You can specify property names or use ordinal numbers to specify the Nth property or the Nth element of an array.

The tilde (`~`) and forward slash (`/`) characters have special meanings and need to be escaped according to the guidelines below:

* To specify a literal tilde (`~`), use `~0`
* To specify a literal slash (`/`), use `~1`

For example, consider the JSON document below.

```javascript
{
    "key": 123,
    "key~with~tilde": 2,
    "key/with/slash": 3,
    "value": {
      "dyid": 987,
      "keywords" : ["insanely","fast","analytics"]
    }
}
```

With this JSON document, the JSON pointer expressions below evaluate to the results shown.

| Pointer              | Result                             | Notes           |
| :------------------- | :--------------------------------- | :-------------- |
| `/`                  | `{` <br>`   "key": 123,` <br>`   "key~with~tilde": 2,` <br>`   "key/with/slash": 3,` <br>`   "value": {` <br>`      "dyid": 987,` <br>`      "keywords" : ["insanely","fast","analytics"]` <br>`   }` | Returns the whole document. |
| `/key`               | 123                                |                 |
| `/key~0with~0tilde`  | 2                                  | Indicates the value associated with the `key~with~tilde` property name. |
| `/key~1with~1slash`  | 3                                  | Indicates the value associated with the `key/with/slash` property name. |
| `/0`                 | 123                                | Uses an ordinal to indicate the value associated with the `key` property name. The `key` property is in the first 0-based position.        |
| `/value/keywords/2`  | analytics                          | Indicates the element "analytics", which is in the third 0-based position of the array value associated with they keywords property. |

### Supported type parameters

Some functions accept a *data type parameter*, indicated in this reference with the `<expected_type>` placeholder. This parameter specifies the expected type as indicated by `<json_pointer_expression>`. The `<expected_type>` is specified using a string literal that corresponds to supported Firebolt SQL data types. The type parameter does not accept all SQL types because the JSON type system has fewer types than SQL and must be one of the following:

* `INTEGER` &ndash; used for integers as well as JSON boolean.
* `DOUBLE PRECISION` when the values in the JSON document are known integers.
* `TEXT` &ndash; used for strings.
* `ARRAY(<type>)` &ndash; indicates an array where `<type>` is one of `INTEGER`, `DOUBLE PRECISION`, or `TEXT`.

The following data types are _not supported_: `DATE`, `TIMESTAMP`, `REAL` (for real numbers, use `DOUBLE PRECISION`).

### JSON common example

Usage examples for JSON functions in this reference are based on the JSON document below, which is indicated using the `<json_common_example>` placeholder.

```javascript
{
    "key": 123,
    "value": {
      "dyid": 987,
      "uid": "987654",
      "keywords" : ["insanely","fast","analytics"],
      "tagIdToHits": {
        "map": {
          "1737729": 32,
          "1775582": 35
        }
      },
      "events":[
        {
            "EventId": 547,
            "EventProperties" :
            {
                "UserName":"John Doe",
                "Successful": true
            }
        },
        {
            "EventId": 548,
            "EventProperties" :
            {
                "ProductID":"xy123",
                "items": 2
            }
        }
    ]
    }
}
```