import subprocess
# NOT:  SSID key : ad
#Password key : sifre
def wifi(b):
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'interface'])
    results = results.decode('utf-8', errors="backslashreplace")
    results = results.split('\n')
    SSID = [b.split(":")[1][1:-1] for b in results if "SSID" in b]

    if SSID:
        try:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', SSID[0], 'key=clear'])

            results = results.decode('utf-8', errors="backslashreplace")
            results = results.split('\n')

            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]

            try:
                ad = SSID[0]
                sifre = results[0]
                if b == 'ad':
                    return ad
                elif b=='sifre':
                    return sifre

            except IndexError:

                return "{}\n".format(SSID[0])


        except subprocess.CalledProcessError:
           
            return "Encoding Error Occured"
    else:
        
        return "Wi-Fi is not connected."

print(wifi('ad')) #ssid
print(wifi('sifre')) #password
        
