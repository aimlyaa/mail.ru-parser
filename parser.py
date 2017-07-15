#ver. 1.1

from bs4 import BeautifulSoup
import urllib.request
import random
import multiprocessing
import subprocess

rand_ = ['/mail/kapustin-psk/', '/mail/29vit1969/', '/mail/artstudio45/', '/mail/franzolik/', '/mail/301558/', '/mail/nika1214/', '/mail/elvira-enukova/', '/mail/romanaristokrat/', '/mail/kuznecova69/', '/mail/aleks47-47/', '/mail/elena210/', '/mail/gubina1956/', '/mail/mmedoctor/', '/mail/shatunovak/', '/mail/lara24/', '/mail/jim55/', '/mail/krekker/', '/mail/alferovne/', '/mail/raisa.ostrovskaya.60/', '/mail/penelopa53/', '/bk/alexargo/', '/mail/dododo55/', '/mail/romanaristokrat/', '/mail/tujh2808/', '/mail/semeisheva_t/', '/mail/asei45/', '/mail/alferovne/', '/mail/albina_fin/', '/mail/argo-psk/', '/bk/alexargo/', '/list/petrd10/', '/mail/yagovenko/', '/mail/lidia_58_58/', '/mail/elvira-enukova/', '/mail/tkom55/', '/mail/elenaserova1966/', '/mail/tarasova__72/', '/mail/elenabug/', '/mail/elvira-enukova/', '/mail/argo2010/', '/mail/337553/', '/mail/788alberto/', '/mail/ivolga-s/', '/mail/natali-manit/', '/list/dan3/', '/mail/via.55/', '/mail/argo_vlz/', '/mail/tujh2808/', '/mail/info-vektorpro/', '/mail/sila_la/', '/mail/nata_gosteva/', '/mail/natali-manit/', '/mail/artstudio45/', '/inbox/espirov/', '/mail/kareva14/', '/mail/argo-mig/', '/bk/fitoline/', '/mail/ag999.99/', '/mail/olga_osipova1975/', '/mail/dahsulja90-90/', '/mail/nika1214/', '/mail/ekshv/', '/mail/788alberto/', '/mail/artstudio45/', '/mail/nurlan-argo/', '/mail/dahsulja90-90/', '/mail/v282ml/', '/mail/levchenko-lyudmi/', '/mail/semeisheva_t/', '/mail/albina_fin/', '/mail/sibvaleo.rus/', '/list/petrd10/', '/mail/sibvaleo.rus/', '/mail/alferovne/', '/mail/buzdalova/', '/mail/ivolga-s/', '/mail/kareva14/', '/mail/yuyuka08/', '/mail/gubina1956/', '/mail/lidia_58_58/', '/mail/eko-shu/', '/mail/lena19702/', '/mail/mr_solnce/', '/mail/svet_barnaul/', '/mail/emtehzagoruiko/', '/mail/sibvaleo.rus/', '/mail/uirwik/', '/mail/wachtanna/', '/mail/ostrovsvtt/', '/mail/argo-psk/', '/mail/29vit1969/', '/mail/igor.koltovich/', '/mail/raz6/', '/mail/nika1214/', '/mail/6503210/', '/bk/fitoline/', '/mail/buzdalova/', '/mail/mr_alex1977/', '/mail/sedelnikova_l/', '/mail/aleks47-47/', '/mail/emtehzagoruiko/', '/mail/kareva14/', '/mail/argomila/', '/mail/orlovskaya-68/', '/mail/argo-olga/', '/mail/788alberto/', '/mail/svet_barnaul/', '/list/ymariha/', '/list/irin180680/', '/mail/argonek/', '/mail/emina2107/', '/mail/nicbah/', '/mail/doctor-ad/', '/mail/raisa.ostrovskaya.60/', '/mail/6503210/', '/mail/lara24/', '/list/dan3/', '/mail/elenaserova1966/', '/mail/irina_shumska/', '/mail/tatyana-volkova-63/', '/mail/argonek/', '/mail/solodov-ataman/', '/mail/via.55/', '/bk/sokolnik/', '/mail/jim55/', '/mail/nataliandr5/', '/mail/tujh2808/', '/mail/irina_tatevosyan/', '/mail/argo_vlz/', '/mail/sedelnikova_l/', '/mail/lara24/', '/mail/6503210/', '/mail/magikdia/', '/mail/argo-olga/', '/mail/igor.koltovich/', '/mail/zibatoma/', '/mail/tkom55/', '/mail/kozlovcevis/', '/mail/sibvaleo.rus/', '/mail/mr_solnce/', '/mail/albina_fin/', '/mail/solodov-ataman/', '/mail/koksaanna/', '/mail/amangeldi.kz/', '/mail/uirwik/', '/mail/ostrovsvtt/', '/mail/satina.natalya.59/', '/mail/r.p.o._argo/', '/mail/emina2107/', '/mail/yagovenko/', '/mail/tatasav-777/', '/mail/aleks47-47/', '/mail/koksaanna/', '/mail/emtehzagoruiko/', '/mail/emina2107/', '/mail/r.p.o._argo/', '/mail/sila_la/', '/mail/wachtanna/', '/mail/via.55/', '/mail/6503210/', '/bk/alexargo/', '/mail/elenabug/', '/mail/kozlovcevis/', '/mail/301558/', '/mail/kovaleva1961no/', '/mail/argomila/', '/mail/koksaanna/', '/mail/svet_barnaul/', '/mail/argonek/', '/mail/301558/', '/mail/olga_osipova1975/', '/list/alla_omsk/', '/mail/argo-psk/', '/mail/figura-84/', '/mail/info-vektorpro/', '/mail/stepchick.89/', '/mail/lara24/', '/mail/gll-58/', '/mail/nicbah/', '/mail/artstudio45/', '/mail/wachtanna/', '/mail/alferovane/', '/mail/29vit1969/', '/mail/jim55/', '/mail/mr_argo/', '/mail/elenaserova1966/', '/mail/gubina1956/', '/mail/r.p.o._argo/', '/mail/levchenko-lyudmi/', '/mail/koksaanna/', '/mail/nika1214/', '/mail/nurlan-argo/', '/mail/ostrovsvtt/', '/mail/lara24/', '/mail/franzolik/', '/mail/yagovenko/', '/mail/natka-zlatka/', '/mail/eko-shu/', '/list/dan3/', '/mail/nkargo/', '/mail/dododo55/', '/mail/chram5/', '/mail/mr_solnce/', '/mail/argo-psk/', '/mail/mr_alex1977/', '/mail/wachtanna/', '/mail/kovaleva1961no/', '/mail/soda1955/', '/mail/ekshv/', '/mail/kareva14/', '/mail/levchenko-lyudmi/', '/mail/wachtanna/', '/mail/gll-58/', '/mail/6503210/', '/mail/eko-shu/', '/mail/tkom55/', '/mail/orlovskaya-68/', '/mail/figura-84/', '/mail/penelopa53/', '/mail/olu51/', '/mail/solodov-ataman/', '/mail/elena210/', '/mail/alferovne/', '/mail/r.p.o._argo/', '/mail/lara24/', '/mail/aleks47-47/', '/mail/301558/', '/mail/elena210/', '/mail/ag999.99/', '/mail/satina.natalya.59/', '/mail/svet_barnaul/', '/mail/alferovane/', '/mail/gubina1956/', '/mail/ostrovsvtt/', '/mail/r.p.o._argo/', '/mail/sibvaleo.rus/', '/mail/albina_fin/', '/mail/tarasova__72/', '/mail/argo2010/', '/mail/kovaleva1961no/', '/mail/yuyuka08/', '/mail/ag999.99/', '/mail/soda1955/', '/mail/tatasav-777/', '/mail/sila_la/', '/mail/ag999.99/', '/list/mix1980/', '/mail/semeisheva_t/', '/mail/krilova_luba/', '/mail/orlovskaya-68/', '/bk/fitoline/', '/mail/helencxhj/', '/list/irin180680/', '/mail/stepchick.89/', '/mail/argo-nick/', '/mail/nataliandr5/', '/mail/sila_la/', '/mail/wachtanna/', '/bk/alexargo/', '/mail/anton-psk/', '/mail/emina2107/', '/mail/6503210/', '/mail/penelopa53/', '/mail/301558/', '/mail/lena19702/', '/mail/semeisheva_t/', '/mail/info-vektorpro/', '/mail/tatasav-777/', '/mail/argo2010/', '/mail/solodov-ataman/', '/mail/nastasya03072011/', '/mail/buzdalova/', '/mail/kuznecova69/', '/mail/mr_argo/', '/inbox/espirov/', '/mail/orlovskaya-68/', '/mail/eko-shu/', '/mail/elena-argo.psk/', '/bk/sokolnik/', '/mail/6503210/', '/mail/sibvaleo.rus/', '/mail/kuznecova69/', '/mail/eko-shu/', '/mail/mr_alex1977/', '/bk/chernova.alina/', '/list/dan3/', '/mail/yuyuka08/', '/mail/dahsulja90-90/', '/mail/franzolik/', '/list/alla_omsk/', '/mail/orlovskaya-68/', '/mail/mr_argo/', '/mail/ostrovsvtt/', '/mail/krilova_luba/', '/mail/emtehzagoruiko/', '/mail/eko-shu/', '/mail/aleks47-47/', '/mail/olu51/', '/mail/shatunovak/', '/mail/337553/', '/mail/andreyargo/', '/mail/omsk-bv/', '/mail/raz6/', '/mail/solodov-ataman/', '/mail/aleks47-47/', '/mail/argo-olga/', '/mail/argoufa/', '/mail/penelopa53/', '/mail/shatunovak/', '/mail/emina2107/', '/mail/yuyuka08/', '/mail/argonek/', '/mail/artstudio45/', '/mail/romanaristokrat/', '/mail/nastasya03072011/', '/list/dan3/', '/mail/olu51/', '/mail/stepchick.89/', '/mail/raz6/', '/mail/krilova_luba/', '/mail/emina2107/', '/mail/alferovne/', '/mail/asei45/', '/mail/yagovenko/', '/mail/wachtanna/', '/mail/jim55/', '/mail/figura-84/', '/mail/raz6/', '/mail/eko-shu/', '/mail/argo-nick/', '/mail/magikdia/', '/mail/tkom55/', '/mail/sila_la/', '/mail/nata_gosteva/', '/mail/lilia.bruch/', '/mail/6503210/', '/mail/tkom55/', '/mail/levchenko-lyudmi/', '/mail/argomila/', '/mail/argo_vlz/', '/mail/eko-shu/', '/mail/emina2107/', '/mail/sedelnikova_l/', '/mail/yura.kon-chuk/', '/mail/tarasova__72/', '/mail/kozlovcevis/', '/mail/stepchick.89/', '/mail/argo-psk/', '/list/alla_omsk/', '/mail/figura-84/', '/mail/albina_fin/', '/mail/elenabug/', '/mail/sila_la/', '/mail/solodov-ataman/', '/mail/yagovenko/', '/mail/788alberto/', '/mail/natali-manit/', '/mail/info-vektorpro/', '/mail/tatasav-777/', '/mail/r.p.o._argo/', '/bk/fitoline/', '/mail/satina.natalya.59/', '/mail/irina_tatevosyan/', '/mail/va_kapustin/', '/bk/alexargo/', '/mail/yagovenko/', '/mail/alferovane/', '/mail/figura-84/', '/list/irin180680/', '/mail/penelopa53/', '/mail/zibatoma/', '/mail/emtehzagoruiko/', '/mail/raz6/', '/mail/info-vektorpro/', '/mail/alferovne/', '/list/argo5/', '/mail/buzdalova/', '/mail/chram5/', '/mail/natka-zlatka/', '/mail/nastasya03072011/', '/mail/krekker/', '/mail/yagovenko/', '/mail/sedelnikova_l/', '/mail/tarasova__72/', '/mail/jim55/', '/mail/raz6/', '/mail/nurlan-argo/', '/mail/gubina1956/', '/mail/natali-manit/', '/mail/argomila/', '/mail/artstudio45/', '/mail/6503210/', '/mail/argo-olga/', '/mail/nata_gosteva/', '/mail/argo2010/', '/mail/voice-argo/', '/mail/svet_barnaul/', '/mail/emina2107/', '/mail/337553/', '/mail/andreyargo/', '/mail/irina_shumska/', '/mail/wachtanna/', '/mail/elena210/', '/mail/ekshv/', '/mail/satina.natalya.59/', '/mail/info-vektorpro/', '/mail/nata_gosteva/', '/mail/argonek/', '/mail/nataliandr5/', '/mail/buzdalova/', '/mail/solodov-ataman/', '/mail/yura.kon-chuk/', '/mail/irina_shumska/', '/mail/voice-argo/', '/mail/raisa.ostrovskaya.60/', '/mail/dododo55/', '/mail/argo_vlz/', '/mail/krilova_luba/', '/mail/sibvaleo.rus/', '/mail/elena210/', '/mail/natka-zlatka/', '/mail/alferovane/', '/mail/omsk-bv/', '/mail/irina_tatevosyan/', '/mail/sila_la/', '/mail/chram5/', '/mail/emina2107/', '/mail/788alberto/', '/mail/tarasova__72/', '/mail/solodov-ataman/', '/mail/lena19702/', '/mail/kozlovcevis/', '/mail/elena210/', '/mail/elvira-enukova/', '/mail/via.55/', '/mail/artstudio45/', '/inbox/espirov/', '/mail/mr_alex1977/', '/mail/ostrovsvtt/', '/mail/artstudio45/', '/mail/yadzaladjan/', '/mail/svet_barnaul/', '/mail/ivolga-s/', '/mail/alferovane/', '/bk/fitoline/', '/mail/magikdia/', '/mail/nicbah/', '/mail/sibvaleo.rus/', '/mail/irina_tatevosyan/', '/mail/franzolik/', '/bk/alexargo/', '/bk/chernova.alina/', '/mail/chram5/', '/mail/lara24/', '/mail/nicbah/', '/mail/sibvaleo.rus/', '/mail/v282ml/', '/mail/stepchick.89/', '/mail/elena210/', '/mail/argomila/', '/mail/artstudio45/', '/mail/mr_argo/', '/mail/sila_la/', '/mail/elena-argo.psk/', '/mail/lidia_58_58/', '/mail/yura.kon-chuk/', '/mail/krekker/', '/mail/yadzaladjan/', '/mail/nastasya03072011/', '/mail/valeolog48/', '/mail/v282ml/', '/mail/tarasova__72/', '/mail/va_kapustin/', '/mail/semeisheva_t/', '/mail/nkargo/', '/list/mix1980/', '/mail/albina_fin/', '/mail/alferovne/', '/mail/nika1214/', '/mail/artstudio45/', '/mail/argonek/', '/mail/sibvaleo.rus/', '/mail/nurlan-argo/', '/mail/mmedoctor/', '/mail/solodov-ataman/', '/mail/va_kapustin/', '/mail/shatunovak/', '/list/argo5/', '/mail/kozlovcevis/', '/mail/aleks47-47/', '/list/petrd10/', '/mail/argomila/', '/mail/ofnatalya/', '/mail/lidia_58_58/', '/mail/mr_argo/', '/mail/sedelnikova_l/', '/mail/alferovne/', '/mail/albina_fin/', '/mail/asei45/', '/mail/romanaristokrat/', '/mail/kovaleva1961no/', '/mail/raz6/', '/mail/chram5/', '/mail/6503210/', '/mail/lesya.argo/', '/mail/voice-argo/', '/mail/satina.natalya.59/', '/mail/sedelnikova_l/', '/bk/alexargo/']
skip = []
base = []
dom = 'none'
login = 'none'

#Парсим url, выдергиваем из неё список друзей и преобразуем в готовую эл.почту
def main(base,skip):
        
        try:
                for b in base:
                        url = ('https://my.mail.ru{idk}'.format(idk=b))
                        del base[0:]
                        html = urllib.request.urlopen(url).read() #Парсинг url
                        soup = BeautifulSoup(html, "html.parser")
                        href = soup.find_all('a',{'class':'b-right-column__block__friends__item booster-sc'}) #Выдергиваем список друзей
                        
                        for h in href:
                                h=h.attrs["href"] #Получаем ссылку на профиль
                                base.append(h)
                                
                        if h in skip: #Защита от зацикливания
                                print('!Защита от зацикливания успешно сработала...')
                                del base[0:]
                                base.append(random.choice(rand_))
                                print('skip: ',skip)
                                main(base,skip)
                        else:
                                
                                for h in base: #Обходим каждую ссылку на профиль и получаем из неё эл.почту.
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
                        print(base)
                        main(base,skip)
                        
        except:
                file.close()
                del base[0:]
                del skip[0:]
                base.append(random.choice(rand_))
                main(base,skip)
def start():
        
        try:
                print("""
                 █████╗ ██╗███╗   ███╗██╗  ██╗   ██╗ █████╗  █████╗ 
                ██╔══██╗██║████╗ ████║██║  ╚██╗ ██╔╝██╔══██╗██╔══██╗
                ███████║██║██╔████╔██║██║   ╚████╔╝ ███████║███████║
                ██╔══██║██║██║╚██╔╝██║██║    ╚██╔╝  ██╔══██║██╔══██║
                ██║  ██║██║██║ ╚═╝ ██║███████╗██║   ██║  ██║██║  ██║
                ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚══════╝╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝
                
Введите кол-во потоков:
                """)
                
                th=int(input())
                print('Выбираю рандомный профиль...')
                
                for i in range(th): #Запуск n-колличества потоков.
                        base.append(random.choice(rand_))
                        p = multiprocessing.Process(target=main, args=(base,skip,))
                        p.start()
                        print('thread ',i,': Начинаю парсить с рандомного email: ',base)
                        del base[0:]
                        
                print("""
Процесс парсинга происходит в скрытом режиме, результат можно посмотреть в файле mail.txt.

Для завершения процессса парсинга введите любой символ.
""")
                answ = str(input())
                subprocess.call('TASKKILL /T /F /IM pythonw.exe ',shell=True) #Убийство всех дочерних процессов и остановка парсинга, сделано на костялях, ибо краб.
                        
        except:
                start()
                
if __name__ == '__main__': 
        start()
