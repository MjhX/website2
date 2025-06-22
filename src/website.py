import os, shutil, re
from markdown_to_html_node import markdown_to_html_node

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
        
def extract_title(markdown):
    ret = re.search(r"\n# .*\n", "\n"+markdown+"\n") # Workaround for no good "start of file or line" options
    if ret == None:
        raise Exception("Header not found")
    return ret[0].replace("# ", "", 1).strip(" \n")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    md = open_and_read(from_path)
    template = open_and_read(template_path)
    content = markdown_to_html_node(md).to_html()
    title = extract_title(md)
    out_page = template.replace("{{ Title }}", title).replace("{{ Content }}", content)
    #os.makedirs(os.path.dirname(dest_path))
    f = open(dest_path,'w')
    f.write(out_page)
    f.close()

def open_and_read(path):
    f = open(path,'r')
    text = f.read()
    f.close()
    return text
