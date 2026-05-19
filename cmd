python3 -m venv venv    
.\venv\Scripts\Activate.ps1
pip install fastapi uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000
http://127.0.0.1:8000

```
PS C:\Users\91638> ipconfig

Windows IP Configuration


Ethernet adapter Ethernet 2:

   Connection-specific DNS Suffix  . :
   Link-local IPv6 Address . . . . . : fe80::825d:b471:dacd:d50d%13
   IPv4 Address. . . . . . . . . . . : 192.168.0.111
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 192.168.0.1
```