from transitions import Machine
import queue

class Order:
    states= ['placed','in_progress','in_delivery','canceled','completed']

    def __init__(self,name):
        self.name=name
        self.machine=Machine(model=self,states=Order.states,initial='placing')


        self.machine.add_transition(trigger='progress',source='placing',dest='in_progress')
        
        self.machine.add_transition(trigger='deliver',source='in_progress',dest='in_delivery')
        
        self.machine.add_transition(trigger='cancel',source='*',dest='canceled')

        self.machine.add_transition(trigger='complete',source='in_delivery' ,dest='completed')



class OrderSystem:


    def __init__(self):
        self.orders={}
        self.event_queue=queue.Queue()

    def create_order(self,name):
        order=Order(name)
        self.orders[name]=order
        self.event_queue.put((order,'progress'))
        print("Created Order")

    def cancel_order(self,name):
        if name in self.orders:
            self.event_queue.put((self.orders[name],'cancel'))
            print("Cancelled Order")

    def deliver_order(self,name):
        if name in self.orders and self.orders[name].state=='in_progress':
            self.event_queue.put((self.orders[name],'deliver'))
            print("Delivered Order")

    
    def complete_order(self,name):
        if name in self.orders and self.orders[name].state=='in_delivery':
            self.event_queue.put((self.orders[name],'complete'))
            print("Completed Order")

    def process_events(self):
        while not self.event_queue.empty():
            order,event=self.event_queue.get()
            getattr(order,event)()



system=OrderSystem()
system.create_order('Order1')
system.process_events()
system.deliver_order('Order1')
system.process_events()
system.complete_order('Order1')
system.process_events()


