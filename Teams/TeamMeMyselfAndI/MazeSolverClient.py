"""
This class is the template class for the MQTT client which receives MQTT messages 
and sends MQTT messages
"""
import paho.mqtt.client as mqtt
import time
import array as arr
import os
from MazeSolverAlgoBreathFirst import MazeSolverAlgoBreathFirst
from MazeSolverAlgoAStar import MazeSolverAlgoAStar

if "MQTTSERVER" in os.environ and os.environ['MQTTSERVER']:
    mqtt_server = os.environ['MQTTSERVER']
else:
    mqtt_server = "127.0.0.1"

class MazeSolverClient:

    # initialize the MQTT client
    def __init__(self,master,algo="BREATHFIRST"):

        print("Constructor Sample_MQTT_Publisher")
        self.master=master

        self.master.on_connect=self.onConnect
        self.master.on_message=self.onMessage

        self.master.connect(mqtt_server,1883,60)
        
        if algo == "BREATHFIRST":
            self.solver = MazeSolverAlgoBreathFirst()
        else:
            self.solver = MazeSolverAlgoAStar()

        #self.solver.printMaze()

    # Implement MQTT publishing function
    def publish(self, topic, message=None, qos=0, retain=False):
        print("XX I WAS IN PUBLISH")
        print("Published message: " , topic , " --> " , message)
        self.master.publish(topic,message,qos,retain)


    # Implement MQTT receive message function
    def onMessage(self, master, obj, msg):
        topic = str(msg.topic)
        payload = str(msg.payload.decode("utf-8"))
        print("TEAM_MeMyselfAndI: Received message:", topic , " --> " , payload)
        if topic == "/maze":
            if payload == "clear":
                self.solver.clearMaze() 
            elif payload == "start":
                print("XX start XX")
                self.solver.startMaze(0,0)
            elif payload == "solve":
                print("XX SOLVED XX")
                self.solveMaze()
            elif payload == "end":
                print("XX Payload END XX")
                self.solver.endMaze()
                self.solver.printMaze()
            else:
                pass
        elif topic == "/maze/dimRow":
            self.solver.setDimRows(int(payload))
            self.solver.startMaze(self.solver.dimRows,self.solver.dimCols)
        elif topic == "/maze/dimCol":
            self.solver.setDimCols(int(payload))
            self.solver.startMaze(self.solver.dimRows, self.solver.dimCols)
        elif topic == "/maze/startRow":
            self.solver.setStartRow(int(payload))
        elif topic == "/maze/startCol":
            self.solver.setStartCol(int(payload))
        elif topic == "/maze/endRow":
            self.solver.setEndRow(int(payload))
        elif topic == "/maze/endCol":
            self.solver.setEndCol(int(payload))
        elif topic == "/maze/blocked":
            cell = payload.split(",")
            self.solver.setBlocked(int(cell[0]),int(cell[1]))
        else:
            pass



    # Implement MQTT onConnecr function
    def onConnect(self, master, obj, flags, rc):
        self.master.subscribe("/maze" )
        self.master.subscribe("/maze/dimRow" )
        self.master.subscribe("/maze/dimCol" )
        self.master.subscribe("/maze/startCol" )
        self.master.subscribe("/maze/startRow" )
        self.master.subscribe("/maze/endCol" )
        self.master.subscribe("/maze/endRow" )
        self.master.subscribe("/maze/blocked" )     
 

    # Initiate the solving process of the maze solver
    def solveMaze(self):
        path=self.solver.solveMaze()

        print(path)

        for step in path:
            step_str = '{},{}'.format(step[0],step[1])
            self.publish("/maze/go" , step_str)

    
if __name__ == '__main__':
    mqttclient=mqtt.Client()

    solverClient = MazeSolverClient(mqttclient,"ASTAR")
    solverClient.master.loop_forever()
