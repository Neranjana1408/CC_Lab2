from locust import HttpUser, task, between

class EventsUser(HttpUser):
    wait_time = between(0.5, 1)  # reduced wait → more load

    @task(3)  # higher weight
    def view_events(self):
        self.client.get("/events?user=locust_user")

    @task(1)
    def refresh_events(self):
        self.client.get("/events?user=locust_user")