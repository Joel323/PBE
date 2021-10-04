import usb.core


dev=usb.core.find(idVendor=0x13ee, idProduct=0x0003)
ep=dev[0].interfaces()[0].endpoints()[0]
i=dev[0].interfaces()[0].bInterfaceNumber
dev.reset()

if dev.is_kernel_driver_active(i):
	dev.detach_kernel_driver(i)

dev.set_configuration()
eaddr=ep.bEndpointAddress


data = [0]*1024
r=dev.read(eaddr, data)

