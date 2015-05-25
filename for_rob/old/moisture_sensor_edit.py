kory@kory:~/Documents/personal$ mkvirtualenv test
New python executable in test/bin/python
Installing setuptools, pip...done.
(test)kory@kory:~/Documents/personal$ pip install websocket-client
Downloading/unpacking websocket-client
  Downloading websocket_client-0.29.0.tar.gz (190kB): 190kB downloaded
  Running setup.py (path:/home/kory/.virtualenvs/test/build/websocket-client/setup.py) egg_info for package websocket-client
    
Downloading/unpacking six (from websocket-client)
  Downloading six-1.9.0-py2.py3-none-any.whl
Downloading/unpacking backports.ssl-match-hostname (from websocket-client)
  Downloading backports.ssl_match_hostname-3.4.0.2.tar.gz
  Running setup.py (path:/home/kory/.virtualenvs/test/build/backports.ssl-match-hostname/setup.py) egg_info for package backports.ssl-match-hostname
    
Installing collected packages: websocket-client, six, backports.ssl-match-hostname
  Running setup.py install for websocket-client
    changing mode of build/scripts-2.7/wsdump.py from 664 to 775
    
    changing mode of /home/kory/.virtualenvs/test/bin/wsdump.py to 775
  Running setup.py install for backports.ssl-match-hostname
    
Successfully installed websocket-client six backports.ssl-match-hostname
Cleaning up...
(test)kory@kory:~/Documents/personal$ 
(test)kory@kory:~/Documents/personal$ 
(test)kory@kory:~/Documents/personal$ ls

MoistureSensor.py


(test)kory@kory:~/Documents/personal$ python MoistureSensor.py 
trying to create websocket
websocket created
----------------------------------
name 'moisture_level' is not defined ("name 'moisture_level' is not defined",)
(test)kory@kory:~/Documents/personal$ 
(test)kory@kory:~/Documents/personal$ 
(test)kory@kory:~/Documents/personal$ python MoistureSensor.py 
trying to create websocket
websocket created
----------------------------------
name 'date_handler' is not defined ("name 'date_handler' is not defined",)
(test)kory@kory:~/Documents/personal$ 
(test)kory@kory:~/Documents/personal$ 
(test)kory@kory:~/Documents/personal$ python MoistureSensor.py 
trying to create websocket
websocket created
----------------------------------
----------------------------------
----------------------------------
^CTraceback (most recent call last):
  File "MoistureSensor.py", line 67, in <module>
    time.sleep(delay)
KeyboardInterrupt
(test)kory@kory:~/Documents/personal$ 
(test)kory@kory:~/Documents/personal$ 
(test)kory@kory:~/Documents/personal$ 
(test)kory@kory:~/Documents/personal$ python MoistureSensor.py 
trying to create websocket
websocket created
----------------------------------
(test)kory@kory:~/Documents/personal$ 
(test)kory@kory:~/Documents/personal$ 
(test)kory@kory:~/Documents/personal$ 
(test)kory@kory:~/Documents/personal$ python MoistureSensor.py 
trying to create websocket
websocket created
----------------------------------
Traceback (most recent call last):
  File "MoistureSensor.py", line 71, in <module>
    raise e
NameError: name 'moisture_level' is not defined
(test)kory@kory:~/Documents/personal$ 
(test)kory@kory:~/Documents/personal$ 
(test)kory@kory:~/Documents/personal$ 
(test)kory@kory:~/Documents/personal$ 
(test)kory@kory:~/Documents/personal$ python MoistureSensor.py 
trying to create websocket
websocket created
----------------------------------
name 'moisture_level' is not defined ("name 'moisture_level' is not defined",)
!!!!!!!!!!!!!!!!!!!!!!!!!!!
Traceback (most recent call last):
  File "MoistureSensor.py", line 72, in <module>
    raise e
NameError: name 'moisture_level' is not defined
(test)kory@kory:~/Documents/personal$ 

