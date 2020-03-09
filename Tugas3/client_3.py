import logging
import requests
import os
import threading



def download_gambar(url=None, nama=None):
    if (url is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/jpeg']='jpg'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = 'Foto/'+nama
        ekstensi = tipe[content_type]
        logging.warning(f"writing {nama}.{ekstensi}")
        fp = open(f"{namafile}.{ekstensi}","wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False




if __name__=='__main__':
    threads = []
    listgambar = []
    listgambar.append("https://asset.kompas.com/crops/qz_jJxyaZgGgboomdCEXsfbSpec=/0x0:998x665/740x500/data/photo/2020/03/01/5e5b52f4db896.jpg")
    listgambar.append("https://asset.kompas.com/crops/sJBbKnpFpTQ037sk4_2VyXOmJ8k=/0x0:1000x667/750x500/data/photo/2020/01/29/5e3120ac8d974.jpg")
    listgambar.append("https://asset.kompas.com/crop/45x7:1374x893/750x500/data/photo/2019/09/12/5d7a0d690be15.png")
    for i in range(3):
        t = threading.Thread(target=download_gambar(listgambar[i], 'Capture %s' % i), args=())
        threads.append(t)

    for thread in threads:
        thread.start()