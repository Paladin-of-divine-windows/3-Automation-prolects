import camelot
import ctypes


table = camelot.read_pdf('49.pdf', pages="2")
print(table)
