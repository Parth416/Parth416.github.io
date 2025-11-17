#!/usr/bin/env python3
"""
AI-Powered Speech Fluency and Stammering Reduction Application
Main entry point for the application

Created: November 17, 2025
Author: Parth416
"""

import sys
import os
import logging
from pathlib import Path

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def setup_logging():
    """Setup logging configuration"""
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_dir / "app.log"),
            logging.StreamHandler(sys.stdout)
        ]
    )

def main():
    """Main application entry point"""
    setup_logging()
    logger = logging.getLogger(__name__)
    
    try:
        logger.info("Starting AI Speech Fluency Application")
        
        # Import here to ensure proper path setup
        from src.gui.main_window import SpeechFluencyApp
        
        app = SpeechFluencyApp()
        app.run()
        
    except ImportError as e:
        logger.error(f"Import error: {e}")
        print("Please ensure all dependencies are installed: pip install -r requirements.txt")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Application error: {e}")
        raise

if __name__ == "__main__":
    main()