import os
import re
import glob

def main():
    top_html = get_top_html()
    bottom_html = get_bottom_html()
    latest_file_name = get_latest_file_name()
    middle_html = get_middle_html(latest_file_name)
    the_html = "".join([top_html, middle_html, bottom_html])
    print(the_html)
    #with open("index.html", "w") as file:
    #    file.write(the_html)

def get_latest_file_name():
    list_of_files = glob.glob('G:/Dropbox/drunkliar/*') # * means all if need specific format then *.csv
    
    #if pic.jpg is in here, use that
    for file_name in list_of_files:
        if re.search("\\\pic.jpg$", file_name, re.IGNORECASE):
            list_of_files = [file_name]
        
    latest_file_name_full= max(list_of_files, key=os.path.getctime)
    latest_file_name = re.search("\\\([^\\\]+)$", latest_file_name_full).group(1)
    return latest_file_name

def get_middle_html(latest_file_name):
    middle_html_1 = "<center>"
    middle_html_2 = ''.join(['<img src="drunkliar/', latest_file_name, '" alt="fun" title="fun" />'])
    middle_html_3 = "</center>"
    middle_html = "\n".join([middle_html_1, middle_html_2, middle_html_3])
    
    return middle_html

def get_bottom_html():
    bottom_html = """
    </body>
</html>"""
    return bottom_html

def get_top_html():
    top_html = """
<html>
    <head>
        <title>no... you are!</title>
        <style>
            a {
            color: white;
            text-decoration: none; /* no underline */
            }
            img {
            max-width: 100%;
            max-height: 100%;
            }        
        </style>
        <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=UA-40545865-2"></script>
        <script>
          window.dataLayer = window.dataLayer || [];
          function gtag(){dataLayer.push(arguments);}
          gtag('js', new Date());

          gtag('config', 'UA-40545865-2');
        </script>    
    </head>
    <body style="background-color:black;">
	<center><font size="24" color="white">See! I told you!</a> :)</font></center>
    """
    return top_html

if __name__ == '__main__':
    main()