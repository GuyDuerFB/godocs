---
layout: default
title: ARRAY_INTERSECT
description: Reference material for ARRAY_INTERSECT function
grand_parent: SQL functions
parent: Array functions
great_grand_parent: SQL reference
published: false
---

# ARRAY\_INTERSECT

Evaluates all arrays that are provided as arguments and returns an array of any elements that are present in all the arrays. The order of the resulting array may be different than the original arrays. Use [`ARRAY_SORT`](../Lambda/array-sort.md) to stipulate a specific order on the results.

## Syntax
{: .no_toc}

```sql
ARRAY_INTERSECT(<array>)
```

## Parameters 
{: .no_toc} 

| Parameter | Description                                            | Supported input types | 
| :--------- | :------------------------------------------------------ | :-----|
| `<array>`   | A series of arrays to be analyzed for mutual elements. | `ARRAY`s of the same type |

## Return Type
`ARRAY` of the same type as the input arrays

## Examples
{: .no_toc}

In the example below, the only element that is shared between all three arrays is `3.`

```sql
SELECT
	ARRAY_INTERSECT([ 1, 2, 3 ], [ 1, 3 ], [ 2, 3 ])
```

**Returns**: `3`

In this second example below, we are using `ARRAY_SORT` to ensure the results are in ascending order.

```sql
SELECT
	ARRAY_SORT(
	    ARRAY_INTERSECT([ 5, 4, 3, 2, 1 ],[ 5, 3, 1 ])
	    )
```

**Returns**: `[1,3,5]`
