from app import create_app, db
from threading import Timer
import webbrowser
from flask_migrate import upgrade
import logging
from flask import Flask



logging.basicConfig(level=logging.INFO)

def open_browser():
    """Browser ko automatically open karne ke liye function, ek hi baar open hoga."""
    url = "http://127.0.0.1:5000/MTM/login"
    
    try:
        webbrowser.open_new(url)  
    except webbrowser.Error:
        logging.error("Browser open nahi ho raha, manually open karein.")


app = create_app()

if __name__ == "__main__":
    with app.app_context():
        try:
            
            upgrade()
        except Exception as e:
            logging.error(f"Database migration error: {e}")

    
    Timer(1, open_browser).start()
    
    
    app.run(host="127.0.0.1", port=5000, debug=True, use_reloader=False)
