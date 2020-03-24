from handler import Handle
import json
import logging

'''
        PROTOCOL FORMAT

string terbagi menjadi 2 bagian yang dipisahkan oleh spasi
Format : command *spasi* parameter *spasi* parameter

        FITUR

a. Meletakkan File 
   Berguna untuk menambahkan file ke dalam folder stock
   Request : addingfile
   Parameter : namafile *spasi* isi dari file
   Response : berhasil -> "File Berhasil Ditambahkan"
              gagal -> "ERROR"

b. Mengambil File
   Berguna untuk mengambil file berdasarkan nama file yang ada pada folder stock
   Request : gettingfile
   Parameter : [namafile yang ingin diambil]
   Response: file terdownload pada diretori utama

c. Melihat List File
   Berguna untuk melihat list file yang ada di dalam folder stock
   Request : listingfile
   Parameter: -
   Response: list file yang ada di dalam folder stock

d. Jika command tidak dikenali akan merespon dengan ERRCMD

'''
p = Handle()

class Machine:
    def proses(self,string_to_process):
        s = string_to_process
        cstring = s.split(" ")
        try:
            command = cstring[0].strip()
            if (command=='addingfile'):
                print("addfile")
                filename = cstring[1].strip()
                file = cstring[2].strip()
                print("Adding",filename)
                p.addfile(filename,file.encode())
                return "File Berhasil Ditambahkan"

            elif (command=='gettingfile'):
                print("getfile")
                filename = cstring[1].strip()
                print("Retrieving", filename)
                hasil = p.getfile(filename)
                return hasil

            elif (command=='listingfile'):
                logging.info("listfile")
                data = {}
                data['files'] = []
                hasil = p.listfile()
                for filename in hasil:
                    data['files'].append({"filename":filename})
                return json.dumps(data, indent=4)
            else:
                return "ERRCMD"
        except:
            return "ERROR"


if __name__=='__main__':
    machine = Machine()
