#CORE PYTHON IMPORTS
import logging, sys, time, urllib, base64, urllib2
#import simplejson as json
import json
from xml.dom.minidom import parseString
#SRC IMPORTS
import webservice
import faxman_config

from pkcs7 import PKCS7Encoder
#DEPENDENCY IMPORTS -- PyCrypto (https://www.dlitz.net/software/pycrypto/ OR <a href="http://pypi.python.org/pypi/pycrypto/2.5">http://pypi.python.org/pypi/pycrypto/2.5</a>)
from Crypto.Cipher import AES



faxman_config.sfax_user
faxman_config.sfax_init_vector
faxman_config.sfax_api_key
faxman_config.sfax_encryption_key
faxman_config.sfax_number

URL2 = "https://api.sfaxme.com"
DOWNLOAD_DIR = "/tmp/"

def getToken():#Generating token
    print ("sfaxWS.py -> getToken")
    try:
        timestr = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        raw = "Username="+faxman_config.sfax_user+"&ApiKey="+faxman_config.sfax_api_key+"&GenDT="+timestr+"&"
        mode = AES.MODE_CBC
        encoder = PKCS7Encoder()
        encryptor = AES.new(faxman_config.sfax_encryption_key, mode, faxman_config.sfax_init_vector.encode("ascii"))
        pad_text = encoder.encode(raw)
        cipher = encryptor.encrypt(pad_text)
        enc_cipher = base64.b64encode(cipher)
        return urllib.quote_plus(enc_cipher)
    except:
       print ("Error getting token " + str(sys.exc_info()[0]) + " " + str(sys.exc_info()[1]))
    return 
"""
    RETURN THE SENDFAXQUEUEID  OF THE OUTGOING FAX, OTHERWISE RETURN NONE IF FAILED TO SEND
"""
def sendFax(fax):
    print ("sfaxWS.py -> sendFax")
    tid = None
    XwsSuccess = "true"
    try:  
            path = "/api/sendfax?token="+getToken()+"&ApiKey="+faxman_config.sfax_api_key+"&RecipientName=Gene&RecipientFax="+ str(fax)+"&OptionalParams=&"
            response = webservice.post(URL2, path, DOWNLOAD_DIR +"test.pdf")
            if XwsSuccess == "true":
                print ("Fax successfully submitted to sfax for delivery to " + str(fax))
                result = json.load(urllib2.urlopen(response))
                tid = result['SendFaxQueueId']
                print tid
            else:
                err = "Error submitting fax for send to " + str(fax)
                err += " ResultCode=" + str(response.getheader("XwsFaxResultCode")) + " ResultInfo=" + str(response.getheader("XwsResultInfo"))
                err += " ErrorCode=" + str(response.getheader("XwsFaxErrorCode")) + " ErrorInfo=" + str(response.getheader("XwsErrorInfo"))
                print (err)
    except:
        print ("Error transmitting data to sfax " + str(sys.exc_info()[0]) + " " + str(sys.exc_info()[1]))
    return tid
    
#sendFax("18889744258")
sendFax("18772418203")