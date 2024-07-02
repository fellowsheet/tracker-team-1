from datetime import datetime


def valid_date(text: str) -> str | None:
    try:
        datetime.strptime(text, "%d-%m-%Y")
        return text
    
    except ValueError:
        return None