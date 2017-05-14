#!/bin/bash

qrcode=`zbarimg -q http://get.shadowsocks8.cc/images/server0$1.png`
echo $qrcode
python ss2.py $qrcode $2

