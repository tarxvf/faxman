import httplib
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib2
#def post(URL, path ):
def post(URL, path, file_to_upload ):
    # Register the streaming http handlers with urllib2
    register_openers()
# Start the multipart/form-data encoding of the file "DSC0001.jpg"
# "image1" is the name of the parameter, which is normally set
# via the "name" parameter of the HTML <input> tag.
# headers contains the necessary Content-Type and Content-Length
# datagen is a generator object that yields the encoded parameters
    datagen, headers = multipart_encode({"file.pdf": open(file_to_upload, "rb")})
# Create the Request object
    response = urllib2.Request(URL + path, datagen, headers)
# Actually do the request, and get the response
    print urllib2.urlopen(response).read()
    #print urllib2.urlopen(response).info().items()
    return response
    
def get(URL, path):
    register_openers()  
    response = urllib2.Request(URL + path)
    print urllib2.urlopen(response).read()
    return response