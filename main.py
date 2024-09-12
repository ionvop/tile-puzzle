import os
import zipfile
import time
import shutil
import datetime


def main() -> None:
    if os.path.exists("Project.sb3"):
        if not os.path.isdir("assets"):
            update()

        os.remove("Project.sb3")

    zipf = zipfile.ZipFile("Project.sb3", "w")

    for file in os.listdir("assets/"):
        path = os.path.join("assets/", file)

        if os.path.isdir(path):
            continue

        zipf.write(path, file)

    zipf.close()
    os.startfile("Project.sb3")
    print(f"Loaded at {datetime.datetime.now()}")
    last_modified = os.path.getmtime("Project.sb3")
    
    try:
        while True:
            if last_modified != os.path.getmtime("Project.sb3"):
                update()
                print(f"Updated at {datetime.datetime.now()}")
                last_modified = os.path.getmtime("Project.sb3")

            time.sleep(1)
    except KeyboardInterrupt:
        os.remove("Project.sb3")
        print(f"Exited at {datetime.datetime.now()}")


def update() -> None:
    if os.path.isdir("assets"):
        shutil.rmtree("assets")

    zipf = zipfile.ZipFile("Project.sb3", "r")
    zipf.extractall("assets")
    zipf.close()


if __name__ == "__main__":
    main()