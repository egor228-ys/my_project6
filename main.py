import logging
from src.auth.auth_service import AuthService
from src.auth.exceptions import AuthError
from src.logger_config import setup_logging

setup_logging()

def main():
    auth = AuthService()
    try:
        auth.register("ivan", "12345")
        auth.login("ivan", "12345")
        auth.login("ivan", "wrong")
    except AuthError as e:
        logging.error(f"Auth error: {e}")
    except Exception as e:
        logging.critical(f"Unknown error: {e}")
    finally:
        logging.info("Application shutdown")

if __name__ == "__main__":
    main()
