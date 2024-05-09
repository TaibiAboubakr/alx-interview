# 0x04-UTF-8_validation

This directory contains solutions for the "UTF-8 Validation" problem. The problem involves determining whether a given data set represents a valid UTF-8 encoding.

## Problem Description

UTF-8 is a variable-width character encoding capable of encoding all 1,112,064 valid character code points in Unicode using one to four one-byte (8-bit) code units. It is the dominant character encoding for the World Wide Web, accounting for more than 95% of all web pages.

In this problem, we are given an array of integers, where each integer represents a single byte of data. We need to determine whether the data set is a valid UTF-8 encoding according to the UTF-8 encoding rules. 

## Solution Approach

The solution involves iterating through the given array of integers and checking whether they form a valid UTF-8 encoding according to the following rules:

1. A character in UTF-8 can be 1 to 4 bytes long.
2. For 1-byte character, the first bit is a 0, followed by its unicode.
3. For n-byte character, the first n bits are all 1's, followed by a 0, then n - 1 bytes with most significant 2 bits being 10.

## Files

1. `0-validate_utf8.py` - Contains the python implementation of the UTF-8 validation algorithm.
