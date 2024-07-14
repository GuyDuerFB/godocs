---
layout: default
title: TAN
description: Reference material for TAN function
grand_parent: SQL functions
parent: Numeric functions
great_grand_parent: SQL reference
published: false
---

# TAN

Calculates the tangent.

## Syntax
{: .no_toc}

```sql
TAN(<value>)
```
## Parameters
{: .no_toc}

| Parameter | Description     | Supported input types | 
| :--------- | :--------------------------------- | :---------|
| `<value>`   | The value that determines the returned tangent | `DOUBLE PRECISION` | 

## Return Type
`DOUBLE PRECISION`

## Example
{: .no_toc}

The following example calculates the tangent of `90`: 
```sql
SELECT
    TAN(90);
```

**Returns**: `-1.995200412208242`
