import getpass
from pyVmomi import vim
from pyVim import connect

class Server:

    def __init__(self, address, username, password=None):

        if not password:
            password = getpass.getpass()

        self.connection = connect.SmartConnectNoSSL(host=address, user=username, pwd=password)

    def list_centers(self):

        return self.list_by_type(vim.Datacenter)

    def list_clusters(self):

        return self.list_by_type(vim.ComputeResource)

    def list_sections(self):

        return self.list_by_type(vim.ResourcePool)

    def list_storages(self):

        return self.list_by_type(vim.Datastore)

    def list_networks(self):

        return self.list_by_type(vim.Network)

    def list_by_type(self, type):

        items = []

        container = self.get_container_by_type(type)

        for item in container.view:

            items.append(item)

        return items

    def get_container_by_type(self, type):

        return self.connection.content.viewManager.CreateContainerView(self.connection.content.rootFolder, [type], True)
