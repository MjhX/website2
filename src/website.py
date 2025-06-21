import os, shutil

def copy_contents(source, destination):
    if not os.path.exists(source):
        raise FileNotFoundError(f"{source} does not exist")
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)
    for i in os.listdir(source):
        source_join = os.path.join(source,i)
        dest_join = os.path.join(destination,i)
        if os.path.isdir(source_join):
            copy_contents(source_join,dest_join)
        elif os.path.isfile(source_join):
            shutil.copy(source_join,dest_join)
        else:
            raise Exception(f"What is {source_join}?")