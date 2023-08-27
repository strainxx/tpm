import os
import sys
import parser
import runpy
import asyncio


def init():
    print("tpm core v.1")
    try:
        import pyrogram
    except ModuleNotFoundError:
        print("Pyrogram not found. Type 'setup' to install")
    print("")


def run():
    runpy.run_path(f"{sys.path[0]}/spammer/main.py")


def command(cmd):
    if cmd == "help":
        print("\n _______ _____  __  __")
        print("|__   __|  __ \|  \/  |\t\tTelergram Package Manager")
        print("   | |  | |__) | \  / |\t\tVersion: beta 1")
        print("   | |  |  ___/| |\/| |")
        print("   | |  | |    | |  | |\t\tModules repo: tpm.aruus.uk")
        print(f"   |_|  |_|    |_|  |_|\t\tModules installed: {len(parser.parse())}\n")
        print("\n\nCommands:")
        print("info - shows all installed plugins\nhelp - shows this\nexit - exit\nsetup - do setup\nsrc - open "
              "github link (only windows??)")

    if cmd == "info":
        parser.info(parser.parse())

    if cmd == "setup":
        os.system("echo tpm was there && pip install pyrogram tgcrypto")

    if cmd == "src":
        os.system("start www.aruus.uk")


def exit():
    pass
