import logging

# Configure logging
logging.basicConfig(
    filename="logs/test_run.log",  # Ensure the path matches your log file
    filemode="a",                 # Append mode; use 'w' to overwrite each run
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,           # Log INFO level and above
)

# Example message to test logging
logging.info("Starting Locust test suite...")





from tests.user_creation import UserCreationTest
from tests.user_list import UserListTest
from tests.user_update import UserUpdateTest
