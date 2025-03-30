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
        webbrowser.open_new(url)  # Sirf ek tab open karega
    except webbrowser.Error:
        logging.error("Browser open nahi ho raha, manually open karein.")

# Flask app create kar rahe hain
app = create_app()

if __name__ == "__main__":
    with app.app_context():
        try:
            # Ensure migrations are applied
            upgrade()
        except Exception as e:
            logging.error(f"Database migration error: {e}")

    # Ek hi baar browser tab open karega
    Timer(1, open_browser).start()
    
    # Flask app run karega, but auto-reload disable hai
    app.run(host="127.0.0.1", port=5000, debug=True, use_reloader=False)
