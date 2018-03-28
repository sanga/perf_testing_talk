from locust import HttpLocust, TaskSet, task


class HitSomeRandomAPIs(TaskSet):
    @task(20)
    def get(self):
        self.client.get("/Caddyfile")

    @task(1)
    def fail(self):
        self.client.get("/file_not_found_404")


class WebsiteUser(HttpLocust):
    task_set = HitSomeRandomAPIs
    min_wait = 5000  # 5s
    max_wait = 9000
