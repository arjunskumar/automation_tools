from PyPDF2 import PdfFileMerger, PdfFileReader

import glob
mergedObject = PdfFileMerger()
 
for fileNumber in glob.glob('/home/arjun/catkin_ws/automation_tools/*.pdf'):
    mergedObject.append(PdfFileReader(fileNumber, 'rb'))
 

mergedObject.write("merged_ouput.pdf")
