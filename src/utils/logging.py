import logging
import os
from datetime import datetime
from pathlib import Path

def setup_critical_logger():
    """Setup logger for critical events that need to be preserved"""
    
    # Create logs directory if it doesn't exist
    logs_dir = Path(__file__).parent.parent.parent / 'logs'
    logs_dir.mkdir(exist_ok=True)
    
    # Create critical logger
    critical_logger = logging.getLogger('critical')
    critical_logger.setLevel(logging.CRITICAL)
    
    # Create file handler
    log_file = logs_dir / 'critical.log'
    handler = logging.FileHandler(str(log_file))
    handler.setLevel(logging.CRITICAL)
    
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    
    # Add handler to logger
    critical_logger.addHandler(handler)
    
    return critical_logger

# Create the logger instance
critical_logger = setup_critical_logger()
