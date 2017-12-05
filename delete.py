# import os
# import urllib2
# from reportlab.lib.pagesizes import letter
# from reportlab.lib.units import inch
# from reportlab.pdfgen import canvas

# filename = './python-logo.png'

# def get_python_image():
#     """ Get a python logo image for this example """
#     if not os.path.exists(filename):
#         response = urllib2.urlopen(
#             'http://www.python.org/community/logos/python-logo.png')
#         f = open(filename, 'w')
#         f.write(response.read())
#         f.close()

# get_python_image()

# c = canvas.Canvas('imageabs.pdf', pagesize=letter)
# width, height = letter
# c.drawImage(filename, inch, height - 2 * inch) # Who needs consistency?
# c.showPage()
# c.save()

import time
start_time = time.time()



def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    # print("--- %s mani ---" % (time.time() - start_time))
    return theSum

print(listsum(range(999)),"--- %s normal ---" % (time.time() - start_time))




def listsum(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        # print("--- %s seconds ---" % (time.time() - start_time))
        return numList[0] + listsum(numList[1:])



print(listsum(range(999)),"--- %s recursive ---" % (time.time() - start_time))








