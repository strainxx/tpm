import core
import parser
import sys
import multiprocessing as mp

running = True


def main():
    global running
    sys.stdin = open(0)
    while running:
        cmd = input("---> ")
        if cmd == "exit":
            print("Terminating run process")
            running = False
            sys.exit(0)
        else:
            core.command(cmd)


if __name__ == "__main__":
    print("Started init...")
    core.init()
    print("Started tpm shell")
    p = mp.Process(target=core.run)
    p1 = mp.Process(target=main)
    p.start()
    p1.start()
    p.join()
    p1.join()
