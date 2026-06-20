# Qrcode Generator - accept payment using qrcode
import qrcode
upi_id = input("Enter your upi id :")

# defining the payment url based on the upi id and the payment app

phonepe_url = f'upi://pay?pa={upi_id}&pn=Receipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Receipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Receipient%20Name&mc=1234'

# Create qrcode for each payment app

phonepe_qr = qrcode.make(phonepe_url)
google_pay_qr = qrcode.make(google_pay_url)
paytm_qr = qrcode.make(paytm_url)

# Save qrcode to image file

phonepe_qr.save('phonepe_qr.png')
google_pay_qr.save('google_pay_qr.png')
paytm_qr.save('paytm_qr.png')

# Display the qrcodes
phonepe_qr.show()
google_pay_qr.show()
paytm_qr.show()

