import openpyxl
import sys

if len(sys.argv) < 2:
    print('no file name input')
    sys.exit()

a = openpyxl.Workbook()
sheet = a.active
sheet.title = 'dataset'
file = open(str(sys.argv[1])+'.txt')
i = 0
for l in file:
    line = l.strip("\n")
    tmp = line.split()
    for j in range(len(tmp)):
        sheet.cell(i+1,j+1,int(tmp[j]))
    i += 1
a.save(str(sys.argv[1])+'.xlsx')

