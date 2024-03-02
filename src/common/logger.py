from datetime import datetime

class Logger:
    def log(self, message, color, item=None):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if item:
            log_message = f'{color}{timestamp} - [{item}] - {message}{Colors.DEFAULT}\n'
        else:
            log_message = f'{color}{timestamp} - {message}{Colors.DEFAULT}\n'
        print(log_message, end='')
        
    def debug(self, message, item=None):
        self.log(message, Colors.BLUE, item)

    def info(self, message, item=None):
        self.log(message, Colors.DEFAULT, item)

    def warning(self, message, item=None):
        self.log(message, Colors.YELLOW, item)

    def error(self, message, item=None):
        self.log(message, Colors.RED, item)

    def success(self, message, item=None):
        self.log(message, Colors.GREEN, item)
        
class Colors:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    DEFAULT = '\033[0m'
    
class Styles:
    DEFAULT = '\033[0m' 
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    