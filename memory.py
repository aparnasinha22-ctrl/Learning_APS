class Memory:
    def __init__(self):
        self.data = []

    def add(self, task, result):
        self.data.append({
            "task": task,
            "result": result
        })

    def get_all(self):
        return self.data

    def __str__(self):
        return "\n".join(
            [f"{i+1}. {item['task']} -> {item['result']}"
             for i, item in enumerate(self.data)]
        )