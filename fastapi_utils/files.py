from io import BytesIO


class NamedBytesIO(BytesIO):

    def __init__(self, *args, name: str, **kwargs):
        super().__init__(*args, **kwargs)
        self.filename = name
