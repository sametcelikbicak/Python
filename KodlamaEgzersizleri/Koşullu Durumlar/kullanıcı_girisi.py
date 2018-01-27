print("""********************
Kullanıcı Girişi
********************
""")

sys_kullanıcı_adı = "samet"
sys_parola = "12345"

kullanıcı_adı = input("Kullanıcı Adı:")
parola = input("Parola:")

if (kullanıcı_adı == sys_kullanıcı_adı and  parola != sys_parola):
    print("Parola hatalı")
elif (kullanıcı_adı != sys_kullanıcı_adı and parola == sys_parola):
    print("Kullanıcı adı hatalı")
elif (kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parola):
    print("Kullanıcı adı ve parola hatalı")
else:
    print("Sisteme başarılı olarak giriş yapıldı.")