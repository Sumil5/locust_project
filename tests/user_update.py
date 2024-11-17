from locust import HttpUser, task, between
import logging

logging.basicConfig(
    filename="logs/test_run.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class UserUpdateTest(HttpUser):
    host = "https://reqres.in"
    wait_time = between(1, 3)

    @task
    def update_user(self):
        payload = {"name": "Jane Doe", "job": "Data Scientist"}
        response = self.client.put("/api/users/2", json=payload)
        if response.status_code == 200:
            logging.info(f"User updated successfully: {response.json()}")
        else:
            logging.error(f"Failed to update user: {response.status_code}, {response.text}")
