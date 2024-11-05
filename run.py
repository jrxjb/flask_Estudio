from multiprocessing import Process
import app
import app_2

def run_app1():
    app.app.run(port=5000)

def run_app2():
    app_2.app2.run(port=5001)

if __name__ == '__main__':
    process1 = Process(target=run_app1)
    process2 = Process(target=run_app2)
    process1.start()
    process2.start()

    try:
        process1.join()
        process2.join()
    except KeyboardInterrupt:
        print("Terminando los procesos")
        process1.terminate()
        process2.terminate()
