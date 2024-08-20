def domba(asal,seberang):
    print(f"Daerah Asal : {asal}")
    if len(seberang) > 0:
        print(f"Seberang Sungai : {seberang}")
    perahu = input("\nNaikkan 1 hewan ke perahu : ")
    print(f"Perahu : {[perahu]}")
    print("Perahu menuju ke seberang sungai...")
    asal.remove(perahu)
    print()
    seberang.add(perahu)
    print(f"Seberang Sungai : {seberang}")
    bawa = input("Adakah hewan yang ingin dibawa kembali? (y untuk membawa kembali) : ")
    if bawa == "y":
        perahu = input("Naikkan 1 hewan yang ingin dibawa kembali ke perahu : ")
        seberang.remove(perahu)
        if ("Serigala" in asal and len(asal) == 2) or ("Serigala" in seberang and len(seberang) == 2):
            print("Yahh... Domba kamu dimakan Serigala :(")
        else:
            asal.add(perahu)
            domba(asal,seberang)
    print("\nKembali ke daerah asal...\n")
    if len(seberang) == 3:
        print("Selamat... Kamu Berhasil")
    else:
        if ("Serigala" in asal and len(asal) == 2) or ("Serigala" in seberang and len(seberang) == 2):
            print("Yahh... Domba kamu dimakan Serigala :(")
        else:
            domba(asal,seberang)

asal = {"Serigala", "Domba 2", "Domba 1"}
seberang = set()
domba(asal,seberang)
