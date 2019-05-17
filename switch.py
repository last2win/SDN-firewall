# -*- coding: utf-8 -*-


from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import RemoteController


class MyTopo(Topo):
    "Firewall topology."

    def __init__(self):
        "Create topo."

        # Initialize topology
        Topo.__init__(self)

        # Add hosts and switches
        h1 = self.addHost('h1')  # 10.0.0.1
        h2 = self.addHost('h2')  # 10.0.0.2
        h3 = self.addHost('h3')  # 10.0.0.3
        s1 = self.addSwitch('s1')

        # Add links
        self.addLink(h1, s1)  # s1-eth1
        self.addLink(h2, s1)  # s1-eth2
        self.addLink(h3, s1)
        self.addLink(h3, s1)


def myNet():
    net = Mininet(topo=MyTopo(),
                  controller=lambda name: RemoteController(name, ip='127.0.0.1'))
    net.addNAT().configDefault()
    net.start()
    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    myNet()

