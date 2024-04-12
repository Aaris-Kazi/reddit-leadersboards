class ApplicationExcption(Exception):
    """
    Custom Excption block to Identify or raise the expected Excptions
    """

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)