"""Main file to run All-in-One application.
"""
import asyncio
from src import all_in_one_app as app


def main():
    """Main function to run the All-in-One application.
    """
    asyncio.run(app.run())


if __name__ == "__main__":
    main()
