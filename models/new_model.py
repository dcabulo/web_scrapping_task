class New:
    def __init__(self, title: str,body: str):
        self.title = title
        self.body = body

    def to_dict(self):
        return {"title": self.title, "body": self.body}

    def __str__(self):
        new = ''
        new += f'Title: {self.title}\n'
        new += f'Body: {self.body}\n'
        return new
