class SingletonService:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonService, cls).__new__(cls)
        return cls._instances[cls]