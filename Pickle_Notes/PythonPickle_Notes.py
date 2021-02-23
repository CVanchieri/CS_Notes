''' Python Pickle Notes '''
# pickle is used for serializing and de-serializing Python object structures, also called marshalling or flattening
# serialization refers to the process of converting an object in memory to a byte stream that can be stored on disk or sent over a network
# this character stream can then be retrieved and de-serialized back to a Python object
# conversion of an object from one representation (data in Random Access Memory (RAM)) to another (text on disk)
# pickling is not compression


''' when to use '''
# useful for applications where you need some degree of persistency in your data
# the program's state data can be saved to disk, so you can continue working on it later on
# can also be used to send data over a Transmission Control Protocol (TCP) or socket connection, or to store python objects in a database
# very useful for when you're working with machine learning algorithms, where you want to save them to be able to make new predictions at a later time, without having to rewrite everything or train the model all over again


''' when no to use '''
# if you want to use data across different programming languages, pickle is not recommended, protocol is specific to Python
# unpickling a file that was pickled in a different version of Python may not always work properly, so you have to make sure that you're using the same version and perform an update if necessary
# try not to unpickle data from an untrusted source, may contain malicious code 


''' what can be pickled '''
# booleans
# integers
# floats
# complex numbers
# normal & unicode strings
# tuples
# lists
# sets 
# dictionaries that contain picklable objects
# classes & functions if definded at the top of a module 
# generators, inner classes, lambda functions, defaultdicts can be pickled but need additional resources, ex lmabda functions need a package 'dill'


''' pickle vs json '''
# json is lightweight format for data-interchange, easily readable 
# json is standardized and not dependent on a language, advantage over pickle 
# json is more secure and faster than pickle
# if Python is the only language pickle is a good choice, can reconstruct complete Python objects 
# cPickle is pickle for C language, up to 1000x faster 
# small files wont notice speed difference 
# cPickle and Pickle can use the same files 


''' how to pickle a file '''
### import the library ### 
import pickle 
# pickling a simple dictionary 
dogs_dict = { 'Ozzy': 3, 'Filou': 8, 'Luna': 5, 'Skippy': 10, 'Barco': 12, 'Balou': 9, 'Laika': 16 } # dictionary 
# specify the name of file to write to
filename = 'dogs' # set the file name 
outfile = open(filename, 'wb') # use open() to write to file with file name, and 'wb', w = writing to file, b = binary mode writen in byte objects 
# pickle the file wanted 
pickle.dump(dogs_dict, outfile) # use dump() to add the data to be pickled with the outfile
# close the file once done, and you have a pickled file called dogs 
outfile.close()
### lambda function ### 
### import library ### 
import dill 
filename = 'dillfile'
dill.dump(lambda x: x**2, open(filename,'wb'))  # use dump () and open() to write to file with file name, and 'wb', w = writing to file, b = binary mode writen in byte objects 


''' how to un-pickle a file '''
filename - 'dogs' # set the file name to open
infile = open(filename,'rb') # use open() to write to file with file name, and 'rb', r = read mode, b = binary mode writen in byte objects
new_dict = pickle.load(infile) # load the pickled infile to a new dict
infile.close() # once loaded close the file


''' compressing pickle files '''
# used for large data sets that take up lots of space 
# can use bzip2 or gzip, bzip2 is slower, gzip prodces 2x as large files to bzip2
### import the libraries ### 
import bz2 
import pickle 
# specify the name of file to write to
filename = 'dogs' # set the file name 
sfile = bz2.BZ2File(filename, 'w') # use BZ2File to compress, name of file, w = writing to file 
# pickle the compressed file wanted 
pickle.dump(dogs_dict, sfile) # use dump() to add the data to be pickled with the outfile
# close the file once done, and you have a compressed pickled file called dogs 
sfile.close()


''' unpickling Python2 objects in Python 3 '''
# not easy 
# unpickle with Python 2 or use Python 3 with encoding='latin1' in the load() function
infile = open(filename,'rb') # use open() to write to file with file name, and 'rb', r = read mode, b = binary mode writen in byte objects
new_dict = pickle.load(infile, encoding='latin1') # load the pickled infile to a new dict with endocing param
# will not work if objects contain Numpy arrays
# might work by using encoding='bytes' in the load() function
infile = open(filename,'rb') # use open() to write to file with file name, and 'rb', r = read mode, b = binary mode writen in byte objects
new_dict = pickle.load(infile, encoding='bytes') # load the pickled infile to a new dict with endocing param


''' pickle and multiprocessing '''
 # with complex computations, it is common to distribute this task over several processes, multiprocesssing 
 # multiprocessing means that several processes are executed simultaneously, usually over several Central Processing Units (CPUs) or CPU cores, thus saving time
 # example is the training of machine learning models or neural networks, which are intensive and time-consuming processes, distributing these on a large amount of processing units, a lot of time can be saved
 # when a task is divided over several processes, these might need to share data, processes do not share memory space, so when they have to send information to each other, they use serialization, which is done using the pickle module


 ''' set up multiproccesing with pickle '''
### import libraries ### 
import multiprocessing as mp
from math import cos
# set up pool abstraction 
p = mp.Pool(2) # set the number of processors to use, handles in background 
# map cos function on a range of 10 to the pool 
p.map(cos, range(10))

### import library ### 
import pathos.multiprocessing as mp
# set up pool abstraction 
p = mp.Pool(2) # set the number of processors to use, handles in background 
# map lambda function on a range of 10 to the pool 
p.map(lambda x: 2**x, range(10))
