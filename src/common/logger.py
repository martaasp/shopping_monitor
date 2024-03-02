from datetime import datetime

class Logger:
    def __init__(self, item_name=None):
        self.set_item_name(item_name)
    
    def set_item_name(self, item_name):
        self.item_name=item_name
    
    def log(self, message, color):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if self.item_name:
            log_message = f'{color}{timestamp} - [{self.item_name}] - {message}{Colors.DEFAULT}\n'
        else:
            log_message = f'{color}{timestamp} - {message}{Colors.DEFAULT}\n'
        print(log_message, end='')
        
    def debug(self, message):
        self.log(message, Colors.BLUE)

    def info(self, message):
        self.log(message, Colors.DEFAULT)

    def warning(self, message):
        self.log(message, Colors.YELLOW)

    def error(self, message):
        self.log(message, Colors.RED)

    def success(self, message):
        self.log(message, Colors.GREEN)
    
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
    