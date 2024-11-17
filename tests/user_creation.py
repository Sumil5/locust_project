from locust import HttpUser, task, between
import logging

logging.basicConfig(
    filename="logs/test_run.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class UserCreationTest(HttpUser):
    host = "https://reqres.in"
    wait_time = between(1, 3)

    @task
    def create_user(self):
        payload = {"name": "John Doe", "job": "Software Engineer"}
        response = self.client.post("/api/users", json=payload)
        if response.status_code == 201:
            logging.info(f"User created successfully: {response.json()}")
        else:
            logging.error(f"Failed to create user: {response.status_code}, {response.text}")
