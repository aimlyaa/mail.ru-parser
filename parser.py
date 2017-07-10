#ver. 1.0
from bs4 import BeautifulSoup
import urllib.request
import random
rand_=['/mail/love-23-06/', '/mail/irinaivanova.1968/', '/mail/cpimskaya/', '/mail/shabl-dabl/', '/mail/korovnikova_tatyana/', '/mail/lenus1000/', '/mail/zaa81/', '/mail/luneva_olia/', '/list/yulia.ya/', '/mail/irina_vas80/', '/mail/l.alla58/', '/mail/koltun79/', '/inbox/l.t.b86/', '/mail/natali1980-07-21/', '/mail/sokolowa29/', '/bk/str79/', '/mail/inulka3012/', '/mail/android19875/', '/mail/kazakova27.78/', '/mail/voronina_t/', '/list/telkem/', '/mail/colomoka/', '/mail/tarantyk/', '/mail/galinka.76/', '/list/marina.kononova.78/', '/mail/kiryuys/', '/mail/shtykalva/', '/list/telkem/', '/mail/aliska-1703/', '/mail/obleukhova77/', '/mail/jlka-d/', '/inbox/alexis-77/', '/mail/aleksei.ponkratov/', '/mail/aifil/', '/mail/lovkui_90/', '/mail/natawa1404/', '/inbox/sergeeva.57/', '/mail/snejana-77/', '/mail/long.62/', '/inbox/lizratoff/', '/mail/valentina.mitrasova.89/', '/mail/grom2685/', '/mail/panda82_05/', '/mail/anastasiya_kuzmina_1986/', '/mail/tatjur/', '/mail/dergunov1986/', '/list/belousovani/', '/mail/mariya-votinceva/', '/mail/128asd/', '/list/ymariha/', '/inbox/_katyuha_/', '/mail/kapustin-psk/', '/mail/yurka0903/', '/mail/argo-olga/', '/mail/tanya2010.71/', '/mail/verochka_kobzeva/', '/mail/lyudvig1958/', '/mail/profi2007-63/', '/mail/marinabatareva/', '/mail/zina76/', '/mail/violive/', '/mail/marif.76/', '/mail/vostrikoval/', '/inbox/olvich/', '/mail/inessadegai/', '/mail/pobeda4-19/', '/mail/gala_zimmerman/', '/list/iperminova/', '/mail/geoboss/', '/mail/tarlain/', '/mail/opavlova75/', '/mail/petryakov_egor/', '/mail/sergey-vlaso/', '/mail/polosina_irina/', '/mail/alexandr3.777/', '/bk/vgs/', '/mail/veta-75/', '/mail/serega73/', '/mail/li.bokotey/', '/mail/kasimov.54/', '/mail/guzel.arsk/', '/mail/shama1d/', '/mail/elenavolodina-1965/', '/mail/iren_mm/', '/mail/maksim_89rus_94/', '/mail/martyshka80/', '/mail/bvk1221/', '/mail/raduga_a/', '/mail/hena80/', '/mail/artushkin/', '/mail/voltol/', '/mail/greg_ishal/', '/bk/fridman67/', '/mail/dam71/', '/mail/rex-2/', '/mail/bma74/']
skip=[]
base=[]
dom='none'
login='none'
def main(base,skip):
        try:
                for b in base:
                        url = ('https://my.mail.ru{idk}'.format(idk=b))
                        del base[0:]
                        html = urllib.request.urlopen(url).read()
                        soup = BeautifulSoup(html, "html.parser")
                        href = soup.find_all('a',{'class':'b-right-column__block__friends__item booster-sc'})
                        for h in href:
                                h=h.attrs["href"]
                                base.append(h)
                        if h in skip:
                                print('!Защита от зацикливания успешно сработала...')
                                del base[0:]
                                base.append(random.choice(rand_))
                                print('skip: ',skip)
                                main(base,skip)
                        else:
                                for h in base:
                                        file = open('mail.txt' , 'a')   
                                        if ('/mail/') in h:
                                                login=h[6:len(h)-1]
                                                dom=h[1:5]
                                                result=('{log}@{domen}.ru'.format(domen=dom,log=login))
                                                file.write(result +'\n')
                                                print(result)
                                        elif ('/inbox/') in h:
                                                login=h[7:len(h)-1]
                                                dom=h[1:6]
                                                result=('{log}@{domen}.ru'.format(domen=dom,log=login))
                                                file.write(result +'\n')
                                                print(result)
                                        elif ('/list/') in h:
                                                login=h[6:len(h)-1]
                                                dom=h[1:5]
                                                result=('{log}@{domen}.ru'.format(domen=dom,log=login))
                                                file.write(result +'\n')
                                                print(result)
                                        elif ('/bk/') in h:
                                                login=h[4:len(h)-1]
                                                dom=h[1:3]
                                                result=('{log}@{domen}.ru'.format(domen=dom,log=login))
                                                file.write(result +'\n')
                                                print(result)
                        file.close()
                        skip.append(h)
                        del skip[0:(len(base)-1)]
                        main(base,skip)
        except:
                file.close()
                del base[0:]
                del skip[0:]
                base.append(random.choice(rand_))
                main(base,skip)
def start():
        print("""
        1 - Начать парсить с конкретного @mail.ru (при наличии у цели соц.сети "мой мир")
        2 - Начать парсить с рандомного @mail.ru.
        """)
        ans = str(input())
        if ans in ('1','2'):
                try:
                        ans=int(ans)
                        if ans == 1:
                                print('введите профиль "Мой Мир" (my.mail.ru) \n Пример: /mail/89255049405/')
                                profile=str(input())
                                try:
                                        base.append(profile)
                                        print('Начинаю парсить с профиля: ',profile)
                                        main(base,skip)
                                except:
                                        print('Невалидная ссылка на профиль, либо профиль скрыт')
                                        start()
                        elif ans == 2:
                                        print('Выбираю рандомный профиль...')
                                        base.append(random.choice(rand_))
                                        main(base,skip)
                                        print('Начинаю парсить с рандомного email: ',base)
                                        
                except:
                        print('Выберете вариант из списка.')
                        start()         
        else:
                print('Выберете вариант из списка.')
                start()
if __name__ == '__main__': 
        start()
