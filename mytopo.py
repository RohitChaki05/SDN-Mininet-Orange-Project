from mininet.net import Mininet
from mininet.node import OVSSwitch, OVSController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def multiSwitchNet():
    # Use OVSController for better compatibility
    net = Mininet(controller=OVSController, switch=OVSSwitch)

    info('*** Adding controller\n')
    net.addController('c0')

    info('*** Adding hosts\n')
    h1 = net.addHost('h1', ip='10.0.0.1')
    h2 = net.addHost('h2', ip='10.0.0.2')
    h3 = net.addHost('h3', ip='10.0.0.3')

    info('*** Adding switches\n')
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')

    info('*** Creating links\n')
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s2)
    net.addLink(s1, s2)

    info('*** Starting network\n')
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    multiSwitchNet()