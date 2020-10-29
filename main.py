import os

print("+---------------------------------------------------+")
print("|\t\t\tSelamat Datang di Sistem Pakar\t\t\t|")
print("|\tDeteksi Emotional Quotient Pada Karyawan\t\t|")
print("+---------------------------------------------------+")
nama = input("Nama\t: ")
pilihan = input("Hallo "+nama+",\nApakah anda ingin melakukan diagnosa? (y/n)")

os.system("clear")

while pilihan == "y" :
  print("\nApakah Anda Menyadari ketika anda kehilangan kontrol? ")
  kd01  = input("Jawab (y/n) : ")

  if kd01 == "y" :
    print("\nApakah Anda mengakui adanya kelemahan dan kekuatan pada diri anda?")
    kd02  = input("Jawab (y/n) : ")

    if kd02 == "y" :
      print("\nApakah Anda meragukan kemampuan diri sendiri?")
      kd03 = input("Jawab (y/n) : ")

      if kd03 == "y" :
        print("\nHai "+nama+", hasil diagnosa awal : Anda memiliki tingkat kesadaran yang tinggi." )
        print("\nSaran : Pertahankan kesadaran yang anda miliki")

      elif kd03 == "n" :
        print("\nApakah Anda tidak mempunyai tujuan yang menantang?")
        kd04 = input("Jawab (y/n) : ")

        if kd04 == "y" :
          print("\nApakah anda membiarkan rintangan yang mengganggu tujuan anda?")
          kd05 = input("Jawab (y/n) : ")

          if kd05 == "y" :
            print("\nHai "+nama+", hasil diagnosa awal : Anda memiliki Tingkat Kesadaran diri yang rendah." )
            print("\nSaran : Mulailah memahami emosi yang sedang dirasakan, kritis terhadap informasi mengenai diri anda sendiri dan menyadari tentang diri anda yang nyata")

          elif kd05 == "n" :
            print("\nApakah anda belajar dari kemunduran?")
            pd01 = input("Jawab (y/n) : ")

            if pd01 == "y" :
              print("Apakah Anda mematuhi nilai-nilai yang ada pada diri sendiri bahkan ketika ada cobaan/tantangan?")
              pd02 = input("Jawab (y/n) : ")

              if pd02 == "y" :
                print("Apakah Anda tetap bersifat positif dalam situasi apapun?")
                pd03 = input("Jawab (y/n) : ")

                if pd03 == "y" :
                  print("\nHai "+nama+", hasil diagnosa awal : Anda memiliki Tingkat Pengaturan diri yang Tinggi." )
                  print("\nSaran : Pertahankan sifat pengaturan diri anda yang sudah baik") 

                if pd03 == "n" :
                  print("Apakah Anda selalu membuat pekerjaan itu menjadi beban atau stress?")
                  pd04 = input("Jawab (y/n) : ")

                  if pd04 == "y" :
                    print("Apakah anda mengetahui resiko dalam mengerjakan sebuah pekerjaan?")
                    pd05 = input("Jawab (y/n) : ")

                    if pd05 == "y" :
                      print("\nHai "+nama+", hasil diagnosa awal : Anda memiliki Tingkat Pengaturan diri yang rendah." )
                      print("\nSaran : Mulailah menangani emosi anda sehingga berdampak positif kepada pelaksanaan tugas")

                    elif pd05 == "n" :
                      print("Apakah anda  yakin bahwa hari esok akan lebih baik dari hari kemarin?")
                      md01 = input("Jawab (y/n) : ")

                      if md01 == "y" :
                        print("Apakah anda  Anda berinisiatif mengambil tindakan untuk menciptakan berbagai kemungkinan?")
                      md02 = input("Jawab (y/n) : ")

                      if md02 == "y" :
                        print("Apakah anda  percaya diri mampu untuk melakukan suatu pekerjaan ?")
                      md03 = input("Jawab (y/n) : ")

                      if md03 == "y" :
                        print("\nHai "+nama+", hasil diagnosa awal : Anda memiliki Tingkat motivasi yang tinggi." )
                        
                        print("\nSaran : Pertahankan sifat motivasi yang anda miliki untuk memotivasi diri sendiri dan orang- orang di sekitar anda")

                      elif md03 == "n" :
                        print("Apakah jika di dalam suatu kelompok, Anda bersikap pasif ?")
                        md04 = input("Jawab (y/n) : ")

                      if md04 == "y" :
                        print("Apakah anda tidak mempunyai harapan yang besar ?")
                        md05 = input("Jawab (y/n) : ")

                        if md05 == "y" :
                          print("\nHai "+nama+", hasil diagnosa awal : Anda memiliki Tingkat motivasi yang rendah." )
                          print("\nSaran : Mulailah memotivasi anda sendiri dan sering mendengarkan ceramah atau seminar yang diadakan para motivator sehingga sedikit demi sedikit anda akan termotivasi")
                        
                        elif md05 == "n" :
                          print("Apakah anda mempunyai perhatian tentang tingkah laku ?")
                          ep01 = input("Jawab (y/n) : ")

                          if ep01 == "y" :
                            print("Apakah anda melibatkan diri menjadi pendengar yang baik ?")
                            ep02 = input("Jawab (y/n) : ")

                            if ep02 == "y" :
                              print("Apakah anda berhubungan baik dengan orang lain yang memiliki latar belakang yang berbeda?")
                              ep03 = input("Jawab (y/n) : ")

                              if ep03 == "y" :
                                print("\nHai "+nama+", hasil diagnosa awal : Anda memiliki Tingkat empati yang tinggi." )
                                print("\nSaran : Pertahankan sifat empati yang anda miliki demi menjalin  hubungan baik terhadap orang lain")

                              elif ep03 == "n" :
                                print("Apakah Anda tidak mengenali kemampuan khusus orang lain?")
                                ep04 = input("Jawab (y/n) : ")

                                if ep04 == "y" :
                                  print("Apakah anda selalu menghindar diri dari orang lain?")
                                  ep05 = input("Jawab (y/n) : ")

                                  if ep05 == "y" :
                                    print("\nHai "+nama+", hasil diagnosa awal : Anda memiliki Tingkat empati yang rendah." )
                                    print("\nSaran : Mulailah berinteraksi dengan orangorang di sekitar anda untuk menjalin baik hubungan terhadap orang lain")

                                  elif ep05 == "n" :
                                    print("Apakah anda memberi umpan balik yang bersifat membangun?")
                                    ks01 = input("Jawab (y/n) : ")

                                    if ks01  == "y" :
                                      print("Apakah anda mengajak orang lain untuk peran serta?")
                                      ks02 = input("Jawab (y/n) : ")

                                      if ks02 == "y" :
                                        print("Apakah anda memahami struktur informal dalam organisasi?")
                                        ks03 = input("Jawab (y/n) : ")

                                        if ks03 == "y" :
                                          print("\nHai "+nama+", hasil diagnosa awal : Anda memiliki Tingkat keterampilan sosial yang tinggi." )
                                          print("\nSaran : Pertahankan sifat keterampilan sosial anda yang sudah baik")

                                        elif ks03 == "n" :
                                          print("Apakah anda tidak memahami aturan yang tak tertulis di dalam organisasi?")
                                          ks04 = input("Jawab (y/n) : ")

                                          if ks04 == "y" :
                                            print("Apakah anda tidak suka bekerja sama dengan orang lain ?")
                                            ks05 = input("Jawab (y/n) : ")

                                            if ks05 == "y" :
                                              print("\nHai "+nama+", hasil diagnosa awal : Anda memiliki Tingkat keterampilan sosial yang rendah." )
                                              print("\nSaran : Mulailah aktif dalam suatu diskusi dan saling bertukar pendapat sehingga mendapatkan hasil yang memuaskan")


  pilihan = input("\nHallo "+nama+",\nApakah anda ingin melakukan diagnosa? (y/n)")

  if pilihan == "y" :
    os.system("clear")
    print("+---------------------------------------------------+")
    print("|\t\t\tSelamat Datang di Sistem Pakar\t\t\t|")
    print("|\tDeteksi Emotional Quotient Pada Karyawan\t\t|")
    print("+---------------------------------------------------+")  

  else : 
    print("+---------Terima kasih ---------------+")







                                          









