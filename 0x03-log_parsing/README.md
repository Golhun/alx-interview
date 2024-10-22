
# 0x03. Log Parsing - README

## Project Overview

This project is aimed at parsing and processing log data in real-time, leveraging key Python concepts such as file input/output, signal handling, and regular expressions. The script processes log entries, aggregates statistics, and handles interruptions gracefully. The core functionality involves reading from standard input (stdin), extracting specific data from each log entry, and computing metrics based on the extracted information.

## Requirements

### General

- Editors allowed: `vi`, `vim`, `emacs`
- Python version: `3.4.3` or higher
- Operating System: Ubuntu 20.04 LTS
- Files must end with a new line
- The first line of each file must be exactly: `#!/usr/bin/python3`
- Code style: Must follow PEP 8 (version 1.7.x)
- All files must be executable
- File lengths will be tested using the `wc` command

### Input Format

Each log entry follows this format:

```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```

- **IP Address**: IPv4 address
- **Date**: Timestamp of the request
- **Status code**: HTTP status code of the request (e.g., 200, 404)
- **File size**: Size of the file requested

If the input format does not match the expected structure, the line is skipped.

### Output Metrics

The script outputs two types of statistics:

1. **Total file size**: Sum of all processed file sizes.
2. **Number of occurrences of status codes**: Counts for status codes such as 200, 301, 400, 401, 403, 404, 405, and 500.

Statistics are printed:
- After every 10 processed lines
- Upon receiving a keyboard interruption (CTRL + C)

### Output Format

```
File size: <total size>
<status code>: <number of occurrences>
```

Status codes are printed in ascending order, and only those with recorded occurrences are displayed.

## Key Concepts

1. **File I/O**: Reading lines from stdin using `sys.stdin` and processing each log entry.
2. **Signal Handling**: Handling keyboard interruptions (CTRL + C) to print statistics before the program terminates.
3. **Data Processing**: Parsing log entries, extracting the status code and file size, and accumulating data.
4. **Regular Expressions**: Validating log entries using regular expressions to ensure the correct format.
5. **Dictionaries**: Using dictionaries to store and update the counts of status codes and the cumulative file size.
6. **Exception Handling**: Managing exceptions during input reading and data processing to ensure robustness.

## Project Files

- **0-stats.py**: The main script that processes the log entries, computes statistics, and handles interruptions.
- **README.md**: This file, providing an overview and guidelines for the project.

## Usage

1. Generate log entries using a script such as the provided `0-generator.py`:
   ```bash
   ./0-generator.py
   ```
   
2. Pipe the generated log entries into the log parsing script:
   ```bash
   ./0-generator.py | ./0-stats.py
   ```

3. The script will output metrics after processing every 10 lines or when interrupted by CTRL + C.

## Example

```
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
```
