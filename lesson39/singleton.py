class Something:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instanse = super().__new__(cls)
        return cls.__instance

    def __init__(self, something):
        self.something = something

    def __del__(self):
        Something.__instance = None
