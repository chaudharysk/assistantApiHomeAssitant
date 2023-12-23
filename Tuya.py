from tuya_iot import TuyaOpenAPI
from requests import get
import credential

ACCESS_ID = 'gqfqg3m5gv59sj3fgt9e'
ACCESS_KEY = '9e78e2d922474a54bc46845f2d9d6a38'
#https://www.youtube.com/watch?v=w-BawMpxBYs&t=1039s
#https://www.youtube.com/watch?v=Jj2T4TuHRRo
#https://developer.tuya.com/en/docs/iot/api-request?id=Ka4a8uuo1j4t4
ENDPOINT = 'https://openapi.tuyain.com' # change this if you are not in India
USERNAME = credential.tuyaUsername
PASSWORD = credential.tuyaPassword

SMARTBULB_DEVICE_ID = 'd74f4045d5b104fd95qcmy'


tuyaOpenAPI = TuyaOpenAPI(ENDPOINT, ACCESS_ID, ACCESS_KEY)
tuyaOpenAPI.connect(USERNAME, PASSWORD,"86",'smartlife')

#command = {"commands":[{"code":"switch_led","value":True}]}
#result = tuyaOpenAPI.post(f"/v1.0/iot-03/devices/{SMARTBULB_DEVICE_ID}/commands", command)

# def switch_light(state):
#     command = {"commands":[{"code":"switch_led","value":state}]}
#     result = tuyaOpenAPI.post(f"/v1.0/iot-03/devices/{SMARTBULB_DEVICE_ID}/commands", command)
#     return result["result"]

def switch_light(value):
    command = {"commands":[{"code":"switch_led","value":value}]}
    result = tuyaOpenAPI.post(f"/v1.0/iot-03/devices/{SMARTBULB_DEVICE_ID}/commands", command)
    return result["result"]
def get_light_status():
    ans = tuyaOpenAPI.get(f"/v1.0/iot-03/devices/{SMARTBULB_DEVICE_ID}/status")
    on_or_off_status = ans["result"][0]["value"]
    brightness = ans["result"][2]["value"]
    temp = ans["result"][3]["value"]
    values = {
                "on_or_off_status":on_or_off_status,
                "brightness":brightness,
                "temp":temp
              }
    return values
def set_brightness(brightness):
    command = {"commands":[{"code":"bright_value_v2","value":brightness}]}
    result = tuyaOpenAPI.post(f"/v1.0/iot-03/devices/{SMARTBULB_DEVICE_ID}/commands", command)
    return result["result"]
def set_temperature(temp):
    command = {"commands":[{"code":"temp_value_v2","value":temp}]}
    result = tuyaOpenAPI.post(f"/v1.0/iot-03/devices/{SMARTBULB_DEVICE_ID}/commands", command)
    return result["result"]