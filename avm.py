import fire
from avm.commands import center, cluster, section, storage, network

class Pipeline:

    def __init__(self):

        self.center = center.Center
        self.cluster = cluster.Cluster
        self.section = section.Section
        self.storage = storage.Storage
        self.network = network.Network

if __name__ == '__main__':

    fire.Fire(Pipeline)
