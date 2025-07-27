import time
import random

#  Decorator Function
def logLightChange(func):
    """Logs whenever the light changes state"""
    def wrapper(self, *args, **kwargs):
        old = self.state
        result = func(self, *args, **kwargs)
        print(f"Light changed at Frame {self.frame_id}: {old} -> {self.state}")
        return result
    return wrapper

# For Queue System    
class Node:
    def __init__(self, vehicle):
        self.vehicle = vehicle
        self.next = None

class VehicleQueue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def addVehicle(self, v_type): # enqueue
        node = Node(v_type)
        if not self.rear:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node
    
    def removeVehicle(self): #dequeue
        if not self.front:
            return None
        v = self.front.vehicle
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return v
    
    def isEmpty(self):
        return self.front is None

# For Traffic Lights 
class TrafficLight:
    def __init__(self, frame_id):
        self.frame_id = frame_id
        self.state = "RED"

    @logLightChange
    def changeState(self, new_state):
        self.state = new_state

# For Frame 
class Frame:
    def __init__(self, fid):
        self.frame_id = fid
        self.queue = VehicleQueue()
        self.light = TrafficLight(fid)

    def addVehicle(self, v_type):
        self.queue.addVehicle(v_type)

    def processVehicles(self, seconds):
        """ vehicles pass while light is green"""
        start = time.time()
        while time.time() - start < seconds:
            if not self.queue.isEmpty():
                v_type = self.queue.removeVehicle()
                name = {1: "Bike", 2: "Car", 3: "Truck"}.get(v_type, "Unknown")
                print(f"Frame {self.frame_id}: {name} passed")
                time.sleep(1)  # short pause for each vehicle
            else:
                break

# For Traffic System 
class TrafficSystem:
    def __init__(self):
        self.frames = {i: Frame(i) for i in range(1, 5)}

    def generateVehicles(self):
        """Generate random vehicles for every frame when it goes green"""
        for frame in self.frames.values():
            for _ in range(random.randint(1, 3)):
                v = random.randint(1, 3)  # 1=> Bike, 2=>Car, 3=>Truck
                frame.addVehicle(v)

    def processGreen(self, fid):
        frame = self.frames[fid]
        frame.light.changeState("GREEN")
        print(f"Frame {fid} GREEN for 15 sec...")
        frame.processVehicles(15)

    def processYellow(self, fid):
        frame = self.frames[fid]
        frame.light.changeState("YELLOW")
        print(f"Frame {fid} YELLOW for 2 sec...")
        time.sleep(2)
        frame.light.changeState("RED")

    def showLights(self):
        print("\n======= Traffic Lights =======")
        for fid, frame in self.frames.items():
            print(f"Frame {fid}: {frame.light.state}")

# For Run Simulation
def runSimulation():
    print("Start Traffic Simulation")
    input("Press Enter to begin...")

    system = TrafficSystem()
    order = [1, 3, 2, 4]  # signal change order
    idx = 0
    cycle = 1

    while True:
        print(f"\n==== CYCLE {cycle} ====")
        system.generateVehicles()  # new vehicles will appear

        current = order[idx]
        idx = (idx + 1) % len(order)

        system.showLights()
        system.processGreen(current)
        system.processYellow(current)

        # after 2 cycles, ask to continue or quit
        if cycle % 2 == 0:
            if input("\nPress Enter to continue, or 'q' to quit: ").lower() == 'q':
                break
        cycle += 1

# Main 
if __name__ == "__main__":
    runSimulation()
