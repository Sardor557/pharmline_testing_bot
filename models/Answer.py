class Answer:
    def __init__(self, isSuccess: bool, message: str, data):
        self.isSuccess: bool = isSuccess
        self.message: str = message
        self.data = data
