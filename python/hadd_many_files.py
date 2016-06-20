import numpy as np
import os
import sys

def macro(name, a, b):
    '''Runs hadd command, with output file name, composed of root files from 
    run a to run b. name input should end in .root and be enclosed in single 
    quotes.
    e.g. macro('test.root', 1, 3) is combines runs 1, 2 and 3 into test.root'''
    
    rtfiles = str_compose(a,b) # this is a string
    final = 'hadd ' + name + ' ' + rtfiles
    os.system('')
    return final

def str_compose(a, b):
    '''Returns a string of the run titles separated by a space, 
    from run a to run b.'''
    ary = np.arange(b+1)
    final = ''
    for i in ary[a:]:
        temp = 't1065-jun-2016-' + str(i) + '.dat-full.root '
        final += temp
    return final
    
