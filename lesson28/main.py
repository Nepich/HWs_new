class TreeNod:
    def __init__(self, some_text, *kids):
        self.__some_text = some_text
        self.kids = kids

    def get_some_text(self):
        return self.__some_text
