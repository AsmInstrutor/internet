import os
import speedtest

testing.internet = speedtest.speedtest()

download = download()
rsDown_test = round(download)
fDown_test = int(rsDown_test / 1e+6 )

upload = test.upload()
rsUp_test = round(upload)
fUp_test = int(rsUp_test / 1e+6 )

print(f" Speed of Download is: {fDown_test}/ms")
print(f" Speed of Upload is: {fUp_load}/ms")

