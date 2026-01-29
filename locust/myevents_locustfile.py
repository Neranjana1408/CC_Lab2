from locust import HttpUser, task, between

class MyEventsUser(HttpUser):
    wait_time = between(0.5, 1)

    @task(2)
    def view_my_events(self):
        self.client.get("/my-events?user=locust_user")

    @task(1)
    def refresh_my_events(self):
        self.client.get("/my-events?user=locust_user")