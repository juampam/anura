import index
geted = index.getTitle()
title = str(geted)
def example():
    div = "\n\t\t<li>\n\t<a href=\"#home\">Home</a></li>\n\t\t\t<li><a href=\"#news\">News</a></li>\n\t\t\t<li><a href=\"#contact\">Contact</a></li>\n\t\t\t<li><a href=\"#about\">About</a></li>"
    nav = "\n\t<ul class=\"navbar\">" + div + "\n\t</ul>\n"
    home = "\t<h1>We are here, let's change this</h1>" + "\n\t<h3>Find instructions and more styles here</h3>\n\t<a class = \"btn bg-sec\" href=\"#\">Coming soon</a>"
    exp = nav + home
    return exp
def head():
    res = str("\t<title>"+title+"</title>\n\t<link rel=\"stylesheet\" href=\"style.css\">\n\t<link rel = \'icon\' href=\"img/logo.ico\" type = \"image/x-icon\"/>")
    return res 
