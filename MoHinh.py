from mininet.topo import Topo

class MyTopo(Topo):
    """Custom topology: 3 switches in a triangle, each switch connected to 2 hosts."""
    def __init__(self):
        """Create custom topology."""
        Topo.__init__(self)
        
        # Add hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        
        # Add switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        
        # Add links between switches (triangle topology)
        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s3, s1)
        
        # Add host-switch connections
        self.addLink(s1, h1)
        self.addLink(s1, h2)
        self.addLink(s2, h3)
        self.addLink(s2, h4)
        self.addLink(s3, h5)
        self.addLink(s3, h6)

# To run this topology with Mininet:
# sudo mn --controller=remote,ip=127.0.0.1,port=6653 --custom filename.py --topo tp

topos = { 'tp': (lambda: MyTopo()) }
