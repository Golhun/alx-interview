# 0x04. UTF-8 Validation

## Overview

This project focuses on validating whether a given dataset represents a valid UTF-8 encoding. It involves using bitwise operations, understanding the UTF-8 encoding scheme, and applying Python programming skills.

## Learning Objectives

- Understand and apply bitwise operations in Python.
- Familiarize yourself with the UTF-8 encoding scheme and its validation rules.
- Work with data at the byte level and manipulate lists in Python.
- Implement Boolean logic to validate UTF-8 encoded data.

## Project Structure

- `0-main.py`: Main script used for testing the implementation.
- `utf8_validator.py`: Contains the implementation of the UTF-8 validation logic.
- `README.md`: Documentation of the project.
- `.gitignore`: Specifies files and directories that Git should ignore.

## Bitwise Operations

Bitwise operations play a key role in validating UTF-8 encoding. You'll use operations like AND (`&`), OR (`|`), and shifts (`<<`, `>>`) to analyze and manipulate the bits in the data.

## UTF-8 Encoding Scheme

UTF-8 is a variable-width character encoding capable of encoding all possible characters. The validation process involves checking if the byte patterns adhere to UTF-8 rules.
