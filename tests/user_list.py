from locust import HttpUser, task, between
import logging

logging.basicConfig(
    filename="logs/test_run.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class UserListTest(HttpUser):
    host = "https://reqres.in"
    wait_time = between(1, 3)

    @task
    def fetch_users(self):
        response = self.client.get("/api/users?page=2")
        if response.status_code == 200:
            logging.info(f"User list fetched successfully: {response.json()}")
        else:
            logging.error(f"Failed to fetch users: {response.status_code}, {response.text}")
