from avm.helpers import server

class Center:

    def __init__(self, address, username, password=None):

        self.server = server.Server(address, username, password)

    def list(self):

        items = self.server.list_centers()

        for item in items:

            print(item.name, item)

    def search_by_name(self, name):

        items = self.server.list_centers()

        for item in items:

            if item.name == name:

                print(item.name, item)
