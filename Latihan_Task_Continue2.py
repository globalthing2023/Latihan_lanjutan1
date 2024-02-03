print("TIKET BUS")
print(("-")*15)
print("Kode Kota:")
print("1.Prabumulih")
print("2.Muara Enim")
print("3.Lubuklinggau")


Kota = int (input("Which City Would you like to go to?(1/2/3): "))

print("Kode Kelas:")
print("1.Ekonomi")
print("2.Bisnis")
print("3.Eksekutif")

Kelas = int (input("What class are you going to go with?(1/2/3): "))
Ticket_Purchase = int (input("How many tickets are you going to buy?: "))
Code = input("Just askin, whats the code?: ")

Ticket_price = 0

if Kota == 1:
    if Kelas == 1:
        Ticket_price = 100000
    elif Kelas == 2:
        Ticket_price = 400000
    elif Kelas == 3:
        Ticket_price = 700000
elif Kota == 2:
    if Kelas == 1:
        Ticket_price = 200000
    elif Kelas == 2:
        Ticket_price = 500000
    elif Kelas == 3:
        Ticket_price = 800000
elif Kota == 3:
    if Kelas == 1:
        Ticket_price = 300000
    elif Kelas == 2:
        Ticket_price = 600000
    elif Kelas == 3:
        Ticket_price = 900000

Diskon = 0
Total_Ticket_Price = Ticket_Purchase * Ticket_price

if Code.lower() == "igs":
    Diskon = Total_Ticket_Price * 0.1
    Total_Ticket_Price -= Diskon

print("-"*15)
print(f"Harga Tiket : Rp {Ticket_price}")
print(f"Subtotal : Rp {Ticket_Purchase * Ticket_price}")
print(f"Diskon : Rp {Diskon}")
print(f"Total bayar : Rp {Total_Ticket_Price}")
