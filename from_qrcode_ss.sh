#!/bin/bash

for no in 1 2 3
do
qrcode=`zbarimg -q http://www.shadowsocks8.com/images/server0$no.png`
echo $qrcode
python ss2.py $qrcode 108$no &
done
