from os import system, name  
from urllib.request import urlopen
from json import loads
from time import sleep
from art import *
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def get_page(lokasi):
    print(lokasi)
    param_1=0
    param_2=1
    base_url = ("https://pse.kominfo.go.id/static/json-static/{}/{}.json?page[page]={}&page[limit]=10&filter[search_term]=".format(lokasi,param_1,param_2))
    with urlopen(base_url) as url:
        data = loads(url.read().decode())
    print("_________________________________________________")
    print("|Stats:|")
    print("|Total page: {}|".format(data['meta']['page']['lastPage']))
    print("|Total data: {}|".format(data['meta']['page']['total']))
    print("|Estimated time: {} Seconds / {} Minutes|".format(data['meta']['page']['total'] *2, data['meta']['page']['total'] *2/60))
    print("_________________________________________________")
    print("Note: This is just an estimation, the actual time may vary depending on your internet connection and the reason why it may be slow is to avoid the server from being overloaded.")

    return data

def main():
    clear()
    Title=text2art("DB PSE",font='block',chr_ignore=True) # Return ASCII text with block font
    print(Title)
    print("Download PSE lokal atau asing")
    print("Input? (lokal/asing/exit)")
    choice = input()
    if choice == "lokal":
        clear()
        print("anda pilih lokal")
        data = get_page("LOKAL_TERDAFTAR")
        print("\n")
        print("Continue? (y/n)")
        choice = input()
        if choice == "y":
            print("accesing site...")
            something = []
            total_page = data['meta']['page']['lastPage']
            for i in range(total_page):
                param_1 = i
                param_2 = i+1
                base_url = ("https://pse.kominfo.go.id/static/json-static/LOKAL_TERDAFTAR/{}.json?page[page]={}&page[limit]=10&filter[search_term]=".format(param_1,param_2))
                with urlopen(base_url) as url:
                    data = loads(url.read().decode())
                    total_data_in_page = len(data['data'])
                    for i in range(total_data_in_page):
                        print(data['data'][i]['attributes']['nama'])
                        sleep(1)
                        something.append({'nama': data['data'][i]['attributes']['nama'], 'website': data['data'][i]['attributes']['website'], 'nama_perusahaan': data['data'][i]['attributes']['nama_perusahaan']})
                        import csv
                        with open('lokal_data.csv', 'w', encoding="utf-8") as csvfile:
                            fieldnames = ['nama','website','nama_perusahaan']
                            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                            writer.writeheader()
                            writer.writerows(something)
        elif choice == "n":
            print("back to main menu...")
            main()
    elif choice == "asing":
        clear()
        print("anda pilih asing")
        data = get_page("ASING_TERDAFTAR")
        print("\n")
        print("Continue? (y/n)")
        choice = input()
        if choice == "y":

            print("accesing site...")
            something = []
            total_page = data['meta']['page']['lastPage']
            for i in range(total_page):
                param_1 = i
                param_2 = i+1
                base_url = ("https://pse.kominfo.go.id/static/json-static/ASING_TERDAFTAR/{}.json?page[page]={}&page[limit]=10&filter[search_term]=".format(param_1,param_2))
                with urlopen(base_url) as url:
                    data = loads(url.read().decode())
                    total_data_in_page = len(data['data'])
                    for i in range(total_data_in_page):
                        print(data['data'][i]['attributes']['nama'])
                        sleep(1)
                        something.append({'nama': data['data'][i]['attributes']['nama'], 'website': data['data'][i]['attributes']['website'], 'nama_perusahaan': data['data'][i]['attributes']['nama_perusahaan']})
                        import csv
                        with open('asing_data.csv', 'w', encoding="utf-8") as csvfile:
                            fieldnames = ['nama','website','nama_perusahaan']
                            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                            writer.writeheader()
                            writer.writerows(something)
        elif choice == "n":
            print("back to main menu...")
            main()
    elif choice == "exit":
        clear()
        print("exiting...")
    else:
        print("salah input retry again")
main()