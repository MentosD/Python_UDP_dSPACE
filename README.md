# Python_UDP_dSPACE

几点说明：
1、 ip汇总
dSPACE host ip：192.168.140.7
PC ip：192.168.140.7

PC收 192.168.140.102:49104
dSPACE发 192.168.140.20:49001

PC发 192.168.140.102
dSPACE收 192.168.140.20 all

2、dSPACE与xPC不同，数据打包后的字节顺序与x86设备不同，double型数据可以用 "!d"，实现将字节顺序倒序，得到正确的结果。
