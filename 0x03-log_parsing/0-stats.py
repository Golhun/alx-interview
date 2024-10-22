#!/usr/bin/python3
'''A script to parse HTTP request logs and compute metrics.
'''

import re


def extract_input(input_line):
    '''Extracts relevant data from an HTTP request log line.

    Args:
        input_line (str): A line from the HTTP request log.

    Returns:
        dict: Dictionary with 'status_code' and
        'file_size' extracted from the log.
    '''
    log_pattern = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+-\d+-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    log_format = '{}\\-{}{}{}{}\\s*'.format(*log_pattern)
    match = re.fullmatch(log_format, input_line)
    info = {
        'status_code': 0,
        'file_size': 0,
    }
    if match:
        info['status_code'] = match.group('status_code')
        info['file_size'] = int(match.group('file_size'))
    return info


def print_statistics(total_file_size, status_codes_stats):
    '''Prints the aggregated log metrics.

    Args:
        total_file_size (int): Sum of all file sizes.
        status_codes_stats (dict): Count of each HTTP status code.
    '''
    print(f'File size: {total_file_size}', flush=True)
    for status_code in sorted(status_codes_stats.keys()):
        count = status_codes_stats.get(status_code, 0)
        if count > 0:
            print(f'{status_code}: {count}', flush=True)


def update_metrics(line, total_file_size, status_codes_stats):
    '''Updates file size and status code count from the log line.

    Args:
        line (str): The log line to process.
        total_file_size (int): Current total file size.
        status_codes_stats (dict): Count of each status code.

    Returns:
        int: Updated total file size.
    '''
    line_info = extract_input(line)
    status_code = line_info.get('status_code', '0')
    if status_code in status_codes_stats:
        status_codes_stats[status_code] += 1
    return total_file_size + line_info['file_size']


def run():
    '''Runs the log parser to read from stdin and compute metrics.'''
    line_num = 0
    total_file_size = 0
    status_codes_stats = {
        str(code): 0 for code in (
            200, 301, 400, 401, 403, 404, 405, 500)}

    try:
        while True:
            line = input()
            total_file_size = update_metrics(
                line, total_file_size, status_codes_stats)
            line_num += 1
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_file_size, status_codes_stats)


if __name__ == '__main__':
    run()
