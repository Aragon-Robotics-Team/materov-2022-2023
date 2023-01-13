import input2 as controller
import multiprocessing

def print(num):
    return num

if __name__ == "__main__":
    # p1 = multiprocessing.Process(target=controller.init())
    p1 = multiprocessing.Process(target=print, args=(10,))

    p1.start()