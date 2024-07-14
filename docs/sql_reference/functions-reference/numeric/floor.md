---
layout: default
title: FLOOR
description: Reference material for FLOOR function
grand_parent: SQL functions
parent: Numeric functions
great_grand_parent: SQL reference
published: false
---

# FLOOR

Returns the largest round number that is less than or equal to the input value. The value is rounded to a decimal range defined by `<decimal>`.

## Syntax
{: .no_toc}

```sql
FLOOR(<value>[, <decimal>])
```
## Parameters 
{: .no_toc}

| Parameter | Description                                                                                                                   | Supported input types | 
| :--------- | :----------------------------------------------------------------------------------------------------------------------------- |:-----|
| `<value>`   | Valid values include column names, functions that return a column with numeric values, and constant numeric values.           | `DOUBLE PRECISION` |
| `<decimal>`   | Optional. A constant that defines the decimal range of the returned value. By default, `FLOOR` returns whole numbers.  | `INTEGER` |

## Return Type
`DOUBLE PRECISION` 

## Example
{: .no_toc}
The following example returns the largest round number that is less than or equal to the value `2.19`: 
```sql
SELECT
    FLOOR(2.19, 1);
```

**Returns**: `2.1`
