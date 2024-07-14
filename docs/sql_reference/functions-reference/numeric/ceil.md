---
layout: default
title: CEIL
description: Reference material for CEIL, CEILING functions
grand_parent: SQL functions
parent: Numeric functions
great_grand_parent: SQL reference
published: false
---

# CEIL
Synonym: `CEILING`

Returns the smallest value that is greater than or equal to `<value>`.

## Syntax
{: .no_toc}

```sql
CEIL(<value>); 
```
OR 
```sql
CEILING(<value>);
```
## Parameters
{: .no_toc}

| Parameter | Description                                                                                                                               | Supported input types                                                          |
| :--------- | :----------------------------------------------------------------------------------------------------------------------------------------- |:-------------------------------------------------------------------------------|
| `<value>`   | The value that will determine the returned value | `DOUBLE PRECISION` |

## Return Type
`DOUBLE PRECISION`

## Remarks
{: .no_toc}

When the input is of type `NUMERIC`, this function throws an overflow error if the result does not fit into the return type.

For example:
```sql
SELECT
    CEIL('99.99'::NUMERIC(4,2));
```

**Returns**: `OVERFLOW ERROR`, because `CEIL` will produce the value 100, but it can not fit into the `NUMERIC` type with only 2 whole digits.


## Examples
{: .no_toc}

```sql
SELECT
    CEIL(2.5549900);
```

**Returns**: `3`

```sql
SELECT
    CEIL('213.1549'::NUMERIC(20,4));
```

**Returns**: `214.0000`
