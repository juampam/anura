import os
import shutil


def example():
    div = "\n\t\t<li><a href=\"#home\">Home</a></li>\n\t\t\t<li><a href=\"#news\">News</a></li>\n\t\t\t<li><a href=\"#contact\">Contact</a></li>\n\t\t\t<li><a href=\"#about\">About</a></li>"
    nav = "\n\t<ul class=\"navbar\">" + div + "\n</ul> " 
    home = "<h1>Let's Jumping and Singing</h1>" + "\n<h3>Frogs are here!</h3>"
    exp = nav + home
    print(exp)
    return exp

def code():
    inp = input()
    ep = inp.split(sep = ' -')
    
    for x in ep:
        y = x.split(sep = ' ')
        print(y)
        for i in y:
            print(i)
        
            if i == "n":
                z = y.remove('n')
                title = y[0]
            if i == "s":
                bcx = title.title()
                stpath = bcx + '/style.css'
            if i == "E":
                example()
            if i == "I":
                name = str("index.html")
            else:
                name = 'changeme.html'

if ep[0] == "create":
        bcx = title.title()
        os.mkdir(bcx)
        path = bcx +'/'+ name
        bcontent = example()
        hcontent = str("\t<title>"+title+"</title>\n\t<link rel=\"stylesheet\" href=\"style.css\">\n\t<link rel = \'icon\' href=\"../logo.svg\" type = \"image/x-icon\"/>")
        head = str("<head>\n" + hcontent + "\n</head>\n")
        #componet = example()
        body = str("<body>\n"+bcontent+"\n</body>")
        file = open(path, "w")
        file.write("<!DOCTYPE HTML>" + os.linesep)
        file.write(head)
        file.write(body)
        file.close()
        file = open(stpath, "w")  
        #Static style (change)
        with open("Default") as f:
            contents = f.readlines()
            line = str(contents)
        file.write(line)
        file.close()

    if ep[0] == "help":
        print("Usage: nezumi <COMAND> <OPTIONS>\n COMANDS:\n\t create: \t create a new project\n\t help\t show help xD")
        print("\t rebuild\t modify atributes")
        print("OPTIONS\n\t -n\t Set name\n\t -s\t set style (Nezumi|Drakula|Tokyo|Monokai|Material) ")
        print("OPTION ORDER: -n -s -I") 
    if ep[0] == "delete":
        bcx = title.title()
        shutil.rmtree(bcx)
    if ep[0] == 'in':
        path = ep[1]
        print(path)
       

    if ep[0] != "create" or ep[0] != "help":
        print("Anura: " + "Error, "+ ep[0] + " is not a Anura command" )
      
    print(ep[0])
code()
