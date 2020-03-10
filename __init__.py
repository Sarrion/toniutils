import sys

def printoni(input_obj, ncol = '', nrow = '', file = sys.stdout):
    matrixprint(dirtoni(input_obj), ncol, nrow, file)
    
    
def matrixprint(inputList, ncol, nrow, file):
    if nrow == '':
        nrow = len(inputList) // ncol
        if len(inputList) // ncol != 0:
            nrow += 1
            
    if ncol == '':
        ncol = len(inputList) // nrow
        if len(inputList) // nrow != 0:
            ncol += 1
    
    if len(inputList) < ncol * nrow:
        inputList += list((ncol * nrow - len(inputList)) * ' ')

    columnList = [inputList[nrow*i:nrow*(i+1)] for i in range(ncol)]
    maxLengths = [max([len(element) for element in column]) for column in columnList]
    for i in range(nrow):
        stringToPrint = ""
        for j in range(ncol):
            stringToPrint += columnList[j][i].ljust(maxLengths[j], " ") + " "
        print(stringToPrint, file = file)

        
def dirtoni(input_obj):
    if isinstance(input_obj, list):
        return [x for x in input_obj if x[0] != '_']
    else:
        return [x for x in dir(input_obj) if x[0] != '_']
    
    
def tree(obj, depth=False):
    try:
        print(obj.__name__)
    except:
        print('{}'.format(obj))
    
    for method in dirtoni(obj):
        print('    {}'.format(method))
        for submethod in dirtoni(eval('obj.{}'.format(method))):
            print('        {}'.format(submethod))
            if depth:
                for subsubmethod in dirtoni(eval('obj.{}.{}'.format(method, submethod))):
                    print('            {}'.format(subsubmethod))