import datetime

def log_error_to_file(message):
    """Log an error message to a file with a timestamp."""
    with open('Error_Logs/error_log.txt', 'a') as log_file:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_file.write(f"{timestamp} - {message}\n")
