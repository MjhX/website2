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

def generate_page(from_path, template_path, dest_path, basepath="/"):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    md = open_and_read(from_path)
    template = open_and_read(template_path)
    content = markdown_to_html_node(md).to_html()
    title = extract_title(md)
    out_page = template.replace("{{ Title }}", title).replace("{{ Content }}", content)
    out_page = out_page.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')
    os.makedirs(dest_path, exist_ok = True)
    out_html = os.path.basename(from_path).split(".")[0]+".html"
    open_and_write(os.path.join(dest_path, out_html), out_page)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath="/"):
    def recurse(partial_path):
        joined_path_dir = os.path.join(dir_path_content, partial_path)
        for i in os.listdir(joined_path_dir):
            joined_i = os.path.join(joined_path_dir,i)
            if os.path.isdir(joined_i):
                recurse(os.path.join(partial_path,i))
            elif os.path.isfile(joined_i):
                if i.endswith(".md"):
                    generate_page(joined_i, template_path, os.path.join(dest_dir_path, partial_path), basepath)
            else:   
                raise Exception(f"What is {joined_i}?")
    recurse("")

def open_and_read(path):
    f = open(path,'r')
    text = f.read()
    f.close()
    return text

def open_and_write(path, output):
    f = open(path,'w')
    f.write(output)
    f.close()
