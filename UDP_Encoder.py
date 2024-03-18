from encoderSensor import encoderValue
from ultrasonicSensor import distanceValueinCM
import socket
from time import sleep
import RPi.GPIO as GPIO
import json


encoderPIN = 23
echo_PIN = 17
trig_PIN = 27

#soketten alınabilecek max veri miktarı (1024 bayt = 1 kilobayt)
bufferSize = 1024

# Raspberry Pi IP address and port no
ServerPort = 2222
ServerIP = "192.168.137.160"
#ServerIP = "10.42.0.1"
#ServerIP = "10.100.166.96"

 
#ilk argüman adres ailesini belirtir.
# iletisim kurulmasi icin birbirlerini tamamlayan ve bir hedefe ulasmak icin nasil iletisim kurulacagini belirleyen adreslere ihtiyac vardir.
# bir nevi standartlastirma icin.
# AF_INET: IPv4 adresleme sistemi, internet uzerinden iletisim icin
# AF_INET6: IPv6 adresleme sistemi, IPv4'un adres sinirlarini asmak ve daha fazla IP adresi saglamak
# AF_UNIX: Unit Domain Socket, unix tabanli isletim sistemleri icin
# AF_PACKET: Raw socketler, agdaki fiziksel ag donanimina dogrudan erismek icin, ag trafigini izlemek icin kullanilabilir.
#ikinci argüman soket turlerini belirtir.
#SOCK_DGRAM: Datagram soketleri, guvenilir olmayan, hizli bir iletisim saglar. UDP (User Datagram Protocol) tarafindan desteklenir.
#SOCK_STREAM: Stream soketleri, guvenilir, baglanti odakli iletisim saglar. TCP (Transmission Control Protocol) tarafindan desteklenir.
#SOCK_RAW: Raw soketler, agdaki veri paketlerine dogrudan erisim saglar. 
#SOCK_SEQPACKET: guvenilir, baglanti odakli iletisim saglar; ancak veriyi paketler halinde degil de bir dizi mantiksal paket olarak iletir.
RPIServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# listening the connection. bind(), soketin belirli bir IP adresi ve port numarasina baglanmasini ve dinlemesini saglar.
RPIServer.bind((ServerIP,ServerPort))
print("Server is up and listening..")

while True:
    # client socketinden gelen cmd(clienttan gelen data) ve client'in address+port bilgilerini alir
    cmd,address = RPIServer.recvfrom(bufferSize)
    #byte dizisi olarak gelen veriyi Unicode karakter dizisi formatina donusturur.
    #utf-8 kodlama bicimi, genellikle metin tabanli verilerin iletiminde kullanilir.
    cmd = cmd.decode("utf-8")
    print(cmd)
    print("Client Address", address[0])
    if cmd=="GO":
        encoder_result = encoderValue(encoderPIN)
        distance_result = 40
        myData = {
            "encoder": encoder_result,
            "ultrasonic": distance_result
        }
        json_data = json.dumps(myData)
        json_encoded = json_data.encode("utf-8")
        RPIServer.sendto(json_encoded, address)
        '''
        data = str(encoder_result)
        data = data.encode("utf-8")
        #sensor verisini utf-8 formatina donusturerek belirtilen adrese (client adresine) gonderir.
        RPIServer.sendto(data,address)
        '''
    if cmd!="GO":
        data = "Invalid Request"
        data = data.encode("utf-8")
        RPIServer.sendto(data,address)
