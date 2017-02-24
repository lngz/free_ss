#!/bin/bash

qrcode=`zbarimg -q https://www.shadowsocks8.biz/images/server0$1.png`
echo $qrcode
python ss2.py $qrcode $2

