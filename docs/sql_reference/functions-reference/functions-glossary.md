---
layout: default
title: Functions glossary
description: Reference for SQL functions available in Firebolt.
grand_parent: SQL reference
parent: SQL functions
---

# Functions glossary

All Firebolt functions in alphabetical order.

| Name         | Function                                | Type    |
|:----------- |:------------------------------------------------ |:-------|
| [ABS](./numeric/abs.md) | Calculates the absolute value of an input value. | Numeric |
| [ARRAY_ANY_MATCH](./Lambda/array-any-match.md) | Returns `true` if the function provided returns `true` for at least one of the elements of an array. Otherwise returns `false`. | Lambda |
| [ARRAY_CONCAT](./array/array-concat.md) | Combines one or more arrays that are passed as arguments. | Array |
| [ARRAY_CONTAINS](./array/array-contains.md) | Returns 1 if a specified argument is present in the array, or 0 otherwise. | Array |
| [ARRAY_COUNT](./Lambda/array-count.md) | Counts the number of elements in a boolean array for which `function(array[i])` evaluates to true, if a function is provided. If not provided, counts the number of elements in the array that evaluate to true. | Lambda |
| [ARRAY_DISTINCT](./array/array-distinct.md) | Returns an array containing only the _unique_ elements of the given array. | Array |
| [ARRAY_FIRST](./Lambda/array-first.md) | Returns the first element in the given array for which the given function returns `true`. | Lambda |
| [ARRAY_FLATTEN](./array/flatten.md) | Converts an array of arrays into a flat array. For every element that is an array, this function extracts its elements into the new array. | Array |
| [ARRAY_TO_STRING](./array/array-to-string.md) | Concatenates an array of string elements using an optional delimiter. | Array |
| [ARRAY_LENGTH](./array/array-length.md) | Returns the length of (number of elements in) the given array. | Array |
| [ARRAY_MAX](./array/array-max.md) | Returns the maximum element in an array. | Array |
| [ARRAY_MIN](./array/array-min.md) | Returns the minimum element in an array. | Array |
| [ARRAY_REVERSE](./array/array-reverse.md) | Returns an array of the same size and type as the original array, with the elements in reverse order. | Array |
| [ARRAY_REVERSE_SORT](./Lambda/array-reverse-sort.md) | Returns the elements of the input array in descending order. If the argument function is provided, the sorting order is determined by the result of applying the function on each element of the array. | Lambda |
| [ARRAY_SORT](./Lambda/array-sort.md) | Returns the elements of the input array in ascending order. If the argument function is provided, the sorting order is determined by the result of applying the function on each element of the array. | Lambda |
| [ARRAY_SUM](./Lambda/array-sum.md) | Returns the sum of elements of the input array. | Lambda |
| [AVG](./aggregation/avg.md) | Calculates the average of an expression. | Aggregation |
| [AVG OVER](./window/avg-window.md) | Returns the average value within the requested window. | Window |
| [BOOL_AND](./aggregation/bool_and.md) | Returns true if all non NULL input value are true. | Aggregation |
| [BOOL_OR](./aggregation/bool_or.md) | Returns true if any non NULL input value is true.  | Aggregation |
| [BTRIM](./string/btrim.md) | Removes all occurrences of optionally specified characters from both sides of a source string. If no trim parameter is specified, all occurrences of common whitespace (ASCII Decimal 32) characters from both sides of the specified source string are removed. | String |
| [CAST](./conditional-and-miscellaneous/cast.md) | Converts data types into other data types based on specified parameters. | Conditional & miscellaneous |
| [CHECKSUM](./aggregation/checksum.md) | Calculates a hash value known as a checksum operation on a list of arguments. | Aggregation |
| [COALESCE](./conditional-and-miscellaneous/coalesce.md) | Checks from left to right for the first non-NULL argument found for each entry parameter pair. | Conditional & miscellaneous |
| [CONCAT or \|\|](./string/concat.md) | Concatenates the strings listed in the input without a separator. | String |
| [COUNT](./aggregation/count.md) | Counts the number of rows or not NULL values. | Aggregation |
| [COUNT OVER](./window/count-window.md) | Count the number of values within the requested window. | Window |
| [CURRENT_DATE](./date-and-time/current-date.md) | Returns the current (local) date in the time zone specified in the session's `time_zone` setting. | Date & time |
| [CURRENT_TIMESTAMP](./date-and-time/current-timestamptz.md) | Returns the current (local) timestamp in the time zone specified in the session's `time_zone` setting. | Date & time |
| [DATE_ADD](./date-and-time/date-add.md) | Calculates a new date or timestamp by adding or subtracting a specified number of time units from an indicated expression. | Date & time |
| [DATE_DIFF](./date-and-time/date-diff.md) | Calculates the difference between the start and end date by the indicated unit. | Date & time |
| [DATE_TRUNC](./date-and-time/date-trunc.md) | Truncates a date or timestamp value to the selected precision. | Date & time |
| [DENSE_RANK](./window/dense-rank.md) | Rank the current row within the requested window without gaps. | Window |
| [EXTRACT](./date-and-time/extract.md) | Retrieves the time unit from a date or timestamp value. | Date & time |
| [GENERATE_SERIES](./conditional-and-miscellaneous/generate-series.md) | Generates a single rowset of values from `start` to `stop`, with a step size of `step` - a table-valued function. | Conditional & miscellaneous |
| [GREATEST](./conditional-and-miscellaneous/greatest.md) | Selects the largest value from a list of any number of expressions. | Conditional & miscellaneous |
| [HLL_COUNT_BUILD](./aggregation/hll-count-build.md)                       | Counts the approximate number of unique not NULL values, aggregating the values to HLL++ sketches represented as the [BYTEA data type](../bytea-data-type.md).                                                                                                                                   | Conditional & miscellaneous |
| [HLL_COUNT_ESTIMATE](./numeric/hll-count-estimate.md)                 | Extracts a cardinality estimate of a single HLL++ sketch that was previously built using the aggregate function [`HLL_COUNT_BUILD`](./aggregation/hll-count-build.md).                                                                                                                                                           | Conditional & miscellaneous |
| [HLL_COUNT_MERGE](./aggregation/hll-count-merge.md)                       | Merges one or more HLL++ sketches that were previously built using the aggregate function [`HLL_COUNT_BUILD`](./aggregation/hll-count-build.md) into a new sketch.                                                                                                                                                               | Conditional & miscellaneous |
| [IFNULL](./conditional-and-miscellaneous/ifnull.md) | Compares two expressions. Returns the first input expression if it’s non-NULL, otherwise returns the second. | Conditional & miscellaneous |
| [ILIKE](./string/ilike.md) | Allows matching of strings based on comparison to a pattern, case-insensitively. | String |
| [INDEX_OF](./array/index-of.md) | Returns the index position of the first occurrence of the element in the array (or 0 if not found). | Array |
| [JSON_EXTRACT](./JSON/json-extract.md) | Takes an expression containing a JSON document, a JSON pointer expression, and an expected data type parameter. If the key specified using the JSON pointer expression exists, and its type conforms with the expected data type parameter, returns the value of the data type specified. Otherwise, returns NULL. | Semi-structured data |
| [JSON_EXTRACT_ARRAY_RAW](./JSON/json-extract-array-raw.md) | Returns a string representation of a JSON array pointed by the supplied JSON pointer. | Semi-structured data |
| [JSON_EXTRACT_KEYS](./JSON/json-extract-keys.md) | Returns an array of strings containing the keys at the nesting level indicated by the specified JSON pointer. | Semi-structured data |
| [JSON_EXTRACT_RAW](./JSON/json-extract-raw.md) | Returns a string representation of the scalar or sub-object under the key indicated by the specified JSON pointer if the key exists. | Semi-structured data |
| [JSON_EXTRACT_VALUES](./JSON/json-extract-values.md) | Returns an array of string values from a JSON document using the key location specified by the specifed JSON pointer. | Semi-structured data |
| [LEAST](./conditional-and-miscellaneous/greatest.md) | Selects the smallest value from a list of any number of expressions. | Conditional & miscellaneous |
| [LENGTH](./string/length.md) | Calculates the length of the input string. | String |
| [LIKE](./string/like.md) | Allows matching of strings based on comparison to a pattern, case-sensitively. | String |
| [LOCALTIMESTAMP](./date-and-time/localtimestamp.md) | Returns the current local timestamp in the time zone specified in the session's `time_zone` setting. | Date & time |
| [LOWER](./string/lower.md) | Converts the input string to lowercase characters. | String |
| [LPAD](./string/lpad.md) | Adds a specified pad string to the start of the string repetitively up until the length of the resulting string is equivalent to an indicated length. | String |
| [LTRIM](./string/ltrim.md) | Removes all occurrences of optionally specified characters from the left side of a source string. If no trim parameter is specified, all occurrences of common whitespace (ASCII Decimal 32) characters from the left side of the specified source string are removed. | String |
| [MAX](./aggregation/max.md) | Calculates the maximum value of an expression across all input values. | Aggregation |
| [MAX_BY](./aggregation/max-by.md) | Returns the value of its first argument for the row that contains the maximum value of the second argument | Aggregation |
| [MAX OVER](./window/max-window.md) | Returns the maximum value within the requested window. | Window |
| [MAX_BY](./aggregation/max-by.md) | Returns the value of the specified input column at the row with the maximum value in the specified value column. | Aggregation
| [MIN](./aggregation/min.md) | Calculates the minimum value of an expression across all input values. | Aggregation |
| [MIN_BY](./aggregation/min-by.md) | Returns the value of its first argument for the row that contains the minimum value of the second argument | Aggregation |
| [MIN OVER](./window/min-window.md) | Returns the maximum value within the requested window. | Window |
| [MOD](./numeric/mod.md) | Calculates the remainder after dividing two values. | Numeric |
| [NTILE](./window/ntile.md) | Divides an ordered set into a number of buckets. | Window |
| [NULLIF](./conditional-and-miscellaneous/nullif.md) | Compares two expressions. Returns NULL if the expressions are equal. Returns the result of the first if they are not equal. | Conditional & miscellaneous |
| [OCTET_LENGTH](./string/octet_length.md) | Calculates the length of the input string in bytes. | String |
| [PERCENT_RANK](./window/percent-rank.md) | Calculates the relative rank of the current row within the requested window. | Window |
| [POSITION](./string/position.md) | Returns the position of the substring found in the string, starting from 1. The returned value is for the first matching value, and not for any subsequent valid matches. In case the substring does not exist, position will return 0. | String |
| [RANDOM](./numeric/random.md) | Returns a pseudo-random unsigned value greater than 0 and less than 1 of type `DOUBLE PRECISION`. | Numeric |
| [RANK](./window/rank.md) | Rank the current row within the requested window with gaps. | Window |
| [REGEXP_LIKE](./string/regexp-like.md) | Checks whether a text pattern matches a regular expression string. Returns 0 if it doesn’t match, or 1 if it matches. | String |
| [REGEXP_REPLACE](./string/regexp-replace.md) | Matches a pattern in the input string and replaces the first matched portion (from the left) with the specified replacement. | String |
| [REPLACE](./string/replace.md) | Replaces all occurrences of the given pattern substring within the input expression with a replacement substring. | String |
| [ROUND](./numeric/round.md) | Rounds a value to a specified number of decimal places. | Numeric |
| [ROW_NUMBER](./window/row-number.md) | Calculate a unique, increasing row number for each row within the window. | Window |
| [RPAD](./string/rpad.md) | Adds a specified pad string to the end of the string repetitively up until the length of the resulting string is equivalent to an indicated length. | String |
| [RTRIM](./string/rtrim.md) | Removes all occurrences of optionally specified characters from the right side of a source string. If no trim parameter is specified, all occurrences of common whitespace (ASCII Decimal 32) characters from the right side of the specified source string are removed. | String |
| [SPLIT_PART](./string/split-part.md) | Divides a string based on a specified delimiter into an array of substrings. The string in the specified index is returned, with 1 being the first index. If the string separator is empty, the input string is returned at index 1. | String |
| [STRING_TO_ARRAY](./string/string-to-array.md) | Splits a given string by a given separator and returns the result in an array of strings. | String |
| [STRPOS](./string/strpos.md) | Returns the position of the substring found in the string, starting from 1. The returned value is for the first matching value, and not for any subsequent valid matches. In case the substring does not exist, strpos will return 0. | String |
| [SUBSTRING, SUBSTR](./string/substring.md) | Returns a substring starting at the character indicated by the start index and including the number of characters defined. Character indexing starts at index 1. | String |
| [SUM](./aggregation/sum.md) | Calculates the sum of an expression. | Aggregation |
| [SUM OVER](./window/sum-window.md) | Calculate the sum of the values within the requested window. | Window |
| [TO_TIMESTAMP](./date-and-time/to-timestamp.md) | Converts a string to timestamp with time zone. | Date & time |
| [TRIM](./string/trim.md) | Removes all specified characters from the start, end, or both sides of a string. By default removes all consecutive occurrences of common whitespace (ASCII character 32) from both ends of a string. | String |
| [TRY_CAST](./conditional-and-miscellaneous/try-cast.md) | Converts data types into other data types based on the specified parameters. If the conversion cannot be performed, returns a NULL. | Conditional & miscellaneous |
| [UPPER](./string/upper.md) | Converts the input string to uppercase characters. | String |
| [VERSION](./conditional-and-miscellaneous/version.md) | Returns the version number information for the Firebolt engine. | Conditional & miscellaneous |
