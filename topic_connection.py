from naoqi import ALProxy
import time


class Commande():
    def __init__(self):

        self.robot_ip = "169.254.179.68"
        self.robot_port = 9559
        self.top_path = "/home/nao/naoqi/topic_pack/"
        self.concept_path = self.top_path+"concept/concept_enu.top"
        self.drink_path = self.top_path+"drink/drink_enu.top"
        self.food_path = self.top_path+"food/food_enu.top"

    def main(self):
        self.concept(self.robot_ip, self.robot_port, self.concept_path)

        
    def drink(self, robot_ip, robot_port, topic_path):

        dialog = ALProxy('ALDialog',robot_ip,robot_port)

        topic_path=topic_path.decode('utf-8')
        topic = dialog.loadTopic(topic_path.encode('utf-8'))

        dialog.subscribe('myModule')
        dialog.activateTopic(topic)

        raw_input(u"Press 'Enter' to continue")

        dialog.deactivateTopic(topic)
        dialog.unloadTopic(topic)
        dialog.unsubscribe('myModule')
        

    def food(self, robot_ip, robot_port, topic_path):

        dialog = ALProxy('ALDialog',robot_ip,robot_port)

        topic_path=topic_path.decode('utf-8')
        topic = dialog.loadTopic(topic_path.encode('utf-8'))

        dialog.subscribe('myModule')
        dialog.activateTopic(topic)

        raw_input(u"Press 'Enter' to continue")

        dialog.deactivateTopic(topic)
        dialog.unloadTopic(topic)
        dialog.unsubscribe('myModule')


    def concept(self, robot_ip, robot_port, topic_path):

        dialog = ALProxy('ALDialog',robot_ip, robot_port)
        memory = ALProxy('ALMemory',robot_ip, robot_port)

        
        topic_path=topic_path.decode('utf-8')
        topic = dialog.loadTopic(topic_path.encode('utf-8'))

        dialog.subscribe('myModule')
        dialog.activateTopic(topic)

        while 1:
            print "The value of myValueName1 is", memory.getData("foood")
            time.sleep(2)

        raw_input(u"Press 'Enter' to exit")

        dialog.deactivateTopic(topic)
        dialog.unloadTopic(topic)
        dialog.unsubscribe('myModule')


if __name__ == '__main__':
    commande = Commande()
    commande.main()
