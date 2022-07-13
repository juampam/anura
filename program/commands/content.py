import index
geted = index.getTitle()
title = str(geted)
def example():
    div = "\n\t\t<li><a href=\"#home\">Home</a></li>\n\t\t\t<li><a href=\"#news\">News</a></li>\n\t\t\t<li><a href=\"#contact\">Contact</a></li>\n\t\t\t<li><a href=\"#about\">About</a></li>"
    nav = "\n\t<ul class=\"navbar\">" + div + "\n</ul> "
    home = "<h1>Let's Jumping and Singing</h1>" + "\n<h3>Frogs are here!</h3>"
    exp = nav + home
    return exp
def head():
    res = str("\t<title>"+title+"</title>\n\t<link rel=\"stylesheet\" href=\"style.css\">\n\t<link rel = \'icon\' href=\"../logo.svg\" type = \"image/x-icon\"/>")
    return res 
