from locust import HttpLocust, TaskSet, task


class HitSomeRandomAPIs(TaskSet):
    @task(2)
    def delayed(self):
        self.client.get("/delay/1")

    @task(1)
    def fail(self):
        self.client.get("/status/500")
        self.client.get("/status/502")
        self.client.get("/status/404")
        self.client.get("/status/401")

    @task(1)
    def exception(self):
        assert 1 == 0

    def on_start(self):
        print("this is where you'd log in for example")

    def on_stop(self):
        print("...and log out")


class WebsiteUser(HttpLocust):
    task_set = HitSomeRandomAPIs
    min_wait = 5000  # 5s
    max_wait = 9000
