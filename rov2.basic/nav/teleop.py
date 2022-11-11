##initiates the teleop loop

from nav.teleopConfig import Config 

def teleopMain(input_queue, output_queue):
    # robot = Config('Mac', True, False, input_queue, output_queue) # comp type, serial on, serial recieve on, input, output queue

    # statuses = [0, 0, 0, 0, 1, 1, 1, 1]
    # output_queue.put(statuses)
    # print("put in queue")

    print("in teleopMain")

    robot = Config('Mac', True, False, input_queue, output_queue)
    print("starting teleop")
    robot.joy_init()
    print("starting joy_init")



if __name__ == '__main__':
    pass