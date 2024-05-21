def makeNPages(n):
    for i in range(n):
        if i == n - 1:
            f = open("hw18/page_{}.html".format(i), "w")
            html = "<html> <body> This is page number {}. <br>".format(i)
            html += '\n <img src="numbers/num{}.jpg"> <br>'.format(i)
            html += '\n The next page is <a href = "page_{}.html"> page 0. </a>'.format(0)
            html += "\n </body> </html>"
            f.write(html)
            f.close()
        else:
            f = open("hw18/page_{}.html".format(i), "w")
            html = "<html> <body> This is page number {}. <br>".format(i)
            html += '\n <img src="numbers/num{}.jpg"> <br>'.format(i)
            html += '\n The next page is <a href = "page_{}.html"> page {}. </a>'.format(i + 1, i + 1)
            html += "\n </body> </html>"
            f.write(html)
            f.close()

makeNPages(6)
        
