#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from tkinter import *
import webbrowser
import sys

current_version = '2.2 – wersja GUI'

# colors
bg = 'black'
fg = '#FCE94F'
abg = '#222222'
hb = '#000000'
# just for terminal 
yellow = "\033[1;33m"
nocolor = "\033[0m"

#info texts
info_1 = '''	I Ching - Księga Przemian. Inaczej: „I-Cing”, a ostatnio często też: „Yijing” – 易經. Księga mówiąca, że jedyna rzecz, która nie podlega przemianie to...\
	...bezustanna przemiana.

	Budowa wyroczni opiera się na współzależności sił wszechwiata „Yang” – siły twórczej i „Yin” – siły subtelnej. „Yang” reprezentuje linia ciągła, „Yin” – przerywana. Trzy takie linie budują trigram.

	Mamy 8 trigramów: Niebo ☰, Ziemia ☷, Ogień ☲, Rzeka ☵, Błyskawica ☳, Wiatr ☴, Góra ☶ i Jezioro ☱. Następnie z dwóch trigramów buduje się heksagram, których mamy 64.

czytaj dalej...'''

info_2 = '''	Księga pochodzi z Chin z czasów dynastii Zhou (750 – 1000 p.n.e.) Zwracali się do Niej – głównie monarchowie chińscy pytająć o pomoc przy podejmowaniu ważnych decyzji państwowych, gospodarczych, czy wręcz terytorialnych.

	Stosowano wtedy głównie gałązek krwawnika. Jest to metoda dosyć żmudna, co jednak pozwala na głębszą koncentrację nad zadawanym Księdze pytaniem.

	Można też użyć trzech monet. Jako, że jest to metoda obecnie najczęściej stosowana, pokrótce metodę tę objaśnię.'''

info_3 = '''	Reszka oznacza 2 punkty, orzełek zaś 3. Tak więc każdy rzut daje wynik \
od 6 – 9 punktów.
Nieparzyste (7 i 9) oznaczają linię Yang:	▄▄▄▄▄▄▄▄▄▄▄▄▄ ,
parzyste zaś (6 i 8) linię Yin:		▄▄▄▄▄   ▄▄▄▄▄ ,
przy czym liczby krańcowe czyli 6 i 9 \
oznaczają Przemianę, (każda taka linia daje dodatkowe wskazówki); linia ciągła („stary” Yang) zmienia się w przerywaną (Yin) – w przypadku gdy rzucimy 3 orzełki; linia przerywana („stary” Yin) zmienia się w ciągłą (Yang) – jeśli rzucimy 3 reszki.
	Takie linie oznacza się dodatkowo przekreślająć pośrodku za pomocą „X” (9pkt.), lub łącząc linię przerywaną za pomocą „O” (6pkt.) (w innych publikacjach najczęściej odwrotnie) .  Monety rzuca się sześciokrotnie zapisując wynik rzutu zapisując linie od dołu do góry; czy też – w przypadku posługiwania się tym programem 🙂, wciskając odpowiedni guzik (6, 7, 8 i 9). Można również używać klawiatury.'''

info_4 = '''	Niniejszy program może wykorzystać również moduł „random”, wirtualnie \
„rzucając” trzema monetami (linia 2304 kodu) 🙂, jednak zdecydowanie lepszym rozwiązaniem będzie użycie – jeśli nie gałązek krwawnika, to przynajmniej monet...

	Życzę Owocnych Przemian! (nie mylić z „dobrą zmianą” 😬)

	Dla ambitnych i zainteresowanych na następnych stronach zamieszczam jeszcze opis posługiwania się gałązkami krwawnika. Polecam również: https://pl.qaz.wiki/wiki/I_Ching_divination , gdzie znajdziemy te, jak też i inne sposoby (również inny skrypt 🙂).'''

info_5 = '''	Chińska tradycja nakazuje, by patyczki sporządzać z gałązek wierzby lub łodyżek krwawnika (achillea millefolium). Rośnie obficie na łąkach i przydrożach. Roślina ma przeciętnie 40-50 cm wysokości, liście pierzaste, kwiatki białe, drobne, zebrane w baldaszki-grona. Najlepiej jest zbierać go w sierpniu-wrześniu.

	Ponieważ potrzebujemy 50 patyczków o długości 7 cm, lub więcej zbieramy przynajmniej 10 łodyżek krwawnika, wybierając proste roślin, oczyszczamy je z liści i nierówności pozostałych po bocznych gałązkach, szlifujmy nieco cienkim nożykiem całą powierzchnię gałązki i rozkładamy wszystko do przesuszenia. Potem dzielimy gałązki na siedmiocentymetrowe (lub dłuższe) odcinki i malujmy je przez zanurzenie w farbie lub pędzelkiem na ciemnoczerwony kolor.'''

info_6 = '''	Mamy więc 50 patyczków. Jeden patyk odkładamy; dalej jest on tylko tzw. „świadkiem”. Pozostałe 49 patyków dzielimy na dwie kupki: lewą i prawą. Lewą kupkę odkładamy. Z obu kupek bierzemy po jednym patyku (tylko przy pierwszym dzieleniu)  i wkładamy je pomiędzy czwarty a piąty (mały) palec lewej dłoni.
	Lewą kupkę bierzemy do lewej dłoni i prawą ręką odejmujemy z niej kolejno po cztery patyki, aż w lewej zostaną 4, 3, 2 lub jeden patyk. Te patyki (czyli resztę z przeliczenia po cztery) wkładamy do lewej dłoni pomiędzy palec czwarty a środkowy (serdeczny).
	Następnie do lewej dłoni bierzemy prawą kupkę i tak samo przeliczamy po cztery, a resztę z przeliczenia wkładamy między palce środkowy (serdeczny) i wskazujący.'''

info_7 = '''	Teraz liczymy, ile mamy w sumie patyków między palcami w lewej dłoni: jeśli przy przeliczaniu nie pomyliliśmy się, może ich być tylko 9 lub 5 (w drugim i trzecim dzieleniu - 8 lub 4).
	9 lub 8 nazwijmy „dużą resztą”; 5 lub 4 „małą resztą”.
	Duża reszta ma charakter Yin, więc zapisujemy jako „2”, mała reszta ma charakter Yang, więc zapisujemy jako „3”. Kiedy już odliczymy pierwszą resztę, odkładamy ją na bok, obok pierwszego patyka - świadka, a z pozostałe patyki dzielimy znów na dwie kupki (z tym, że już nie zabieramy po jednym patyku), odliczamy po cztery i wyciągamy resztę, która tak samo jak poprzednio, może być duża, czyli „2”, albo mała, czyli „3”. Odkładamy tę drugą resztę obok pierwszej, i tak samo jak robiliśmy za drugim razem, odliczamy trzecią.

	Cały proces powtórzamy jeszcze pięciokrotnie...'''

# main dictionaries
######### THE VERY BOOK!
hexagram1 = {'title':'Niebiosa', 'ctitle':'T’ian', \
'picture':'''Niebo ponad niebem. Potęga smoka. Klucz.
Wybraniec działa odważnie. Posiada moc i jest niezwyciężony.''', \
'judgment':'''Który tworzy, przynosi największy sukces.
Pozostań na swojej ścieżce.''', 'interpretation':'''	Jest to otwierający heksagram Pana Stworzenia, Kreatora, który posiada moc przekształcania rzeczywistości zgodnie ze swoją wolą. Jesteś twórcą swojego świata. Właściwie nic nie może ci przeszkodzić w realizacji twoich zamierzeń. Twoja moc wynika z idealnej harmonii z siłami nieba. Dzięki temu możesz nieustannie czerpać z niebiańskich zasobów energii i wzmacniać się nieprzerwanie. Połączenie wyjątkowej aktywności i wielkiego poczucia bezpieczeństwa wyklucza wszelkie wahania i pozwala realizować najbardziej śmiałe pomysły. Ponieważ taki stan nie trwa długo, powinieneś teraz wykorzystać swoje położenie i urzeczywistniać swoje plany. Czas sprzyja. T'ian reprezentuje niebo i wielkie przedsięwzięcie. T'ian to twórcza i dynamiczna moc, której można użyć zarówno konstruktywnie jak i destruktywnie.
	Czas obiektywny heksagramu: 20 V + 20 VI, późna wiosna.''', \
'1a':'''Smok jest ukryty. Nie nadszedł jeszcze czas działania.''' , '1b':'''Smok - energia twórcza yang jest jeszcze w ukryciu. Nie wywiera swojego dobroczynnego wpływu. Wybraniec nie robi [z niej] użytku i czeka [w ukryciu] na właściwy moment. Wierny sobie, oszczędza wewnętrzną siłę. Nie zbacza z wytyczonej drogi.''', '2a':'''Smok pojawia się w przestrzeni. Zasięgnij rady mądrego umysłu.''', '2b':'''Zaczyna się wpływ yang. Twórcze siły nieba objawiają się w świecie ludzi i wydarzeń. Pojawił się ktoś silny w polu twojej aktywności. Zbliż się do niego, nie obawiaj się, że cię odrzuci. Połącz z nim siły i pomóż mu realizować jego cele.''', '3a':'''Wybraniec jest aktywny, kreatywny i czujny w dzień. Jego umysł jest wciąż zatroskany w nocy. Zagrożenie. Bez winy.''', '3b':'''Wybraniec działa. Moc jest z nim. Korzysta z nieograniczonej siły yang. Musi jednak uważać, gdyż ma wiele do zrobienia w świecie różnych interesów. Można łatwo zgubić drogę poprzez wygórowane ambicje i nadmiar autentycznych możliwości. Nie daj się zwieść na pokuszenie.''', '4a':'''Smok [niepewnie] wzlatuje nad głębiną w przestworza. Bez winy.''', '4b':'''Dylemat. Przyszła chwila decyzji. Wybraniec musi wybrać pomiędzy dwoma światami: zewnętrznym, gdzie wykorzystując swą moc, trzeba walczyć, by sięgnąć po władzę i prowadzić innych oraz wewnętrznym, gdzie moc służy do rozświetlenia swego wnętrza po to, by iść drogą świętości, samodoskonalenia i mądrości. Być panem ludzi czy umysłu? W tej kwestii nie można mu niczego doradzić. Musi zdecydować sam, wybierając wierną sobie drogę.''', '5a':'''* Smok szybuje w niebiosach. Skorzystaj z rady mądrego umysłu.''', '5b':'''Wybraniec uzyskał niebiańską harmonię. Jest ważny. Jego wpływowi chętnie ulegają inni. Teraz sam może udzielać rad. Spotkanie z nim ma dobroczynny wpływ.
Mistrz jest potrzebny do tego, aby móc sięgnąć po swoje najwyższe osiągnięcia.''', '6a':'''Smok wzlatuje zbyt wysoko. Zuchwały smok zazna żalu i smutku. Wina.''', '6b':'''Nie przekraczaj swoich granic, właściwej dla siebie miary. Wygórowane ambicje i nadmierne zaufanie we własne siły oraz lekceważenie kompromisów doprowadzą do upadku nawet wielkiego człowieka. Popatrz na los Ikara.''', 'all1':'''Pojawia się rzesza bezgłowych smoków. Powodzenie. Fortuna.''', 'all2':'''Sześć linii zmiennych to doskonała równowaga elementów yin i yang, uzyskana moc. Sprzyja to twórczemu oddziaływaniu na świat. Można działać w świetle dnia. Jest to moment kreacji nowego. Chwila sprzyja, ale nie potrwa długo. Działaj zatem zdecydowanie, ale łagodnie, aby wykorzystać sprzyjający czas. Niebawem dzień zmieni się w noc.'''}

hexagram2 = {'title':'Ziemia', \
'ctitle':'Kun', \
'picture':'''Ziemia ponad ziemią. Przestrzeń.
Jej istotą jest uległość i przyjmowanie.
Wybraniec ma szerokie horyzonty. Przewodzi światu.
Czyni swój charakter wszechstronnym, szczerym, i nośnym, przez co zdolny się staje utrzymywać i znosić ludzi oraz rzeczy.''', \
'judgment':'''Uległa przynosi pomyślność. Jest jak stałość i wierność klaczy. Podejmując działanie, gdy chce przewodzić, zgubi drogę. Gdy podąży śladem, znajdzie przewodnika.
Szukaj przyjaciół na zachodzie i południu (królestwo Czou, pierwiastki żeńskie). Porzuć tych na północy i wschodzie (królestwo Szang, pierwiastki męskie).''', \
'interpretation':'''	Uleganie to nie bierne przyjmowanie. Człowiek musi posiadać wewnętrzną siłę i wagę charakteru oraz szerokość poglądu, aby być zdolnym unosić świat i nie ulec jego wpływom. Żeńska siła yin, która rządzi tym heksagramem, nie może być interpretowana jako bezmyślna uległość i poddaństwo. Zawiera ona w sobie moc działania w świecie materialnym, popartą pokorą w stosunku do sił niebios. Otwarcie na ich inspirujący wpływ rodzi dojrzałą uległość, która pozwala odnosić sukcesy w życiu. Tutaj moc bierze się z harmonii i współodczuwania z elementem yang. Stapiając się z wpływową męską siłą, uzyskuje się jej moc, a podążając za nią można osiągnąć powodzenie. Nie wolno samemu próbować forsownych rozwiązań właściwych sile yang. Człowiek jest aktywny nie w samodzielnej funkcji, ale jako pomocnik i wykonawca. Dysponując inteligentną uległością siły yin, należy szukać poparcia dla swoich inicjatyw u sił yang. Postawa pomocnika wyrażona w tym heksagramie pozwala osiągnąć sukces. Zadaniem jest, by nie dążyć do przewodnictwa - bo przez to można tylko pobłądzić - lecz pozwolić się poprowadzić. Kto umie zachować się wobec losu z oddaniem, z pewnością znajdzie stosowne dla siebie kierownictwo. Szlachetny pozwala kierować sobą. Nie idzie ślepo przed siebie, lecz z okoliczności wnioskuje, czego się od niego żąda, i postępuje wedle tych wskazań losu.

Czas obiektywny heksagramu: 20 XI - 20 XII, późna jesień.''', \
'1a':'''Rosa zamarza. Zbliżają się mrozy.''', \
'1b':'''Uważaj. Nadciąga chłód i ciemność. Ruch zamiera. Można temu zapobiec, dostrzegając w porę oznaki stagnacji i podejmując działania zaradcze.''', \
'2a':'''* Prosta, kwadratowa i wielka; nie powtórzona.''', \
'2b':'''Sukces przychodzi bez wysiłku.
Taka jest Ziemia. Równowaga yin i yang daje prostotę i bezpośredniość.
Działasz w zgodzie z prawami Natury. Możesz podążać tą drogą naprzód, nie napotykając zbytniego oporu.''', \
'3a':'''Zamyka w sobie pewien wzór. Ukrywa twarz.''', \
'3b':'''Stały w swej mądrości. W służbie królewskiej nie szuka korzyści, ale przysparza chwały królowi swoimi czynami.
Masz coś cennego, ale nie w pełni decydujesz o swoim losie. Unikaj szkodliwych pochlebstw, próżność nimi się karmi. Ukryj swoje talenty i nie ujawniaj ich zbyt wcześnie. Dzięki temu uzyskasz spokój działania. Teraz jest czas na działanie w służbie publicznej.''', \
'4a':'''Wór jest związany. Bez winy. Bez pochwały.''', \
'4b':'''Wielkość przyciąga i jątrzy wśród nieprzyjaciół. Powstrzymaj się i nie pokazuj swoich możliwości, aż nadejdzie właściwy czas. Inaczej spotkasz się z fałszywym uznaniem lub wrogością. Przygotuj się do nadchodzących działań. ''', \
'5a':'''Żółty ubiór pod spodem daje najwyższe powodzenie. ''', \
'5b':'''Jest jak słońce wśród ciemności. Symbol powściągliwości. Zachowuje złoty środek. Pozostaje dyskretny. Objawia się w dokonaniach, nie pokazując swoich możliwości i talentów. ''', \
'6a':'''Wielki bój. Smoki staczają bitwę. Płynie purpurowa i żółta krew. Droga dobiega końca. ''', \
'6b':'''Zasada ciemna uzurpuje sobie władzę i staje się rywalem zasady jasnej. Walka na szczycie. Bunt Lucyfera przeciwko Bogu. Ciemne moce walczą przeciwko bogom Walhalli, a końcem jest Zmierz Bogów.
Smok, symbol nieba, zewnętrzna, pierwotna siła światła, przybywa i pokonuje fałszywego smoka, do którego postaci podniosło się to, co ziemskie. W tej walce, która jest przeciwna naturze, obie prymarne siły ponoszą straty.
	Jeżeli upiera się trwać na swojej pozycji, która nie jest mu należna, i chce władać zamiast służyć, to ściąga na siebie gniew tego, co silne. Dochodzi do walki, w której ciemne zostaje strącone, ale szkodę ponoszą obie strony.
	Też: Toczy wewnętrzną walkę. Siły ciemności walczą w nim przeciw boskim siłom nieba. Obecna ciemność musi ustąpić jasności, ale łatwo się nie podda. Zanim jasność odniesie zwycięstwo, obie strony odniosą rany. Zwycięstwo nad samym sobą okupione zostanie ranami na duszy. ''', \
'all1':'''Bądź niezłomny na swojej ścieżce. ''', \
'all2':'''Są to ostatnie chwile ciemności, niebawem siła yin zmieni się w moc yang. Wkrótce nadejdzie właściwy czas do działania. Bądź przygotowany na tę zmianę i wyjdź jej naprzeciw. Twoje położenie jest właściwe, zgodne z naturalnym biegiem rzeczy. '''}

hexagram3 = {'title':'Rosnąca udręka', \
'ctitle':'Tun', \
'picture':'''Rzeka nad gromem. Gejzer. Początkowe perturbacje.
Wybraniec zapanowuje nad chaosem, starannie porządkując swoje życie. ''', \
'judgment':'''Powodzenie. Trzymaj się swojej ścieżki. Można podjąć decyzję. Nie miej dokąd pójść. Bądź jak wódz, nie polegaj na samym sobie. Dobrze jest ustanowić zwierzchników. Przemyśl każde posunięcie. ''', \
'interpretation':'''	Dałeś się oczarować przypadkowemu zdarzeniu, spotkałeś się z nową fascynacją, która jednak ma charakter chwilowego olśnienia i nie jest naturalnym przedłużeniem twojej poprzedniej drogi - wywołuje to zarazem zaciekawienie i konsternację. Potraktuj to zamieszanie jako wyzwanie i pojawienie się nowych, niezwykłych i fascynujących szans. Jednak nie są one łatwe do wykorzystania. Musisz się liczyć z trudnościami od początku i przez długi czas. Trzeba się najpierw przebić przez obronny mur świadomości. Wytrwałość i niezłomność pomogą ci w tym, lecz jeśli nie zapanujesz nad chaosem, spowodują narastającą udrękę. Możesz pójść tą drogą, są widoki na przyszłość, ale wymagają hartu ducha. Doprowadzaj do ładu swój umysł i inicjuj działanie gromadząc posiłki ludzi, którzy będą mogli ci pomóc.''', \
'1a':'''* Tam i sam. Rozterki powodują trudności. Nie należy dokądś iść. Sprzyja powołanie zwierzchnika. ''', \
'1b':'''Nie pchaj się do przodu. Pilnuj swego miejsca zamieszkania.
Skup się na problemach domowych. Poczekaj, gromadząc posiłki i wzmacniając swoją pozycję. ''', \
'2a':'''Niedaleko podejrzanie gromadzą się narowiste konie. Nadchodzi zalotnik. Stara się o jej rękę. Porwano zaprzęg, lecz nie ma rabusia. Dziewczynka postanawia nigdy nie zajść w ciążę. Po dziesięciu latach zajdzie w ciążę. ''', \
'2b':'''Jesteś otoczony przez trudności. Natrafiasz na niespodziewanego sprzymierzeńca. Przytłoczony zmartwieniami trudno odgadnąć ci jego zamiary. Myślisz, że są wrogie. Jakkolwiek w rzeczywistości jego intencje są uczciwe, a jego propozycja nęcąca, to ponieważ nie jest to ktoś godny zaufania, nie angażuj się i odmów, gdyż możesz wplątać się w jeszcze większe kłopoty. Odczekaj, aż uzyskasz większą kontrolę nad swoim losem. Powinieneś najpierw dorosnąć do odpowiedzialności. Może to potrwać bardzo długo, gdyż musi minąć pełny cykl kosmiczny. Dopiero wtedy wszystko powróci na swoje właściwe miejsce. Wtedy też przyjdzie czas, że będziesz mógł w pełni rozkoszować się swoim partnerem. ''', \
'3a':'''Kto bez łowczego podąża za sarną w głąb lasu, zagubi się w leśnej kniei. Nieskazitelny dostrzega omeny na jego drodze i świadom czyhających niebezpieczeństw rezygnuje z polowania. Jeżeli postąpisz naprzód, pożałujesz tego. ''', \
'3b':'''Jesteś w opałach. Nie masz doświadczeń w walce na nieznanym gruncie. Zatracisz się, brnąc bez przewodnika na oślep. Musisz się wycofać i poczekać na lepszy czas. Jeżeli nie odstąpisz, czeka cię frustracja i poniżenie. ''', \
'4a':'''Porwano zaprzęg. Konie wracają. Dosiada klaczy i podąża naprzód. Dąży do związku. Wszystko sprzyja. ''', \
'4b':'''Masz kłopoty. Należy działać, ale jesteś osamotniony i brak ci środków.
Musisz zwalczyć swoje poczucie ważności i poszukać wsparcia. Prawdopodobna pomoc jest nieopodal. Poszukaj jej. Zrób pierwszy krok, nie obawiaj się upokorzenia i połącz swoje siły z kimś znaczącym, kto jest w twoim zasięgu. Potem wszystko poukłada się pomyślnie. ''', \
'5a':'''* Otaczanie sadła. Mała determinacja jest pomyślna, wielka determinacja jest niepomyślna. ''', \
'5b':'''Niebezpieczeństwo. Autorzy ciemnych interesów zabezpieczają swoje zyski, maskują i ukrywają je. Choć mogłeś ponieść straty materialne, działaj ostrożne, metodą małych kroków. ''', \
'6a':'''Porwano zaprzęg. Konie wracają. Dosiada klaczy, ale nie rusza do przodu. Strumień krwawych łez. ''', \
'6b':'''Zło urosło w siłę. Jesteś zagubiony, a twoje położenie jest beznadziejne. Dzieje się tak wtedy, gdy chce dosiadać klaczy, a jest zbyt słaby, sam i pozbawiony pomocy. Odczuwasz udrękę niemożności działania.
Zaplątałeś się fatalnie. Pogrążyłeś się w chaosie i zamęcie. Twoja frustracja jest tak wielka, że paraliżuje cię całkowicie. Teraz tylko w zdecydowanej walce, „na śmierć i życie” możesz to zło ukrócić. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram4 = {'title':'Młodzieńcza niewiedza', \
'ctitle':'Meng', \
'picture':'''Źródło tryska u podnóża góry. Młodość. Niewiedza.
Chaos i oświecenie.
Wybraniec konsoliduje swój charakter sumiennością swoich czynów. ''', \
'judgment':'''Młodzieńcza niewiedza jest fortunna. Nie szukam nowicjusza. To on poszukuje mnie. Daję mu pierwsze pouczenie. Kiedy pyta po raz drugi i trzeci o to samo, jest natrętny, lekkomyślny i brak mu szacunku. Sprawia tym kłopot, a moje światło jest coraz trudniejsze do zrozumienia. Natrętowi nie udzielam więcej nauk.
Powodzenie, jeśli obstajesz stanowczo przy swoim.
Trwaj na swojej ścieżce. ''', \
'interpretation':'''	Neofita, niedoświadczony nie jest ograniczony normami sytuacji, które inni jej uczestnicy muszą respektować. Jego szczęście nie zależy od wiedzy o uwarunkowaniach sytuacji. Dlatego upiecze mu się wiele, nawet gdy popełni mnóstwo nieprawidłowości sprzecznych z obowiązującymi schematami. Wbrew pozorom jego niekonwencjonalne zagrania i poczynania zostaną nagrodzone przez los, a wpadki puszczone płazem. Inni, nie widząc w nim zagrożenia swoich pozycji, gotowi są mu wiele wybaczyć. Póki zachowa swoją niewinność, będzie odnosił sukcesy, a jego czyny będą usprawiedliwione. Jeśli jednak będzie chciał się pozbyć swojej naiwności, musi poszukać odpowiedniego nauczyciela oraz poddać się jego pouczeniom i wskazówkom. Uczeń powinien mieć świadomość swojej niewiedzy i dążyć do pozbycia się swojej ignorancji, a jego mistrz powinien mu udzielać jasnych i zrozumiałych pouczeń. Nie można dopuścić do bałamutnego, niezgodnego z duchem nauki interpretowania mądrości, gdyż niewłaściwa i fałszywa interpretacja wiedzy kreuje przesądy i złudzenia, które powiększają ignorancję. Mistrz musi przekazywać wiedzę w sposób należyty i kompetentny, aby nie pogłębiać niewiedzy ucznia.''', \
'1a':'''Ignorant powinien zostać poddany surowej dyscyplinie, aby naiwność nie wstrzymywała jego rozwoju. Jednak powinien mieć własną wolę. Inaczej zostanie upokorzony. ''', \
'1b':'''Życie to poważna sprawa. Nie można podchodzić do niego z lekceważeniem. Gotowość do przyjęcia za nie odpowiedzialności wymaga wzmocnienia charakteru. Potrzebujesz hartu ducha. Sam znajdź dyscyplinujące cię środki. Spróbuj zacząć od hamowania swoich naturalnych impulsów. Niech ćwiczenie wypływa z twojego przekonania i twojej woli. To nie może być autorytarny dryl narzucany sobie wbrew swoim przekonaniom. ''', \
'2a':'''* Wyrozumiały w stosunku do ignoranta. Wie, jak radzić sobie z kobietami. Pomyślne jest wysłać dziewczynę jako żonę. Syn może przyjąć odpowiedzialność za rodzinę. ''', \
'2b':'''Umiesz postępować z ignorantami. Tam, gdzie inni tracą cierpliwość i nie chcą mieć z nimi do czynienia, ty, dzięki swej inteligencji i sile osobistej, potrafisz wpływać na postępowanie dyletantów, nie uciekając się do przemocy. Twój odpowiedni stosunek do młodzieńczej niewiedzy umożliwia podchodzenie do niej z pobłażliwością i wyrozumiałością. Dzięki temu udaje ci się kierować niedoświadczonymi, zachowując swój autorytet. ''', \
'3a':'''Nie należy wiązać się z tą kobietą. Zatraca się, widząc majętności mężczyzny. Nie będzie z tego nic dobrego. ''', \
'3b':'''Wyidealizowany obraz osoby, który sobie tworzysz, nie ma nic wspólnego z prawdą. Dążąc do sukcesu, poszukując miłości czy pragnąc wiedzy, ulegasz komuś, kto na pozór jest wzorem tego, czego szukasz. Jeśli będąc młodym i niedoświadczonym, chcesz znaleźć kogoś właściwego do naśladowania, powinieneś poczekać, dopóki twoje autentyczne pozytywne cechy nie zostaną dostrzeżone i nie spotkają się z zaciekawieniem osób wpływowych. Nie myl osoby swojego guru ze swoimi wyobrażeniami o niej. Jeżeli w tej sytuacji zajmujesz pozycję mistrza, nie daj się zwieść swoim uczuciom. Twój uczeń nie dostrzega ciebie, ale to, co sobą reprezentujesz. Zarówno uczeń, jak i mistrz nie powinni kultywować takich związków, gdyż są one niezdrowe dla obu stron. ''', \
'4a':'''Spętany łańcuchem ignorancji. Wina. Żal. ''', \
'4b':'''Pogrążył się we własnych fantazjach i nierealnych mrzonkach i nie potrafi się od nich uwolnić. Nie zdaje sobie sprawy, że opanowały go utopijne wizje. Spowity w ciemność ignorancji zazna upokorzenia, jeżeli nie przestanie oszukiwać siebie samego. Kto ma klapki na oczach i nie potrafi zaakceptować zmian na lepsze, z pewnością ściągnie na siebie nieszczęście. ''', \
'5a':'''* Dziecięca naiwność przynosi powodzenie. ''', \
'5b':'''Bądźcie jak dzieci, a osiągniecie Królestwo Niebieskie. Ufność, brak pożądań, optymizm, wiara i nadzieja pozwalają pokonać słabość dzięki mocy, która z nich wyrasta. Taki stan niewinnej świadomości naturalnie harmonizuje bowiem z niebiańskimi prawami. ''', \
'6a':'''Gdy karci ignoranta, by go chronić, zapobiega złu - pomyślna. Gdy ma nieczyste intencje powoduje wrogość - złowróżbna. ''', \
'6b':'''Karcąc niepoprawnego dyletanta zraża się go do występku. Nie można tolerować złych czynów wynikających z młodzieńczego niedoświadczenia i głupoty, gdyż będą narastać jeden za drugim, prowadząc na manowce życia i powodując cierpienie. Należy zapobiegać złym uczynkom, a kara nie może być celem, musi wynikać z samej zasady postępowania, nie może być wynikiem gniewu i egoistycznych intencji. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram5 = {'title':'Oczekiwanie na wyjście', \
'ctitle':'Siu', \
'picture':'''Rzeka na niebie. Przechodzenie przez rzekę. Zamoczony. ''', \
'judgment':'''Szczerość daje jasność widzenia i przynosi wielki sukces. Pozostań na swojej ścieżce. Korzystne będzie przekroczyć wielką wodę. ''', \
'interpretation':'''	Czas ważnego działania. Należy czekać na właściwy moment, dbając, by posiadana moc nie uległa rozproszeniu. Czekaj i zbieraj siły. Czekając w spokoju, pozbywając się oczekiwań i pragnień, można poradzić sobie z problemem, który nieuchronnie cię zniszczy, jeżeli nie uczynił tego dotąd. Jeżeli sprawy wymknęły ci się spod kontroli i władzę nad tobą posiada ktoś inny, od którego zależysz całkowicie, uważasz, że to już koniec. Wiedz jednak, że i z tego można wyjść. Trzeba wzmocnić swoją siłę woli, opierając ją o fundament wewnętrznej prawdy. Uczciwość wobec niej da jasny osąd sytuacji i pozwoli uniknąć zagrożenia. Niebawem przekroczysz ważny próg życiowy. Odwołaj się do swoich głębokich zasad i zgodnie z nimi uczyń decydujący krok, który, choć niesie niebezpieczeństwo, jest właściwy i pozwoli ci wyjść z zagrożonej strefy i powrócić z sukcesem. W ten sposób odzyskasz utraconą wolność.''', \
'1a':'''Czekanie na odległej polanie. Jeżeli wytrwasz w cierpliwości, nie zrobisz błędów. Bez winy. ''', \
'1b':'''Kiedy wszystko idzie pomyślnie i dopisuje dobre samopoczucie, nie należy martwić się niebezpieczeństwem, które jeszcze jest daleko, choć w głębi świadomości można już odczuć jego destrukcyjny wpływ. Coś wisi w powietrzu, ale nie można tracić równowagi z powodu niejasnych imaginacji o przyszłości. ''', \
'2a':'''Czekanie na mokrym piasku. Pomówienia. W końcu pomyślność. ''', \
'2b':'''Zagrożenie jest coraz bliżej. Powoduje swary i niesnaski wewnątrz twojego otoczenia. TY i twoi bliscy jesteście pod wpływem oskarżeń z zewnątrz, a oskarżacie się nawzajem, szukając winnego. Należy tego zaprzestać. Trzeba połączyć siły, zdemaskować i pokonać oszczercę, zanim zwycięży. Gdy żal i poczucie winy zostaną pokonane, wszystko skończy się pomyślnie. ''', \
'3a':'''Zamoczony w bagnie. Sprowadza nieprzyjaciela. ''', \
'3b':'''Niebezpieczeństwo, które wyczuwasz, jest realne. Trzeba mieć tego świadomość i starać się uporać z nim możliwie szybko, ale trzeba działać ostrożnie. Czekającego w bagnie wciąga ono w swe zdradzieckie objęcia, gdy postępuje gwałtownie i pośpiesznie. Grzęznąc w kłopotach, ściąga na siebie uwagę wroga, który będzie chciał wykorzystać jego trudne położenie. Doceń powagę sytuacji i spróbuj opuścić zagrożoną strefę, by nie dopuścić do klęski. ''', \
'4a':'''Czekanie w jaskini. Zamoczony we krwi. Wydostaje się z jaskini. ''', \
'4b':'''Znalazłeś się w krańcowo niebezpiecznym położeniu. Rzecz idzie o życie lub śmierć. Można przypuszczać, że nieuchronnie popłynie krew. Musisz zaakceptować obecną sytuację i pogodzić się z losem.
Uspokój się. Usiądź w pozycji lotosu, bądź nieporuszony jak skała.
Nie podejmuj żadnych działań, gdyż tylko pogorszą sprawy. Pielęgnuj swój charakter, abyś był zdolny i przygotowany na wydobycie się z tej matni. Zanim wyjdziesz z tej koszmarnej sytuacji, przygotuj się na drogę najeżoną cierniami oraz wyjątkowo przykre wydarzenia. ''', \
'5a':'''* Czekanie na uczcie. Zamacza usta w winie.
Pomyślna, jeśli będziesz wytrwale trzymać się swojej ścieżki. ''', \
'5b':'''Chwila wytchnienia wśród napierających z zewnątrz zagrożeń. Trzeba wykorzystać tę krótką przerwę, przywrócić zachwianą równowagę i wzmocnić się, aby być gotowym na dalsze zmagania. Ponieważ jest wytrwały, może być pewien swego i dlatego wewnętrzny spokój go nie opuści. Niebezpieczeństwo ciągle zagraża, do rozwiązania problemów jeszcze daleko, ale droga, po której kroczy, jest właściwa. ''', \
'6a':'''Wpada do jamy. Nadchodzą trzej niespodziewani goście. Okaż im cześć i szacunek, a wszystko zakończy się pomyślnie. ''', \
'6b':'''Wpadł w pułapkę i popadł w krańcową desperację, nie widząc drogi wyjścia. Wydaje mu się, że jego problem nie ma rozwiązania. Jednak oczekiwanie dobiegło kresu. We właściwym bowiem czasie powracają do zagubionego nieszczęśnika trzej nieoczekiwani goście, by wybawić go z zagrożenia. Ich ingerencja jest tak zaskakująca, że zrazu nie można poznać, czy niosą zniszczenie, czy pomoc. Trzeba temu nowemu elementowi sytuacji zaufać, nie okazywać niechęci i przyjąć go z szacunkiem, a wywiedzie człowieka na wolność. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram6 = {'title':'Konflikt', \
'ctitle':'Song', \
'picture':'''Rzeka oddala się od nieba. Antagonizm.
Szukanie sprawiedliwości.
Wybraniec wnikliwie zastanawia się nad początkiem sporu. ''', \
'judgment':'''Jest szczery, ale i tak natrafia na przeszkody. Przewidująco zatrzymuje się na ścieżce. Daje to korzyść.
Podążanie do końca jest niefortunne. Dobrze jest zasięgnąć rady mądrego umysłu. Nie należy przebywać wielkiej wody. ''', \
'interpretation':'''	Spór prawny. Nie jest to dobry czas na szukanie sprawiedliwości.
Nie należy toczyć bitwy prawnej i wszczynać sporów w ważnych kwestiach. Obie strony prezentują rozbieżne od początku dążenia. Każda z nich, będąc wierną sobie, prokuruje waśnie. Obie przekonane są o swoich racjach i jawnie demonstrują swój punkt widzenia. W takiej sytuacji nieuchronnie dochodzi do sporu, a jeśli nie pohamować się w porę, wybucha konflikt. Mając świadomość tych uwarunkowań, trzeba wyjść antagoniście w pół drogi, aby rozwiązać problem i konflikt zażegnać. Dobrze jest poradzić się mądrego człowieka i przyjąć jego mediację obiektywnego arbitra. Najpierw trzeba usunąć przyczyny powstałych swarów. Dopóki nie rozwiąże się spornych kwestii, nie można podejmować żadnych przełomowych działań. Jeżeli sporu nie można rozstrzygnąć, należy przystać na kompromis albo się wycofać. Nie wolno być upartym i dać się ponieść emocjom. Gdy będzie zapamiętały w uporze, pożałuje. Należy szukać przymierza z tymi, którzy patrzą na sprawy podobnie. Heksagram dotyczy procesu cywilnego.''', \
'1a':'''Nie jest uparty w sprawie. Spotkają go zniewagi, lecz przyniesie to korzyść. ''', \
'1b':'''Konflikt jest dopiero w stadium początkowym. Można teraz łatwo go uniknąć, zrywając kontakty i wycofując się z kłopotliwej sytuacji. Nie uniknie się, co prawda, pomówień i obelg, ale lepsze to niż eskalacja konfliktu, zwłaszcza że druga strona jest silniejsza. ''', \
'2a':'''Zbyt mały, aby angażować się w konflikt, Zostawia wolne pole. Wraca do miasta. Trzysta rodzin nie ma strapień. ''', \
'2b':'''Jeżeli podejmiesz walkę przysporzysz kłopotu sobie I zgryzot swojemu otoczeniu. Gdy ma się do czynienia z przeważającymi siłami, nie ma hańby w odstąpieniu od starcia. Tylko źle rozumiane poczucie honoru pcha naprzód w takiej sytuacji. Należy się wycofać, Nie przyniesie to ujmy na honorze. ''', \
'3a':'''Posłuszny starodawnym cnotom skłonny jest do hipokryzji. Zagrożenie. W końcu fortunna. Jeżeli sprawujesz rządy, nie szukaj sławy. Powstrzymaj się od działania. ''', \
'3b':'''Można zdobyć różne dobra i mieć je aktualnie w posiadaniu, ale one są zawsze przejściowe. Dotyczy to zarówno rzeczy, jak i wartości niematerialnych. Nawet twoje złote myśli nie są naprawdę twoje, bo należą do gatunku ludzkiego. Jeżeli więc stracisz coś, co w istocie nie należy do ciebie, głupotą i chciwością można tylko tłumaczyć twoje roszczenia do tych wartości. Nie próbuj odzyskać swoich praw do własności, która ci się nie należy. To, co pozostaje naprawdę twoje, i tak pozostanie w twoim posiadaniu, jeżeli tylko zasłużyłeś na to uczciwym wysiłkiem. Jeżeli masz możliwość zarządzania, ciesz się samą możliwością wpływu na bieg rzeczy. Nie szukaj pustej sławy i prestiżu wynikającego z pełnionej roli. ''', \
'4a':'''Nie wchodzi w konflikt. Zawraca i poddaje się losowi. Zmienia nastawienie i znajduje spokój w wytrwałości. ''', \
'4b':'''Dysponujesz przeważającymi siłami w stosunku do drugiej strony konfliktu. Choć wiesz, że w razie starcia zwyciężysz, wycofaj się, gdyż racja nie jest po twojej stronie. Nie ma chwały z takiego zwycięstwa. Powinieneś zawrócić i pogodzić się z [swoim] losem. Zmień swój stosunek do sprawy, a wszystko się ułoży. ''', \
'5a':'''* Rozstrzygnięcie sporu przez niego przynosi najwyższą fortunę. ''', \
'5b':'''Jeżeli jesteś uczciwy, potężny i sprawiedliwy, arbiter, do którego warto się zwrócić, będzie z tobą w zgodzie. Najwyższe powodzenie, najwyższa pomyślność. ''', \
'6a':'''Obdarowany przez króla skórzanym pasem. Oddane honory odbiorą mu trzy razy przed końcem dnia. ''', \
'6b':'''Zwyciężasz w konflikcie. Dopiąłeś swego. Ale to zwycięstwo ma gorzki smak. Chociaż obdarowano cię z tego tytułu nagrodami, to jednak twój sukces nie jest trwały, a zwycięstwo ostateczne. Pokonani przeciwnicy nie uznają twojego triumfu i dlatego możesz spodziewać się odwetu i prób jego ponawiania. Niebawem ten sam konflikt pochłonie cię na nowo. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram7 = {'title':'Wojsko', \
'ctitle':'Szi', \
'picture':'''Podziemna rzeka. Armia i wojna. Żołnierze.
Wojownicy. Masa ludzka.
Wybraniec żywi i naucza lud pomnażając swoich zwolenników. ''', \
'judgment':'''Dowódca armii powinien być niezłomny i wytrwały.
Doświadczenie i stanowczość człowieka dojrzałego przynosi szczęście. Nie ma błędu. ''', \
'interpretation':'''	Żeby przeprowadzić swoje zamierzenia, potrzebne są oddanie sprawie, nieugiętość, odwaga i nieustępliwość, znajdujące wyraz w determinacji w dążeniu do celu i realizacji zadań. Być może na swojej drodze spotkasz niebezpieczeństwa, ale nie należy się ich wystraszyć i poddawać się, pozwalając, by zahamowały działanie. Należy zebrać zwolenników i zapewnić sobie ich poparcie „przekonując do swoich planów. Ponieważ sytuacja na początku jest trudna, zanim podejmą decyzję o współdziałaniu, muszą być uświadomieni o grożących niebezpieczeństwach. Jeżeli dostarczysz im duchową i materialną strawę, powiedziesz ich za sobą. Zważ jednak, aby nie omamić ich złudnymi nadziejami, gdyż prawda i tak, jak oliwa, wypłynie na powierzchnię, a wtedy odsuną się od ciebie. Przy organizacji kampanii, należy kontrolować i pilnować porządku, a rozpoczęcie kampanii powinno być zdecydowane i pewne. Twoje pojedyncze zwycięstwa pomogą zjednoczyć siły i wzmocnić wewnętrzne struktury armii. Miej również na uwadze, że armii i siły należy używać wyjątkowo ostrożnie. Wojna to ostateczność; gdy już wybuchnie, żałoba jest nieuchronna. Ponieważ doskonały dowódca nie walczy, nikt na świecie go nie pokona. Wygrywa bitwy bez jednego strzału. Skoro zwyciężył, taka była konieczność; lecz nie siłą i gwałtem. Używa inteligencji i doświadczenia, stosując fortele i podstęp, wprowadzając przeciwnika w błąd.''', \
'1a':'''Armia pod rozkazami idzie naprzód. Fiasko, gdy rozkazy nie są stosowne, albo szyk właściwy. ''', \
'1b':'''Przed rozpoczęciem działań powinieneś dokładnie zbadać swoją strategię. Musi być uczciwa i mieć sprawiedliwe zasady. Zadbaj też o właściwy porządek pośród swojego wojska. ''', \
'2a':'''Pośród wojska. Powodzenie. Nie ma winy. Król odznacza go trzykrotnie. ''', \
'2b':'''Zostajesz wyróżniony i nagrodzony za rzeczywiste zasługi. Zaszczyty te należy przyjmować bez niepotrzebnej hipokryzji. Nie są czymś niewłaściwym. Zwierzchnik obdarza cię, bo uosabiasz wspólny sukces. ''', \
'3a':'''Wojsko przynosi straty. Klęska. ''', \
'3b':'''Tutaj niewłaściwe użycie armii prowadzi do porażki. Niewłaściwie oceniłeś swoje siły. Poddajesz się swoim słabościom, zamiast skupić się na przewodzeniu. Przypadkiem, nieświadomie oddajesz pole komuś niepowołanemu, kto chce zająć twoje miejsce. Zagraża ci porażka na rzecz uzurpatora. ''', \
'4a':'''Armia wycofuje się. Nie pomylisz się. ''', \
'4b':'''Gdy nieprzyjaciel przeważa, nie należy stawać do beznadziejnej walki. Powinieneś dokonać kontrolowanego odwrotu na z góry upatrzoną pozycję i umocnić ją. Pokonasz przeszkody, ale poczekaj na bardziej właściwy czas działania. ''', \
'5a':'''* Zwierzyna na polu. Należy ją schwytać lub wypłoszyć. Niech najstarszy przewodzi wojsku. Młodszy wiezie wozem trupy ofiar. Determinacja nie jest pomyślna. ''', \
'5b':'''Zwycięstwo. To już nie wojna, ale polowanie na niedobitki. Wróg już nie zagraża, zakuwany jest w kajdany. Nie należy dalej forsować agresywnych działań. ''', \
'6a':'''Wielki wódz mianuje namiestników prowincji. Przyznaje rodom strefy wpływów. Nie angażuje pionków. ''', \
'6b':'''Zwyciężyłeś. Możesz sam rządzić. Rozdaj nagrody i rządź poprzez ludzi z kwalifikacjami. Jeżeli dasz władzę małym - nadużyją jej. Wystarczy, jak za zasługi dasz im pieniądze. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram8 = {'title':'Związek', \
'ctitle':'Pi', \
'picture':'''Rzeka nad ziemią. Więź. Sprzymierzenie. Starożytni królowie, ustanawiając swe niezliczone królestwa, nadawali ziemię w lenno, zawierali przymierza z reprezentującymi ich książętami i pielęgnowali związki z nimi. ''', \
'judgment':'''Związek sprzyja szczęściu. Skonsultuj się z wyrocznią ponownie, by dowiedzieć się, czy twój umysł jest wystarczająco jasny, a ty wystarczająco niezłomny. Jeśli tak, nie ma winy. Niezdecydowani dołączą stopniowo.
Wahającym się zbyt długo fortuna nie sprzyja. ''', \
'interpretation':'''	Związek symbolizuje obcowanie i wzajemna bliskość. Związek to praca zespołowa, współpraca i partnerstwo. Szczerość i uczciwość przyniosą pozytywne rezultaty. Łącz się z innymi. Więzi są czymś radosnym i służą jednoczeniu się. Człowiek potrzebuje związków z ludźmi i z otaczającym światem. Inaczej popada w alienację i odosobnienie. Nie należy izolować się od bliskich kontaktów z innymi.
	Jednak aby móc się związać, potrzeba zwalczyć swoje nadmierne poczucie własnej ważności. Ono nie pozwala zbliżyć się do drugich na tyle, aby nawiązać bliski kontakt. Najpierw trzeba spełniać życzenia innych, aby później nasze życzenia były spełniane przez nich. Związek powinien dawać poczucie bezpieczeństwa wszystkim zaangażowanym stronom. Należy również uważać, aby nie rozpadł się na skutek nieekwiwalentnej wymiany korzyści. Wszyscy muszą czerpać ze związku w jednakowym stopniu. Jeżeli chcesz być przywódcą w takim związku, musisz zapytać się wyroczni, czy dysponujesz odpowiednimi cechami i czy nadajesz się, by pełnić tak odpowiedzialną funkcję. Kto pozostaje niezdecydowany, traci okazję otrzymaną od losu.''', \
'1a':'''Sprzymierz się z nim. Oto jest powrót na właściwą drogę. Prawdomówność sprzyja związkowi. Napełnij glinianą misę. ''', \
'1b':'''Szczerość, uczciwość i lojalność są podstawą każdego prawdziwego związku. Muszą być autentyczne i wynikać z wewnętrznej prawdy oczyszczonego umysłu, a nie wyrażać się tylko poprzez czarowne deklaracje. Takiemu związkowi szczęście sprzyja w każdej sytuacji.
Właściwa droga to sprzymierzyć się z kimś, kto w danej sytuacji jest naturalnym przywódcą. Dobrze jest złożyć małą ofiarę. ''', \
'2a':'''Prawdziwy związek pochodzi z wewnętrznej głębi. Niezłomność na ścieżce przynosi szczęście. ''', \
'2b':'''Związek w świecie zewnętrznym pojawia się wtedy, gdy zgoda jest wewnątrz nas. Tylko wtedy można nawiązać z innymi prawdziwe więzy. ''', \
'3a':'''Wiąże się z nieodpowiednimi istotami. ''', \
'3b':'''Kto znajduje się w otoczeniu kogoś z innego kręgu, powinien być ostrożny. Nie może pozwolić sobie na zaangażowanie się w fałszywą poufałość z kimś, kto należy do innej sfery, mimo że dzieli jego zasady i wartości. Należy wycofać się z tego środowiska. Można zachować indywidualne, towarzyskie związki z niektórymi członkami.
W ten sposób zachowa się niezależność, która posłuży do właściwych związków, jakie przyjdą później. ''', \
'4a':'''Prawdziwy związek ze światem zewnętrznym.
Wytrwałość przynosi pomyślny los. ''', \
'4b':'''Trzymanie się razem ze społeczeństwem spoza granic imperium, aby podążać za wyższym. Sprzymierzeńcy są poza domeną. Szukaj ich przyjaźni. Korzystne jest zawrzeć z nimi przymierze. W przyszłości możesz potrzebować ich pomocy. ''', \
'5a':'''* Pojawia się związek. Król prowadzi polowanie z trzech stron, pozostawiając wolne pole do ucieczki.
Podkomendni nie potrzebują przestróg. Powodzenie. ''', \
'5b':'''Władca przestrzegający tradycji i obyczajów pociąga za sobą społeczność. Ci, którzy nie są zainteresowani, dostają wolną drogę. Ostają się tylko wierni sprawie, którzy dobrowolnie wchodzą w związek. Nie potrzeba wówczas przemocy i nadzoru. ''', \
'6a':'''Związek bez przywódcy. Niepowodzenie. ''', \
'6b':'''Gdy przymierze nie ma przywódcy, nie rokuje sukcesu. Brak decyzji, przedłużające się wahanie, przed którym ostrzega wyrocznia, powoduje, że przeoczyłeś właściwy moment sprzymierzenia. Teraz możesz się spodziewać, że ci się nie uda. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram9 = {'title':'Małe ograniczające', \
'ctitle':'Siao czu', \
'picture':'''Wiatr wieje na niebie. Małe, które ogranicza. Cień pada na sprawy.
Wybraniec udoskonala i pielęgnuje swoje zalety, wysubtelnia zewnętrzną formę swego charakteru. ''', \
'judgment':'''Rozwijając małe, osiąga powodzenie. Wiatr gna gęste chmury z zachodu, lecz deszcz nie spada. Poczekaj jeszcze i przygotowuj się. ''', \
'interpretation':'''	Twoja małość cię ogranicza, zatrzymałeś się w rozwoju. Jesteś zbyt słaby i nieprzyszykowany jeszcze do realizacji swoich celów. Twoja podświadomość rzuca się cieniem na twoje działania. Zrób porządek w swoim wewnętrznym świecie. Poskrom księżyc w tobie.
	Musisz najpierw stopniowo wzmocnić swój charakter, abyś mógł przyjąć na siebie ciężar rzeczy wielkich. Pożyteczne zmiany nadejdą, ale musisz poczynić jeszcze dużo przygotowań. Powinieneś pielęgnować zdolność przystosowywania się do sytuacji, aby niepotrzebnie nie przyspieszać biegu spraw i walczyć z losem. Droga do wielkości wiedzie poprzez mniej istotną aktywność, bez specjalnego celu, która jednak kreuje podstawy do rozwoju i otworzy szanse na działanie.''', \
'1a':''' Zawrócenie na ścieżkę. Jak można teraz popełnić błąd? Powodzenie.''', \
'1b':''' Masz siłę, ale brak ci rozwagi i postępujesz pochopnie, chcąc działać.
Nie forsuj działań, bo i tak nie osiągniesz czego pragniesz. Zawróć na swoją drogę. Pokora ci nie zaszkodzi. Gdy będziesz działał zgodnie ze swoim Tao, choć droga jeszcze daleka, nadejdzie szczęście.''', \
'2a':''' Nieskazitelny pozwala pociągnąć się do odwrotu. Wycofał się na właściwą ścieżkę. Trzyma się jej. Korzystne jest iść ze sprzymierzeńcami. Powodzenie.''', \
'2b':'''Podąża w złym kierunku, ale dostrzegając w porę przeszkody, reflektuje się i powraca na właściwą drogę i dołącza do linii pierwszej. Przyjmuje nastawienie, które chroni go przed zatraceniem czy zagubieniem. Taka postawa prowadzi do powrotu do tych, którzy dzielili z nim cele i kierunki, ale wycofali się, zostawiając go samego wtedy, gdy zboczył z drogi. ''', \
'3a':'''Powóz stracił koła. Mąż i żona patrzą na siebie z wściekłością. Rozstają się. ''', \
'3b':'''Uparte, mimo dostrzegania przeszkód, podążanie naprzód niszczy harmonię i zakłóca równowagę. Usiłowania dalszego forsowania egoistycznych i samowolnych rozwiązań są bezcelowe, wóz bez kół nie pojedzie. Spotkają się one jedynie z gwałtowną reakcją i oporem nawet bliskich osób. ''', \
'4a':'''◆ Jeżeli jest szczery, groźba rozlewu krwi się oddala. Nie zbłądzi. ''', \
'4b':'''Kto jest prawą ręką władcy znajduje się w trudnej sytuacji i będąc nieskazitelnym, ciągle narażony jest na różnorakie zagrożenia. Musi pozostać szczery i bezinteresowny, nie poddając się strachowi i naporowi agresywnych sił, a osiągnie powodzenie. ''', \
'5a':'''* Szczery i lojalny w swojej przyjaźni pozyskuje sprzymierzeńców. ''', \
'5b':'''Lojalne związki oparte są na wiarygodności i oddaniu. Szczerością pozyskuje się przyjaciół, na których zawsze można polegać. Łączy ich nić sympatii i porozumienia. Takie związki są źródłem obfitości, dlatego należy dbać o swoje przyjaźnie, podtrzymując drogocenne kontakty. ''', \
'6a':'''Spadł deszcz i ustał. Ruch zostaje wstrzymany. Nieskazitelny ocenia postęp uzyskany do tej pory. Dostrzega poprawę. Kobieta, mimo że niewinna, jest zagrożona; jest jak księżyc zbliżający się do pełni. Złowróżbna, jeżeli będziesz wcielać w życie swoje cele. ''', \
'6b':'''Mniej istotne działania podejmowane do tej pory zaczynają przynosić oczekiwane skutki. Małe przemienia się w wielkie, ale nie można go wykorzystać, gdyż w momencie kumulacji energii yin brak jest czynnika yang, który element yin by równoważył. Gdy kobieta jest za bardzo wyeksponowana, naraża się na niebezpieczeństwo. Działanie w takiej chwili powoduje zagrożenie i utratę osiągniętej pozycji. Po pełni księżyc zaczyna zanikać. Poczekaj więc, już wkrótce nadejdzie właściwy czas na działanie. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram10 = {'title':'Stąpanie', \
'ctitle':'Lu', \
'picture':'''Niebo ponad jeziorem. Nadepnięcie.
Jezioro odbija wszechświat w lustrze wód.
Wybraniec odróżnia wysokie od niskiego i rozważa wolę ludu. ''', \
'judgment':'''Stąpa po ogonie tygrysa, ale go nie pożre.
Posunięcie ryzykowne. Powodzenie. ''', \
'interpretation':'''	Wyjątkowo trudna i poważna sytuacja. Wielkie zagrożenie.
Podążając do przodu, trzeba rozglądać się wokoło, patrzeć przed i za siebie. Należy unikać gwałtownych ruchów. W ten sposób można uchronić się przed niebezpieczeństwem i odnieść korzyść z tej sytuacji, nabierając doświadczenia. Obecność stałego zagrożenia wyczula bowiem zmysły i wyostrza uwagę, co przyczynia się do klarowniejszego widzenia otaczającej rzeczywistości, a to z kolei sprzyja efektywnemu działaniu. W swojej aktywności należy rozróżniać pomiędzy pozycją, jaką ktoś zajmuje, i funkcją, którą pełni, a jego cechami charakteru. Czasami zdarza się, że eksponowane miejsce zajmuje ktoś słaby, a w położeniu niższym jest ktoś, kto może okazać się naprawdę niebezpieczny.
	Ktoś podejmuje właściwe działania zmierzające do obalenie tyrana, którego symbolizuje tygrys. Trzeba nadepnąć mu na ogon, by sprawdzić jego reakcje. W ten sposób można poznać jego mocne i słabe strony. Należy najpierw zbadać grunt, aby móc potem przygotować najlepszy plan. Trzeba przy tym zachować jak najdalej idącą ostrożność, niebezpieczeństwo grozi bowiem zewsząd. Sprzyja temu przestrzeganie dobrych obyczajów. Kto jest temu posłuszny, zajmuje miejsce władcy i pozostaje bez błędu, a jego światło świeci jasno.''', \
'1a':'''Stąpa znaną ścieżką. Jeśli podąży naprzód, nie zbłądzi. ''', \
'1b':'''Umiar w postępowaniu nie pozwala dojść do głosu nadmiernym ambicjom. Zajmując niską pozycję, można dojść wyżej, ale trzeba mieć zaufanie do swoich sił i podejmowanych działań. Nie należy zbyt wcześnie się określać, pozostawiając sobie swobodę decyzji. ''', \
'2a':'''Stąpa równą drogą. Trzyma się swojej ścieżki.
Zachęcająca. Najwyższe powodzenie.''', \
'2b':'''Nie poddajesz się pokusom świata, nie interesuje cię i nie angażujesz się w pogoń za sławą, władzą, pieniądzem i miłością. Dlatego nie dręczą cię z tego powodu, jak innych, obawy i wątpliwości. Posiadasz prawdę w sobie i postępujesz swoją drogą. Nic nie stanie ci na przeszkodzie, bo niepotrzebnie nie kusisz losu. ''', \
'3a':'''◆ Jednooki widzi, kulawy chodzi. Stąpa po ogonie tygrysa, który go gryzie. Fiasko. Tak postępuje wojownik tylko z rozkazu króla. ''', \
'3b':'''Ignorant, i do tego słaby, który chce rządzić, naraża się na niebezpieczeństwa, których nie jest świadom. Jeżeli zdecydujesz się na działania ponad twoje siły, czeka cię klęska. Tak można postępować tylko w ostateczności, ale nie jest to ta chwila. Król Wen miał świadomość, że nim przystąpi do ogólnego powstania, musi dopracować swój plan w najdrobniejszych szczegółach. Tylko wtedy, gdy plan jest gruntownie dopracowany, można osiągnąć cel. Inaczej sny o potędze prowadzą do klęski. ''', \
'4a':'''Stąpa po ogonie tygrysa w wielkiej panice. Przezorność i roztropność sprzyjają. W końcu fortunna. ''', \
'4b':'''Chcesz zrealizować brawurowe zadanie. Możesz je wykonać, ale wymaga to świetnej oceny sytuacji i wyjątkowej ostrożności. Musisz być jednocześnie elastyczny i pewny siebie oraz posiadać przekonanie o celowości twoich działań. Skorzystaj ze swego instynktu. ''', \
'5a':'''* Stąpa rezolutnie. Podąża ze świadomością zagrożenia. ''', \
'5b':'''Wewnętrzna siła osobista, którą posiadasz, pomaga pokonać niebezpieczeństwa, ale bądź świadom, jego stałej obecności. ''', \
'6a':'''Bada drogę, po której stąpa. Zważa na pomyślne znaki. Gdy osiągnął cel teraz, wszystko się dopełni i fortuna się do niego uśmiechnie. ''', \
'6b':'''Cel został osiągnięty. Świadomie zakończyłeś działanie. Śledząc przebytą drogę, można odczytać jej kres. Poznasz i ocenisz siebie, gdy spojrzysz wstecz poprzez efekty twoich działań. Gdy są pozytywne, dalsza aktywność będzie udana. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram11 = {'title':'Pokój', \
'ctitle':'Tai', \
'picture':'''Niebo i Ziemia jednoczą się. Pokój. Znaczenie. Ważność.
Władca, podążając drogą nieba i ziemi, wspomaga ich naturalną harmonię, ucząc tego lud; zwraca uwagę na to, jak korupcja i zepsucie wpływają na państwo. ''', \
'judgment':'''Małe zanika, wielkie się rodzi. Powodzenie. Postęp rodzi pomyślność. Zwiastuje fortunę. ''', \
'interpretation':'''	Cieszysz się bardzo dużym poczuciem bezpieczeństwa, jednocześnie odczuwasz głęboki wewnętrzny spokój. Taki harmonijny związek nieba i ziemi w tobie przynosi dobrodziejstwo i rodzi wielkie możliwości. Pozwala w spokoju przemyśleć i przeanalizować swoje cele oraz ustalić plan działania. Nie należy jednak tak pogrążyć się w idyllicznym spokoju, aby popaść w stan nirwany na dłużej. Nie można odrywać się od świata i rezygnować z aktywnego wpływu na bieg rzeczy. Trzeba wykorzystać osiągnięty ład i pokój wewnętrzny, aby zrealizować wielkie przedsięwzięcia. Trzeba tylko zejść z nieba na ziemię, a wielkie się narodzi, przynosząc pozytywny rozwój wypadków.
	Kiedy ludźmi włada duch z niebios, również ich zmysłowa natura ulega jego wpływowi i znajduje właściwe dla siebie miejsce. Mali, słabi, pospolici są w trakcie odchodzenia, a wielcy, mocni, dobrzy — w ekspansji. Niesie to pomyślny los i powodzenie. Jest to czas nowego początku. Niewykluczone, że będzie się trzeba cofnąć o krok, aby potem zrobić dwa naprzód, ale nie należy się tym przejmować - idzie w dobrym kierunku. Nie należy tracić z oczu wytyczonego celu. Należy postępować uczciwie i być sprawiedliwym.
	Spośród dwóch żywiołów to, co jasne, jest wewnątrz, na decydującym miejscu w centrum, to, co ciemne - siła yin, jest zaś na zewnątrz. Siła yang jest wewnątrz, zatem jasność działa z całą swoją mocą, a ciemność jest jej powolna. W ten sposób obie strony czynią zadość swojej naturze.
	Czas obiektywny heksagramu: 20 II + 20 III, przedwiośnie.''', \
'1a':'''Wraz z kwiatem wyrywa darń. Podążanie naprzód przynosi powodzenie. ''', \
'1b':'''Początkiem ery Szangow stało się obalenie ostatniego władcy z dynastii Sia, tyrana Sia Ćje. - Odetnij się od kombinatorów i złoczyńców; kontakt z ludzkim nieszczęściem rodzi depresję i niepokój. Usuń podobnych ludzi ze swego życia, jak wyrywa się chwasty. Rezultat będzie korzystny. Zrób generalne porządki w swoim otoczeniu. ''', \
'2a':'''Wyrozumiały wobec słabszych. Zdecydowanie przekracza rzekę. Pamięta o tych, co są daleko. Nie ogląda się na towarzyszy, unikając stronniczości. Podąża środkiem. ''', \
'2b':'''Sprzyjający moment, aby przezwyciężyć własne słabości, zacząć energicznie działać i w ten sposób wyruszyć ku sukcesom. Gdy wszystko jest poukładane, a sprawy mają się dobrze, czas spokoju powinno się wykorzystać na nauczanie ludzi prostych. Nie będzie to czas stracony. Gdy nadarzy się szansa, należy podjąć ryzykowną aktywność, nie zatracając dalekosiężnego celu działania. Nie należy kierować się układami ani interesami; podążać drogą środka, zachowując równowagę między elastycznością a stałością.
Zbieraj niewykształconych ludzi ze wszystkich stron. Nie zaniedbuj kompetentnych, którzy żyją daleko od ciebie. Posłuż się tymi, którzy potrafią przeprawić się przez rzekę bez łodzi. Być może będzie trzeba pominąć niektórych przyjaciół. Postępuj sprawiedliwie. Taka była strategia pierwszych władców z dynastii Szang. Gwarancją sprawiedliwości społecznej było danie wszystkim równych szans na uzyskanie stanowiska w administracji państwowej. Nie faworyzuj nikogo. Wybierz osoby, którym naprawdę warto zlecić wykonanie danego zadania. Oto cechy dobrego przywódcy.''', \
'3a':'''Naruszony pokój. Każda równia ma swój stok.
Nie ma powrotu bez odejścia. Przetrwaj w trudnym czasie, unikając pomyłki. Nie użalaj się na ten fakt. Szczerość przyniesie szczęście.''', \
'3b':'''Zmiany przeistaczają świat zgodnie z odwiecznym prawem Natury. I dobrobyt kiedyś się kończy. Sytuacja może być trudna, ale zachowując niezłomność ducha trzeba ją przetrwać. W ten sposób nie utraci się kontroli nad losem. Lud Szangów, jak każda nacja, przeżywał na zmianę okresy pokoju i dobrobytu oraz niepokojów i niezgody. Dzięki wytrwałości, pozytywnemu nastawieniu i szczerości po złych dniach nastaną dobre. Nie załamuj się w trudnych okresach. Ciesz się dobrymi. ''', \
'4a':'''Trzepocze się jak ptak. Nie polega na swoim bogactwie; razem ze swoimi sąsiadami, bez przebiegłości i szczery. ''', \
'4b':'''Waha się w niepewności. Jest poruszony i zaniepokojony, drży jego nerwowo bijące serce. Ma coś wartościowego, ale w tym przypadku nie można się na tym opierać. ''', \
'5a':'''* Władca wydaje córkę za mąż. Najwyższe powodzenie. ''', \
'5b':'''Choć na dworze zajmuje wyższą pozycję, żona jest posłuszna mężowi. Prawo naturalne powinno być ważniejsze niż ustanowione.
Dzięki temu władca uzyskuje wpływy na obcym gruncie. Bardzo fortunna. ''', \
'6a':'''Mury zamku kruszą się i wpadają do fosy. Nie korzysta z pomocy armii; z tego miasta obwieszcza swoje prawo do panowania. Powiadamia sprzymierzeńców. Determinacja jest niepokojąca. ''', \
'6b':'''Nadchodzą wielkie sukcesy. Symbolizuje je zdobycie miasta, które zapewne zdobyto fortelem, używając sprzymierzonych sił wewnątrz miasta. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram12 = {'title':'SEPARACJA', \
'ctitle':'P’I', \
'picture':'''Niebo i Ziemia rozchodzą się. Oddzielenie. Zastój. Stagnacja. Zatrzymanie. Wybraniec unika kłopotów, wycofując się i ukrywając swoje zalety. Nie przyjmuje gratyfikacji. ''', \
'judgment':'''Źli ludzie nie sprzyjają, czynią trudności. Poszukiwanie porozumienia z zepsutymi ludźmi nie służy Nieskazitelnemu. Uniemożliwia zachowanie własnej drogi. Wielkie zanika, małe się rodzi. ''', \
'interpretation':'''	Trzeba powstrzymać swoją aktywność, gdyż zmierza w złym kierunku. Gdy niebo i ziemia zdążają w przeciwnych kierunkach, powiązania w świecie spraw ludzkich ulegają destrukcji. Zgodność nieba i ziemi wyrażana przez niezmienną zasadę synchronizacji i łączenia dwóch światów zostaje zagubiona, a związki między nimi zerwane. Jasność zamienia się w ciemność. Władzę przejmują zdemoralizowani ludzie, odsuwając zacnych. Nie powinni oni bronić swych pozycji, walcząc mieczem szlachetnych zasad, bo to nic nie da w świecie niegodziwców. Nie zrozumieją ich intencji i nie ulegną wpływom dobra. Nie jest to czas patriotów. Trzeba wycofać się, zachowując wierność sobie i poczekać na właściwy moment.

Czas obiektywny heksagramu: 20 VIII + 20 IX, nadejście jesieni.''', \
'1a':''' Razem z dzikim kwiatem wyrywa darń. Niezłomność przynosi poprawę. Pomyślna.''', \
'1b':''' Usuwając chwast, zatrzymuje się złe oddziaływania z nim związane. Należy zdecydować się na pierwszy krok i pozbyć się niechcianych wpływów.''', \
'2a':'''◆ Cierpliwy i wytrzymały. Dobrodziejstwo dla prostaka. Dla wielkiego człowieka negatywne. Separacja sprzyja nieskazitelnemu osiągnąć powodzenie.''', \
'2b':'''Wycofanie się z sytuacji pozwala zachować właściwą ścieżkę i odnieść sukces. Człowiek słaby jest szczęśliwy znosząc poddaństwo.
Człowiek zacny cofa się w wewnętrzny świat swoich cnót, nawet gdy jest to dla niego bolesne. ''', \
'3a':'''Upokorzony przez swoje zamiary. Smutek. ''', \
'3b':'''Chce zrobić coś, co skończy się dlań niechlubnie. To jest ostrzeżenie przed niewłaściwym działaniem. Na pewno skończy się to żałośnie. Niech się powstrzyma. ''', \
'4a':'''Działa według woli nieba. Bez winy. Nadchodzą przyjaciele, by budować z nim dom. ''', \
'4b':'''Nadchodzi kres separacji. Swoje powołanie do przywrócenia rzeczywistego, pierwotnego porządku wszechświata Nieskazitelny musi opierać nie tylko na wewnętrznym przekonaniu, czując za sobą poparcie niebios, ale musi mieć autentyczne poparcie sojuszników.
Czas mu sprzyja. Wszyscy popierać będą jego poglądy. ''', \
'5a':'''* Przemaga cierpienia i trudności. Fortuna dla wybrańca. „Co będzie, jeśli się nie uda? Co będzie, jeśli się nie uda?” Przywiązuje się do konaru dębu. Wychodzi na dobre człowiekowi honoru. Solidarność zwycięży. ''', \
'5b':'''Światełko w tunelu. Nadchodzi czas zmiany i aktywności; pojawił się przywódca, który ruszy sprawy naprzód, ale przyszłość pozostaje niepewna. Aby odnieść sukces, potrzeba wielkiej przezorności i mocnej podpory, na której można oprzeć działanie. ''', \
'6a':'''Koniec separacji. Najpierw rozłączenie, potem radość. ''', \
'6b':'''Trzeba mieć świadomość, że separacja też kiedyś ma swój kres, ale należy wspomóc jej zakończenie, przezwyciężając ją celowymi działaniami, gdyż inaczej będzie się utrzymywać. Wysiłek włożony w pracę nad problemami sprawia, że pokonane zostają cierpienia i trudności. Wtedy najgorsze już mija. Odtąd można spodziewać się coraz lepszego losu. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram13 = {'title':'Wspólnota w otwartej przestrzeni', \
'ctitle':'Tong żen', \
'picture':'''Ogniska płoną pod gwieździstym niebem.
Wspólnota z ludźmi.
Wybraniec układa rody i rzeczy zgodnie z ich wartością. ''', \
'judgment':'''Wspólnota w przestrzeni sprzyja osiągnięciu szczęścia.
Sprzyjające będzie przekroczyć wielką wodę. Korzystne jest, by wybraniec realizował swój plan. Odniesie sukces. ''', \
'interpretation':'''	Autentyczna wspólnota nie opiera się na wspólnocie egoistycznych interesów, ale na wspólnym związku z Jednią i działaniu zgodnie z prawdziwą naturą świata. Tylko wtedy, gdy wszystkie zaangażowane strony widzą swoje miejsce w związku ze wszystkim, możliwe jest osiągnięcie szczęścia. Prawdziwa, oparta na takich głębokich wartościach wspólnota, to taka integracja jednostek, która pozwala podjąć wielkie zespołowe działania we wspólnym interesie. Życie w autentycznej jedności nie polega na mieszaninie indywidualnych cech, ale na wspólnym punkcie widzenia i zgodzie na konieczną organizację struktur społecznych. Wspólnota pozwala odnaleźć poczucie przynależności do wielkiej rodziny ludzkiej i odsunąć ewentualne niebezpieczeństwo poprzez wewnętrzną integrację zaangażowanych osób. Wspólnota z ludźmi znajduje miłość.
	Powinieneś zgromadzić swoich ludzi w ustronnym miejscu i tam przygotować się do działań. Musisz zapewnić sobie wsparcie i uformować przymierza szybko i po cichu. Jeśli dobrze się przygotujesz, twój zamysł się spełni. Bądź gotów na wielką przygodę. To jest jak przekraczanie Rubikonu. Ale uważaj: nie możesz się spospolitować - powinieneś wspólnotę zorganizować według określonego porządku.''', \
'1a':'''Wspólnota u wrót. Bez winy. ''', \
'1b':'''Jest jasny, silny i wolny od egoizmu. Aby wspólnota mogła realizować cele, wszyscy muszą mieć takie same prawa, a plany działań muszą być znane wszystkim jej członkom. To sprzyja integracji grupy. Należy unikać niejasnych i tajnych powiązań prowadzących do rozpadu i dezintegracji społeczności. Tu jeszcze można się wycofać. ''', \
'2a':'''* Wspólnota w świątyni przodków. Niepokój. ''', \
'2b':'''Czas przed bardzo ważnym działaniem. Wspólnota zbiera się, aby uzyskać błogosławieństwo. Na tym etapie nie można się już wycofać. Stąd wyrusza się w nieznane, dlatego odczuwane jest zaniepokojenie. ''', \
'3a':'''Zrezygnowanie ukrywa to w kniei i wspina się na wysoką górę. Przez trzy lata to się nie podniesie. ''', \
'3b':'''Przeszkody są zbyt duże. Okazuje się to nie takie proste. Przedsięwzięcie, które wydawało się łatwe, proste i szybkie, na skutek komplikacji tutaj rozciąga się na dłuższy czas. ''', \
'4a':'''Wstępuje na mury gotów do walki, ale nie atakuje. Powodzenie. ''', \
'4b':'''Odpowiednio szacując swoje siły, uświadamia sobie swoją przewagę i powstrzymuje się od konfrontacji. Właściwa taktyka to elastyczność i umiarkowanie w działaniu, które sprzyjają sukcesowi. Wtedy można pokonać mury nieufności, które jeszcze istnieją w świadomości - do porozumienia już niedaleko. ''', \
'5a':'''* Włączony do wspólnoty najpierw płacze, potem się śmieje. Odnoszą wspólny sukces i spotyka się z przywódcą. ''', \
'5b':'''Dokonał razem z partnerami czegoś wielkiego. Połączył się z innym w silnym, płynącym z głębi serca związku, pokonawszy wiele trudności po tym, jak rozdzieliły ich nieporozumienia. Jest członkiem wspólnoty co, wbrew początkowym obawom, daje mu więcej wolności i radości, niż miał przedtem. ''', \
'6a':'''Wspólnota na przedmieściach. Nie ma winy. ''', \
'6b':'''Wspólnota, w której jesteś, jest wspólnotą idei. Połączyłeś się z ludźmi, z którymi łączy cię miejsce, gdzie przebywacie. Jesteście odcięci od reszty społeczeństwa, ale żal i poczucie winy znikają, gdyż wasze położenie was jednoczy. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram14 = {'title':'Wielka nagroda', \
'ctitle':'Ta yu', \
'picture':'''Ogień na niebie. Tłum i wielkie bogactwo.
Wybraniec daje odpór złu i wspiera dobro, będąc posłusznym woli i porządkowi niebios. ''', \
'judgment':'''Wielka nagroda rodzi twórczą siłę i powodzenie. Najwyższe szczęście. Obfitość i powodzenie bez przeszkód. ''', \
'interpretation':'''	Rzeczy przypadają komuś w udziale. Nagroda w postaci bogactwa nie pojawia się sama z siebie. Wyznacza ją linia losu będąca w zgodzie z właściwym czasem i ładem Nieba oraz udziałem we właściwej wspólnocie. Łagodność, pokora i brak pazerności sprzyjają osiągnięciom w świecie materialnym. Należy powstrzymywać się od złych myśli, a pielęgnować dobre. Wtedy osiąga się moc, którą można kontrolować, dzięki czemu uzyskuje się jej dobroczynny wpływ na bieg rzeczy. Chciwy i pożądający dóbr materialnych nie osiągnie bogactwa.
	Jeśli będziesz szlachetny, zgromadzi się wokół ciebie grupa zwolenników. Jest to okres wspaniałych osiągnięć i pomyślności. Twoja praca zostanie zauważona i doceniona. Nie pozwól jednak, by sukces uderzył ci do głowy. Przyjmij nagrodę, gdy przyjdzie, z pokorą.''', \
'1a':'''Strzegąc się zła, nie zrobi błędów. Jeśli będzie uważał na zagrożenia i trudności, uniknie pomyłek na końcu swej drogi. ''', \
'1b':'''Zbierasz dobra materialne. Na razie unikasz problemów, nie mniej one i tak się pojawią. Twoje bogactwo będzie kłuło w oczy zazdrośników, a ty będziesz musiał chronić swoje dobra. Powinieneś mieć to na uwadze i nie działać wbrew swoim zasadom. Uważaj, aby nie pochłonęło cię twoje poczucie ważności. Strzeż się pychy, zuchwałości i rozrzutności. ''', \
'2a':'''Wielki załadowany wóz. Fortunna, w jakimkolwiek kierunku pójdzie. ''', \
'2b':'''Bogaty jest nie ten, kto tylko posiada bogactwo, ale ten, kto go używa w dobrym celu. Nieważne, ile masz, ważne, czy i na co wydajesz. ''', \
'3a':'''Książę ofiaruje to Synowi Niebios. Prostak temu nie podoła. ''', \
'3b':'''Wielki człowiek nie utożsamia się ze swoim bogactwem. Potrafi poświęcić swoje skarby dla dobra wielkiej sprawy. Mały człowiek tego nie potrafi, bo przywiązany jest do swych dóbr. Dlatego bogactwo go zniewala. Krzywdzi tym siebie, gdyż starania o te dobra więzią jego myśli, czyniąc z niego człowieka ociężałego. Prostak nie potrafi unieść ciężaru bogactwa. ''', \
'4a':'''Porównuje siebie z sąsiadem. To nie jest pełnia. Bez winy. ''', \
'4b':'''Trudno dorównać silnym i bogatym sąsiadom. Kto przecenia swoją wartość, daje się ponieść zawiści i pysze. Nie rób tego. ''', \
'5a':'''* Wzajemne zaufanie. Czyja prawda prosta jest, a jednak dostojna, ten ma pomyślny los.
 ''', \
'5b':'''Jeśli nie posiadasz mocy, nie musisz być słabym. Bogactwo można uzyskać przez prostolinijność i szczerość oraz współpracę z silnymi i wytrwałymi. ''', \
'6a':'''Przychylność niebios. Wszystko sprzyja. ''', \
'6b':'''Osiągnął pełnię potęgi i bogactwa. Niech teraz poszuka mędrca i stanie się uczestnikiem jego mądrości. Gdy odkryje jego skarb zrozumie, że Niebo pomaga tylko temu, kto jest niezłomny w swoich dążeniach, i że wszystko zależało od niego samego. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram15 = {'title':'Umiarkowanie', \
'ctitle':'Kian', \
'picture':'''Góra w środku ziemi. Skromność i umiar.
Wybraniec pomniejsza to co wielkie i powiększa to co małe, doprowadzając wszystko do właściwych wymiarów. ''', \
'judgment':'''Umiar prowadzi do sukcesu. Człowiek umiarkowany doprowadza sprawy do pożądanego finału. ''', \
'interpretation':'''	Umiarkowanie to skrywana wielkość. Człowiek umiarkowany, będąc na szczycie hierarchii społecznej, nie okazuje swojej wielkości, pozostając skromnym, dzięki temu zachowuje swoją pozycję i uzyskuje jasny wgląd w rzeczywistość. Jeżeli jest umiarkowany, zajmując niższe miejsce w hierarchii, zostanie dostrzeżony i nagrodzony. Cnota umiarkowania pozwala osiągnąć wyznaczony cel.
	Wywyższanie się ponad poziom własnego działania jest nieskromne. Jeżeli istnieje jakieś działanie, do którego szczególnie się nadajesz, nie rozkoszuj się nim, nie rób planów, nie fantazjuj. Jest to dar od Boga. Po prostu zajmij się tym.''', \
'1a':'''Pokorne umiarkowanie. Możesz przekroczyć wielką wodę. Pomyślna. ''', \
'1b':'''Gdy umiarkowanie jest częścią twojej istoty i potrafisz zachować umiar w każdych okolicznościach, możesz podjąć niebezpieczne działania. ''', \
'2a':'''Wołające umiarkowanie. Niezłomność przynosi sukces. ''', \
'2b':'''Umiar w czynach a nie tylko w słowach, zawiera moc wynikającą ze zrozumienia zasad funkcjonowania świata. To przywołuje podobne.
Gdy ktoś tak postępuje, dostrzegają to inni. Dlatego obdarzają go zaufaniem i mogą na nim polegać. ''', \
'3a':'''* Znojne umiarkowanie nagrodzone. Wybraniec doprowadza sprawy do szczęśliwego końca. Osiąga sukces. ''', \
'3b':'''Postępując z umiarem, zostaje nagrodzony, choć trzeba się przy tym natrudzić. ''', \
'4a':'''Fałszywa skromność. Nie ma nic niepomyślnego. ''', \
'4b':'''Wszystko ma swoje granice, także skromność. Nie można w niej przesadzać i nie ma sensu dalej kultywować skromności, gdy wielkość jest już dostrzegana. ''', \
'5a':'''Nie obnosi się bogactwem przed sąsiadem. Należy zaatakować i użyć siły. Wszystko sprzyja. ''', \
'5b':'''Umiarkowanie to nie słabość ukryta pod maską dobra, która pozostawia sprawy własnemu biegowi. Umiarkowanie to spokój wewnętrzny wynikający z wiedzy. Teraz wiesz, że musisz działać energicznie i zdecydowanie, wczuwając się w rolę przywódcy. Sytuacja tego wymaga. ''', \
'6a':'''Wołające umiarkowanie. Należy użyć armii do podporządkowania własnych ziem. ''', \
'6b':'''Prawdziwe umiarkowanie wyraża się w odpowiednim stosunku do poczucia własnej ważności i we właściwym postępowaniu. W chwilach konfliktów z partnerami i bliskimi osobami nie należy zrzucać winy na nich, ale ujawnić wspólne błędy, co będzie wyrazem pokory.
Gdy to nie wystarczy, musisz użyć siły, by zaprowadzić porządek, chociaż miałbyś być wobec nich surowy. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram16 = {'title':'Entuzjazm', \
'ctitle':'Yu', \
'picture':'''Brzmi uderzenie gromu. Drży ziemia.
Zadowolenie. Przygotowanie.
Starożytni królowie wysławiali cnoty i zasługi bohaterów muzyką i składali je w ofierze Najwyższemu, wzywając do uczestnictwa swoich przodków. ''', \
'judgment':'''Gotowość. Korzystne jest zmobilizować siły i działać. ''', \
'interpretation':'''	Pojawia się przywódca potrafiący poprowadzić żołnierzy do walki w odpowiednim momencie i tchnąć w nich poczucie siły i zadowolenia. Ponieważ pozostaje w zgodzie z duchem czasu i cieszy się poparciem otoczenia, niech nie obawia się opozycji, może podjąć każde ryzyko. Potem odda cześć temu, który jest przyczyną wszystkiego i w którym się wszystko zawiera. Jeśli zaniecha działań, skończy się bezwładem.
	Gdy pojawia się entuzjazm, należy energicznie i zdecydowanie działać. Uderzenie gromu sygnalizuje: czas jest właściwy, teraz można w pełni wykorzystać posiadaną moc. Bóg jest z nim. Entuzjazm pojawia się, gdy świat natury i świat człowieka są zsynchronizowane i łączy je harmonia. Sprzyja temu właściwa postawa moralna. Zawsze należy działać w zgodzie z naturą rzeczy, która manifestuje się w wiecznym ruchu spraw. Przywiązanie do tradycji i wewnętrzne cnoty przejawiają się w entuzjazmie, który gromadzi zwolenników. Tak wódz zbiera posiłki przed bitwą.
	Władca, który czci (muzyką) boskość we własnych przodkach, staje się przez to Synem Niebios, w którym świat niebiański i świat ziemski łączą się w mistycznej unii. To jest najwyższe podsumowanie chińskiej kultury.
	„Kto by tę ofiarę w pełni zrozumiał, ten mógłby rządzić światem, jak gdyby ów na jego dłoni się obracał”. (Kung Fu Tsy)''', \
'1a':'''Zadowolony sam z siebie. Złowróżbna. ''', \
'1b':'''Należy uważać na arogancję. Przesadna pewność siebie po początkowych sukcesach prowadzi do spoczęcia na laurach i do zmniejszenia czujności, co pozwoliłoby przeciwnikowi przeprowadzić niespodziewany atak. Należy zachować czujność i być sumiennym przez cały czas. ''', \
'2a':'''Niewzruszony jak skała. Umie przewidywać. Niezłomność przynosi powodzenie. ''', \
'2b':'''Nie żywiąc iluzji entuzjazmu towarzyszy, nie daje się im pociągnąć.
Umie bezbłędnie odczytać znaki czasu, aby w porę wycofać się wobec niesprzyjającej zmiany, która może nadejść. ''', \
'3a':'''Śpiewa z entuzjazmem. Nadmiar emocji. Żal. ''', \
'3b':'''Za duże zadowolenie z siebie. Kto zbytnio ufa własnym siłom, zapominając o tym, kto naprawdę rządzi, ponosi w istocie porażkę. ''', \
'4a':'''* Źródło entuzjazmu. Dokonuje wielkich czynów. Bez wątpliwości. Nadchodzą przyjaciele. ''', \
'4b':'''Wierzy we własne siły, wolny od wątpliwości staje się pewny siebie i zdecydowany w działaniu, czym budzi entuzjazm otoczenia. Dzięki zaufaniu otoczenia otrzymuje wielką pomoc. Ludzie garną się do niego. Tak trzymać! ''', \
'5a':'''Jest chronicznie chory, ale nie umiera, żyjąc na granicy śmierci. ''', \
'5b':'''Presja, jakiej był poddany, sprawia, że dochodzi do martwego punktu. Jego swoboda ruchów jest bardzo ograniczona, a wewnętrzny entuzjazm i zadowolenie nie mogą się ujawnić. Dzieje się tak, gdyż trapią go pewne problemy i ograniczenia. ''', \
'6a':'''Uwodzicielski urok entuzjazmu. Nadchodzi przemiana. Nie pomyli się, gdy porzuci swoją ścieżkę, kiedy osiągnie kres. ''', \
'6b':'''Kto da się zwieść entuzjazmowi, będzie miał problemy. Powinien w porę zdać sobie sprawę z ułudy, w której się pogrążył i wycofać się. Dzieje się tak, gdy pogoń za przyjemnościami nie zna granic.
Ekstaza na dłuższą metę jest bardzo szkodliwa, grozi nawet śmiercią. Jeżeli potrafi zrezygnować i potraktować swoją ekstatyczną pasję jako pouczające doświadczenie, zapobiegnie nieszczęściu. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram17 = {'title':'Naśladowanie', \
'ctitle':'Sui', \
'picture':'''Piorun w chmurach. Pójście śladem.
Następstwo. Przystosowanie.
Wieczorną porą wybraniec zajeżdża do domu na odpoczynek, by zregenerować siły. ''', \
'judgment':'''Najwyższe powodzenie. Jeżeli naśladuje właściwie, wtedy nie ma błędu. Sprzyjająca jest wytrwałość.
Korzystne jest zachować stałość i prawość do samego końca. Tak podąża za kimś cały świat. ''', \
'interpretation':'''	Póki nie pozna siebie, nie nauczy się wybierać. Póki nie nauczy się wybierać, nie dorośnie. Póki nie dorośnie, niczego nie osiągnie.
	By stać się przykładem dla innych, sam musi najpierw odnaleźć swój wzór do naśladowania. Gdy chce rządzić, niech nauczy się służyć; gdy chce pomagać, niech nauczy się wymagać; gdy chce kochać i być kochanym, niech nauczy się słuchać i dawać. Należy odnaleźć właściwe źródło inspiracji, a podążanie za nią musi być wytrwałe.
Kto podąża właściwym śladem, niech spodziewa się nagrody.
	Po okresie ciężkiej pracy, by znaleźć spokój i odpoczynek, tak jak w czasie zimowej ciemności i odpoczynku natury, człowiek powraca do siebie, do środka. To jest jego schronienie i nie należy szukać innego. Pozostaje sam u siebie, ponad wszystkim; to jest jego skarb. W takim odpoczynku hartują się siły do nowych przedsięwzięć.''', \
'1a':'''Zmienia chorągiew. Urząd zapewne powiadomi. ''', \
'1b':'''Wyjście poza bramę, aby spotkać się z innymi da pomyślne wyniki. Determinacja sprzyja.
Porzuca dotychczasowy sposób postępowania, gdy nie może spełnić oczekiwań. Zmienia swoją taktykę, pozostając jednakże wierny sobie. Dobrze jest dołączyć do ludzi, którzy też myślą inaczej. ''', \
'2a':'''Idzie za chłopcem. Pozostawia mężczyznę. ''', \
'2b':'''Człowiek słaby nie rezygnuje ze znajomości, nawet gdy mu szkodzą. Nie potrafi podjąć męskiej decyzji. Boi się i nie wie, że siła ma swoje znaczenie i należy umieć się nią posługiwać. Zachowuje się jak dorosły, choć w środku jest dzieckiem. Naśladując w ten sposób, traci kontakt z rzeczywistością i zatraca się w świecie złudzeń. ''', \
'3a':'''Idzie za mężczyzną. Pozostawia chłopca. Korzystna jest wytrwałość. Sprzyjające, aby zadecydować o miejscu zamieszkania. ''', \
'3b':'''Człowiek silny potrafi wybierać. Wie, że zawsze coś jest za coś i każdy wybór polega na rezygnacji z czegoś. Należy szukać kontaktu z ludźmi doświadczonymi, a zaprzestać kosztownych znajomości z młodymi, nowicjuszami, choć może to wywołać poczucie straty. Nie można tego uniknąć; trzeba się z tym pogodzić i wytrwać w swojej decyzji. W ten sposób niedoświadczeni zrezygnują z twojego towarzystwa. Tak zyskuje się moc. Dobrze jest podjąć decyzję co do miejsca pobytu, co może znaczyć przeprowadzkę, zmianę miejsca pracy, zmianę otaczających ludzi, środowiska, itp. ''', \
'4a':'''Przyciąga naśladowców. Niezłomność przynosi nieszczęście. Odwołując się do swoich intencji, uzyska jasność. Jaka może być w tym wina? ''', \
'4b':'''Jest wzorem do naśladowania dla innych, którzy widzą w nim człowieka silnego. Może jest silny, choć mogą to być tylko pozory. Taka siła przyciąga prostaków, którzy manipulują pochlebstwem i gotowością oddania, mając na względzie jedynie własne korzyści. Nie są szczerzy i nie będzie można na nich polegać. Niech zapyta siebie, czy jego intencje są szczere i czy ma dość mocy, by być wzorem. ''', \
'5a':'''* Jest nieskazitelny. Powodzenie. ''', \
'5b':'''Człowiek powinien mieć kogoś, kto będzie dla niego wzorem do naśladowania, swojego guru. Jeśli podąża śladem dobra na ścieżce serca, nabiera poczucia mocy i staje się piękny dla innych, zapewniając sobie szczęśliwe życie. ''', \
'6a':'''Uwiązanie w przywiązaniu. Król składa ofiary w zachodnich górach. ''', \
'6b':'''Jest bezkrytyczny. Przywiązuje się do niesprawdzonych, obcych idei. Ważna jest dla niego jego pozycja, a nie sens tego, co robi.
Tańczy, jak mu zagrają, i nie ma własnej woli. Takie naśladowanie jest bezsensowne. Złóż ofiarę w intencji uwolnienia się. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram18 = {'title':'Naprawianie zniszczeń', \
'ctitle':'Ku', \
'picture':'''Wiatr wieje u podnóża góry. Zniszczenie. Rozpadanie się.
Wybraniec budzi ludzi, wstrząsając nimi, i wzmacnia ich ducha, nabierając pewności siebie. ''', \
'judgment':'''Naprawianie zniszczeń przynosi najwyższe szczęście.
Powodzenie bez przeszkód. Korzystne jest przekroczyć wielką wodę. Trzy dni przed przemianą. Trzy dni po przemianie. ''', \
'interpretation':'''	Ku oznacza zepsucie, ale też czarną magię. Zastane przedsięwzięcie toczy wewnętrzna zgnilizna. To, co zepsute, nie jest wynikiem fatum, ale nadużycia wolności. Należy porzucić fałsz i wrócić do dobra. Zbyt długie tolerowanie zła powoduje pogrążanie się w nim. Wynika to z braku wewnętrznej ostoi, na której można się oprzeć i która pozwala na właściwy osąd rzeczy. Należy wniknąć w siebie i odnaleźć jądro swoich autentycznych zasad. Pozwoli to na przyjęcie jednego punktu widzenia. Należy się go trzymać. Kto zawsze ma ambiwalentny stosunek do różnych rzeczy, nie jest w stanie zająć własnego stanowiska i właściwie ocenić sytuacji. Gdy wewnątrz jest przeciw, pozorna zgoda, jaką wyznaje, prowadzi do hipokryzji, która na dłuższą metę szkodzi każdemu. Naprawianie zniszczeń i powrót do dobra to dążenie do jedności myśli i czynów; autentyczność świadomości i aktywności niepowodowanych wysiłkiem woli, ale odczuciem przenikającej wszystko jedności; porzucenie zła to odejście od nabytej dwulicowości; to powrót do pierwotnej natury Buddy, która w człowieku została zafałszowana. Wymaga to wytrwałości i nieustępliwości w dążeniu do celu. Można rozpocząć działanie, ale wymaga to dogłębnej analizy zarówno przed początkiem aktywności, jak i czas jakiś po rozpoczęciu działania. Wtedy nowe zastąpi zepsute stare. Gdy już się naprawi, będzie porządek.
	Trzy dni przed rozpoczęciem i nowym początkiem wykorzystaj na oczyszczenie umysłu, ciała i ducha; pomódl się i pomedytuj. W ciągu trzech dni po przemianie wprowadź nowe zasady i ustal nowe cele.''', \
'1a':'''Naprawia to, co zniszczył ojciec. Na tym polega mądrość syna. Skoro jest syn, na [zmarłym] ojcu nie ciąży ujma. Jeśli mu się uda, zmaże winę ojca. W swych myślach przyjmuje ojca. Zagrożenie. W końcu fortunna. ''', \
'1b':'''Ojciec pozostawia mu dzieło, którego fundamenty są stałe, w czym jest zasługa ojca. Ale przedsięwzięcie toczy zepsucie. To sztywne trzymanie się tradycji powoduje zepsucie. Jednak gdy zepsucie nie jest wielkie, nietrudno naprawić szkody. Należy zreformować i odnowić tradycję i zasady tak, aby nie zniszczyć dawnych wartości. Reformując strukturę systemu, trzeba być ostrożnym, szczególnie na początku, gdyż początek zdecyduje o dalekosiężnych skutkach. Dlatego reforma musi być przemyślana. ''', \
'2a':'''Naprawia to, co zniszczyła matka. Hipokryzja nie przynosi szczęścia. ''', \
'2b':'''Uległość i bierność w nadmiarze powodują słabość. Nie wolno tego nie dostrzegać. Można naprawić zło spowodowane taką słabością, ale trzeba uważać, by nie znaleźć się na drugim biegunie, popadając w nadmierną stanowczość, pryncypialność i surowość. ''', \
'3a':'''Naprawia to, co zniszczył ojciec. Lekkie wyrzuty sumienia, niewielki błąd. ''', \
'3b':'''Nie należy nadużywać mocy w naprawianiu. Zanadto intensywne naprawianie starych błędów może powodować niesnaski i nieporozumienia. Jednak korzystny wynik działania usprawiedliwia brak taktu. ''', \
'4a':'''Toleruje to, co zniszczył ojciec. Tak ściąga na siebie pogardę innych. Pożałuje, jeżeli nie zejdzie ze swojej ścieżki. ''', \
'4b':'''Kto przymyka oczy na szkody spowodowane błędami przeszłości, pozwala, aby się powiększały. Nie należy chować głowy w piasek i trzeba czym prędzej podjąć działania naprawcze. Chodzi tu o proces wewnętrznej przemiany, która kogoś niesamodzielnego zmienia w niezależną, samodzielną, świadomą jednostkę. Dojrzewanie połączone jest zawsze z kłopotami i cierpieniami, i z tym trzeba się liczyć. Kto jest słaby, pozostaje ustępliwy i wyrozumiały, co przynosi żal i wstyd. ''', \
'5a':'''* Naprawia to, co zniszczył ojciec. Używa wozu.
Los go nagradza. ''', \
'5b':'''Szkody spowodowane błędami ojca są najtrudniejsze do naprawiania. Dlatego należy z uporem dążyć do ich usunięcia, mając na uwadze, że ci którzy widzą te błędy, są świadomi swojego w nich współudziału. Ich życzliwość będzie sprzyjać. Szukaj u nich poparcia. Takie działanie przynosi chlubę. Jeśli chcesz naprawić sytuację, musisz najpierw uzyskać reputację człowieka honoru. Użyj wszelkich swych sił, umiejętności i możliwości. ''', \
'6a':'''Nie służy królom ani książętom. Oddaje się wzniosłym celom. ''', \
'6b':'''Człowiek rezygnuje z niszczących związków w świecie materialnym, świecie celów i pragnień. Jest ponad to, pokonał swoje ambicje i nierealne aspiracje. Jednak nie lenistwem, pychą, czy obojętnością. Teraz dąży do najwyższych z ludzkich celów, chce osiągnąć doskonałość i dlatego jego poczucie wyższości jest właściwe. Nie pracuje dla jednej tylko epoki, lecz dla całego świata i wszystkich czasów.

Co pewien czas na świat przychodzi niezrównany mistrz, przewodnik zbłąkanych ludzi, oświecony, Przebudzony, błogosławiony Budda, który rozumie wszechświat, bogów i ludzi i głosi swą naukę innym. Głosi słowo prawdy i jej ducha, prawdy pięknej w swej istocie i spełnieniu; opowiada o wyższym życiu, jego czystości i doskonałości. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram19 = {'title':'Przybywanie', \
'ctitle':'Lin', \
'picture':'''Ziemia ponad mokradłem. Las. Nieznane.
Wybraniec jest niewyczerpany w swoim zamiarze i gotowości nauczania ludzi; ma pieczę nad nimi i jest niezmiernie dla nich wyrozumiały. ''', \
'judgment':'''Najwyższe powodzenie bez przeszkód. Korzystna jest wytrwałość. Ktoś staje się wielkim. Niepomyślny los w ósmym miesiącu. ''', \
'interpretation':'''	Heksagram przedstawia sytuację i postępowanie w obliczu nieznanej, obcej rzeczywistości. Aby osiągnąć sukces w rzeczywistości, która rządzi się swoimi odrębnymi prawami, potrzebne jest dostosowanie się do jej swoistych wymagań. Można ją eksplorować, ale nie wolno naruszyć panujących tam stosunków. Tak można zostać ekspertem w obcej dziedzinie. Gdy jako znawca odrębnej rzeczywistości posiądzie się odpowiedni autorytet jako mistrz, można rozpocząć twórczy proces, który będzie tę rzeczywistość przekształcać. Wtedy świat będzie wzajemnie z nim współdziałał i zostanie w nim zrealizowane wszystko, co sobie życzy. Działanie wymaga determinacji i wykorzystywania wszystkich pojawiających się dogodnych sytuacji. Wymaga stałego procesu nadzoru nad rozkwitem przedsięwzięcia. Taka kontrola sprzyja rozwojowi obecnej koniunktury. Ponieważ proces twórczy odbywa się poprzez interakcje sił pozytywnych i negatywnych, należy zważać na pojawiające się zagrożenia. Mogą one szczególnie zaistnieć w ósmym miesiącu. Ważne jest baczyć na zdrowie i swój autorytet. Może nastąpić wstrząs, trudności lub kłopoty. Heksagram Przybywanie, tak jak heksagram Kontemplacja, po części daje, a po części bierze.
	Czas obiektywny heksagramu: 20 I + 20 II, środek zimy.''', \
'1a':'''* Przybywa do zakazanego lasu. Wzajemne zbliżenie. Sam zachęca do zbliżenia. Wytrwały na swojej ścieżce. ''', \
'1b':'''Na razie dostęp do świata, w który chcesz wejść, jest ci zabroniony i ten świat jeszcze nie będzie współdziałał z tobą. Nie martw się. Idee pojawiające się w twojej świadomości niedługo zaistnieją u innych. Nie trać z oczu swoich planów i nie bój się swojej pionierskiej roli w ich realizacji. Nie zgub swojego celu, choćby w tej chwili otaczający cię świat wydawał się niedostępny. Czekaj na właściwy moment i zbieraj swych zwolenników. ''', \
'2a':'''* Przybywa do zakazanego lasu. Wzajemne zbliżenie. Zachęcany do zbliżenia. Fortunna. Wszystko sprzyja. ''', \
'2b':'''Posiadasz dość siły osobistej. Twoje ugruntowane zasady i twoja wewnętrzna moc pozwalają na zbliżenie do wielkich potęg. Możesz podjąć realizację swoich planów. Zachęta płynie z góry. Zachowaj rozsądek. Nie daj się ponieść emocjom. Pomimo że dostęp do odrębnego świata jest zabroniony, to los będzie ci sprzyjał. Mimo zakazów i własnych oporów właśnie powinieneś wejść w obcy ci świat, gdzie osiągniesz powodzenie. ''', \
'3a':'''Czarujący las. Beztroskie zbliżenie. Nic nie przynosi korzyści. Jeśli ubolewa nad tym, nie popełni błędów. ''', \
'3b':'''Las jest przyjazny tylko pozornie, w istocie jest nieprzychylny i niezgłębiony. Jeśli wierząc bezgranicznie w swoje siły, zachowuje się nonszalancko w obliczu obcego obszaru rzeczywistości, popełnia błąd i obraca przeciwko sobie otoczenie. Nie uda się oswoić tej odrębnej rzeczywistości. ''', \
'4a':'''Przybycie do lasu. Nie ma zmartwień. ''', \
'4b':'''Otacza go przyjazna atmosfera wzajemnego porozumienia. Sytuacja wolna jest od napięć. Należy aktywnie wejść w ten nieznany obszar. Wykreowane związki wynikające z penetracji tej rzeczywistości będą sprzyjać osiągnięciu sukcesu. ''', \
'5a':'''Przybycie do lasu. Mądre zbliżenie. Fortunna. Postępuje rozsądnie, jak wielki włościanin. ''', \
'5b':'''Podstawą sukcesu w radzeniu sobie z odrębną rzeczywistością jest osiągnięcie wewnętrznej zgody z prawami tej rzeczywistości. Wielki włościanin pozwala swojej posiadłości żyć swoimi prawami i umiejętnie adaptuje się do niej do końca znanych sobie realiów. Kto włącza nieznane w swój zasięg, niech ma na względzie, że i on staje się częścią odrębnego świata. Niech odnosi się doń z należytym poważaniem. ''', \
'6a':'''Przybycie do gęstego lasu. Wspaniałomyślne zbliżenie. Powodzenie. Nie ma zmartwienia. ''', \
'6b':'''Odrębna, obca, rządząca się swoimi tajemniczymi prawami rzeczywistość pozostała nieodgadniona, niepoznawalna i niezgłębiona.
Taką należy ją pozostawić i uszanować, gdyż jest poza zasięgiem ludzkiego pojmowania. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram20 = {'title':'KONTEMPLACJA', \
'ctitle':'Kuan', \
'picture':'''Wiatr wieje nad ziemią. Spoglądanie w górę. Obserwowanie. Rozważanie i analizowanie. Siła osobowości.
Starożytni królowie odwiedzali krainy świata i przyglądali się panującym obyczajom. Obserwowali lud i udzielali nauk. ''', \
'judgment':'''Wróżbita obmył ręce, ale nie śpieszy się ze złożeniem ofiary. Pogrąża się w głębokiej zadumie, tak aby ceremonia ofiarowania była doskonała. Patrzą na niego ufni, pełni szacunku. ''', \
'interpretation':'''	Przemyśl to. Jest to czas skupienia przed podjęciem ważnej decyzji. Uwaga koncentruje się na chwili Teraz. Chwila jest ważna, gdyż jest granicą między przyszłością a przeszłością. Przyszłość [niepewność przyszłości] decyduje o TERAZ ze względu na przeszłość. Człowiek skupia się i rozważa sprawy w zadumie. Rozpamiętuje miniony czas, mając na uwadze istotne wydarzenia. Dzięki temu może wniknąć w tajemnice świata i ujrzeć odwieczny porządek rzeczy. Ich znajomość pomaga skutecznie wpływać na bieg spraw. Medytacja pozwala zwalczać niecierpliwość i dobrze zastanowić się nad dalszą drogą. Wahanie o którym mowa w heksagramie dotyczy pozycji na jakiej najlepiej można wykorzystać swoje zdolności i ambicje i kroczyć ścieżką doskonałości. Należy ubiegać się o takie stanowisko, które najlepiej pasuje do umiejętności, pragnień i potrzeb. Trzeba uważnie obserwować potencjalnych wspólników lub partnerów, zanim się z kimkolwiek związywać. Należy dobrze przeanalizować sprawę: czy to, o czym myśli, jest naprawdę takie ważne i potrzebne? Spokojne przemyślenie spraw przywróci równowagę ducha. Niech nie podejmuje pośpiesznych decyzji, których potem mógłby żałować.
	Heksagram Kontemplacja, tak jak heksagram Przybywanie, po części daje, a po części bierze. Kontemplacja jest braniem, a nauka dawaniem.
	W kontemplacji Tao tego heksagramu zawarte jest osiągnięcie oświecenia.
	Czas obiektywny heksagramu: 20 IX + 20 X, równowaga jesienna — początek jesieni.
	Tao - droga, proces wszechświata - porządek przyrody. Tao to ostateczna, niemożliwa do opisania rzeczywistość, proces kosmiczny, który obejmuje wszystkie rzeczy, a charakteryzuje się nieustannym przepływem i zmianą. Odbywają się one w zgodzie ze stałymi wzorcami powracającymi cyklicznie.
	Ten, kto zgadza się z kierunkiem Tao, postępując za naturalnymi procesami nieba i ziemi, stwierdza, iż z łatwością może panować nad światem. (Huai Nan Tsy - II w. p.n.e.)''', \
'1a':'''Patrzy oczami dziecka. Prostaka wina nie dotyczy. Nieskazitelny doznaje upokorzenia. ''', \
'1b':'''Rozważa sprawy naiwnie jak dziecko. Gdy tak rozmyśla ignorant, nie ma w tym błędu. Jednak gdy tak postępuje mędrzec, przynosi mu to ujmę; powinien głęboko wnikać w sprawy i rozumieć ukryte mechanizmy rządzące światem. ''', \
'2a':'''Patrzy zerkając zza drzwi. Dla kobiety korzystna jest wytrwałość. ''', \
'2b':'''Kto ma zawężone pole widzenia, wszystko odnosi do siebie i ponieważ jego ogląd rzeczywistości jest ograniczony, nie jest świadomy uwarunkowań rządzących światem. Komu zwykłe, proste życie wystarcza, takie ograniczenie percepcji nie szkodzi. Nie ma w tym niczego złego. Gdy jednak ktoś preferuje życie aktywne i chce mieć wpływ na sprawy, takie podejście do rzeczy jest nierozsądne. ''', \
'3a':'''Kontempluje swoje życie i adekwatnie wybiera podążanie lub wycofanie się. ''', \
'3b':'''Medytacja i spoglądanie wstecz na swoje życie ma służyć samowiedzy; rzetelnej, obiektywnej i wolnej od osobistych iluzji ocenie skutków własnej aktywności. Sprzyja temu porzucenie wąskiego, egoistycznego punktu widzenia. Gdy tak postąpi, będzie mógł podjąć właściwą decyzję. ''', \
'4a':'''Kontempluje chwałę królestwa. Korzystna jest audiencja u władcy. ''', \
'4b':'''Patrzy wzwyż na blask państwa. Rozważa siebie względem czegoś większego niż on sam. Powinien swoimi umiejętnościami wspomóc królestwo, otrzymując odeń prerogatywy i możność samodzielnych decyzji. Powinien dążyć do osiągnięcia wpływowej pozycji. ''', \
'5a':'''* Kontempluje swoje życie. Nieskazitelny jest bez winy. ''', \
'5b':'''Tylko przez chwilę można podjąć właściwą decyzję. Trzeba uważać, by jej nie przegapić. Kto przewodzi, sam musi umieć w każdym momencie ocenić następstwa swojej aktywności. ''', \
'6a':'''* Kontempluje siebie i osądza. Nieskazitelny nie popełnia błędu. ''', \
'6b':'''Kto pojął proces kontemplacji, potrafi odróżnić wielkie i mądre od małego i głupiego. Nie będąc powiązany ze światem, mędrzec może zająć pozycję arbitra i osądzać innych. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram21 = {'title':'Przegryzanie', \
'ctitle':'Szi he', \
'picture':'''Grom i błyskawica. Przegryzanie.
Starożytni królowie egzekwowali kary stosownie do wykroczeń, czym nadawali świetność prawu. ''', \
'judgment':'''Przegryzanie zawiera w sobie zalążek powodzenia.
Sprzyjającym jest przeprowadzić sprawę sądową.
Wybraniec trzyma się obowiązującego prawa. ''', \
'interpretation':'''	Jest coś, co przeszkadza. Działaj energicznie, ale nie pochopnie.
Za sprawą kłamcy i hochsztaplera pojawiają się poważne problemy.
Strzeż się obłudy, zdrady i fałszu. Pod pozorem prawdy oszust wyrządza krzywdę. W takiej sytuacji nie można biernie czekać, trzeba stanowczo zareagować. Jeżeli jest to konieczne, należy znaleźć schronienie w instytucjach systemu społecznego. W uzasadnionych przypadkach można użyć nielegalnych metod by chronić swoje prawa. Gdy sytuacja dotyczy spraw osobistych, należy spodziewać się nieuczciwości i oszustwa partnera. Trzeba taki związek zdecydowanie przerwać. Nie należy jednak dać się ponieść emocjom i mścić się na winowajcy. Krzywdzi cię, gdyż twoje dwuznaczne zasady sprzyjają jego destrukcyjnej działalności. Nie powinny tobą kierować odruchy i wola zemsty, lecz wyższe zasady i poczucie sprawiedliwości.
Kiedy utrwalisz prawość swoich zasad, będziesz mógł wymierzyć stosowną karę temu, który chciał cię pognębić.

Heksagram dotyczy procesu karnego; mówi o ciężkich zmaganiach i przegryzaniu się przez przeszkody oraz karaniu przestępców. Trzeba dążyć do wyjawienia prawdy. Uważaj na podpisywane umów - jeśli nie jesteś ich pewien, nie podpisuj.''', \
'1a':'''Jego stopy w dybach. Traci duże palce u stóp. Bez winy. ''', \
'1b':'''Ktoś wykorzystuje twoją uległość. Należy go skarcić, tak jak karci się niesforne dziecko, nie dopuszczając by wyrządził większe szkody. Inaczej wejdzie ci na głowę.

Człowiek pospolity nie wstydzi się nieczułości i nieprawości się nie lęka. Jeżeli nie widzi, aby przyzywała go jakaś korzyść, nie ruszy się. Jeżeli go nie zastraszyć, nie poprawi się. Jednakże gdy w małych sprawach zostanie przywiedziony do porządku, także w wielkich będzie miał się na baczności. Oto szczęście dla człowieka pospolitego. ''', \
'2a':'''Gryzie miękkie mięso. Traci nos. Bez winy. ''', \
'2b':'''Wyrządzona mu krzywda jest ogromna i nieuzasadniona. Gotów jest, tracąc wyrozumiałość, popaść w przesadę i reagować z nadmierną surowością. Wzburzenie jest słuszne, a kara, którą chce wymierzyć, zasłużona. ''', \
'3a':'''Gryzie stare, wysuszone mięso. Natrafia na truciznę. Niewielkie upokorzenie. Bez winy. ''', \
'3b':'''Uwaga na zasadzki, podstęp, zdradę - na stare, „zasuszone”, przykre sprawy, które powstały kiedyś, a dziś mogą rzutować na sytuację. Można sobie z nimi poradzić bez wielkich szkód. ''', \
'4a':'''Gryzie suche, łykowate mięso. Znajduje stalową strzałę. Korzystna jest wytrwałość i świadomość trudności. Powodzenie. ''', \
'4b':'''Nieprzyjaciel jest potężny, dysponuje ogromną władzą. Karząc takiego przeciwnika, trzeba być twardym jak stal. Niezbędne w takich sytuacjach: hart ducha i zachowywana czujność i wiedza, jak postąpić, pozwolą w końcu go pokonać. Zło powstało już dawno temu i zostało przechowane niby suszone mięso. Temu złu trzeba świadomie stawić czoło, mieć wolę walki oraz stosowną broń. Ów oręż jest ukryty w samej istocie zła - trzeba go pokonać jego własną bronią. ''', \
'5a':'''* Gryzienie suszonego mięsa i natknięcie się na truciznę; determinacja jest niebezpieczna; nie ma kłopotów. ''', \
'5b':'''Podobnie jak przy linii trzeciej - ostrzeżenie przed ukrytymi zagrożeniami, podstępem i zdradą. Ale tutaj nie trzeba trzymać się jednej określonej linii działania. Należy być elastycznym, stosować uniki, widzieć dobre strony pozornie złej sytuacji. ''', \
'6a':'''Człowiek nosi jarzmo. Traci uszy. Złowróżbna. ''', \
'6b':'''Człowiek pospolity myśli, jakoby dobro w małych sprawach nie miało wartości, dlatego je zaniedbuje. Myśli on, że małe grzechy nie szkodzą, dlatego się od nich nie odzwyczaja. Zatem małe grzechy nagromadzają się tak, że nie można już ich ukryć, a jego wina urasta tak, że się już od niej uwolnić nie sposób. Niepokorny, niesłuchający i niezważający na ostrzeżenia, zapiekły w występku jest zatwardziałym gnębicielem.
Należy go surowo ukarać, kimkolwiek jest. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram22 = {'title':'Piękno', \
'ctitle':'Pi', \
'picture':'''Ogień płonie u podnóża skały. Wdzięk. Powab piękna.
Ozdoba. Forma.
Wybraniec koordynuje aktualne sprawy, nie waży się jednak podejmować problematycznych decyzji. ''', \
'judgment':'''Powab sprzyja osiągnięciu sukcesu. Trzymaj się swojej ścieżki, ale nie ugnij się pod własnym ciężarem.
Rzeczy nie powinny jednoczyć się pochopnie ani bezładnie. ''', \
'interpretation':'''	Piękno, chociaż pożądane, jest tylko formą rzeczy, a nie jej istotą. Ładny wygląd to tylko dekoracja, która często może skrywać nieprzyjemne treści. Piękno swym powabem wodzi na pokuszenie ludzi słabych. Jednak obcowanie z nim może dać wgląd w istotę rzeczy, co przyczynia się do lepszego zrozumienia rzeczywistości.
Ponieważ piękno lepiej kontemplować i podziwiać niż je posiadać, dlatego nie podejmuj ważnych decyzji i przełomowych działań.
Mogą być opacznie odebrane. Skup się na sprawach codziennych.
Zewnętrzny powab zakłóca spokój ducha. Gdy chcą się zjednoczyć, niech wnikną w swoje wnętrze. Jeśli tam panuje zgoda, wtedy łączenie jest właściwe.''', \
'1a':'''Ozdabia stopy. Porzuca wóz i idzie. ''', \
'1b':'''Żyje jak w bajce. Problemy zwykłych ludzi są mu obce. Nie musi się wysilać. Nie ma potrzeby, by zmieniał coś w życiu, nie ma na tyle siły, by oprzeć swoje życie na woli realizacji celów. Niech nie żąda więcej, a życie dopasuje się do jego pragnień. ''', \
'2a':'''* Ozdabia brodę. ''', \
'2b':'''Broda nie jest człowiekowi niezbędna. Dbałość o nią świadczy, że świadomość koncentruje się na drobnostkach. Myślisz, że wiesz, czym tak przyciągasz innych i starasz się to pielęgnować i udoskonalać. Popadasz w próżność i niewątpliwie w ten sposób niszczysz swój naturalny wdzięk. ''', \
'3a':'''Jest elegancki i uwielbiany. Gdy pozostanie na ścieżce, pomyślna. ''', \
'3b':'''Delektujesz się swoim pełnym przyjemności życiem. Oto nowa przyjemność w twoim życiu. Potraktuj ją jako chwilową rozkosz, nie przywiązuj się, nie staraj się jej zatrzymać, gdyż zaszkodzi twojemu beztroskiemu stylowi życia powodując rozczarowanie, frustrację i zniszczenie. ''', \
'4a':'''Powab czy prostota? Biały koń wygląda wyniośle.
Szuka związku. To nie rabusie, którzy w pomieszaniu go obmawiają. ''', \
'4b':'''Dostrzegają piękno i urok, które roztaczasz. Chcesz się oświadczyć.
Masz jednak wątpliwości, czy szukając związku, nadal czarować pięknem, czy powrócić do stanu prostoty. Wahasz się, bo czujesz, że możesz się zagubić i stracić wolność. Trzeba powrócić do stanu prostoty, co symbolizuje kolor biały. Wprawdzie nie obejdzie się bez poczucia żalu, taka postawa wyjaśni intencje drugiej strony. Jakkolwiek może się tak wydawać, nie ma ona złych zamiarów, chociaż w konfuzji może posłużyć się obmową. Nie daj się zaskoczyć. ''', \
'5a':'''Powab wśród ogrodów na wzgórzach. Zwój jedwabiu jest mały i cienki. Upokorzenie przemienia się w końcu w pomyślność. ''', \
'5b':'''Ma już dość pustego blichtru. Rozczarował się socjetą, której był członkiem ze względu na jej egotyzm, próżność i pogoń za dobrami materialnymi. Opuszcza ją, by w odosobnieniu powrócić do swoich najgłębszych zasad. Szuka nowego kręgu przyjaciół. Na początku trudno mu będzie znaleźć wspólny z nimi język, ale ponieważ ma dobre intencje, stopniowo wejdzie w nowe towarzystwo. ''', \
'6a':'''* Powab prostoty. Bez winy. ''', \
'6b':'''Niepotrzebne dekoracje zostały usunięte. Proste jest piękne. Nieskazitelność tej prostoty polega na jedności formy z jej treścią, która wyraża jedność myśli i działania przejawiającą się w szczerości.

Oto jest Tao: jedność pięknego umysłu i takiej formy. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram23 = {'title':'Rozpad', \
'ctitle':'Po', \
'picture':'''Góra spoczywa na ziemi. Nachylenie stoku. Erozja.
Wywyższeni chronią swoje pozycje, szukając sojuszników w tych co poniżej. ''', \
'judgment':'''Niekorzystne jest jakiekolwiek działanie. ''', \
'interpretation':'''	Rozluźnienie struktury i tendencja opadająca powoduje w końcu rozkład i ruinę. Element ustępliwy przemienia silny skutkiem niezauważalnego, stopniowego wpływu. Linie yin mają zamiar się powiększać.

Kto spoczął na laurach, tego samozadowolenie usypia jego czujność. Dlatego niegodziwcy chcą zająć jego pozycję. Napierają ze wszystkich sił. Równowaga zostaje zachwiana. Walka przeciwko takim siłom nie da pozytywnych rezultatów. Należy zachować kamienny spokój, aby przetrwać zagrożenie. Nie należy podejmować działań, gdyż tylko przyspieszą rozpad. Trzeba poczekać na właściwą porę. Aby zachować swoją pozycję, warto pomagać zajmującym niższe położenie w hierarchii, pozyskując w nich sprzymierzeńców.
Dzięki temu będzie można zachować własne stanowisko. Nie tyle jest istotne zanikanie światła i przybywanie cienia, ile ważna jest solidność podstaw. Góra tym mniej jest zdana na rozpad, im szerzej spoczywa na ziemi. Poprzez obfite dary, tak jak to leży w naturze ziemi, można zagwarantować sobie spokój leżący w naturze góry.

Czas obiektywny heksagramu: 20 X - 20 XI, środek jesieni.''', \
'1a':''' Łamią się nogi łoża. Upada. Dozna klęski, jeżeli będzie uparty. Nieszczęście.''', \
'1b':'''Ktoś kopie pod nim dołki. Chce podważyć jego pozycję. Podstępne knowania i pomówienia osłabiają jego pozycję władcy. Podwładni odwracają się od niego. Nie należy działać, choć i to nie uchroni przed porażką. ''', \
'2a':'''Łamie się rama łoża. Upada. Dozna klęski, jeżeli będzie uparty. Nieszczęście. ''', \
'2b':'''Twoja pozycja jest mocno osłabiona. Twoi przeciwnicy rosną w siłę. W każdej chwili grozi ci upadek. Musisz zachować wyjątkową ostrożność. Działania, które podjąłeś wcześniej, by się ratować, nie przyniosły rezultatu, bo nie mogły. Powstrzymaj się od aktywności, nie bądź uparty. ''', \
'3a':'''On rozpada się razem z nimi. Bez winy. Traci sąsiada na górze i na dole. ''', \
'3b':'''Ktoś jest w złym otoczeniu, od którego uzależniony jest przez zewnętrzne powiązania. Ale ten układ jest w stanie rozkładu. Posiada on jednak wewnętrzne powinowactwo z człowiekiem wyższym, dzięki czemu znajduje w sobie punkt oparcia, aby wyzwolić się spod obyczajów pospolitych ludzi ze swego otoczenia. Wprawdzie w ten sposób obróci się przeciw tym ludziom, ale nie jest to błędem. ''', \
'4a':'''Łoże łamie się. Rani człowieka. Złowróżbna. ''', \
'4b':'''Runęła cała konstrukcja. Totalna klęska. Nie dało się jej uniknąć; była tak nagła. ''', \
'5a':'''Sznur ryb. Łaskawość dam dworu. Wszystko przynosi korzyść. ''', \
'5b':'''Po trudnych przejściach, otrzymuje nieoczekiwane dary od losu.
Wchodzi w łaski dam dworu, dzięki czemu będzie mógł żywić się w pałacowej kuchni i odzyskać spokój ducha. ''', \
'6a':'''* Wielki owoc jeszcze niezjedzony. Zacny człowiek wsiada do wozu. Dom prostaka zostaje zburzony. ''', \
'6b':'''I rozpad kiedyś dobiega końca. Kto wytrwał w ciężkich chwilach i nie poddał się złu, może zebrać plon swojej szlachetności i liczyć na odzyskanie utraconej pozycji. Słaby, który nie oparł się pokusom, nie ma się gdzie schronić, jego upadek jest wielki. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram24 = {'title':'Punkt Zwrotny', \
'ctitle':'Fu', \
'picture':'''Piorun w ziemi. Powrót. Odrodzenie. Powracanie.
Podczas zimowego przesilenia starożytni królowie zamykali granice. Karawany nie podążały, a władcy nie odwiedzali prowincji. ''', \
'judgment':'''Powrót sprzyja osiągnięciu szczęścia. Odchodzi i powraca na swoją ścieżkę; nie ma w tym winy. Gdy
przyjdzie pogrzeb nie ma zmartwienia. Przybywają przyjaciele. Droga prowadzi tam i z powrotem. Powrót po siedmiu dniach. Dobrze jest coś przedsięwziąć. Przeszkody nie będą hamować. ''', \
'interpretation':'''	Kto zbyt daleko odszedł z właściwej drogi, zatraca się w świecie iluzji i spotyka go klęska. Po okresie upadku następuje jednak powrót na właściwą drogę. Nie będzie to łatwe. Powrót jest jak nawrócenie - wymaga przyznania się do błędów przed samym sobą.
Trzeba przełknąć gorzką pigułkę nieprzyjemnej prawdy. Zanim powrócisz z dalekiej podróży, musi minąć pełny cykl kosmiczny, dlatego trochę to potrwa. Trzeba czasu, aby nawiązały się nowe związki.
Dlatego należy postępować powoli, stopniowo odbudowując swoje życie i odnajdując swoje zagubione Tao. Uważaj, aby nie dać się zwieść ponownie fałszywej krainie złudzeń. Zapowiedzią prawdziwego powrotu będzie pojawienie się przyjaciół.

Stare się przeobraża. Zostaje odrzucone, na jego miejsce przychodzi nowe; oba procesy zgodne są z czasem i nie powodują żadnych zakłóceń. Tworzą się związki ludzi o wspólnych podstawach.
Ten ruch integracyjny dokonuje się zgodnie z czasem w pełnej publicznej jawności, dlatego wszelki egoistyczny partykularyzm jest wykluczony i nie wynikają stąd błędy. Ruch jest cykliczny, a jego droga tworzy zamkniętą, pełną całość. Dlatego nie trzeba niczego na siłę sztucznie przyspieszać. Wszystko przychodzi samo z siebie, kiedy nastaje właściwa pora. Oto Tao nieba i ziemi.

Wszystkie zmiany dokonują się w sześciu stadiach, a siódmym jest powrót. Nastaje wtedy ruch tam, gdzie dotąd wszystko spoczywało.

Czas obiektywny heksagramu: 20 XII + 20 T, przesilenie zimowe.''', \
'1a':'''* Po krótkim błądzeniu powrót bez żalu. Największe powodzenie. ''', \
'1b':'''Jeśli człowiek nie zrobił wielu kroków w niewłaściwym kierunku i powraca na właściwą drogę, nie ma co żałować. Rozpocznij od nowa. Wróży szczęście. Początki imperium Czou były niewłaściwe.
Na szczęście władcy dynastii się poprawili, nim było za późno. Nie ma co płakać nad rozlanym mlekiem, szkoda czasu. Podejmij natychmiastowe kroki, jeśli chcesz naprawić swój błąd, a powrót na właściwą drogę będzie szczęśliwy i wcale nie dramatyczny. ''', \
'2a':'''Godny powrót. Powodzenie. ''', \
'2b':'''Powrót wymaga zachowania właściwej postawy. Potrzebna jest samokontrola. Pomedytuj, zaczerpnij głęboko powietrza, odpocznij, odpręż się, zregeneruj siły. Przebacz i puść winy w niepamięć. Powrócisz na swoją ścieżkę szczęśliwie. ''', \
'3a':'''Ponowne nawrócenie. Zagrożenie. Bez winy. ''', \
'3b':'''Błędy mogą się powtórzyć, bo jest niestały w swoich dążeniach.
Jego wewnętrzne impulsy, którym nie potrafi się oprzeć, ciągle spychają go z właściwej drogi. Ma tendencje, aby rezygnować, gdy już jest u celu, bojąc się, że sukces ściągnie na niego uwagę otoczenia.
Nie ma w tym jego winy, gdyż taka postawa nikogo, prócz niego samego, nie krzywdzi. Jeśli nadal poszukuje dobrej drogi, w końcu czeka go powodzenie. ''', \
'4a':'''Odchodzi z innymi. Powraca sam. ''', \
'4b':'''Czasem człowiek znajdzie się w niestosownym towarzystwie. Jeżeli posiada mocne zasady, nie poddaje się presji zewnętrznej. Potrafi oprzeć się i zawrócić, nawet będąc otoczonym przez niegodziwców, gdyż nie po drodze mu z nimi. Nie zawsze większość ma rację. Jeśli uważasz, że dokonali złego wyboru albo wydali niesłuszny osąd, podążaj własną drogą. Nie daj się nagiąć do ich woli. ''', \
'5a':'''Szlachetny powrót. Bez żalu. ''', \
'5b':'''Nawrócenie na właściwą drogę wymaga przyznania się do błędów.
Nie można zasłaniać się wymówkami. Trzeba mieć dość odwagi, pokory i siły osobistej, by odkupić winę. ''', \
'6a':'''Pobłądził w powrocie. Zamieszanie. Nieszczęście. Wina. Złowróżbna. Władca i wojsko poprowadzone tą drogą dozna klęski, a jej skutki będą odczuwane nawet po dziesięciu latach. ''', \
'6b':'''Był na właściwej drodze, ale nie wykorzystał szansy. Na przeszkodzie stanął strach. Przywiązanie do przebrzmiałych idei i uparte trwanie w zdezaktualizowanych poglądach powodują fałszywą ocenę sytuacji i prowadzą do zguby. To, co uważasz za upór i silny charakter, jest w istocie obawą przed nieznanym. Zamyka to możliwość powrotu na właściwą drogę. Niestety całe siły zostały skoncentrowane na niewłaściwym celu. Nieuchronne zmiany nadejdą i tak, czy tego chcesz czy nie, ale ty nie będziesz na powierzchni.
Zamieszanie, które spowodują, nie pozwoli ci nawet przez dziesięć lat zorientować się, w jakim kierunku powinieneś zmierzać. Czeka cię więc długa zima. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram25 = {'title':'Zaskoczenie', \
'ctitle':'Wu wang', \
'picture':'''Grzmot błyskawicy na niebie. Nieobliczalne. Niewinność. Epidemia.
Starożytni królowie postępowali w zgodzie z naturą, wiedzieli, kiedy działać, żywili wszystkie stworzenia. ''', \
'judgment':'''Najwyższe powodzenie. Korzystne jest podjąć decyzję. Jeżeli to nie stoi prosto, to będzie inspekcja.
Jeżeli ktoś nie jest taki, jaki być powinien, ma niepomyślny los i nie jest dlań sprzyjającym, by przedsiębrać cokolwiek. ''', \
'interpretation':'''	Heksagram przedstawia nieobliczalne zmiany, których nie sposób przewidzieć. Aby sobie z nimi poradzić, potrzebne są działania zgodne z naturą. Gdy energia nieba wciela się w jakąś formę, nie można dokładnie przewidzieć, co powstanie. Można spotkać się z czymś nieoczekiwanym, nieprzewidywalnym, ale nie wolno stracić swojej niewinności. Niewinność jest tutaj parasolem ochronnym na niepomyślny los. Niewinność to taki stan bytu, który akceptuje to, co jest, i w którym świat traktuje się jako punkt oparcia, co pozwala spuścić z oka nawykowe mechanizmy obronne. Zagrożona na skutek plotek może być twoja reputacja. Czasem zły los spotyka niewinnego. Możesz być wystawiony na próbę. Może chodzić o życie. Zdaj się na harmonię natury. Podejmij stosowne działania, aby zlikwidować negatywne skutki niespodziewanego zrządzenia losu.
Dokonaj koniecznego przeglądu swych sił.''', \
'1a':'''Koniec epidemii. Dobrze jest postąpić krok naprzód. ''', \
'1b':'''Zaraza, która pustoszyła twoje życie, skończyła się i nie jest już groźna. Możesz podążyć dalej zgodnie ze swoim instynktem. ''', \
'2a':'''Nie ma siewu ani zbierania plonów, nie ma karczowania nowych pól ani obrabiania starych. Sprzyjające, aby mieć dokąd pójść. ''', \
'2b':'''Fala zarazy ogarnęła ziemię. Zagraża klęska ekonomiczna. Warto mieć jakieś rezerwowe plany, by przetrwać. ''', \
'3a':'''Nieszczęście bez winy. Uwiązał to do wołu. Wędrowiec zyskuje tyle samo, co mieszkaniec miasta. ''', \
'3b':'''Miałeś pecha. Nieszczęście może przyjść bez powodu. Cierpliwie to znoś. Nie trać panowania nad sobą. To, co zaburza, związane jest z tobą i nie zależy od miejsca, gdzie przebywasz. Są widoki na poprawę twojej sytuacji. ''', \
'4a':'''Zdolny być zdecydowanym. Nie ma kłopotu. ''', \
'4b':'''Teraz można podjąć zdecydowane działanie, zgodne z niewinną intencją. Będzie można polepszyć swój los i poprawić naturę. ''', \
'5a':'''* Nieoczekiwana choroba. Nie używa leków. Naturalnie powraca do zdrowia. ''', \
'5b':'''Dotknęła cię niespodziewana przypadłość. Nie należy się z tego powodu martwić i popadać w desperację. Pozwól aby twoja naturalna harmonia, która została naruszona, sama powróciła do równowagi. ''', \
'6a':'''Fałszywa niewinność. Nic nie przynosi korzyści. ''', \
'6b':'''Ambicja bez wiedzy jest bezmyślną walką z losem. Nie ma nic gorszego niż ślepe ufanie własnym iluzjom. Powoduje to jedynie nieszczęście - zło bezradności. Warto wyciągnąć nauki na przyszłość z tego, co się wydarzyło. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram26 = {'title':'Wielkie magazynowanie', \
'ctitle':'Ta cz’u', \
'picture':'''Niebo we wnętrzu góry. Wielkie zyski.
Wybraniec korzysta ze słów i czynów starożytnych, wzbogacając się wiedzą dawnych czasów i czynami przeszłości, aby gromadzić cnoty i wzmacniać swój charakter. ''', \
'judgment':'''Nieskazitelność pozwala skorzystać z wielkiego zapasu. Dobrze jest jadać poza domem. Korzystne będzie przekroczyć wielką wodę. Polega na czasie. ''', \
'interpretation':'''	We wnętrzu góry ukryte są skarby. Tak jak i w słowach, i czynach przeszłości. Właściwe studiowanie nie ogranicza się do wiedzy o przeszłości; nauki wzięte z historii należy stosować w praktyce, aby ponownie przekształcać je w teraźniejszość. Rodzi się coś wielkiego.
Należy tę wielką, twórczą siłę pielęgnować. Niezbędna jest nieskazitelność - ciągła kontrola własnych zachowań i poskramianie swojego cienia, ustawiczna praca nad poprawą charakteru. Należy wzmacniać siłę osobistą, z której rodzi się moc. Nie trwoń swojej energii. Umacnianie siły osobistej dokonuje się w świecie zewnętrznym, a nie poprzez wycofanie się z życia. Człowiek szlachetny nie może uchylać się od działań w świecie zewnętrznym, nawet gdy to wymaga wyrzeczeń.
Przekroczenie wielkiej wody wynika z wewnętrznych trygramów czen, który również oznacza drewno, ponad tuei, jezioro. To niebezpieczne przedsięwzięcie jest możliwe, bo linie druga i piąta tworzą związek zgodności. Dzieła dokonuje się poprzez niepoddawanie się pokusom świata zewnętrznego, pomimo obcowania z nim. Kto dba o rozwój wielkiego, uzyskuje moc, która czyni go równym Niebiosom. Czas wykorzystać swoje pomysły. Wytęż siły i postaraj się zrealizować swoje marzenie. Nie zastanawiaj się nad nim - działaj! Zbierz się na odwagę i wejdź w wielki strumień. Nurt porwie cię ze sobą. Jeśli będziesz siedział w domu lub spędzał mile czas z przyjaciółmi czy w inny sposób zwlekał, przegapisz okazję dokonania czegoś wielkiego. Dzięki zgromadzonej sile osobistej możesz kroczyć ku odległym celom, podejmując się wielkich i istotnych działań. Będą udane.''', \
'1a':'''Niebezpieczeństwo tuż, tuż. Zatrzymaj się! ''', \
'1b':'''Napotyka wielkie przeciwności w wypełnianiu swoich zadań. Nie należy ich przezwyciężać, gdyż brakuje jeszcze mocy. Wielkie dopiero się zaczyna. Korzystne jest odstąpić i nie podejmować działań. ''', \
'2a':'''Usunięto z wozu oś. ''', \
'2b':'''Przeciwne siły, które się pojawiają, są tak wielkie, że nie można ich przemóc. Na razie są silniejsze od ciebie. Twojej siły i talentu nie możesz jeszcze użyć. Musisz poczekać. ''', \
'3a':'''Oswojony koń postępuje za innymi. Jest zdecydowany na swojej ścieżce w obliczu trudności. Codziennie ćwiczy się w powożeniu kwadrygą i w zbrojnej osłonie. Możesz podążyć w każdym kierunku. ''', \
'3b':'''Przyłączyłeś się do ludzi, z którymi dzielisz zasady i dążenia. Dzięki wspólnemu działaniu wielkie tak się nagromadziło, że może zagrażać. Należy je oswoić. Potrzeba do tego prawości i nieustannego ćwiczenia w doskonaleniu swych umiejętności, zarówno w tym co prowadzi naprzód, jak i w tym, co osłania przed atakiem. Gdy jesteś już wyćwiczony możesz realizować cele. ''', \
'4a':'''Drewniana osłona na rogi młodego byka. Bardzo pomyślna. ''', \
'4b':'''Ważna jest dyscyplina w działaniu. Trzeba ująć w karby wielką siłę, aby nie stała się narzędziem zniszczenia. Moc trzeba w czasie wzrostu umiejętnie temperować. Twój pomysł zostanie zrealizowany, powściągaj jednak swoje junackie nastawienie. ''', \
'5a':'''* Kły wykastrowanego dzika. Fortunna. ''', \
'5b':'''Wielkie nie jest już groźne, można nad nim zapanować dzięki zmianie jego natury na łagodniejszą. W ten sposób uzyskuje się pełną kontrolę nad wielką mocą. ''', \
'6a':'''* Podąża drogą Niebios. Najwyższe powodzenie. ''', \
'6b':'''Wielkie rozwija się drogą Niebios, nie potrzebuje już ograniczeń.
Jego moc niesie ze sobą siłę kreacji szczęścia. Tak dzieje się wtedy, gdy jego pragnienia ziszczają się. Osiąga znamienitą pozycję i wpływy pozwalające działać dla dobra ogółu. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram27 = {'title':'Usta', \
'ctitle':'Yi', \
'picture':'''Piorun u podnóża góry. Pożywienie.
Wybraniec zwraca uwagę na swoje słowa i jest umiarkowany w jedzeniu i piciu. ''', \
'judgment':'''Należy poprawnie się odżywiać. Wybraniec zważa na to, czego ktoś szuka, by tym napełnić swoje usta.
Czeka go fortuna. ''', \
'interpretation':'''	Rozwój organizmu i rozwój ducha zależy od spożywanego pokarmu. Dlatego tak ważne jest to, co spożywamy. Tak jak spożywany pokarm wzmacnia ciało, tak słowa są pokarmem dla duszy. Złe pożywienie szkodzi organizmowi; złe słowa zatruwają umysł. Zarówno jedno jak i drugie powinno być z właściwego źródła. Należy zadbać o odpowiednie pożywienie, a znajdując je, spożywać z umiarem. Trzeba zwracać uwagę na to, co wchodzi przez usta i co przez nie wychodzi. Karm swoje ciało i ducha odpowiednią strawą. Karm swoje nadzieje i marzenia. Aby poznać, z kim mamy do czynienia, należy zwrócić uwagę, komu ten człowiek użycza swojej opieki i które strony swojego jestestwa żywi i ma za szczególne ważne. Ciało posiada części szlachetne i nieszlachetne.
Tak samo ktoś jest szlachetny lub nie. W tym heksagramie nie zachodzą związki zgodności pomiędzy odpowiednimi liniami dolnego i górnego trygramu. Dolny szuka pożywienia dla siebie, górny karmi innych.''', \
'1a':'''Odrzuca wyroczne skorupy i patrzy na mnie z grymasem na ustach. Nieszczęście. ''', \
'1b':'''Wyroczne skorupy to wyrocznia I Cing. Jest krynicą mądrości i drogowskazem do doskonałości. Zamiast, korzystając z jej rad, szukać nieskazitelności i wolności, odrzuca jej nauki z niezadowoleniem.
Zazdrości innym dóbr materialnych i chce je też posiadać, co obciąża jego umysł. Oto popadł w stan, kiedy nie liczą się sprawy ducha, a jego świat wypełnia walka o materialny byt. ''', \
'2a':'''Podąża na szczyt w poszukiwaniu pożywienia.
Jednak odżywia się na pagórku. Nieszczęście. ''', \
'2b':'''Chce być wielkim, a poprzestaje na małym. Sam potrafi zdobyć pożywienie, ale ciągle przyjmuje je z innych źródeł wypaczając tym swój charakter. ''', \
'3a':'''Nie przyjmuje pożywienia. Kontynuacja przynosi nieszczęście. Niech nie stosuje tego przez dziesięć lat.
Nic nie służy podążaniu.''', \
'3b':'''To nie jest właściwe pożywienie, więc nie przyjmuj go, i to jest rada na długie lata. ''', \
'4a':'''Pragnie pożywienia ze szczytu góry. Lustruje otoczenie okiem zgłodniałego tygrysa. Nie ma winy. ''', \
'4b':'''Chce być wielkim i zapewnić sobie odpowiednią pozycję życiową.
Jest to naturalne, zgodne z jego predyspozycjami i nie ma w tym niczego złego. Musi zapewnić sobie wsparcie, korzystając ze swojej siły i zdolności przywódczych. Jeśli okoliczności sprzyjają, należy żywić się pokarmem innych. ''', \
'5a':'''* Pozostaje na swoim. Wytrwałość co do miejsca zamieszkania przynosi powodzenie. Nie przekraczaj wielkiej wody. ''', \
'5b':'''Zbytnio przejął się poszukiwaniem odpowiedniego pokarmu. Szukając właściwej diety, zagubił się w różnych smakach. Powinien nie przesadzać w ilości, ale zdecydować się na określoną dietę, pozostając wierny swoim zasadom. Dotyczy to zarówno jedzenia jak i strawy duchowej. Póki tego nie zrobi, nie może podejmować żadnych większych przedsięwzięć. ''', \
'6a':'''* Źródło pożywienia. Fortunna, lecz niebezpieczna. Korzystne jest przekroczenie wielkiej wody. ''', \
'6b':'''Lata wytrwałości i ciężkiej pracy przyniosły efekty. Czas wcielić twoje idee w życie. Masz niezbędne ku temu środki i poparcie. Mędrzec ponieważ posiada wiedzę i mądrość, może nauczać innych, dla których staje się źródłem strawy duchowej. Musi jednak pamiętać, że ciąży na nim wielka odpowiedzialność za słowa, które wychodzą z jego ust. Będąc tego świadom, może się podjąć wielkich dzieł. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram28 = {'title':'Wielki sprawdzian', \
'ctitle':'Ta kuo', \
'picture':'''Jezioro ponad drzewem. Przechodzenie wielkiego testu.
Wielkie przekroczenie.

Jeżeli Wybraniec musi wyrzec się świata, wycofuje się i pozostaje bez lęku i żalu. Sam daje sobie radę i naucza. ''', \
'judgment':'''Belka podtrzymująca strop ugina się pod ciężarem.
Konieczne jest podjęcie jakichkolwiek działań; dobrze jest znaleźć kierunek - w ten sposób korzystne. ''', \
'interpretation':'''	Sytuacja jest kryzysowa. Trzeba starać się ratować chwiejącą się konstrukcję, która lada chwila runie. Nagromadzona wielkość przytłacza. Karmienie bez spożytkowania prowadzi za daleko. Wewnątrz i u góry nagromadzona jest wielka siła, która nie znajduje ujścia. Nadmiar wody niszczy drzewo. Wielkie zebrało się, ale jest niewykorzystane. Sytuacja jest niezwykle niebezpieczna. Konstrukcja może się zawalić. Obciążenie kalenicy podtrzymującej dach jest zbyt wielkie. Należy niezwłocznie pomyśleć o znalezieniu wyjścia.
Jednak do sprawy trzeba podejść delikatnie i ostrożnie. Należy powoli spuścić powietrze. Trzeba podjąć jakieś działania, gdyż można w ten sposób obniżyć poziom nagromadzonej energii, która może posłużyć realizacji dobrych celów. Zrób cokolwiek, ale działaj. Jeżeli inaczej się nie da, należy z pogodą ducha wyrzec się świata. Nie każdy potrafi tak uczynić.''', \
'1a':'''Rozkłada pod przedmiotami białą matę na ziemi. Bez winy. ''', \
'1b':'''Sytuacja jest potencjalnie niebezpieczna, gdyż chce, posiadając moc, rozpocząć działanie w niewłaściwym czasie. Wymaga nadzwyczajnych środków ostrożności. Wskazana jest nawet przesadna przezorność, gdyż niedocenienie zagrożenia może drogo kosztować. ''', \
'2a':'''* Uschnięty jawor wypuszcza pąki. Stary człowiek poślubia młodą żonę. Wszystko sprzyja. ''', \
'2b':'''Z kim przestajesz takim się stajesz. Przebywanie w pobliżu źródła młodości powoduje odmłodnienie. Przypływ sił witalnych przynosi renesans uczuć i świeże spojrzenie, które sprzyjają nieprzewidzianym, pozytywnym zwrotom sytuacji. ''', \
'3a':'''Belka stropowa ugina się bliska złamania. Nieszczęście. ''', \
'3b':'''Nie zwraca uwagi na przejawy konfliktów i erozji układów, w których żyje. Lekceważąc zagrożenie i okazywaną pomoc stara się wpłynąć na bieg rzeczy. Nadmiar siły wyrażany w niesłusznym uporze prowokuje porażkę. ''', \
'4a':'''* Wzmocniono belkę stropową. Sprzyjający znak, ale szkoda się dzieje. Niepokój. ''', \
'4b':'''Mimo że podjąłeś jakieś działania i jest lepiej, to jeszcze stan sprawy budzi niepokój, choć zewnętrznie nie widać objawów przeciążenia. ''', \
'5a':'''Uschnięta wierzba kwitnie. Stara kobieta bierze młodego męża. Bez winy. Bez chwały. ''', \
'5b':'''Kto posiada moc, lecz nie wie, kiedy ustąpić, przypomina starą kobietę poślubiającą młodzieńca. Zbytnia fascynacja własną osobą powoduje utratę poczucia rzeczywistości. To niczego nie zmieni, ponieważ młody mąż nie odmładza starej żony, która i tak nie może wydać potomstwa. W takim postępowaniu nie ma niczego złego, ale nie przynosi ono też żadnych korzyści. ''', \
'6a':'''Wchodzi do wody, która sięga mu ponad głowę.
Nieszczęście. Nie ma winy innych. ''', \
'6b':'''Pogrąża się, nie zważając na niezwykłość okoliczności. Przekracza
swoją miarę. Działa samowolnie, ściągając na siebie zagrożenie,
Musi stawić czoło ekstremalnemu niebezpieczeństwu, będąc świadom, że sam jest sobie winien. Jeśli wytrwa i przejdzie próbę, jest szansa na powrót. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram29 = {'title':'Topiel', \
'ctitle':'Kan', \
'picture':'''Rzeka ponad rzeką. Głębia. Otchłań.
Wpadnięcie w pułapkę.
Wybraniec nieustannie doskonali się i edukuje świat. ''', \
'judgment':'''W topieli można odnaleźć esencję rzeczy. Jeśli zachowa serce, zwiastuje powrót. Wtedy każde działanie jest korzystne. ''', \
'interpretation':'''	Sytuacja pogrążania się w zagrożeniu. Oko w oko z niebezpieczeństwem. Dla kogoś kto znajduje upodobanie w niebezpieczeństwie i lubi odczuwać strach, pokonywanie zagrożeń staje się napędem życiowym. Kto obcuje z niebezpieczeństwem na co dzień, potrafi przeniknąć jego naturę, dzięki czemu nikt nie będzie w stanie mu zagrozić.
Potrafi on doskonale kontrolować swoją przestrzeń, nie pozwalając, aby coś lub ktoś go zaskoczył. Takie podejście do zagrożeń może objawiać się w inklinacji do niebezpiecznych sportów lub zawodów.
Zetknięcie się z niebezpieczeństwem, zaglądnięcie śmierci w oczy, powoduje podnietę i wyzwala energię do działania. Obcowanie z zagrożeniem wyostrza zmysły i pozwala wykorzystać swoje doświadczenia do ochrony swojej pozycji. Jest to pozycja strażnika, który przeszukuje teren w poszukiwaniu ewentualnych zagrożeń. W ten sposób wyrabia sobie specyficzną intuicję, dzięki której wychwytuje ukryte przed innymi sygnały zagrożenia. Wyostrzone zmysły powodują jasność widzenia i umożliwiają kontrolę nad sytuacją, a podjęte działania pozwalają wyjść z trudnych okoliczności. Warunkiem jest skromność i współczucie. Jeśli nie jest dość odważny, niech możliwie szybko wycofa się z tej sytuacji.''', \
'1a':'''Podwójna głębia. Z czeluści wpada w przepaść. Nieszczęście. ''', \
'1b':'''Przyzwyczajenie do niebezpieczeństwa powoduje utratę wrażliwości na zagrożenie. Niebezpieczeństwo zamiast zwiększać czujność powoduje jego lekceważenie. Rutyna wynikająca ze stałego obcowania z zagrożeniem może spowodować, że nie ustrzeżesz się jeszcze większych kłopotów. ''', \
'2a':'''* W głębi czai się niebezpieczeństwo. Niewielkie korzyści. ''', \
'2b':'''Niebezpieczeństwo jest realne. To nie przelewki. Przebywając wśród ludzi nikczemnych sam staje się nikczemnikiem. Jeśli jesteś świadom niebezpieczeństw, jakie ci zagrażają, to nawet kiedy nie możesz się z nich wyrwać, w okolicznościach, w jakich się znalazłeś, możesz odnaleźć pewne korzyści. ''', \
'3a':'''Gdzie nie spojrzy, czeluść nad czeluścią. Niebezpieczeństwo jest wszędzie. Zatrzymuje się i czeka, aby nie wpaść w otchłań. Nie działaj. ''', \
'3b':'''Zabrnął za daleko w niebezpieczeństwie. Samowolne i nieodpowiedzialne działania pogrążyły go w niebezpieczeństwie. Każdy następny krok wywołuje następne, nieznane zagrożenia. To pułapka. Niezależnie od tego, jak nieprzyjemne jest dla ciebie twoje położenie, nie działaj. Musisz poczekać, aż sytuacja się zmieni i będziesz mógł wycofać się, znajdując wolną drogę. ''', \
'4a':'''Dzban wina i miska ryżu; prosto i szczerze ofiarowane. Bez winy. ''', \
'4b':'''Znalazłeś schronienie w niebezpieczeństwie, które oblega cię zewsząd.
To skromne miejsce, poniżej twoich oczekiwań; nie możesz wykorzystać wszystkich twoich umiejętności. Możesz realizować się w sposób ograniczony, zniżając się do poziomu twojego dobroczyńcy. W totalnym niebezpieczeństwie porzucasz swoje sztywne i wyszukane formy zachowania i poddajesz się prostocie. Jest to droga wyjścia z zagrożonej strefy. ''', \
'5a':'''* Wody głębi dochodzą do brzegów i nie przelewają się. Bez winy. ''', \
'5b':'''Zagrożenie jest wielkie, ale nie śmiertelne. Można, jakkolwiek z trudnością, przeprawić się przez rzekę. Skoncentruj się na pokonywaniu zagrożeń, z którymi się stykasz. Nie wchodź w sytuacje inne niż ta, z którą masz do czynienia. Niech nie ponoszą cię zbytnie ambicje. ''', \
'6a':'''Spętany sznurem, otoczony kolczastym murem.
Przez trzy lata nie widzi drogi wyjścia. Złowróżbna. ''', \
'6b':'''Kto nie zważał na znaki ostrzegawcze dawane przez los i brnął w niebezpieczne sytuacje, popełniając błąd za błędem, zboczył z drogi i znalazł się w pułapce bez wyjścia. Twoje problemy skumulowały się i pociągnęły cię na dno głębi. Nie można już uniknąć niebezpieczeństwa i nie ma sposobu, aby sobie z nim poradzić. Jesteś w matni i zajmie ci dużo czasu, nim znajdziesz drogę wyjścia. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram30 = {'title':'Ogień', \
'ctitle':'Li', \
'picture':'''Ogień w ogniu. Bucha płomień. Jasność. Lgnąca.
Wybraniec pielęgnuje swą światłość, jego blask rozjaśnia cztery strony świata. ''', \
'judgment':'''Korzystna jest niezłomność. Daje powodzenie. Hodowanie krowy przynosi pomyślność. Pasterz prowadzi swoje stado. ''', \
'interpretation':'''	Atrybuty ognia to ciepło, płomień wyznaczający kształt oraz jasność. Jasność pojawia się wtedy, gdy człowiek pokonał stający mu na drodze strach. Kto posiada w sobie wewnętrzną jasność rozświetla to, co na zewnątrz. Roztacza wokół siebie blask i ciepło, które przyciągają innych ludzi. Lgną do niego jak pszczoły do miodu. Żeby ogień mógł się palić, potrzebuje zasilającego paliwa. Płomień jasności bazuje na ciemnym paliwie, jakie trzeba mu dostarczać, aby podtrzymać jego istnienie.
Doglądanie krowy symbolizuje rozwijanie tych cech w człowieku, które rozniecają wewnętrzny ogień. Krowa jest symbolem najwyższej uległości. Należy więc dbać o cechy yin, aby mogły podtrzymać ogień i światłość. Dlatego trzeba pielęgnować to, co w człowieku uległe, łagodne, pasywne i ustępliwe. Gdy człowiek hoduje w sobie uległość i dobrowolne uzależnienie, osiąga jasność umysłu bez ostrych cech i odnajduje swoje miejsce w świecie. Ponieważ zbytnie przybliżanie się do ognia i zbyt długie przebywanie w jego pobliżu może spowodować poparzenia, należy zachować umiar i odpowiedni dystans, by się nie sparzyć. Zbyt wielka jasność spala na popiół. Dobrze jest zatem w odpowiednim czasie zejść ze słońca. Noc jest tak samo potrzebna jak dzień. Krowa, to także żywicielka. Kto dba o swój właściwy rozwój wie, że mleko najbardziej potrzebne jest na początku rozwoju. Aby uniezależnić się i usamodzielnić, dobrze jest zadbać o karmicielkę. Nie każdy potrafi to zrozumieć. Wewnętrzna światłość pozwala poprowadzić za sobą zwolenników.''', \
'1a':'''Ślady stóp krzyżują się. Jeśli ktoś traktuje to z powagą, nie ma błędów. ''', \
'1b':'''Brzask. Światło poranka. Należy skoncentrować się na sprawach najważniejszych, eliminując chaos w świadomości, aby uzyskać jasność w ocenie sytuacji. Jeżeli człowiek jest poważny i skupiony, osiąga jasność umysłu niezbędną do rozliczenia się z mnogimi wpływami, które go zalewają. ''', \
'2a':'''* Żółty ogień. Najwyższe szczęście. ''', \
'2b':'''Słońce w południe. Żółty symbolizuje równowagę i harmonię złotego środka. Wewnętrzna światłość rozświetla zewnętrzną aktywność. Wszystko sprzyja. ''', \
'3a':'''Zachód słońca. Jedni biją w bębny, inni opłakują swą starość. Nieszczęście. ''', \
'3b':'''Nadchodzi zmierzch. Gdy zbliża się schyłek życia, słabi ludzie wpadają w rozpacz lub beztrosko cieszą się chwilą. Wewnętrzny ogień świadomości rozpala się i pochłania ich. Nie są w stanie przyjąć właściwej postawy, reagują emocjonalnie. Nieskazitelny, pozostając niezłomnym, niestrudzenie poszukuje prawdy. ''', \
'4a':'''Nadchodzi nagle, bucha płomieniem, gaśnie i zostaje zapomniany. ''', \
'4b':'''Słomiany ogień. Sytuacja fałszywego rozszerzania świadomości. Chwilowy rozbłysk świadomości, niepoparty wewnętrzną prawdą i mocą. Kruchy twór. Takim podejściem do rzeczy nie zbuduje się niczego trwałego. ''', \
'5a':'''* Płyną łzy, szloch i lament. Korzystne. ''', \
'5b':'''Dochodząc do apogeum życia, spoglądając wstecz i zdając sobie sprawę ze znikomości swoich wysiłków, traci nadzieję i poddaje się rozpaczy.
Rozpala się wewnętrzny ogień świadomości i pochłania go. Musi się temu poddać, składając ze swojego dotychczasowego życia ofiarę całopalną.
Niech powstanie jak Feniks z popiołów, zupełnie odmieniając swoje życie. Tylko w ten sposób odzyska spokój ducha. Niech poniecha lęku i nadziei, wejrzy w nicość wszystkich rzeczy i strzegąc jasności swego widzenia zapłacze i westchnie; wtedy jego żal przemieni się w pomyślny los. Tu chodzi o rzeczywiste nawrócenie. Niechaj się wyspowiada. ''', \
'6a':'''Król posługuje się nim w natarciu i do wymierzenia kary. Niszczy przywódców buntu, oszczędzając żołnierzy. Nie ma błędów. ''', \
'6b':'''Niszczyciel działający z rozkazu władcy nie może karać na ślepo. Kara ma dać nauczkę i przywrócić zaburzony porządek. Dlatego trzeba usunąć prowodyrów, którzy są naprawdę winni, zachowując zwykłych ludzi, którzy dali się uwieść złu. Użyty w tym celu ogień jest zarazem ogniem zniszczenia, jak i oświecenia. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram31 = {'title':'Wpływ', \
'ctitle':'Sian', \
'picture':'''Jezioro na górze. Zaloty. Oddziaływanie. Przyciąganie.
Wybraniec kontroluje swój umysł, jego cnoty przykuwają uwagę ludzi, którzy gotowi są go ugościć. ''', \
'judgment':'''Uczucie. Powodzenie. Małżeństwo przynosi szczęście. ''', \
'interpretation':'''	Wpływ to wzajemne oddziaływanie oparte na sympatii, które umożliwia osiągnięcie szczęścia. Ludzie zaangażowani w tę sytuację odczuwają nieuświadomione przyciąganie, które jednak może być kontrowane przez świadomą analizę, co powoduje, że wzajemnie się odpychają. Ażeby tego uniknąć, związek oparty na wpływie wymaga, by strona, która ma siłę i możliwość aktywnego działania, wykazała elastyczność i poddała się stronie biernej. Wykaże tym samym gotowość na jej przyjęcie. Dzięki temu pojawia się uczucie, które pozwala wyzwolić kreatywną energię obu osób, nawet jeśli dzielą ich różnice mentalności, temperamentu, pozycji i wieku.''', \
'1a':'''Porusza dużym palcem nogi.''', \
'1b':'''Pojawiają się zalążki wpływu na sytuację. Nie można jeszcze oddziaływać bezpośrednio, gdyż zamiary są jeszcze nieznane, a cele nieustalone.''', \
'2a':'''Napręża łydki. Złowróżbna, gdy nie będzie czekać.''', \
'2b':'''Nie orientuje się do końca dokąd kieruje swe kroki. Decyzja o związku podjęta zbyt pochopnie. To nie jest związek uczuciowy, ale instrumentalne traktowanie drugiej osoby. Należy to rozważyć i nie śpieszyć się. ''', \
'3a':'''Napręża uda. Podąża za złudzeniami. Jeśli nie zejdzie ze swej ścieżki, dozna upokorzenia. ''', \
'3b':'''Sądzi, że się zakochał. Powinien dokładnie zbadać swoje uczucia, jakie żywi do tej osoby. Powinien powstrzymać się i nie podążać za pierwszym impulsem, który często wywołuje fałszywe wyobrażenia. Jeżeli uzna, że jego uczucia są szczere, powinien zbliżyć się do obiektu swoich uczuć. ''', \
'4a':'''* Napręża całe ciało. Niezłomność niesie powodzenie. Poczucie winy znika. Wpływa tylko na tych, których zna. ''', \
'4b':'''Na ścieżce serca należy stosować się do wewnętrznych odczuć. Uczucie jest miarą zgodności działań z Tao człowieka. Jeżeli znasz uniwersalne zasady, a nie stosujesz się do nich, nie uzyskasz wpływu na innych z wyjątkiem tych, których znasz, gdyż oni pozwolą, by nimi manipulowano. W ten sposób ograniczasz swoje oddziaływanie na innych. Jeżeli ufasz swoim głębokim zasadom i będziesz się do nich odwoływał, nie ulegając wahaniom i nie zmieniając decyzji, możesz pociągnąć za sobą wszystkich. ''', \
'5a':'''* Napręża plecy. Nie ma winy. ''', \
'5b':'''Zebrałeś wystarczająco dużo siły osobistej. Możesz wykorzystać swoją silną wolę i świadomie wpływać na innych. Twoje działania nie wywołują oporu i są akceptowane. Masz moc otwartej świadomości, dzięki której łączysz innych we wspólnym działaniu. Jeżeli w swoich działaniach nie będziesz elastyczny, pozostaniesz niewrażliwy na pożyteczne wpływy innych. ''', \
'6a':'''Napręża szczęki i język. ''', \
'6b':'''Słowa bez czynów są tylko pustym gadaniem. Kto jest tylko mocny w słowach, a nie wyraża się poprzez działanie, nie zdoła trwale wpłynąć na innych. Konsekwencje takiej postawy nie będą miały jakiegoś specjalnego znaczenia. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram32 = {'title':'Trwanie', \
'ctitle':'Heng', \
'picture':'''Piorun i wiatr są wieczne. Długotrwałość. Stałość.
Wybraniec trwa zdecydowanie na swojej pozycji. Nie zmienia swojej drogi. ''', \
'judgment':'''Wytrwałość przynosi szczęście. Bez winy. Dobrze jest coś przedsięwziąć. ''', \
'interpretation':'''	Heksagram ten przedstawia ciągłość stale zachodzących we wszechświecie zmian, dialektyczną jedność przeciwieństw. Każda chwila powstaje z syntezy chwil poprzednich, które są przez tę syntezę niszczone. Trzeba mieć określony, pozytywny cel i takież nastawienie oraz wytrwale zmierzać do jego realizacji. Nie znaczy to, że trzeba być sztywnym, trwać w doktrynerstwie czy fanatyzmie.
Chodzi o to, aby istnieć w zgodzie ze swoim czasem i zmieniać się wraz z nim. Jedyne, przy czym trzeba trwać zawsze, to prawda i dobro; one zawsze, wcześniej czy później, przynoszą szczęście.
Zło i fałsz prowadzą na zatracenie.

Heng jako całość wróży szczęście, choć poszczególne komentarze nie są korzystne.''', \
'1a':'''Daleka trwałość. Nieustępliwość przynosi nieszczęście. Nic nie przynosi korzyści. ''', \
'1b':'''Trwałość, jak inne rzeczy, trzeba osiągnąć poprzez pracę. Kto chce zbyt szybko i za dużo, nie uzyska nic. Stałego, silnego związku nie da się stworzyć z dnia na dzień. Grozi to całkowitym załamaniem relacji. Niechaj przyjaźń, partnerstwo czy romans dojrzewają powoli. Raptowna zmiana nie jest zmianą. Wywołuje jedynie zamieszanie. ''', \
'2a':'''* Znika poczucie winy. ''', \
'2b':'''Zgromadziłeś wielką siłę osobistą. Masz moc, by działać. Nie masz jednak możliwości rozwinięcia skrzydeł. Brak ci środków materialnych. Tych celów nie możesz zrealizować. Zrezygnuj ze swoich planów, może są zbyt ambitne. Zachowaj jednak swoją drogę. Zwróć się do swego wnętrza i trwaj przy swoich zasadach. Przyjdzie czas, że sytuacja zmieni się na korzystną. ''', \
'3a':'''Brak wytrwałości przynosi ujmę. Jeśli pozostanie na tej ścieżce, dozna upokorzenia. ''', \
'3b':'''Wytrwałość jest cnotą, brak konsekwencji w wytrwałości rodzi żal.
Poddawanie się swoim złudzeniom, nastrojowi, uleganie strachowi pod wpływem zewnętrznych oddziaływań i wynikające stąd wahania powodują błądzenie i złe osądy innych ludzi. Dlatego prowadzi to do upokorzeń. ''', \
'4a':'''Nie ma łowów na pustych polach. ''', \
'4b':'''Trwasz przy zamiarach, nawet gdy nie można ich zrealizować. Chcąc znaleźć, należy szukać tam, gdzie możliwość sukcesu jest największa. Na pustym polu nie złowisz zwierza. Szukajcie, a znajdziecie, ale szukajcie rozsądnie. ''', \
'5a':'''Trwanie w nieskazitelności. Pomyślna dla kobiety. Złowróżbna dla mężczyzny. ''', \
'5b':'''Kto jest nieskazitelny i trwa w cnotach, nie może ślepo im ulegać.
Bezkrytyczna wierność zasadom uczciwości, szczerości i stałości może istnieć jedynie w oderwaniu od problemów realnego, codziennego życia. Istnieją sytuacje, które inaczej wyglądają z punktu widzenia kobiety, a inaczej z punktu widzenia mężczyzny. Dlatego cnota jest dobra dla kobiet, których miejscem jest dom, gdzie są strażniczkami ogniska domowego i tradycji, a zła dla mężczyzn, których domeną jest świat zewnętrzny i aktywne jego przekształcanie. ''', \
'6a':'''Trwanie w niepokoju przynosi nieszczęście. Złowróżbna. ''', \
'6b':'''Nie można ciągle żyć w stanie niepokoju. Trwały niepokój rodzi się, gdy człowiek nieustannie rozmyśla o swoich brakach. Ich rozpamiętywanie wiąże niepodzielnie jego uwagę i staje się kotwicą aktywności, unieruchamiając go na mieliznach życia. Powoduje to fałszywy ogląd rzeczywistości. Determinacja w takim postępowaniu gwarantuje klęskę. Należy zastanowić się nad sobą i mieć odwagę przyznania się do własnych braków. Trzeba zniszczyć taką trwałość, bo inaczej ona zniszczy człowieka. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram33 = {'title':'Odwrót jako władanie', \
'ctitle':'Tun', \
'picture':'''Niebo ponad górą. Niedostępne. Poza zasięgiem. Wycofanie.
Wybraniec utrzymuje prostaków na dystans, godnie, z rezerwą. ''', \
'judgment':'''Ustępliwość przynosi korzyści. Powodzenie w małych sprawach. ''', \
'interpretation':'''	Stajesz w obliczu wielkich potęg tego świata, które masz przeciw sobie. Światło wycofuje się przed nią w bezpieczne rejony, gdzie ciemność nie wtargnie. Ciemne siły wzrastają zgodnie z prawami wszechświata. Świadczą o tym pojawiające się wydarzenia, które musisz traktować jak znaki czasu. Nie przestrasz się ich i nie rejteruj przed nimi w panice. Odwrót wpisany jest w bieg tego świata. To proces naturalny, niezależny od woli i działań ludzi. Siła ciemności wzmaga się i podnosi.
Zatem Twoje wycofanie musi być rozważne, spokojne i celowe. Tym samym unikniesz gwałtownego ataku sił natury i chociaż utracisz pozycje, zachowasz swoje siły i trzon charakteru. Odwrót nie jest wymuszoną ucieczką słabego, ale dobrowolnym wycofaniem się silnego. Odsuń się od ludzi i kontaktów, które nie dają Ci radości i nie pomagają w realizacji zamierzeń. Nie ma sensu tracić czasu na niegodziwców; strzeż się ich nienawiści, ale nie okazuj swojej; pozostań obojętny na ich reakcje.
Wycofaj się w samotność i swój wewnętrzny świat. Odwrót to kontrolowane wycofanie się; nie jest ucieczką i ratowaniem się za wszelką cenę, jest oznaką siły. Póki posiada się dość siły i panuje nad położeniem, nie wolno przeoczyć właściwej chwili. Trzeba w porę zrozumieć, co mówią znaki czasu, i wtedy, zamiast wdawać się w desperacką walkę na śmierć i życie, przygotować się do czasowego odwrotu. Sukces polega na tym, aby umieć wycofać się we właściwym czasie i we właściwy sposób.

Czas obiektywny heksagramu: 20 VII + 20 VIII, pełnia lata.''', \
'1a':'''◆ Z tyłu odwrotu. Zagrożenie. Nieskazitelny ochrania odwrót. ''', \
'1b':'''Ponieważ jesteś w tylnej straży, zawczasu wiesz, gdzie czyha niebezpieczeństwo, dzięki temu możesz się na nie niepotrzebnie nie narażać i odpowiednio wcześnie zareagować. Wycofanie się w ostatnim momencie jest niebezpieczne, ale zdążysz się schronić zachowując spokój. Tylko po co czekać na realizację rzeczy niesprzyjających? Lepiej odejść zawczasu. ''', \
'2a':'''◆ Trzymaj się rzemienia z żółtej skóry wołowej.
Nie należy się go pozbywać. Nikomu się nie uda tego obalić. ''', \
'2b':'''Jesteś usidlony przez działania prostaków i związane z nimi ciemne siły. Masz skrępowane ruchy. Jednak ktoś chce Cię wyrwać z tej sytuacji, a jest mocniejszy od ciebie. Trzymaj się go, a jego siła wyprowadzi cię z opresji. Zastosuj wszelkie potrzebne rygory. ''', \
'3a':'''Zatrzymany odwrót. Zagrożenie. Słudzy i konkubiny przynoszą nieszczęście. ''', \
'3b':'''Odwrót jest odwrotem. Podjętej decyzji nie należy poddawać w wątpliwość. Ingerencja osób trzecich nie może hamować twojego odwrotu. Nie czas na wahania. Wycofaj się. Gdy grozi niebezpieczeństwo, nie należy zaangażować tych osób we wspólne działanie.
W ten sposób nie mogą one powstrzymać twojego odwrotu. ''', \
'4a':'''Samodzielny odwrót jest fortunny dla człowieka wielkiego, prostakowi przynosi upadek. ''', \
'4b':'''Tu jest wyjście. To jest sytuacja, której mogą sprostać tylko ludzie na odpowiednio wysokim poziomie rozwoju. Zacny człowiek sam stanowi o swoim odwrocie. Wie, że nie wszystko złoto, co się świeci. Potrafi się oprzeć pokusie, wycofując się bez poczucia żalu, pozostając wierny swoim zasadom.
Słaby człowiek tego nie potrafi. Wycofując się, ma poczucie straty i dręczy go z tego powodu żal. Zaczyna nienawidzić siebie za odwrót. ''', \
'5a':'''* Rozsądne władanie, którym można się radować. Fortunna, gdy pozostaniesz na swojej ścieżce. ''', \
'5b':'''Odwrót od złych działań i niewłaściwych tendencji skutkuje mądrym władaniem. Decyzje wtedy podejmowane są dobroczynne. ''', \
'6a':'''Godny odwrót. Zdecydowanie. Wszystko przynosi szczęście, gdyż nie ma już miejsca na wątpliwości. ''', \
'6b':'''Dzięki ustępliwości gromadzisz wewnętrzne skarby. W ten sposób będziesz mógł sprostać wszystkiemu. A jeżeli można sprostać wszystkiemu, nic nie ogranicza. Wewnętrzne odłączenie od wzbierającej pospolitości jest niepodważalnym faktem, a przez to człowiek ma wolność odejścia. Gdy jasno i bez wątpliwości widzi drogę przed sobą, pojawia się pogodna perspektywa, przy której bez namysłu wybiera to co właściwe i prawe. Dokładnie wiadomo, co trzeba robić dalej. W takich okolicznościach wykonanie powziętej decyzji nie jest już trudne. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram34 = {'title':'Wielka potęga', \
'ctitle':'Ta czuang', \
'picture':'''Piorun na niebie. Potęga natury. Wielka moc.
Wybraniec porzuca to, co nie jest zgodne z porządkiem świata. ''', \
'judgment':'''Korzystna jest niezłomność na ścieżce. Dojrzałość sprzyja. ''', \
'interpretation':'''	Moc pojawia się wtedy, gdy pokonani zostali dwaj pierwsi wrogowie człowieka: strach i jasność. Jeśli ktoś ulegnie swojemu pierwszemu wrogowi - strachowi, pozostanie słabym, nic nieznaczącym człowiekiem, który zawsze będzie miał nieuzasadnione pretensje do świata. Kiedy jednak pokona pierwszego wroga, pojawia się jasność. Jednak jasność wkrótce staje się drugim wrogiem człowieka.
Trzeba go też pokonać. Jeśli człowiek podda się temu podstępnemu wrogowi, może pozostać błaznem albo sprawnym wojownikiem, który jednak nigdy nie doświadczy prawdziwego zrozumienia. Gdy jednak człowiek pokona jasność, uzyskuje moc. Moc również staje się wrogiem człowieka, jeżeli nie potrafi nad nią zapanować. Moc wymaga samokontroli i uporządkowania. Jej nadużycie obraca się przeciw człowiekowi. Gdy człowiek zostanie pokonany przez swojego trzeciego wroga - moc, staje się tyranem i nigdy już nie osiągnie prawdziwego szczęścia. Kto zaś zapanuje nad swoją mocą, ten osiąga możliwość kreowania swojego świata zgodnie ze swoją wolą, a wola jego pozostaje zgodna z wolą nieba. Może więc zrealizować każdy cel. Trzeba szczególnie uważać i ostrożnie obchodzić się z mocą, aby nie dać się jej zniewolić.

Istotą tego heksagramu jest przeciwstawienie sobie potęgi i przemocy. Tutaj moc zostaje obłaskawiona, traci swoją gwałtowność.

Czas obiektywny heksagramu: 21 V - 20 VI, koniec wiosny.''', \
'1a':'''Moc w wielkich palcach stóp. Kontynuacja jest złowróżbna. ''', \
'1b':'''Masz za mało siły, by podjąć działanie. Nie uzyskasz wpływu na sytuację. Nie podejmuj aktywności pochopnie. ''', \
'2a':'''Powodzenie, jeżeli nie zboczysz ze swojej ścieżki. Korzystne jest być zdeterminowanym. Wytrwałość przynosi pomyślny los. ''', \
'2b':'''Masz dość energii, by rozpocząć działanie. Dojrzałeś już do podjęcia decyzji i twoje wybory powinny być słuszne. Jesteś pełen optymizmu. Ale uważaj, wielka moc potrzebuje samoograniczenia. Trzeba stopniowo wprowadzać ją do użycia. Stanowczo trwaj przy swoim.
Nie ustępuj na krok. Mimo wszystko w końcu wygrasz. ''', \
'3a':'''Prostak chełpi się swoją siłą. Niebezpieczeństwo. Wielki człowiek tak nie postępuje. Byk bodzie płot. Uwięził swoje rogi. ''', \
'3b':'''Kto jest świadom swojej siły i zawsze używa jej do osiągania celów, gdy będzie tak postępował w sytuacji, w jakiej się znalazł, dozna porażki. Tak postępuje prostak, którego wiara we własne siły graniczy z zadufaniem. Należy zrezygnować z użycia siły i pójść na kompromis. W ten sposób uniknie się uwikłania w problemy. ''', \
'4a':'''* Byk bodzie płot, ogrodzenie się otwiera i jest już wolny. Znika poczucie winy. Moc wielkiego wozu zależy od jego osi. Fortunna, jeżeli zachowasz swoją ścieżkę. ''', \
'4b':'''Moc może się ujawnić, nie ma już ku temu przeszkód. Stałość wewnętrznych zasad i tworząca ją moc wewnętrznej prawdy pozwalają podjąć i kontynuować działanie. Decyzje podjęte w tym momencie będą pomyślne. ''', \
'5a':'''Z łatwością porzuca byka. Bez poczucia winy. ''', \
'5b':'''Odwaga i niespożyte siły nie są jeszcze gwarancją niezwyciężoności. Porzuć taką postawę bez żalu i stań się bardziej łagodny i tolerancyjny. ''', \
'6a':'''Byk bodzie płot. Utknął. Nie może się wycofać, ani pójść naprzód. Postęp niemożliwy. Pomyślna, gdy uznasz swój błąd. ''', \
'6b':'''Zablokowałeś się. Bezmyślne uparte działanie zapędziło cię w ślepy zaułek. Cokolwiek teraz zrobisz, obróci się przeciw tobie i spowoduje jeszcze większe ograniczenie. Powinieneś odstąpić od swoich nierealnych planów. Sama ambicja nie wystarczy. Jeżeli będziesz silny, wyciągniesz wnioski z tej wpadki i będzie ona dla ciebie nauczką na przyszłość. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram35 = {'title':'Postęp', \
'ctitle':'Cin', \
'picture':'''Słońce wznosi się ponad ziemię. Progresja. Na wzór wód.
Wybraniec rozświetla swoje cnoty. ''', \
'judgment':'''Potężnemu władcy ofiarowują stadninę koni. Trzykrotnie w jednym dniu podejmowany jest u dworu, gdzie zasięgają jego rad. ''', \
'interpretation':'''	Heksagram przedstawia różne kwestie, w których można się zagłębić na ścieżce postępu, w drodze do sukcesu. Na tym polega talent w dziedzinie dowodzenia i zarządzania, aby zagłębić się, a nie utonąć. Jasność osądu każdej sytuacji pozwala podejmować optymalne decyzje. Należy swoje kierownicze zdolności ujawnić, by wykorzystać je w celu wspólnego dobra. Gdy tak się stanie, uzyska się uznanie i zostanie się nagrodzonym. Przypadną nagrody i awans. Będzie można być albo znakomitym doradcą znaczącej osoby, albo samemu będzie można promować zdolnych i wyróżniających się podwładnych. Kto chce zarządzać i wcielać w życie wielkie plany, potrzebuje również lojalności swoich podwładnych.
Trzeba o to zadbać.''', \
'1a':'''Zanurza się głęboko. Powracanie do wody. Samotnie podąża w prawdzie. Jeśli nie potrafi wzbudzić zaufania, niech się z tym pogodzi. Nie ma winy. ''', \
'1b':'''Coś zniknęło i jest głęboko ukryte. Mało kto daje temu wiarę. Jednak ty znasz prawdę. Jeśli chcesz, a nie potrafisz do tego przekonać innych, nie martw się tym. ''', \
'2a':'''Zanurzony w smutku. Trzymaj się swojej ścieżki. Powodzenie dzięki matce. ''', \
'2b':'''Mimo prób wyjawienia prawdy i zbliżenia się do mocnego człowieka kontakt nie zostaje nawiązany. Postęp zostaje zahamowany. Wywołuje to strapienie i smutek. Jednak nie należy rezygnować. Należy odwołać się do żeńskich sił, na których można polegać, i tam szukać wsparcia. ''', \
'3a':'''Zanurzony w zgodzie ze wszystkimi. Wszystkie nieszczęśliwe wydarzenia idą w niepamięć. Nie ma winy. ''', \
'3b':'''Sam nie jest w stanie podążać naprzód, ale postęp możliwy jest dzięki wspólnemu postępowi opartemu na zaufaniu. Przy poparciu zwolenników może realizować swoje cele. Powoli zyskuje coraz większe zaufanie wspólników czy rodziny, jest doceniany. Z czasem jego grzechy z przeszłości i nieprzyjemne doświadczenia pójdą w niepamięć. ''', \
'4a':'''Idzie naprzód jak świstak. Zagrożenie, jeżeli nie zejdziesz ze swojej ścieżki. ''', \
'4b':'''Zwykłeś postępować potajemnie, ukrywając swoje zamiary. Dotąd twój spryt i inteligencja zapewniały ci sukces twojej taktyki. Teraz jednak znajdujesz się w zasięgu kogoś bystrego i spostrzegawczego. Twoje posunięcia mogą wyjść na jaw. Uważaj. Gdy zostaną odkryte, grozi ci klęska. Powinieneś zmienić taktykę na bardziej otwartą. ''', \
'5a':'''* Żal znika. Nie przejmuje się zyskiem lub stratą. Dobrze jest działać. Przedsięwzięcia przynoszą korzyści. Wszystko sprzyja. ''', \
'5b':'''Nie należy przywiązywać zbytniej wagi do dóbr materialnych, zdając sobie sprawę z ich ulotności i zmienności; nie należy być ich sługą, ale korzystanie z nich powinno dawać możliwość wpływu na bieg rzeczy. Wiedząc o tym, można podejmować właściwe działania. Nie ma sensu się roztkliwiać nad sobą ani żałować poniesionych strat. ''', \
'6a':'''Zanurzony w odwecie. Idzie naprzód z nastawionymi rogami, by ukarać najeźdźców. Niebezpieczeństwo sprzyja. ''', \
'6b':'''Nie schodź ze swej ścieżki, mimo że wywoła to żal.
Musisz podjąć stanowcze i zdecydowane działanie, aby przyspieszyć postęp, który hamowany jest przez wrogie siły. Surowa reakcja jest usprawiedliwiona. Użyj swojej potęgi, by pokonać siły obcej agresji.
Tak czy inaczej spowoduje to wyrzuty sumienia. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram36 = {'title':'Zmrok', \
'ctitle':'Ming yi', \
'picture':'''Słońce zachodzi nad ziemią. Zapada zmrok.
Wybraniec, przebywając wśród ludzi, zakrywa swój blask, ale pozwala mu świecić. ''', \
'judgment':'''Napotykając przeciwności, korzystne jest pozostać niezłomnym.
Coś zostaje uszkodzone albo ktoś zraniony. ''', \
'interpretation':'''	W mrocznych czasach prześladowań ludzie szlachetni i mądrzy zmuszeni są żyć w mroku i narażeni są na zranienie przez egoistów, prostaków i ludzi podłych. Gdy pojawia się zewnętrzna ciemność, powinna być zrekompensowana rozświetleniem wnętrza. Gdy jesteś w opresji, nie poddaj się siłom ciemności. Nie pozwól, aby cię wchłonęły. Możliwe, że przez jakiś czas będziesz musiał być niewolnikiem. Musisz ukryć swe prawdziwe uczucia i myśli, gdy znajdujesz się w niesprzyjających okolicznościach. Nie zważaj na otaczające cię zło. Zachowaj wewnętrzną światłość i zasady. Poddaj się w swoich reakcjach zewnętrznych, ale wewnątrz pozostań sobą. Zachowaj dyskretny urok mądrości.''', \
'1a':'''Światło gaśnie, gdy wzlatuje. Skrzydła opadają. Zacny człowiek nie je przez trzy dni wędrówki, ale potem znajduje schronienie.''', \
'1b':'''Chce się wzbić do lotu mimo ogromnych trudności, jakie napotyka. Nie pozwalają one na rozwinięcie skrzydeł. Przeciwności przytłaczają go. Nieustannie zmagając się z niebezpieczeństwem, narażony jest na pociski (zawistnego) losu. Nie trać ducha, pozostań optymistą. Twoje trudności są tymczasowe; jesteś „w drodze”, a wszelkie trudy, kłopoty i niedole są immanentną cechą twojej ścieżki. Taka jest cena zmian. Niedługo znajdziesz właściwe miejsce. ''', \
'2a':'''* Światło gaśnie. Człowiek ranny jest w lewe udo, woła o pomoc. Szybki koń ratuje go. Fortunna. ''', \
'2b':'''Znalazł się w trudnej sytuacji. Siły ciemności biorą górę. Ale można jeszcze odwrócić niebezpieczną tendencję. Mimo że są rany, wywołane szkody nie są poważne, a istotne siły nienaruszone. Może wybrnąć z trudności, jeżeli będzie miał w pogotowiu jakiś odwód. ''', \
'3a':'''Zmrok podczas łowów na południu. Prowodyr zostaje pojmany. Nie od razu powróci porządek. ''', \
'3b':'''Siły ciemności dokonały spustoszenia. Wyrządziły wielką krzywdę.
Można spodziewać się odwetu. Usilna praca pozwoli przywrócić ład, ale nie nastąpi to szybko. Zamęt, który wywołały, jest zbyt wielki.
To może tkwić wewnątrz człowieka. ''', \
'4a':'''Przenika lewą stroną brzucha. Odnajduje jądro ciemności. Wymyka się przez wrota. ''', \
'4b':'''Znalazłeś się w zasięgu tyrana. Jesteś blisko ducha ciemności. Przejrzałeś go na wylot. Znasz jego zamiary. Uzyskujesz pewność, że może być już tylko gorzej. Wycofaj się otwarcie i nie obawiaj się reakcji despoty, gdyż jesteś dla niego niczym i nic dla niego nie znaczysz. ''', \
'5a':'''* Mroczne czasy księcia Czi. Korzystna jest niezłomność. ''', \
'5b':'''Jest zakładnikiem ciemnych sił. Należy zaadaptować się do fatalnych warunków zewnętrznych, ukrywając swe prawdziwe oblicze i uczucia. Potrzeba pielęgnować wewnętrzną jasność i umacniać hart ducha, stale bacząc na zagrożenia. Można liczyć tylko na siebie i na własny spryt. ''', \
'6a':'''* Zapada zmrok. Najpierw spada popod ziemię, potem wspina się do nieba. ''', \
'6b':'''Zaszło słońce. Zenit sił ciemności; ciemne siły osiągające swój punkt szczytowy, przemagają siłę światła, które jest w punkcie dołowania - osiąga swój nadir. Ciemności opanowały cały świat. Złe siły panujące nad twoim życiem pognębiły cię całkowicie. Ale nie martw się, ciemność nie trwa wiecznie. Kiedy przemiana się dokona, z chwilą totalnego triumfu, ciemność zginie, by narodziła się znowu jasność.
Taka jest kolej Rzeczy. Spójrz na znak tai chi. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram37 = {'title':'Ród', \
'ctitle':'Czia żen', \
'picture':'''Wiatr roznieca płomień z ognia. Rodzina. Naród.
Słowa wybrańca zawsze zgodne są z jego czynami, w życiu dochowuje wierności swym niezłomnym zasadom. ''', \
'judgment':'''Jest czas, by kobieta podążyła własną drogą.
Kobiecie korzystnie jest założyć rodzinę. ''', \
'interpretation':'''	Ród to płomień domowego ogniska, rozniecany przez kobiety w celu harmonii i szczęścia w rodzinie. Sprzyja im wewnętrzna organizacja oparta na hierarchii i szacunku dla wszystkich. Każdy wykonuje swoje obowiązki i każdy ma swoje prawa. Ich przestrzeganie scala ród i staje się powodem sukcesów jego członków. To miniaturowy model państwa. Gdy przestrzegane są ogólnie przyjęte zasady, słowa mają swoją moc, ponieważ każdy odbiera je tak samo. Należy unikać hipokryzji; nie ulegać słabościom wynikającym z energii yin: pragnieniom, pożądaniom, zachłanności, zazdrości, emocjom i nastrojom. Trzeba zapanować nad nimi, jak dbająca o swoją reputację kobieta, czyniąc z nich swoich przewodników w drodze do szczęścia.''', \
'1a':'''Ustala podział ról w rodzinie. Żal znika. ''', \
'1b':'''Autorytet w grupie powinien być silny od samego początku. Należy ustalić zasady i przypisać role, co sprzyja utrzymaniu dyscypliny.
Niezdecydowanie i słabość powodują niepewność, a wynikający stąd brak zaufania do przywódcy rodzi opór, który pokonywać przyjdzie siłą. Wszyscy powinni podporządkować się zwierzchności. ''', \
'2a':'''* Kobieta zajmuje się kuchnią. Nie ma miejsca, by gdzieś iść. Pomyślne. ''', \
'2b':'''Gdy członkowie rodziny z radością, bez przymusu i z przeświadczeniem o ich konieczności wykonują swoje obowiązki, wtedy w domu jest pożywienie dla wszystkich i nie ma po co szukać gdzie indziej.
Każdy w rodzinie powinien być sobą i znać swoje miejsce oraz korzystać z jej dostatku. ''', \
'3a':'''Ród postępuje nienależycie. Żona i dzieci są zapatrzeni w siebie. Niepokój. Surowość niesie szczęście, choć powoduje wyrzuty sumienia. ''', \
'3b':'''Nie można dopuścić do rozprzęgnięcia wśród bliskiego otoczenia.
Kobieta i dzieci czynią siebie pępkiem świata, wokół którego ma się obracać życie rodziny. Zbytnia tolerancja powoduje utratę autorytetu, a nadmierna surowość wzbudza poczucie winy. Trzeba przywrócić porządek i wymusić przestrzeganie zasad, jakkolwiek wywoła to poczucie winy. ''', \
'4a':'''Ona wzbogaca ród. Wielka pomyślność. ''', \
'4b':'''Umiarkowani, niepozorni i zaradni są pozbawieni egoizmu i przynoszą korzyść swoim bliskim. Należy szanować i doceniać ich wysiłek, bo dzięki nim rośnie zamożność i pomyślny los rodziny. ''', \
'5a':'''* Jest panem na włościach. Bez obaw. Fortunna. ''', \
'5b':'''Prawdziwe rządy nie opierają się na strachu. Autorytet musi wynikać z wewnętrznej siły, która przyciąga innych, wzbudzając w nich respekt i atencję. Taka siła obdarza miłością, która jest wolna od niepokoju. ''', \
'6a':'''Oto jest powrót jakby chyłkiem. Wzbudza szacunek swoją pracą. W końcu los sprzyja. ''', \
'6b':'''Powrót syna marnotrawnego na łono rodziny. Zostaje przyjęty i zaskarbia sobie szacunek poprzez swoją pracę na rzecz rodziny. Dzięki temu dojdzie do siebie po trudnych przejściach i poniesionych porażkach. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram38 = {'title':'Opozycja', \
'ctitle':'Kui', \
'picture':'''Ogień nad jeziorem. Przeciwieństwo. Nieporozumienie.
We wszelkiej wspólnocie wybraniec zachowuje swą odrębność. ''', \
'judgment':'''Neutralizacja. Powodzenie kryje się w sprawach małych. Można kogoś postraszyć. ''', \
'interpretation':'''	Patrzenie na sprawę z różnych punktów widzenia, co prowadzi do nieporozumień, niechęci czy niezgody. Symbolizuje wzajemne łączenie antagonistycznych czynników. Pomimo że oba pierwiastki pozostają w opozycji, to jednak łączy je silny związek. Opozycje niekoniecznie są szkodliwe. Dzięki wzajemnemu ścieraniu się przeciwieństw powstają nowe wartości, służące postępowi i zmianom na lepsze. Na ludzkim planie takie opozycje rodzą konflikty, które jednak łatwo można zażegnać, gdyż mają swoje źródło w wyrażanych na zewnątrz pozach, a nie wynikają z prawdziwych różnic wewnętrznych. Aby zakończyć nieporozumienia i wynikający stąd konflikt oraz przywołać wielkie, należy skupić się na rzeczach małych, przyziemnych, związanych z codziennym życiem, właściwych sile yin. Można też komuś pogrozić, by wymóc na nim zgodne działanie. Udawanie na zewnątrz pozornej zgody i dostrzeganie różnych stanowisk pomaga zająć pozycję mediatora w sporach. Jednak brak wewnętrznej zgody i wynikające stąd niezdecydowanie nie pozwalają dokonywać wielkich czynów.''', \
'1a':'''Znika poczucie winy. Stracił swojego konia. Niech go nie szuka. Wróci sam. Spotkanie ze złym człowiekiem; gdy się strzeże, nie popełni błędu, a ów człowiek będzie nieszkodliwy. ''', \
'1b':'''Czujesz, że straciłeś coś, co należy tylko do ciebie. Nie martw się, odzyskasz to. Może chodzić o środek transportu. Zapomnij o przykrych sprawach. Ktoś odszedł na skutek nieporozumień w ważnych sprawach. Nie trać czasu na próby zmiany jego decyzji. Gdy zdasz sobie sprawę, że powodem starcia było nieporozumienie, wróci sam. Mimo że na swojej drodze spotkasz złego człowieka, którego można się obawiać, nie zagrozi ci - od razu rozpoznasz, kto zacz i jego niecne intencje. ''', \
'2a':'''* Spotyka swojego mistrza na uboczu. Nie ma błędu. ''', \
'2b':'''Nieporozumienie z kimś dla ciebie ważnym, z kim nie możesz znaleźć wspólnego języka. Twoja postawa i niedostępność powodują, że musi cię unikać. Spotykasz się z nim sam na sam w ustronnym miejscu. Organizuje takie spotkanie niby przypadkiem. Przyjmij to pozytywnie i chętnie rozmów się z nim bez skrępowania. Będzie to okazja do wyjaśnienia nieporozumień. ''', \
'3a':'''Ciągną powóz do tyłu, woły są zatrzymane. Ogolono mu głowę i obcięto nos. Mężczyzna w wozie jest zły. Zły początek, ale dobry koniec - dzięki spotkaniu kogoś mocnego. ''', \
'3b':'''Nie jest dobrze. Wszystko, co robisz, układa się niepomyślnie. Źli ludzie sprzysięgli się przeciwko tobie, co doprowadziło do nieszczęścia. Dosięgła cię klęska nie tylko materialna, ale i niesława. To, co zaczęło się dawno temu, właśnie tak się realizuje. Musisz przeczekać zły czas, dobry los nadejdzie i wynagrodzi ci twoją krzywdę.
Pomimo upokorzenia wszystko dobrze się skończy. ''', \
'4a':'''Sam pośród przeciwieństw. Spotyka dobrego człowieka i szczerze łączy z nim swój los. Zagrożenie, ale nie zbłądzi. ''', \
'4b':'''Został zdradzony. Jest w opozycji do całego otoczenia. Czuje się izolowany. Powinien poszukać kogoś podobnego sobie, z kim będzie mógł dzielić los. Szczerość tego związku pozwoli na wspólne pokonanie trudności. ''', \
'5a':'''* Znika poczucie winy. Przedarł się przez powłokę. Uczepił się towarzysza zębami. Czy z taką pomocą może popełnić błąd? ''', \
'5b':'''Kłopoty i utrapienia się kończą. Albo sam przeniknąłeś mur izolacji, jakim się otoczyłeś - przedarłeś się przez zasłonę zaślepienia, uznając swoją winę w sprawie i chcesz naprawić błąd, albo udało się to komuś, kto ma wobec ciebie dobre intencje. Takiemu towarzyszowi należy okazać przychylność i uczucie, i pozwolić mu przyłączyć się do siebie. Ten ktoś to linia druga, z którą linia piąta tworzy związek. ''', \
'6a':'''Sam w opozycji. Ktoś się zbliża. Widzi brudną świnię i wóz pełen demonów. Celuje z łuku, potem zwalnia cięciwę. To nie wróg, lecz przyjaciel. Demony to nie złodzieje. Przybywają na wesele. Gdy podąża do przodu, spada deszcz. Przychodzi szczęście. ''', \
'6b':'''Będąc osamotniony wśród przeciwieństw, niewłaściwie oceniasz motywy kogoś, kto próbuje się do ciebie zbliżyć. Ulegasz fałszywemu złudzeniu. Myślisz, że ma ukryte złe zamiary i chce podstępnie cię wykorzystać. Twoja agresywna postawa obronna jest niepotrzebna. Mężczyzna prowadzący wóz, w którym siedzą cudzoziemcy, to przyjaciel i ma szczere zamiary - chce się z tobą zaprzyjaźnić. Porzuć swój oręż i przyjmij go. Komentarz dotyczy przymierzy króla Wen z obcymi plemionami. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram39 = {'title':'Przeszkoda', \
'ctitle':'Ćian', \
'picture':'''Rzeka na górze. Wodospad. Trudność do pokonania.
Wybraniec uważnie przygląda się swojemu wnętrzu i rozwija własne cnoty. ''', \
'judgment':'''Należy kierować się ku przyjaznej ziemi i nie zapuszczać się na teren nieprzyjaciela. Porada mądrego człowieka sprzyja szczęściu. Wytrwałość na swojej ścieżce sprzyja. ''', \
'interpretation':'''	Przeszkody, które napotykasz, są naturalnym elementem drogi, po której kroczysz. To ze względu na to, że wybrałeś sobie odległy i ambitny cel. Dobrze jest znaleźć doradcę, który pomógłby ci przeanalizować sytuację tak, abyś nie chciał od razu zwalczać przeszkód ani ich usuwać. Lepiej byłoby zatrzymać się, by przygotować się do przezwyciężenia przeszkód, gdyż można i należy je pokonać.
Trzeba pomyśleć również o tym, czy nie uda się ich ominąć. Kto z daleka widzi nadchodzące niebezpieczeństwo, umie mu przeciwdziałać. Bądź mądry przed szkodą. Jeśli nie wiesz, co robić, poradź się mądrego człowieka. Niebezpieczeństwo jest na zewnątrz - należy wycofać się, najlepiej do wspólnoty, i pozostać na właściwym miejscu. Korzystne będzie znaleźć chwilę czasu na przemyślenie oraz zmodyfikowanie swojej strategii i spojrzenie w głąb siebie, by skorygować wady charakteru.''', \
'1a':'''Idzie naprzód, wraca wozem z powrotem. Napotyka wielkie przeszkody. Zostaje nagrodzony. ''', \
'1b':'''Zaczyna się skromnie i rysują się wielkie trudności, ale wyprawa skończy się powodzeniem. ''', \
'2a':'''Królewski wasal napotyka przeszkodę za przeszkodą. To nie jego wina. Nadal wypełnia swoje zadanie. ''', \
'2b':'''Trudności kumulują się, ale obowiązek w stosunku do kogoś nakazuje iść naprzód. Nie można odstąpić albo iść na łatwiznę. Trzeba nieugięcie pokonywać napotykane przeszkody, zachowując związek z mocodawcą. ''', \
'3a':'''Idzie naprzód. Napotyka wielkie przeszkody. Zawraca. ''', \
'3b':'''Powrót do punktu wyjścia. Człowiek, który bezkrytycznie dąży naprzód mimo piętrzących się przeszkód, wpada w kłopoty i musi zawrócić. ''', \
'4a':'''Idzie naprzód. Napotyka wielkie przeszkody. Przystaje, zbierając zwolenników.''', \
'4b':'''Aby pokonać trudności, potrzebne jest poparcie innych. Należy współdziałać. Ale to wymaga przygotowań i czasu. Nie licz, że poprą cię od razu. Porzuć dumę, przedyskutuj z nimi problem i zwróć się do nich po pomoc. ''', \
'5a':'''* Pośród wielkich przeciwności. Przybywa przyjaciel.  ''', \
'5b':'''Ktoś jest w wielkich tarapatach. Pojawia się przyjaciel, z którym wspólnie pokonają przeszkody. ''', \
'6a':'''Idzie naprzód. Napotyka wielkie przeszkody. Przystaje i osiąga szczęście. Pomyślna, jeśli zasięgniesz rady mądrego człowieka. ''', \
'6b':'''Nie ma co forsować przeszkód, które są nie do pokonania. Aby dać sobie z nimi radę i się od nich uwolnić, najlepiej odstąpić od ich przezwyciężania. Warto w tej kwestii porozmawiać z mądrym człowiekiem. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram40 = {'title':'Uwolnienie', \
'ctitle':'Ćie', \
'picture':'''Piorun wyzwala oberwanie chmury. Wyzwolenie.
Wybraniec jest wyrozumiały wobec winowajców, wybacza błędy i darowuje kary. ''', \
'judgment':'''Należy pozostać na przyjaznej ziemi; nie ma dokąd pójść. Powrót przynosi szczęście. Ma dokąd iść, by spędzić noc; pomyślne. ''', \
'interpretation':'''	Sytuacja, w którą się uwikłałeś, dobiegła albo dobiega końca. Następuje wyzwolenie od dręczących cię problemów. Wychodzisz z trudnej sytuacji. Jeśli jeszcze nie czujesz się zupełnie bezpieczny, dalej zachowaj czujność. Jeżeli już jesteś bezpieczny, zapomnij o złej przeszłości. Nie pozwól, by stała się twoją obsesją i negatywnie wpływała na twoją percepcję rzeczywistości. Było - minęło, nie warto sobie tym zaprzątać głowy. Inaczej znowu uwikłasz się w niepotrzebne problemy. Procesy prawne, przestępstwa i dramaty uczuciowe odpadają i zanikają. Przebacz sobie i innym.
	Każdemu zdarzają się błędy na jego drodze do wolności. Kto potrafi wyzwolić się ze swoich błędów, umie zapomnieć o złej przeszłości i powrócić do zwykłego, codziennego życia. Gdy burza oczyszcza atmosferę, pozwala wybaczać błędy i umożliwia właściwe usuwanie skutków pomyłek. Możesz się odprężyć po przebytych doświadczeniach. Niewątpliwie coś straciłeś, ale nie martw się, teraz niechybnie nastąpi rozkwit. Ale żeby tak było, potrzebujesz poparcia. Jeżeli będziesz je miał od samego początku, powodzenie przyjdzie szybko. Jeśli jednak nie znajdziesz go od razu, nie przejmuj się tym, zastanów się, kto mógłby ci pomóc.''', \
'1a':'''Nie ma żadnej winy. ''', \
'1b':'''Uwolniłeś się z kłopotów. Wycisz się i w spokoju wracaj do sił. ''', \
'2a':'''* Upolowane trzy lisy. Otrzymuje złote strzały. Niezłomność przynosi szczęście. ''', \
'2b':'''Aby przywrócić porządek, należy obezwładnić prowokatorów, którzy siecią intryg omotali przywódcę. Trzeba dokonać tego w sposób jasny i prosty, dysponując mocą nieskazitelności, tak aby nie wywołać niepotrzebnych podejrzeń. ''', \
'3a':'''Gdy ktoś ugina się pod swoim ciężarem i mimo to na wozie jedzie, zachęca tym rabusiów, by doń przyszli. Wóz pełen skarbów przyciąga złoczyńców. Jeśli nie porzuci swej ścieżki, dozna upokorzenia. ''', \
'3b':'''Zajmowanie eksponowanego stanowiska oparte na przesadnym wyobrażeniu o sobie, a nie poparte wiedzą i doświadczeniem przyciąga uwagę złoczyńców. Kto korzysta z niezasłużonych przywilejów, wcześniej czy później pożałuje tego. Jeśli będziesz się upierał przy tym wozie, później będziesz żałował. ''', \
'4a':'''Uwalnia duży palec u nogi. Przybywają godni zaufania przyjaciele. ''', \
'4b':'''W czasie, gdy znajdowałeś się w trudnych chwilach, uzależniłeś się od kogoś niezbyt godnego zaufania. Zanim zupełnie wyzwolisz się od złych wpływów, musisz uwolnić się od tej osoby. Ona jest łącznikiem między tobą a siłami zła. Zrezygnuj z niej, a wtedy będziesz mógł uzyskać zaufanie i otrzymać wsparcie od kogoś szlachetnego.
Pozbądź się nikczemników ze swojego otoczenia. ''', \
'5a':'''* Jeżeli nieskazitelny potrafi wyzwolić siebie, nadejdzie pomyślność. W ten sposób zdobywa szacunek i poważanie prostaków. ''', \
'5b':'''Twoje uwolnienie, o którym mowa w poprzedniej linii, wcale nie jest pewne. Zależy wyłącznie od ciebie. Musisz całkowicie zerwać z nikczemnikami, nie dlatego, że szukasz kompromisu, ale dlatego, że jesteś przekonany o słuszności takiego działania. Nie chodzi tylko o uniknięcie zagrożenia, ale o poprawę twojego losu. ''', \
'6a':'''Książę strzela do jastrzębia na wysokim murze i zabija go. Wszystko zmienia się na korzyść. ''', \
'6b':'''Żądny władzy nikczemnik wzniósł się wysoko i zdobył wysoką pozycję. Trzeba go wyeliminować. Może tego dokonać ktoś odpowiedni rangą i dysponujący właściwymi środkami. Uwalnia się tym samym od jego złych wpływów i usuwa wszelkie niebezpieczeństwa. Sprzyja to wszechstronnej poprawie. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram41 = {'title':'Umniejszenie', \
'ctitle':'Sun', \
'picture':'''Jezioro w środku góry. Pomniejszenie.
Wybraniec tłumi złe zachowanie i kontroluje swoje żądze. ''', \
'judgment':'''Bardzo fortunna, gdy umniejsza ze szczerością. Nie będzie błędów. Jest powrót. Niech trzyma się swojej ścieżki. Dobrze jest coś przedsięwziąć. Kiedy fundusze są ograniczone, co można ofiarować Niebu? Wystarczą dwie miseczki ofiarne. ''', \
'interpretation':'''	Można powrócić na właściwą drogę. Gniew, pycha, pożądanie, zazdrość, lenistwo, strach i zachłanność to najwięksi wrogowie człowieka na drodze do wolności. Jeśli się ich nie ujarzmi, one zniewolą człowieka. Trzeba nad nimi zapanować, jak również nad niskimi instynktami. Należy kultywować charakter. Utrata, której dotyczy ten heksagram, nie zawsze jest wydarzeniem niepomyślnym. Tutaj strata dotyczy tego, co w nadmiarze. Trzeba dostrzec korzyść, jaką daje umniejszanie, przez pozyskanie tego, co w niedomiarze. Wypływająca ze świadomej utraty szczerość intencji nie pozwala dojść do głosu wybujałym ambicjom. Dzięki temu zyskuje się harmonię i można podjąć każde działanie.
	W czasie skromnych środków ważna jest siła wewnętrznej prawdy; nie trzeba wstydzić się prostoty, to prostota jest źródłem wewnętrznej siły. Można wykonywać pewne posunięcia na próbę, bez większego zaangażowania. Siła wewnętrznych przekonań musi pokryć niedostatki zewnętrznego wystroju; siła treści musi poradzić sobie ze skromnością formy. Nie ma potrzeby prezentowania Bogu fałszywych pozorów. Głos serca ujawni się, choćby środki były niepozorne. Dobrze jest złożyć ofiarę, by zapewnić sobie przychylność siły wyższej. W wymiarze ekonomicznym zaciśnięcie pasa i ograniczenie wydatków pomoże zrealizować plany i uchroni od strat.''', \
'1a':'''Skończył dotychczasowe działanie i spieszy z pomocą przyjacielowi. Nie ma winy, ale musi dokładnie rozważyć, jak dalece innych można umniejszać. ''', \
'1b':'''Zostaw swoje sprawy i nie wahaj się pośpieszyć przyjacielowi z pomocą. Nie bądź samolubny, pomagaj z potrzeby serca i daj tyle, ile możesz. Przyjaciela poznaje się w biedzie. Zyskasz znacznie więcej, niż stracisz. Niech twoje działania będą szczere, a motywy bezinteresowne. Ale nie narzucaj się ze swoją pomocą, gdyż możesz zostać wykorzystany ponad miarę. ''', \
'2a':'''Stać prosto nie jest pomyślnie. Nie pomniejszaj tego, ale to powiększaj. ''', \
'2b':'''Sytuacja jest taka, że należy być elastycznym w postawie i działaniu. Nie trzymaj się sztywno poprzednich ustaleń, które mogą być nieadekwatne. Zmień strategię i zamiast coś robić mniejszym, rób to większym. ''', \
'3a':'''◆ Trzech podróżuje razem, jeden ubywa. Samotny znajdzie towarzysza wędrówki. ''', \
'3b':'''Trójkąty na dłuższą metę stają się nie do zniesienia. Ktoś musi odejść. To możesz być ty. Nie martw się. Utrata niektórych rzeczy sprzyja powodzeniu. Działając w pojedynkę, łatwiej i prędzej znajdziesz towarzystwo kogoś, z kim będzie ci po drodze. ''', \
'4a':'''Umniejsza swoje błędy. Pozyskuje radość. Nie ma winy. ''', \
'4b':'''Niewłaściwe zachowanie i działania odstręczają wszystkich dookoła. Należy zmienić swoje postępowanie. Utrata zła to zbliżanie się do dobra. Tracąc, ciągle się zyskuje, co wyzwala radość. ''', \
'5a':'''* Obdarowany dziesięcioma parami wyrocznych skorup żółwia. Nie odmawia, przyjmując dar. Największa pomyślność. ''', \
'5b':'''Dziesięć skorup żółwia to I Cing - najcenniejszy przedmiot ze świata rzeczy podarowany człowiekowi przez Niebiosa. Dar ten to pomost jednoczący Ziemię i Niebiosa, człowieka z Bogiem. Wyrocznia pomoże odczytać znaki i poznać los. Kto się do nich stosuje, osiąga wielkie szczęście. ''', \
'6a':'''◆ Gdy zyska bez strat innych - nie ma winy. Nieskazitelność przynosi najwyższe szczęście. Ma sługi, ale nie ma domu. Można podjąć każde działanie. ''', \
'6b':'''Zacny człowiek powiększa się, nie ujmując innym. W swoim działaniu jest bezinteresowny i obce jest mu wykorzystywanie innych do egoistycznych celów. Wzmacniając swoją pozycję, korzysta z pomocy ludzi życzliwych i lojalnych, którzy wiedzą, że szczęściem jest służyć takim ludziom, bo oni są sługami Niebios i wskazują drogę tym, którzy są sługami ludzi. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram42 = {'title':'Powiększenie', \
'ctitle':'Yi', \
'picture':'''Wiatr ponad gromem. Powiększenie.
Wybraniec wzmacnia swoje zalety, pozbywa się dostrzeżonych wad. ''', \
'judgment':'''Korzystne jest wykonać jakiś ruch.
Korzystne jest przebyć wielką wodę. ''', \
'interpretation':'''	Jesteś w sytuacji, gdy zebrałeś dość siły osobistej, by podjąć jakieś przedsięwzięcia. Być może to, o którym myślisz, pomoże ci zrealizować większe jeszcze zamierzenia. W każdym razie przyczyni się pozytywnie do twoich zamiarów, a być może to ono będzie lokomotywą ciągnącą twój pociąg. Jest to sprzyjający czas na podjęcie realizacji wielkich celów, czy przeprowadzenia znaczących zmian.
Należy go wykorzystać, żeby nie przegapić szansy rozwoju. Ludzie, którzy cię otaczają, są gotowi do poświęceń, co dodatkowo sprzyja szansom realizacji zadań. Ty sam również jesteś gotów do poświęceń. Będąc w sprzyjającej sytuacji, powinieneś dalej pracować nad sobą, by wyeliminować dostrzeżone u siebie błędy.''', \
'1a':'''Pomyślne będą wielkie czyny. Bardzo fortunna. Najwyższe powodzenie. Bez winy. ''', \
'1b':'''Jest to czas na dokonywanie wielkich czynów; będą udane. Posiadając poparcie wielkich mocy, może osiągnąć to, czego sam nie dokona nigdy. Będąc przy tym szczerym i bezinteresownym. może podjąć się dowolnie wielkich zadań. Ich realizacja, poparta wytężoną pracą, da pomyślne rezultaty. ''', \
'2a':'''* Obdarowany dziesięcioma parami wyrocznych skorup. Nawet sam król nie odmawia, przyjmując dar, i nie sprzeciwia się wyrokom, oddając cześć Bogu. Najwyższe szczęście. ''', \
'2b':'''Kto przyjmuje rady Niebios, powiększa swoje siły. Gdy jego moc współgra z prawami wszechświata, powodzenie jest gwarantowane. Na przeszkodzie nie staną żadne okoliczności, choć ktoś może występować przeciw niemu. Dopóki nie ulegnie zmianie relacja z dobroczyńcą, nic mu nie przeszkodzi. Nie lekceważ i nie zmarnuj szansy, którą posiadasz, tego „centymetra sześciennego szczęścia”, który każdy otrzymuje od losu. ''', \
'3a':'''Odnosi korzyści wskutek niesprzyjających wydarzeń. Pozostaje bez winy, jeśli jest uczciwy.
Trzyma się złotego środka i prezentuje pieczęć przed księciem. ''', \
'3b':'''Gdy czas jest korzystny, można odnieść pożytek także z niepomyślnych wydarzeń. Siła osobista, wewnętrzna moc poparta szczerością buduje prestiż i wzbudza szacunek. Choć inni mogli się poczuć dotknięci tym niefortunnym zdarzeniem, tobie to nie zaszkodzi, gdyż pozostajesz wierny sobie i jesteś uczciwy wobec nich. Oni to dostrzegają i uznają. ''', \
'4a':'''◆ Trzyma się złotego środka. Książę stosuje się do jego rad. Można go obdarzyć zaufaniem tak wielkim, żeby powierzyć mu przeniesienie stolicy. ''', \
'4b':'''Jesteś figurą. Posiadasz autorytet, który został uznany. Cenią cię za twoją mądrość i rozwagę. Posiadasz moc i prawdę w sobie. Tego nie można stracić. Można to tylko wykorzystać w szczytnym celu.
Dzięki temu, że jesteś w bliskim kontakcie z decydentem i posiadłeś jego zaufanie, masz możność wpływania na bieg rzeczy. Gdy odwoła się do twojej pomocy, nie możesz odmówić. Musisz przyjąć odpowiedzialność za wypełnienie wielkich zadań, które ci powierzy.
Nie bój się odpowiedzialności. Musisz wypełnić Tao tej linii. ''', \
'5a':'''* Czystość intencji to życzliwość, szczerość i hojność, którymi chce obdarzać. Jest na ścieżce serca. Nie ma co do tego wątpliwości. ''', \
'5b':'''Masz cnoty, które przysługują wielkim ludziom. Jesteś jak król, który obdarowuje lud swoimi dobrami. Roztaczasz swój charyzmatyczny wpływ dokoła. Inspirujesz innych, jesteś dla nich wyrocznią. ''', \
'6a':'''Traci swoje poparcie. Zmienia swoje przyjaźnie. Powiększenie zostaje wstrzymane. Obracają się przeciwko niemu. Ktoś go atakuje. Złowróżbna. ''', \
'6b':'''Gdy zajmuje się eksponowaną pozycję, nie można zmieniać swoich przyjaźni. Na takiej pozycji serce musi pozostać sługą obowiązku. W przeciwnym razie, ci którzy na niego liczyli, zawiodą się i straci ich sympatię. Może nawet ściągnąć na siebie gniew co bardziej porywczych. Inni wzgardzą nim. Nie wróży to nic dobrego. Nie możesz zawieść ich oczekiwań. Pozostań sobą i przyłóż się bardziej do swoich obowiązków. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram43 = {'title':'Przełom', \
'ctitle':'Kuai', \
'picture':'''Jezioro ponad niebem. Przełamanie.
Zerwanie stosunków. Zdecydowanie.
Wybraniec dzieli się swoją wiedzą. Baczy, by nie izolować się w swoich cnotach. ''', \
'judgment':'''Trzeba stanowczo odkryć i rzetelnie przedstawić sprawy na królewskim dworze. Ogłaszanie zgodnie z prawdą niesie niebezpieczeństwo. Należy zaalarmować sprzymierzeńców, ale nie używać broni. Korzystne jest się porozumieć. ''', \
'interpretation':'''	Gdy do głosu dochodzą namiętności, mącą rozum i spokój.
Łyżka dziegciu niszczy beczkę miodu. Nie każdy człowiek jest kryształowo czysty. Bazując na nie do końca usuniętych, ciemnych skłonnościach, jeden niegodziwiec w sferach władzy może usidlić ludzi dobrych i zacnych, chcących przeprowadzić konieczne reformy. Ażeby nie dopuścić do ich upadku, należy niezwłocznie ujawnić intryganta i jego spisek. Należy jednak być ostrożnym, choć trzeba zachować stanowczość i zdecydowanie. Nie należy używać przy tym siły, gdyż może to być źle zrozumiane i stać się wodą na młyn nikczemnika. Nie wolno wchodzić w otwarty konflikt, bo daje to szansę złu. Trzeba powiadomić i spokojnie uświadomić otoczenie o grożącym niebezpieczeństwie i niecnych zamiarach spiskowca. Walcząc ze złem, trzeba być bezkompromisowym i kierować się dobrem.
To, co się dzieje, jest nieuchronne, dlatego właściwą postawą jest spokojna, pogodna i chłodna stanowczość. Zasada ciemna zostaje wyparta i obiektywnie pokonana. Nie wolno, zdając sobie sprawę z niebezpieczeństwa, udawać, że się go nie dostrzega, zachowując swoje spostrzeżenia dla siebie. Podobnie jak nie należy trzymać nagromadzonych dóbr tylko dla siebie, a dobrze jest dzielić się nimi z innymi. Dotyczy to zarówno dóbr materialnych, jak i duchowych.
Aby słowa miały znaczenie, a rządzenie było skuteczne i łatwiejsze, dobrze jest sporządzić stosowne dokumenty pisane.
	Czas obiektywny heksagramu: 20 IV + 20 V, środek wiosny.''', \
'1a':'''Siła palców stóp pozwala ruszyć, ale nie dojść. Ruch naprzód skończy się upadkiem. Wina. ''', \
'1b':'''Kto podjął decyzję o przełomowym znaczeniu, niech wie, że jeszcze nie jest należycie przygotowany. Stojąc po kostki w błocie, można postąpić naprzód, ale gdy brak sił, nie można pokonać oporu materii i inicjatywa działania kończy się porażką. Dalsze postępowanie naprzód spowoduje, że ugrzęźnie już na samym początku przełomu. ''', \
'2a':'''Oręż w pogotowiu w nocy. Zachowuje czujność.
Wołanie o pomoc powstrzymuje napastników. Nie należy się bać. ''', \
'2b':'''Ktoś dybie na twoją osobę, chce pogwałcić twoje prawa. Niepostrzeżenie prowadzi przeciw tobie działania. Musisz zachować wyjątkową czujność. Gdy zwrócisz się o pomoc, nastąpi przełom i zdołasz udaremnić niecne zamiary. Nie daj się zastraszyć. ''', \
'3a':'''Zawziętość na twarzy. Przebywa w obozie wroga. Biorą go na języki. Jest sam na deszczu. Zagrożenie. Nie ma winy. ''', \
'3b':'''Jest jedynym sprawiedliwym pomiędzy niegodziwcami. Ci, którzy patrzą na to z boku i walczą ze złem, nie mogą pojąć, że przebywając pośród zła, można się jemu oprzeć. Dlatego odnoszą się do niego z nieufnością. Nie rozumieją, że nie każdy musi ulec złu, kiedy go ono zewsząd otacza. Nie wiedzą, iż skoro tam przebywa, ma do tego ważne powody i że cały czas, wbrew pozorom, pozostaje,sobą dzięki swej wewnętrznej mocy, której oni nie posiadają. Dobrego karczma nie zepsuje, złego kościół nie naprawi. ''', \
'4a':'''Zdarta skóra na udach. Ledwo chodzi. Dając się poprowadzić jak owca, rozprasza wyrzuty sumienia. Pozostaje głuchy na te słowa. ''', \
'4b':'''Nie bądź osłem. Upór jest nie na miejscu. Jeśli będziesz forsował swoje działania, popadniesz w jeszcze większe kłopoty. Samowolne działania niepoparte wiedzą o swoim faktycznym położeniu, prowadzą do klęski. Powinieneś zdecydowanie porzucić taką postawę. Ty jednak jesteś zaślepiony swoim uporem i uważasz, że ta wyrocznia ciebie nie dotyczy. Nie chcesz słuchać dobrych rad. Pożałujesz tego. ''', \
'5a':'''* Wyrywając i paląc chwasty, trzeba być niezłomnym i stanowczym. Trzyma się środka. Bez winy. ''', \
'5b':'''Hydra zła, która opanowała ośrodki władzy, jest trudna do pokonania. Walka z nią przypomina pracę Syzyfa. Gdy odetnie się jedną głowę, zaraz pojawia się nowa, następna. Ośmiornica zła, która podąża za hydrą, jest immanentną cechą słabego systemu społecznego. Jednak nie można się załamywać. Należy wytrwale trzymać się swoich zasad i stanowczo zwalczać dostrzeżone zło. Tak jak trzeba uprawiać ziemię, by nie rosły na niej chwasty, tak trzeba kultywować tradycje i dobre obyczaje, żeby nie pojawiały się chwasty społeczne. Jeśli już chwasty się pojawią, należy wyrwać je i spalić. ''', \
'6a':'''◆ Nikt nie reaguje na wołania. Pomoc nie nadchodzi. Złowróżbna. ''', \
'6b':'''Niebezpieczeństwo niepostrzeżenie stało się bardzo groźne. Coś niepozornego, co cały czas czyhało w ciemnym, ustronnym miejscu, urosło nagle do niebotycznych rozmiarów i pochłonęło cię całkowicie. Nie zachowałeś należytej ostrożności. Teraz wołanie o pomoc jest już spóźnione. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram44 = {'title':'Spotkanie', \
'ctitle':'Kou', \
'picture':'''Wiatr wieje pod niebem. Pokusa. Wabik.
Wyjście naprzeciw.
Książę rozsyła swoje rozkazy na cztery strony świata. ''', \
'judgment':'''Spotkanie z silną i zawziętą kobietą.
Nie należy się z nią żenić. ''', \
'interpretation':'''	W swojej drodze spotykasz różnych ludzi, a niektórzy z nich mogą ci pomóc zrealizować twoje cele. Takich szukaj i przyjmuj do grona swoich przyjaciół. Układy i przyjaźnie z ludźmi inteligentnymi będą cię stymulować i podnosić na duchu. Od czasu do czasu napotykasz też przynęty, które wodzą cię na pokuszenie. Nie martw się tym. To jest immanentną cechą systemu. Służy dla twojego dobra, abyś mógł sprawdzić swoją siłę osobistą i moc ducha. Ta akurat pokusa ma związek ze zbytnim nagromadzeniem się czynnika yang, któremu nie powinieneś ulegać. Naturalnym jest, że przyciąga on element yin. Musisz być odporny i nie dać się wciągnąć w tę sytuację. Liczy się umysł, a nie piękno. Musisz zachować właściwą postawę i nie pozwolić, aby siła yin zdobyła nad tobą dominację. Nie znajduj w tym upodobania, nawet gdy wygląda nieszkodliwie i zachęcająco. Ponieważ siła yin jest potrzebna do rozwoju siły yang, należy jej używać, ale w odpowiednich dawkach i proporcjach. Wtedy można wykorzystać ją do wzmocnienia elementu yang. Ale uważaj, nie igraj z nią niefrasobliwie. Lepiej więc w zarodku niszczyć zło, gdyż nawet jeden agresywny elemernt yin, a z takim masz tu do czynienia, może zniszczyć wiele elementów yang. Furia wygląda tak niewinnie, ale nie wolno ulec takiej sile yin. Wyjście naprzeciw jest konieczne dla pierwiastków, które się wzajemnie uzupełniają i są sobie przeznaczone. Jednakże musi ono być wolne od nieczystych, niskich motywów, bo inaczej stanie się czymś złoczynnym. Jeśli nie potrafisz wyjść jej naprzeciw i sprzeciwić się, przywiąż się do słupa jak Odyseusz do masztu statku i nie daj się uwieść zwodniczemu śpiewowi syreny.
	Czas obiektywny heksagramu: 20 VI - 20 VII, przesilenie letnie.''', \
'1a':'''◆ Przywiązany do słupa. Ruch w jakąkolwiek stronę przynosi fiasko. Wychudzona świnia wałęsa się po okolicy. Zachowaj swoją ścieżkę. ''', \
'1b':'''Należy okiełznać rumaka męskich pragnień. Gdy siła yang przybierze ponad miarę, wtedy puszczają hamulce i mąż podąża samowolnie, ściągając na siebie nieszczęście. Siła yin tu podobna jest do wygłodzonej świni. Nadmierne chuci należy zwalczać z całą mocą. ''', \
'2a':'''* Ryba w pojemniku. Nie ma zmartwienia. Niesprzyjające dla gości. ''', \
'2b':'''Tu jest coś cennego. Ale pójść tam w odwiedziny, by z tego skorzystać, jest niekorzystne. Niedobry czas na audiencję. ''', \
'3a':'''Zdarta skóra na pośladkach. Ból w krzyżach.
Ledwo chodzi. Nie ma wielkiego zagrożenia. ''', \
'3b':'''Ktoś jest w długiej podróży i znosi jej trudy. Cel wyznacza poświęcenie. Jeśli wytrwa, odniesie sukces w wyprawie. ''', \
'4a':'''Nie ma ryby w pojemniku. Złowróżbna.''', \
'4b':'''Tu brak jest czegoś cennego. Zbytnia swoboda doprowadziła do tego, że sytuacja wymknęła się spod kontroli. Siły ciemności, które wydawało się, że zostały opanowane, przejmują inicjatywę. Dałeś się im uwieść. One wezmą, co chcą, i pozostawią cię z pustymi rękami. ''', \
'5a':'''* Melon pieczołowicie zawinięty w liście. Skrywa swoją niebiańską naturę. Owoc sam spada z nieba. ''', \
'5b':'''Nieoczekiwane dary lub zrządzenia losu. Może to być świetny pomysł, który się pojawił jakby z nieba. Można go z powodzeniem użyć jako wzór. Te niespodziewane dary należy zazdrośnie chronić przed niepowołanymi. ''', \
'6a':'''Wychodzi na spotkanie z nastawionymi rogami.
Ma poczucie winy. Nie zrobi błędu. ''', \
'6b':'''Należy aktywnie wystąpić przeciw zarozumialstwu i pysze. Twoja agresywna postawa jest uzasadniona. Choć możesz odczuwać żal z powodu tego, że się uniosłeś, to jednak taka reakcja jest usprawiedliwiona, gdyż bronisz w ten sposób swojej wolności. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram45 = {'title':'Zgromadzenie', \
'ctitle':'Czui', \
'picture':'''Jezioro nad ziemią. Woda gromadzi się nad ziemią.
Jezioro dusz. Zbieranie się razem.
Wybraniec szykuje swój oręż, aby być gotowym na nieprzewidziane. ''', \
'judgment':'''Ukończone. Król zdąża do świątyni, by złożyć ofiarę.
Powodzenie, jeżeli gotów jest zapłacić cenę. Wielka ofiara stwarza pomyślny los.
Dobrze jest zobaczyć się z wielkim człowiekiem; wtedy gromadzenie ma właściwą podstawę. Korzystne jest wykonać jakiś ruch, gdyż to jest oddanie się nakazom nieba. ''', \
'interpretation':'''	Sytuacja zbierania tego wszystkiego, co buduje prawdziwe szczęście. To zbieranie jest jak budowanie wewnętrznego, własnego sanktuarium, niezależnie od świątyni, w której zbiera się ze sprzymierzeńcami. W świątyni tej będzie mógł dotrzeć do korzeni swojej natury, w których zawarta jest cała mądrość gatunku ludzkiego. Kiedy ze sobą łączą się przodkowie, czas teraźniejszy i niebiosa, wtedy można dokonać wielkich czynów. Należy gromadzić ludzi wokół siebie dzięki swym wewnętrznym walorom. Silne centrum tworzy silną grupę, słabe rodzi swary i wewnętrzne antagonizmy. Im większa grupa, tym więcej niebezpieczeństw. Lider musi umieć im przeciwdziałać.''', \
'1a':'''Ambiwalencja uczuć powoduje chaos i rozproszenie. Głośny krzyk sprowadza sprzymierzeńca. Niebawem będzie się radować. ''', \
'1b':'''Należy się zdecydować na wybór lidera, który poprowadzi sojuszników do zwycięstwa. Tylko silny i aktywny ośrodek władzy jest w stanie zgromadzić potrzebne do odniesienia sukcesu siły. Kto chce być przywódcą, musi z kolei przekonać oponentów do swojej wizji i pociągnąć zwolenników za sobą. Wtedy razem osiągną powodzenie. ''', \
'2a':'''Niech da się poprowadzić sojusznikowi. Nie zrobi błędu. Gdy jest szczery, wystarczą małe ofiary. ''', \
'2b':'''Kiedy gromadzi się siły do realizacji celu, nie należy postępować autorytarnie, ale zdać się na doświadczenie i znajomość rzeczy swoich doradców. Jeśli jest uczciwy, to wiele nie kosztuje. Niech będzie świadom, że postępując w ten sposób, gromadzi niewidzialne, tajemnicze siły dobrej energii, co sprzyja realizacji jego zamiarów. ''', \
'3a':'''Gromadzą się i wzdychają na myśl o stratach.
Nie ma z tego korzyści. Posuwa się do przodu. Doznaje lekkiego upokorzenia. ''', \
'3b':'''Gdy gromadzi się w imię dobra, nie należy opłakiwać poniesionych strat. Idąc dalej tą drogą, spotyka się z niewielkim upokorzeniem, ale droga jest słuszna. Należy iść ku centrum zbierając po drodze sojuszników. W ten sposób można dotrzeć w okolice władcy. ''', \
'4a':'''Wielkie powodzenie. Nie będzie błędu. ''', \
'4b':'''Twoje położenie jest korzystne. Tak trzymać! Jesteś figurą w tej sytuacji i prawą ręką władcy. Będąc członkiem większej grupy, działasz w jego i jej imieniu. Twoje zadanie to zintegrowanie sił pod wspólnym berłem. Pozostań taki, jaki jesteś, szczery, wierny swoim zasadom i bezinteresowny. Ta linia oznacza pomyślny los i szczęśliwe zakończenie dzieła. ''', \
'5a':'''* Gromadzą się wokół figury. Ukończona pozycja. Przewodzi im, przekonując niedowiarków. Korzystne są niezłomność i zdecydowanie. Znikają wyrzuty sumienia. ''', \
'5b':'''Ludzie w grupie samorzutnie gromadzą się wokół niego i jego dzieła. Nie wszyscy są do końca szczerzy w swoich intencjach, szukając indywidualnych korzyści. Należy porozmawiać z nimi, by poznać ich motywy i w razie potrzeby wyrazić otwarcie swoje zastrzeżenia.
Trzeba przekonać ich do sprawy, co będzie wymagało nie lada wysiłku, ale dokonanie trwałego dzieła tego wymaga. ''', \
'6a':'''Zamieszanie, płacz i łzy. Nie zrobisz błędu. ''', \
'6b':'''Zgromadzenie może być źle lub niewłaściwie zrozumiane. Dzieje się tak, gdy nie potrafi rozróżniać między dobrem a złem. Wtedy gromadzenie zamienia się w zamęt i wywołuje zawód, co wyraża się poprzez płacz. Kto nie dostrzega dobrych intencji w gromadzeniu, narażony jest na taki koniec. Kto ma dobrą wolę, pozostaje bez winy. Tak wygląda sąd ostateczny. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram46 = {'title':'Dojrzewanie, drzewo', \
'ctitle':'Szeng', \
'picture':'''Drzewo wzrasta, tkwiąc korzeniami w ziemi.
Wydobywanie się i dojrzewanie. Pięcie się w górę.
Wybraniec wznosi wielkie konstrukcje, opierając się o rzeczy małe. ''', \
'judgment':'''Dojrzewanie niesie najwyższe powodzenie, bez przeszkód.
Należy skonsultować się z wielkim umysłem.
Wyrusza na południe po szczęśliwy los. ''', \
'interpretation':'''	Człowiek dojrzały dokładnie wie, czego chce. Wie, jak przeprowadzić swoją wolę, ale nie ma w tym nic z egoizmu, gdyż plany zgodne są z naturalnym biegiem rzeczy. Dobre ziarno dojrzewa w harmonii ze swoim otoczeniem, przystosowując się do zastanych warunków, nie próbując na siłę realizować swojej woli istnienia.
Dlatego nie wywołuje wokół siebie konfliktów. Człowiek powinien wzrastać jak drzewo. Musi mieć korzenie, to znaczy, nie podążać za tym, co dalekie, bo tak czynią słabi; nie może ignorować tego, co bliskie, gdyż tak również czynią słabi. Gdy pojmie, że jego korzenie są tu, gdzie się znajduje, i że one wyznaczają jego los, wówczas znajduje się na drodze do rzeczy wielkich. Należy stopniowo budować swoją potęgę, mając ostoję w swoich korzeniach. Tak trzeba ćwiczyć swoją wolę. Powinien mieć mądrego przewodnika, który go poprowadzi. Może to I Cing? On jest wśród jego przyjaciół.''', \
'1a':'''◆ Dojrzewanie oparte na zaufaniu. Wielka pomyślność. ''', \
'1b':'''Przygotowując się do wielkich czynów, nabiera doświadczenia w otoczeniu sprzyjających zwierzchności. Zaczyna od mało znaczącej pozycji, ale mając odpowiednie poparcie, może się spodziewać oczekiwanej promocji. ''', \
'2a':'''Wystarczy nawet mały dar, jeżeli jest szczery. Nie będzie błędu. ''', \
'2b':'''Przyjrzyj się żołędziowi i spójrz na dąb. Trzeba umieć dojrzeć w rzeczach małych - rzeczy wielkie. Na razie jeszcze dysponujesz skromnymi zasobami i możliwości twoje są ograniczone. Jednak gdy będziesz nadal zachowywał swój uczciwy charakter, możesz liczyć na tego, który zajmuje wyższą pozycję. To silny człowiek, który nie pasuje do swego otoczenia. Dostrzega on twoje zaangażowanie i na razie nie będzie wymagać więcej, niż możesz z siebie dać. ''', \
'3a':'''Dojrzewanie w pustym miejscu. ''', \
'3b':'''Jesteś tutaj sam. Jesteś pionierem, który zaczyna wszystko od początku. Twoje działania nie napotykają żadnego oporu. Wydaje ci się to niezwykłe i co najmniej dziwne, ale nie zaprzątaj sobie tym głowy. Wykorzystaj ten okres, aby po tej linii najmniejszego oporu dojść najdalej, jak możesz. ''', \
'4a':'''Król składa z nim ofiarę na górze Czi. Fortunna. Nie ma winy. ''', \
'4b':'''Proces dojrzewania jest zakończony. Dorosłeś i teraz jesteś w bliskich stosunkach z ludźmi ze szczytów hierarchii społecznej. Twoje wysiłki i trud zostają nagrodzone, a ty stajesz się równoprawnym członkiem elity. Ponieważ zajmujesz eksponowaną pozycję, masz możność wpływu na bieg rzeczy. Wykorzystaj to. ''', \
'5a':'''Stopniowe dojrzewanie. Korzystna jest niezłomność. Trzymaj się swojej ścieżki, a wzniesiesz się do nieba bram. ''', \
'5b':'''Wielki sukces można osiągnąć tylko przez stopniowe nabieranie doświadczenia. Trzeba budować mocne podstawy sukcesu na małych doświadczeniach, które są jak schody prowadzące do poszczególnych pięter sukcesu. Nie należy nasilać działań i przeskakiwać ostatnich etapów, choćby wydawało się, że sukces jest już na wyciągnięcie ręki. Trzeba dostojnie sięgnąć po to, co i tak należy do ciebie, jak po koronę, która wieńczy twoje wysiłki. Dlatego nie przyspieszaj i krocz dalej swoim rytmem, zaszczyty nie uciekną. ''', \
'6a':'''Dojrzewanie w ciemności. Niezbędna jest wytężona uwaga. ''', \
'6b':'''Gdy proces dojrzewania następuje w ciemności, niewiele wiadomo o otaczającym świecie. Gdy idzie się przez zupełnie nieobliczalny świat, brakuje rozeznania, dokąd się zmierza i nie wiadomo, co pozostawiło się za sobą. W takim przypadku można polegać tylko na sobie i sile swojej woli i determinacji. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram47 = {'title':'Okowy', \
'ctitle':'K’un', \
'picture':'''Jezioro ponad rzeką. Wyczerpanie. Opresja.
Wybraniec wybiera i realizuje cele, do których może dążyć przez całe życie; choćby i życie ryzykował, aby postępować ze swoją wolą. ''', \
'judgment':'''Powodzenie. Wielki człowiek trzyma się swojej ścieżki, nie popełnia błędów, dlatego przynosi szczęście.
Nie ma zaufania do słów. ''', \
'interpretation':'''	Pod jeziorem otwiera się czeluść i woda spływa do podziemnej rzeki. Jest to czas ucisku i ciężkiej próby charakteru. Otoczenie niestety nie traktuje go poważnie. Mimo to optymizm pozwoli przetrwać trudny czas i przezwyciężyć przeszkody. Należy pozostać szlachetnym; mimo że jego słów się nie szanuje, nikt nie będzie nikogo obwiniał.
	Niekorzystny czas dla ludzi słabych. Każde działanie wzmacnia ich spętanie poprzez własne wyobrażenia, lęki, pożądania, emocje i przywiązania. Nie umieją oni porzucić ich bez żalu jako rzeczy przemijających. Element yang jest w opresji spowodowanej przez element yin. Efekty ich działań pochłaniane są przez iluzje świata wyobrażeń, za którym podążają. Zbytnio angażują się w pogoń za zyskiem i dobrami materialnymi. Im więcej i szybciej gonią, tym mniej mają czasu na życie. Powoli stają się automatami sterowanymi przez system złudzeń i pożądań. Nie zauważają nawet, kiedy ich życie staje się odhumanizowanym kieratem. Mądry człowiek stara się unikać spętania w okowach, rozwijając swą prawość oraz odrzucając bez żalu zbędne imaginacje, iluzje i emocje. Jest oszczędny w słowach, bo wie, że w obecnej sytuacji i tak mu nie uwierzą.''', \
'1a':'''Przywalony drzewem w mrocznej dolinie. Leży tam przez trzy lata. ''', \
'1b':'''Niepowodzenia, które cię prześladują, mają źródło i przyczynę w tobie samym. Uparłeś się odnieść sukces w świecie materialnym, a teraz coraz bardziej dochodzi do twojej świadomości, że ta myśl cię przytłacza i więzi w ciemnych rejonach psychiki. Nie wiesz, że twoje spętanie myślowe, blokujące wszelki ruch, jest wytworem twojego umysłu, który dał się zwieść fałszywym wyobrażeniom o naturze rzeczywistości. Żeby się wyzwolić z okowów swoich myśli, musisz najpierw bez żalu porzucić myśl o wzbogaceniu, a potem stopniowo możesz uwalniać się z krępujących cię więzów. Tylko ludzie silni potrafią przetrzymać ciężkie czasy, które cię czekają. Musisz być silny i nie poddawać się rozpaczy. ''', \
'2a':'''* Okowy nałożone podczas uczty. Nadchodzi dostojnik, niesie królewskie szaty. Gdy wyruszy na wyprawę, spotka go niepowodzenie. Nie ma winy. ''', \
'2b':'''Ktoś znaczący ucieka się do przemocy, abyś został jego terminatorem. Powinieneś przyjąć propozycję i zacząć wspólne działanie, nawet gdy wiesz, że ta praktyka poniesie fiasko. Nie ma w tym twojej winy. ''', \
'3a':'''Przygniótł go kamień. Leży w chaszczach. Wraca do domu i nie widzi żony. Złowróżbna. ''', \
'3b':'''Działa samowolnie i sam stwarza sobie przeszkody, których nie ma, albo wyolbrzymia te istniejące naprawdę. Jest zaabsorbowany swoimi wewnętrznymi problemami tak bardzo, że nie widzi, co się wokół niego dzieje - nie dostrzega prawdziwego źródła życia i radości.
I do tego jest obojętny na dobre rady. Nie wróży to nic dobrego. ''', \
'4a':'''Odsiecz nadciąga powoli. Jest otoczony w złotym rydwanie. Upokorzenie. Po końcu pomyślna. ''', \
'4b':'''Jest w wyjątkowo niebezpiecznej sytuacji, nie może właściwie liczyć na pomoc. Niech przyjmie ze spokojem swój los. „W końcu moje trwanie”. To jest jedna z najgorzej wróżących linii w Księdze. ''', \
'5a':'''* Odcięto mu nos i stopy. Spętany przez dostojnika. Zdrada. Stopniowo powróci radość. Należy odbyć rytuały ofiarne. ''', \
'5b':'''Jesteś za dobry na otoczenie, w którym się znajdujesz. Twoja szczera, bezinteresowna postawa drażni zarówno tych z dołu, jak i tych na górze. Tu i tu bowiem nie brak egoistycznych sił. Chcą się ciebie pozbyć, bo jesteś dla nich kamieniem obrazy. Jesteś zbyt nieskazitelny, zbyt doskonały. Spodziewaj się wiarołomstwa twoich zwierzchników. Ale nie martw się. Jest to jednocześnie początek twojego wyzwolenia, dlatego powinieneś uczcić to ceremonią ofiarną. ''', \
'6a':'''Spętany przez winorośl na skale mówi do siebie: „Jeżeli się poruszę, pożałuję”. Jeżeli pożałuje tych słów i ruszy naprzód, wykona dobre posunięcie. ''', \
'6b':'''Okowy nie są okowami, co najwyżej więzami. Realne pęta są bardzo kruche. Łuski spadają z oczu; pułapka nie jest pułapką, tak jak jest nią samo wyobrażenie o niej. Strach ma wielkie oczy. W takiej sytuacji należy podjąć zdecydowaną decyzję i ruszyć naprzód. Brak stanowczej decyzji wybawienia się z opresji rodzi wyrzuty sumienia.
Droga w zasadzie jest wolna, a pułapka jest tylko pozorna. Chociaż tego nie wiesz, siła opresji już opadła. Możesz pójść naprzód. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram48 = {'title':'Studnia', \
'ctitle':'Cing', \
'picture':'''Woda nad drzewem. Studnia. Źródło.
Wybraniec aktywizuje ludzi i inspiruje do budowania wspólnoty. ''', \
'judgment':'''Król może przenieść stolicę, ale studnia pozostaje tam, gdzie była; nie można jej przenieść. Ci co odchodzą i ci co przychodzą jednakowo czerpią ze studni.
Jeśli wysycha, i człowiek się nie napije. Złowróżbna, jeżeli nie napełni wiadra. ''', \
'interpretation':'''	Heksagram ukazuje trwałe urządzenie świata. Przedstawia związki człowieka z naturą i przeszłością. Ludzka moc nie jest w stanie tych uwarunkowań zmienić, dlatego wyznaczają one zakres dostępnej człowiekowi wolności. Studnia stanowi źródło wody, z którego człowiek może czerpać nieustannie. Z darów natury można korzystać, ale można je też zlekceważyć. Choć w świecie ustawicznych przemian ciągle zmieniają się państwa i prawa, a na przestrzeni wieków w teatrze życia zmieniają się dekoracje, to jednak niezmienne pozostają prawa natury i psychologii ludzkiej. Dla człowieka sprzed wieków, dla ludzi dzisiejszych i dla tych, którzy przyjdą później, dostępna jest ta sama studnia natury ludzkiej. Tego nie można zmienić. Kto bywał w różnych miejscach i poznawał różnych ludzi, jest świadom, że na całym świecie ludzie nie różnią się między sobą i wszędzie można spotkać te same typy ludzkie. Kto je poznał, ten wie, że w każdym człowieku znajduje się czynnik duchowy, obraz, cząstka Boga, który jednak dla większości ludzi pozostaje niedostępny ich świadomości lub jest opatrznie przez nich rozumiany. Kto posiada wiedzę o naturze ludzkiej, może być nauczycielem dla innych, wykorzystując swoje doświadczenie, intuicję i szczerość intencji. Można zaufać swojej intuicji, jeśli wynika ona z dogłębnej autoanalizy i została potwierdzona w kontaktach z innymi ludźmi.
Mistrz, który opanował wiedzę o głębi natury ludzkiej i nie pozwolił sobie zatonąć w jej otchłani, powinien wspomagać w rozwoju innych, czyniąc z nich swoich uczniów. Każdy może się napić z jego studni, a woda jest krystalicznie czysta i ma wyborny smak. Coś, co jest ponadczasowe, oprze się wszelkim zmianom, zachowując swoją świeżość przez wieki. Taką studnią jest I Cing. Zaczerpnij z tej wielkiej studni mądrości, by zwiększyć zasoby swej wiedzy i poprawić swoją pozycję. W zasięgu twojej ręki są bogactwa, i tylko od twojej woli zależy, czy będziesz umiał z nich skorzystać.''', \
'1a':'''Błoto w studni. Nie można pić wody. ''', \
'1b':'''Sądzisz, że coś wiesz i coś osiągnąłeś i możesz wpływać na innych, ale tak naprawdę z twojej studni nie można korzystać. To się nazywa zarozumiałość. Poszukaj lepiej nauczyciela, abyś pozbył się swojej niewiedzy i wewnętrznego zamętu. ''', \
'2a':'''Wyciąga żaby ze studni. Wiadro przecieka. ''', \
'2b':'''Wiadro jest nieszczelne. Choć można korzystać ze studni, bo woda w niej jest już czysta, to jednak jest niedostępna, ponieważ nie ma czym jej czerpać. Sytuacja, gdy zacny człowiek pragnie dobra innych i chce im pomagać, ale nie potrafi wycofać się ze strefy złych oddziaływań. Może jest zbyt wygodny, a może zbyt niechlujny. ''', \
'3a':'''Woda w studni jest czysta, ale nikt jej nie pije. Zabiega o to, by można z niej czerpać. Szuka dostojnika. ''', \
'3b':'''Kto posiadł mądrość, powinien starać się o to, aby została spożytkowana. Trzeba wykazać inicjatywę, by można czerpać z jego studni. Należy zbliżyć się do ośrodka decyzyjnego, ażeby móc mu służyć swym doświadczeniem i wiedzą. Światły władca dostrzeże jego mądrość i będzie chciał korzystać z jego rad. ''', \
'4a':'''Ocembrowano studnię i przykryto daszkiem. Bez winy. ''', \
'4b':'''Czysta woda w studni, choć można z niej czerpać, jest niedostępna.
W takich chwilach nie należy angażować się w sprawy innych ludzi, ale trzeba odizolować się od świata i uporządkować swoje wnętrze.
W ten sposób woda w jego studni pozostanie czysta i gdy przyjdzie czas, będzie można z niej korzystać. ''', \
'5a':'''* W studni znajduje się źródło krystalicznie czystej wody. Można z niej czerpać. ''', \
'5b':'''Posiadł prawdę o szczęściu i wie, na czym polega szczęśliwe życie. Mógłby być wielkim autorytetem. Źródło jego mądrości płynie z wewnętrznej harmonii, spokoju i zrozumienia. Takiego skarbu nie można ukrywać. Należy go udostępnić światu. Nie wiadomo bowiem, gdzie jest skarb i kto potrzebuje z niego skorzystać. ''', \
'6a':'''Studnia nie jest przykryta. Można z niej czerpać bez przeszkód. Największe szczęście. ''', \
'6b':'''Kto poznał ludzką naturę, nie musi się obawiać, że pogrąży się w jej otchłani. Niosąc korzyści innym, nie rani siebie. Człowiek daje szczęście innym dzięki własnej wiedzy i aktywności. Każdy może z jego krynicy mądrości czerpać do woli, bo źródło to jest niewyczerpalne. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram49 = {'title':'Rewolucja, przewrót', \
'ctitle':'Ke', \
'picture':'''Ogień niżej, jezioro wyżej. Jezioro ognia.
Zmiana skóry. Przeobrażenie. Reformacja. Obalenie starego. Zmiana upierzenia.
Wybraniec, ustalając położenie gwiazd, wyznacza porę roku i czas. ''', \
'judgment':'''Właściwy dzień. Wtedy zawracaj. Pozyskaj zaufanie ludzi.
Wszyscy wierzą mu, gdy nadejdzie ten dzień. Jego przepowiednia spotka się z uznaniem. Najwyższe powodzenie bez przeszkód. Należy trzymać się swojej ścieżki. Korzystne jest zachować stałość i prawość do samego końca. Żal znika. ''', \
'interpretation':'''	Rewolucja dokonuje się zgodnie z prawami tego świata albo wtedy, gdy zawodzą już inne możliwości. Zbliża się istotny przełomowy dzień. Jeśli ktoś chce sam dokonać rewolucji, niech zastanowi się, czy rzeczywiście jest potrzebna. Jeżeli tak, to ponieważ niesie ona ze sobą zasadnicze zmiany, należy się do nich odpowiednio przygotować. Prawdziwa rewolucja, to znaczy taka, która ma się udać i rzeczywiście coś zmienić na lepsze, wymaga właściwego, wolnego od egoizmu przywódcy, cieszącego się poparciem ludu.
Najistotniejszym czynnikiem w przeprowadzeniu rewolucji jest wybór odpowiedniego czasu działania. Dlatego, ażeby mieć kontrolę nad rewolucyjnymi zmianami, potrzebna jest kontrola nad czasem.
Należy wybrać optymalny moment na rozpoczęcie przewrotu, zgodny z naturalnym biegiem rzeczy.
	Uporządkowanie rachuby czasu według kalendarza wskazuje trygram tuei, który oznacza wróżbitę, twórcę kalendarza. Jasne rozróżnianie, to trygram li, którego atrybutem jest jasność umysłu.
	Czas obiektywny heksagramu: 21 III - 20 IV, równowaga wiosenna — początek wiosny.''', \
'1a':'''Zawinięty w żółtą skórę wołu. ''', \
'1b':'''Rewolucja jest ostatecznością, gdy nie ma już innych możliwości.
Nawet wtedy, gdy chcesz pozmieniać wszystko, należy ograniczyć się zasadami złotego środka, którymi zawsze trzeba się kierować, powstrzymując się od nieprzemyślanych działań. Konieczna jest wyjątkowa roztropność. ''', \
'2a':'''Kiedy nadchodzi ten dzień, dokonuje gruntownej zmiany. Fortunna, gdy sztywno trzyma się zasad. Nie będzie błędu. ''', \
'2b':'''Jest to chwila rozpoczęcia rewolucji. Przewrót właśnie się zaczyna.
Ponieważ zmiany będą radykalne, należy być gruntownie przygotowanym, aby móc przeprowadzić je pomyślnie. Tylko odpowiedni lider może podjąć się takiego dzieła. Kto sam nie przygotuje się do zmian, nie zdoła ich urzeczywistnić. Trzeba stanowczo trzymać się własnej woli. ''', \
'3a':'''Niefortunna, gdy zbyt sztywno trzyma się zasad.
Jeśli zmiany, które chce przeprowadzić, przeanalizuje trzykrotnie - jest powrót. ''', \
'3b':'''Nie należy zbyt uporczywie trzymać się własnych ustaleń, bo wywołają tylko pozorny przewrót. Należy zastosować się do woli kogoś innego, kto wie, jak go przeprowadzić, ale tylko po dogłębnej analizie, że to jest słuszne. Nie każdy przewrót jest prawdziwą rewolucją. Nie każdy niszczy stare struktury prowadząc do realnych zmian.
Jest to przewrót pozorny, gdzie stare zastępuje się też starym, tylko ubranym w nową, odkrywczo brzmiącą ideologię. Prawdziwy przewrót zastępuje stare struktury nowymi, zgodnymi z duchem czasu.
Trzeba umieć odróżnić jeden od drugiego. Wtedy można skupić się na autentycznej przemianie. Jeśli pozostaje w przeszłości, dążąc do przyszłości, grozi mu utrata dystansu i porażka. ''', \
'4a':'''Znika poczucie winy. Oto jest powrót, który zmienia uprawnienia; pomyślne. Wierzą mu. Szczerość zmienia przeznaczenie na lepsze. ''', \
'4b':'''Odpowiedzialny za przewrót musi dysponować siłą osobistą, zajmować eksponowaną pozycję społeczną i posiadać autorytet. Czując za sobą poparcie ludzi, którzy mu ufają, może przeprowadzić prawdziwe, rewolucyjne zmiany. Jest to sytuacja, gdy stare, spróchniałe struktury, stwarzające pozór silnych, dają się łatwo obalić i zastąpić nowymi, opartymi na autentycznych wartościach. Obiecujące, jeżeli wystąpi przeciw strukturom władzy. ''', \
'5a':'''* Mocny człowiek przeobraża się jak tygrys. Ufają mu bez konsultacji z wyrocznią. ''', \
'5b':'''Emanuje energią i pewnością siebie, posiada wyraźny cel działania.
Wszyscy to dostrzegają. Patrzą na niego i wiedzą, że to on jest przywódcą, który ma przeprowadzić rewolucyjne zmiany. Nie ma co do tego żadnych wątpliwości, nie trzeba tego sprawdzać.
Pielęgnowanie siły yang, a tłumienie siły yin pozwala pozbyć się nabytego temperamentu i charakteru. Jest to pełne mocy przeobrażenie silnego człowieka. Nie trzeba odwoływać się do wyroczni, by być pewnym przeobrażeń. ''', \
'6a':'''Zacny człowiek przeobraża się jak lampart. Prostak zmienia tylko oblicze. Niefortunna, gdy sztywno trzyma się zasad. Obiecująca, gdy weźmie pod uwagę miejsce zamieszkania. ''', \
'6b':'''Prawdziwa przemiana to przemiana głęboka, docierająca do samej istoty człowieka i obejmująca całe jego jestestwo. Tak zmienia się człowiek zacny, dostrzegając jej konieczność i korzyści, jakie mu ona przyniesie dla rozwoju osobistego. Gdy się ma do czynienia z prostakami, trzeba mieć świadomość, że oni zmieniają się jedynie powierzchownie, chcąc tylko okazać posłuszeństwo i wyciągnąć egoistyczne korzyści. Ich prawdziwe intencje pozostają ukryte.
Ważne jest, aby wybrać właściwe miejsce na transformację. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram50 = {'title':'Naczynie ofiarne', \
'ctitle':'Ting', \
'picture':'''Ogień nad drzewem. Płonie stos ofiarny.
Ustanowienie nowego.
Wybraniec utwierdza swoje przeznaczenie, stabilizując swoją pozycję. ''', \
'judgment':'''Święte Naczynie Ofiarne na trójnogu. Spełniona ofiara. Najwyższa pomyślność. Wielki sukces.
Wrota są otwarte. ''', \
'interpretation':'''	Naczynie ofiarne reprezentuje zarazem materialistyczną podstawę rzeczy, jak i jej duchową nadbudowę. Chociaż duchowość bazuje na materialnym podłożu, to jednak pełni w stosunku do niego rolę nadrzędną i może sterować materialną podstawą. Nie mniej jednak oba czynniki są potrzebne do właściwego funkcjonowania osoby ludzkiej. Dzięki duchowości człowiek łączy się z niebiańskim światem, antycypując w ten sposób przyszłość gatunku ludzkiego.
Mając tego świadomość wie, że kulturowa nadbudowa służy duchowości i rozwojowi człowieka; dlatego znajdując swoje miejsce w rzeczywistości, tak by życie pozostawało w harmonii z losem (Tao), i zachowując pokorę wobec wszechświata, może wieść on podwójnie szczęśliwe życie, zarówno w świecie materialnym, jak i duchowym. Sprzyja temu kultywowanie chińskiej jogi.
	Każda nowa cywilizacja zaczyna od przeobrażania metalu. Jeśli pozostaje w łączności z Niebem, prawidłowo organizuje życie społeczne na nowo i dostarcza właściwej strawy dla wszystkich. Dzięki temu powstaje trwały porządek. Dbają o to książę wraz z mędrcem.
	W twoim zasięgu leży dokonanie, które uczyni cię wolnym. To jest bogactwo świętych narzędzi duchowych, które tryska ku twojej pomyślności i radości odkryć. Otwórz się na przyjęcie narzędzi duchowych. Masz prawo do ściśle określonych darów i talentów. Te narzędzia wskażą ci drogę i możliwości, jak współpracować z innymi ludźmi i własnym procesem życiowym. Otwórz się na nowe podejście do narzędzi twojego boskiego przeznaczenia i ich hojne dary.
Doprowadź do końca, co kiedyś zacząłeś. Pamiętaj, że Ty również jesteś narzędziem Ducha, wrotami Światła. Stań się ucieleśnieniem wrodzonej wspaniałości. Dostrzeż Ducha w sobie - swoje piękno i siłę.''', \
'1a':'''Naczynie ofiarne przewrócone do góry dnem. Dobrze jest oczyścić je z zaschniętego pokarmu. Przyjmuje kobietę razem z jej dzieckiem. Nie ma winy. ''', \
'1b':'''Dobrze jest zrobić istotne porządki w swoim otoczeniu i życiu. Można bez obawy zadbać o swoje sprawy osobiste. Tutaj obca krew nie zagraża. ''', \
'2a':'''Naczynie ofiarne wypełnione żywnością. Są zazdrośni, ale nie mogą zaszkodzić. Fortunna. ''', \
'2b':'''Jest na tyle mocny i nieskazitelny, że sukcesy, które odnosi, choć wzbudzają zazdrość u innych, nie mogą być podważone. Niech nie zwraca uwagi na bezinteresowną zawiść i nie okazuje im swojego poczucia wyższości. ''', \
'3a':'''Wymiana uchwytów naczynia ofiarnego. Rozminął się z ideą. Aktywność zostaje wstrzymana. Najlepsze kąski nie zostały zjedzone. Gdy spadnie deszcz, oczyści i da ulgę. Poczucie winy zaniknie. W końcu fortunna. ''', \
'3b':'''Zewnętrzne okoliczności sprawiają, że nie można skorzystać z dobrobytu. Jest w takim miejscu, gdzie nie może ujawnić swoich walorów. To, co najwartościowsze, nie zostaje spożytkowane. Dzieje się tak dlatego, że nikt go nie zauważa, ani nie darzy uznaniem.
Cały talent i zalety idą przez to na marne. Trzeba zmienić to niekorzystne położenie, a wtedy los się uśmiechnie. ''', \
'4a':'''Połamane nogi naczynia ofiarnego. Pokarm wylewa się i bruka księcia. Klęska. ''', \
'4b':'''Przyjął na siebie zbyt wielkie obciążenie jak na jego możliwości i nie wytrzymał ciężaru odpowiedzialności, która go przygniotła. Zadania przerosły jego siły, doświadczenie i charakter. Nie dorósł do nich.
Predestynowany do wielkich czynów, nie podołał im, okazując się niepoważny i niewiarygodny. Sprofanował drogocenny skarb, zmarnował swój „centymetr sześcienny szczęścia” darowany przez los.
Przegrał wszystko, a mógł osiągnąć tak wiele. Na myśl przychodzi cytat: „Miałeś chamie złoty róg, ostał ci się jeno sznur”. ''', \
'5a':'''* Naczynie ofiarne ma złote uchwyty. Trzymaj się swojej ścieżki. ''', \
'5b':'''Osiągnął harmonię, pojął istotę szczęścia. Jego szczęście jest trwałe. Postępuje zgodnie z naturalnym biegiem rzeczy. Teraz może spożytkować swój bezcenny pokarm, składając go w ofierze ludzkości.
Powinien znaleźć wspólników, którzy pomogą mu rozpowszechniać skarby jego mądrości. Jak król może podjąć odpowiednie decyzje. ''', \
'6a':'''* Naczynie ofiarne ma uchwyty z nefrytu. Wielkie powodzenie. Każdy ruch jest pomyślny. ''', \
'6b':'''Pokonał strach, osiągnął jasność widzenia, posiada moc. Jest człowiekiem wiedzy. Posiadł ją, a jego zrozumienie jest trwałe. Chociaż posiada moc, przekracza siebie i nie używa jej, zyskując w ten sposób wolność działania. Może realizować swoje wielkie cele. Staje się szlachetnym i mądrym przewodnikiem, który w swych wędrówkach porusza się z niezwykłym powabem i godnością, naucza i odsłania tajemnice. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram51 = {'title':'Piorun', \
'ctitle':'Dzen', \
'picture':'''Błyskawica rozświetla, grom uderza. Zaburzenie.
Wzdrygnięcie.
Wybraniec odczuwa lęk i drżenie. Bada siebie, porządkuje swoje życie i rozważa błędy. ''', \
'judgment':'''Piorun przynosi postęp. Kiedy bije piorun, najpierw wywołuje strach, potem śmiech. Przeraża na sto mi, ale wróżbita - książę Czou nie pozwala, by spadła ani kropla z kielicha ofiarnego, ani okruch z łyżki ofiarnej. ''', \
'interpretation':'''	Piorun sygnalizuje czas nieoczekiwanych i destrukcyjnych wydarzeń. W takiej sytuacji można sprawdzić siebie. Trzeba zachować wzmożoną ostrożność i opanowanie. Należy spodziewać się, że wstrząs spowoduje ogólną panikę, szok, może nawet doprowadzi do histerii. Nie można temu ulec i dać się włączyć w tę sytuację. Należy zachować spokój - nie upuścić łyżki. Rozświetlone przebłyskiem transcendentnej mocy wnętrze pozwala odkryć i usunąć złe myśli.
Należy pokornie przyjąć tę chwilę oświecenia i wykorzystać ją do powrotu na właściwą ścieżkę. Gdy przetrwa się ten wstrząs, będzie się można z niego śmiać.''', \
'1a':'''* Błysk i grzmot. Trwoga, a potem śmiech. Pomyślne. ''', \
'1b':'''Ten grzmot nie dotyczy ciebie. Nie musisz się obawiać. [Ostrzeżenie] nie jest skierowane do ciebie. Gdy zdasz sobie z tego sprawę, kamień spadnie ci z serca i odczujesz ulgę. Nowy duch, który wstąpi w ciebie, pozwoli ci osiągnąć powodzenie. ''', \
'2a':'''Nadchodzi grom. Sprowadza niebezpieczeństwo. Traci swoje skarby i musi wspinać się na dziewięć wzgórz. Niech nie rusza za nimi w pogoń. Odzyska je po siedmiu dniach. ''', \
'2b':'''Dotknęła cię materialna strata. Nie spodziewałeś się tego, dlatego jest to dla ciebie wstrząs. Wpadasz w furię i popadasz w rozpacz, traktując dobra materialne jako cząstkę swojej istoty. Podejmujesz wielkie wysiłki w celu ich odzyskania i w ten sposób niszczysz siebie samego. Czy myślisz, że tracąc dobra materialne, straciłeś sens życia? Nie pozwól, aby nieszczęście, które cię dotknęło, zniszczyło twoją duszę.
Jeśli zdołasz oderwać się od swojego problemu i zrozumiesz, że świat materialny jest płynny i ulega zmianom, możesz schronić się w głębi swojej jaźni, aż cierpienie minie. Wtedy odzyskasz swoje dobra. ''', \
'3a':'''Grom uderza. Powoduje lęk i zdenerwowanie. Jeżeli twoje obawy powstrzymują cię od zejścia ze ścieżki, nie zrobisz błędu. Ostrożne działanie uwalnia z kłopotów. ''', \
'3b':'''Grom zwiastuje niebezpieczeństwo. Twoje poczucie zagrożenia jest trafne. Nie możesz biernie czekać na rozwój wypadków i dać się ponieść losowi. Czasem los sam powoduje zawirowania na drodze, którą podąża człowiek. Musisz zareagować i podjąć delikatne działanie, aby uwolnić się z zagrożenia. Nie przegap tego momentu i nie daj się zwieść z właściwej drogi. ''', \
'4a':'''Piorun grzęźnie w bagnie. ''', \
'4b':'''Nie masz dość odwagi, siły osobistej i polotu, aby pozbyć się niespodziewanego niebezpieczeństwa. W ten sposób pogarszasz swoją sytuację i wpadasz w poważne trudności. Będziesz musiał długo żyć z tym niechcianym problemem. ''', \
'5a':'''Pośród grzmotu piorunów. Zagrożenie. Jednak nic nie jest stracone; realizuje swoje cele. ''', \
'5b':'''Nie pozwól, aby liczne nieoczekiwane wydarzenia zaburzyły linię twojego losu i zepchnęły cię z twojej drogi. Musisz zachować zimną krew i jasny ogląd sytuacji i nie zważając na niebezpieczeństwa, kontynuować działania, z którymi jesteś związany. Gdy w tych trudnych warunkach porzucisz realizację swego dzieła, poniesiesz stratę. ''', \
'6a':'''Pośród grzmotu piorunów popada w ruinę. Przerażony rozgląda się wokoło. Złowróżbna, jeżeli pójdzie naprzód. Jeżeli to [działanie] nie dotyczy jego, lecz najpierw sąsiada - nie ma winy. Przyjaciel wyraża swoje żale. ''', \
'6b':'''Gdyby był przezorny, dostrzegłby pierwsze oznaki zagrożenia i zważał na ostrzeżenia. Zatrzymałby się i nie spowodował tego całego zamieszania. Swoją bezmyślnością i samowolnym działaniem dopuścił, aby zagrożenie przeniknęło jego istotę. Żyje w totalnym strachu, który doprowadza go do szaleństwa. Jeżeli przeżyte wstrząsy nie doprowadziły jeszcze do zaburzeń w jego osobowości, powinien zatrzymać się i zdecydowanie wycofać z tej sytuacji, nie zważając na złość, gniew i wyrzuty najbliższej osoby, gdyż w przeciwnym razie grozi mu katastrofa. Gdy wywołane zagrożenie nie dotyczy jego, lecz bliskiej mu osoby, nie ma w tym jego winy. To postawa jej samej i działania w stosunku do niego doprowadziły ją do rozpaczy, wywołując w niej strach i rozżalenie. Być może to od niej trzeba się uwolnić. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram52 = {'title':'Góra', \
'ctitle':'Ken', \
'picture':'''Góra obok góry. Trwanie w spokoju. Dotarcie do celu.
Uspokojenie. Zatrzymanie.
Wybraniec zatrzymuje się na swoim miejscu. Skupia się w sobie, nie wybiega myślami poza swoje położenie. ''', \
'judgment':'''Prostuje plecy i pozbywa się poczucia własnego ciała.
Poruszają się po dziedzińcu, na którym przebywa, ale nie dostrzegają go. Nie można dostać jego ciała. ''', \
'interpretation':'''	Heksagram przedstawia sytuację dotarcia do celu podróży. To miejsce pełne tajemnic; tam wszystkie rzeczy mają swój początek i koniec; tam śmierć i narodziny mieszkają obok siebie. Należy wspomagać siłę osobistą spokojem i hamowaniem wewnętrznym, wyrażającym się w powstrzymywaniu się od niepotrzebnych działań, które mogą prowadzić na manowce, rozpraszając zgromadzoną siłę osobistą. Nie wolno pozwolić, by myśli wybiegały poza cel i skupiały się niepotrzebnie na mniej istotnych zagadnieniach. Należy porzucić własne ego, wyrażające się poprzez pożądania i pragnienia i nie różnicować siebie i innych ludzi. W ten sposób człowiek łączy się z nimi i uświadamia sobie, że jest wspólną cząstką większej całości. Nikt wtedy nie będzie mógł zburzyć jego spokoju wewnętrznego, pozostanie niewzruszony jak skała, jednocześnie będzie wiedział, czym jest prawdziwy bezruch. Znaczy to, że będzie wiedział, kiedy się powstrzymywać od aktywności, a kiedy działać. Dzięki temu będzie mógł podjąć się realizacji ambitnych planów. Miarą spokoju wewnętrznego, który sprzyja właściwemu widzeniu rzeczy, jest napięcie mięśni obwodowych, zależnych od kręgosłupa. Jeżeli umysł jest spokojny, wolny od stresów, wtedy ciało jest rozluźnione, a człowiek pozbywa się egoistycznego poczucia własnej ważności, uzyskując wewnętrzną elastyczność, co sprzyja powodzeniu podejmowanych działań. Wszystkie stresy człowieka magazynują się w obwodowym układzie nerwowym, poprzez kręgosłup w mięśniach szyi, karku i pleców. Gdy człowiek uwalnia się od stresów, napięcie tych mięśni maleje i człowiek się rozluźnia. Dlatego dobrze jest skorzystać z masażu pleców, który rozluźniając mięśnie, uspokoi umysł.
Równie dobrze jest usiąść w pozycji lotosu i pomedytować.''', \
'1a':'''Uspokaja duże palce stóp. Nie popełni błędów, jeżeli pozostanie na swojej ścieżce. ''', \
'1b':'''Jeżeli ogarniają cię wątpliwości i zaczynasz się wahać, to masz słuszność. W tej chwili nie trudno o pomyłkę, dlatego trzeba się zatrzymać, by dokładnie rozważyć początek, gdyż ma on wpływ na dalsze działania. Jeżeli twoje uczucia pozostaną negatywne, powinieneś zmienić kierunek swojej drogi. ''', \
'2a':'''Uspokaja łydki. Nie może przyjść z pomocą temu, za kim podąża. Nie ma radości w jego sercu. ''', \
'2b':'''Łydki podążają za stopami i symbolizują niesamodzielną i zależną rolę podwładnego. Jeżeli nie ma on dość siły, powstrzymuje w działaniu zwierzchnika, powodując jego niepowodzenie. Dlatego jego serce się nie raduje. ''', \
'3a':'''Sztywny w biodrach. Uspokaja lędźwie. Zagrożenie. Ból, ale studzi podniecenie. Serce rozpacza. ''', \
'3b':'''Zostałeś ugodzony „do żywego”. Może trafiła cię strzała Amora. Niebezpieczeństwo leży w zbytnim rozpaleniu ognia pożądania. Chęć natychmiastowego zaspokojenia i spowodowane tym zawirowania emocjonalne burzą wewnętrzny spokój. Mimo że można to odczuć boleśnie, należy się opanować, odnajdując równowagę w wolności. ''', \
'4a':'''Uspokaja tors. Bez winy. ''', \
'4b':'''Blisko, coraz bliżej. Dzięki umiejętności zapanowania nad emocjami, popędami i odruchami swojego ego, zbliżasz się do momentu, kiedy osiągniesz autentyczny wewnętrzny spokój. Aby dopiąć tego celu, musisz podjąć jeszcze jeden wysiłek i powstrzymać resztki negatywnych odruchów. Uda ci się, mimo zewnętrznych niepokojów, osiągnąć wewnętrzny spokój. ''', \
'5a':'''Uspokaja szczęki. Układa swoje słowa. Żal znika. ''', \
'5b':'''Należy wziąć odpowiedzialność za swoje słowa i powstrzymać się od niepotrzebnych wypowiedzi. Jeśli już koniecznie chcesz coś powiedzieć, dobrze zaplanuj swoją wypowiedź. Słowa mogą być zarówno konstruktywne, jak i destruktywne. Pomyśl, zanim cokolwiek powiesz, żebyś potem nie żałował swych słów. ''', \
'6a':'''* Doskonałe ukorzenione uspokojenie. Fortuna sprzyja. ''', \
'6b':'''Osiągnął wewnętrzną harmonię. Pełen spokoju patrzy na świat. Moc jego spokoju jest trwała jak góra. Pomyślna we wszystkich planach. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram53 = {'title':'Stopniowy postęp', \
'ctitle':'Ćian', \
'picture':'''Drzewo na górze. Krok za krokiem do przodu.
Wybraniec postępuje rozważnie, doskonaląc swój charakter. ''', \
'judgment':'''Korzystna jest niezłomność na ścieżce. Mężczyzna stopniowo doprowadza do małżeństwa. Panna młoda poślubia męża. W końcu pomyślna. ''', \
'interpretation':'''	Heksagram symbolizuje proces stopniowego podążania do celu.
Rzeczy toczą się zgodnie ze swoim naturalnym biegiem. Należy łagodnie, bez pośpiechu przywracać zagubiony ład. W poszukiwaniu utraconego raju trzeba stopniowo, krok po kroku powracać na właściwą ścieżkę. Jak mężczyzna poszukujący swojej kobiety,; należy być roztropnym, wytrwałym w swej drodze, nie ulegać zbędnym pokusom i cierpliwie podążać, mając świadomość, że niespieszne, ale zdeterminowane działanie zaprowadzi go w końcu do kobiety jego serca. Gdy odnajdzie swoją drugą połowę i się z nią połączy, przywróci utracony odwieczny porządek rzeczy.''', \
'1a':'''Dziki łabędź zbliża się do głębiny. Młodszy syn jest zagrożony. Niebezpieczeństwo czyha. Uważaj! ''', \
'1b':'''Znajdujesz się w chwili, która jest początkiem czegoś zupełnie nowego. Sytuacja, w którą wstępujesz, pochłonie cię nieodwołalnie i całkowicie na bardzo długi czas, czy tego chcesz, czy nie. Będzie decydowała o twoim postępowaniu i wymagała od ciebie ogromnej siły woli, abyś mógł jej sprostać. To pierwszy szczebel drabiny. To jest sytuacja progowa. ''', \
'2a':'''* Dziki łabędź zbliża się do skały. Odpoczywa, jedząc i pijąc. Rokuje powodzenie. ''', \
'2b':'''Jest na dobrej drodze. Pierwszy trudny etap poza nim. Skały przy brzegu symbolizują pierwszy moment na długiej drodze, jaka go czeka, kiedy może bezpiecznie odpocząć i wzmocnić swoje siły. Dobrze, gdy zawoła towarzyszy i będzie wśród przyjaciół. Pozostając samotny, wpadnie w kłopoty. Szóstka na drugim miejscu jest obrazem dziewczyny wychodzącej za mąż. Jest ona w związku zgodności z dziewiątką na piątym miejscu. ''', \
'3a':'''Dziki łabędź zbliża się do pustyni. Mężczyzna wyrusza i nie wraca. Kobieta nosi w łonie dziecko, ale go nie rodzi. Nieszczęście. Złowróżbna. Należy bronić się i zwalczać rabusiów. Sprzyjającym jest ująć tego, kto kradnie. ''', \
'3b':'''Będąc osamotniony i chcąc szybciej dotrzeć do celu, podjąłeś ryzykowne działania i w rezultacie zboczyłeś z właściwej drogi. Była to albo chwila słabości, albo zbytnia ufność we własne siły. Niestety, spowodowała, iż znalazłeś się w groźnej sytuacji. Jeżeli nie podejmiesz zaraz energicznych działań, trudno ci będzie się wycofać i sprawa ta zaabsorbuje cię na dłużej. Przypadnie ci rola karzącego miecza sprawiedliwości. Nie będzie to łatwa rola. Będziesz musiał roztropnie walczyć z rabusiami uważając, by nie stać się jednym z nich. ''', \
'4a':'''Dziki łabędź zbliża się do lasu. Tam może usiąść na wygodnej gałęzi drzewa. Zapewne dostanie to, co złodzieje odrzucili. Nie popełni błędu. ''', \
'4b':'''Znalazłeś się w niewygodnej sytuacji. Zawirowania na twojej drodze były skutkiem niezwykłych okoliczności, spowodowały stratę i utratę równowagi wewnętrznej. Musisz wykazać się inteligencją, sprytem i łagodnością, aby znaleźć się na właściwym miejscu. Znajdź bezpieczne miejsce, gdzie będziesz mógł odpocząć i zregenerować siły, zanim podejmiesz nowe wyzwanie lub zaangażujesz się w związek.
Teraz musisz zadowolić się tym, co ci pozostało. ''', \
'5a':'''* Dziki łabędź zbliża się ku kopcowi. Kobieta nie zachodzi w ciążę przez trzy lata, lecz w końcu nic jej nie przeszkodzi. ''', \
'5b':'''Osiągnąłeś znaczące postępy na swojej drodze. Ponieważ jest to twoja własna droga, wyobcowałeś się ze swojego środowiska. Masz poczucie spełnienia, ale jednocześnie masz świadomość, że jesteś osamotniony i niezrozumiany. Nie martw się tym. Postęp trwa, a obecny stan jest przejściowy. Powrócisz do społeczności, ale potrwa to dłużej, niż sądzisz. Wszystko w końcu ułoży się pomyślnie, gdy twoje wysiłki zostaną dostrzeżone, uznane i zaakceptowane. ''', \
'6a':'''Dziki łabędź podąża ku chmurom. Jego pióro, które opadło na ziemię, może służyć za ozdobę w świętej ceremonii. Pomyślna. Wróży szczęście. ''', \
'6b':'''Pióropusz na głowę. Ukończyłeś z sukcesem swoje dzieło, zostajesz uhonorowany. Droga życia się dopełniła. Nastąpił ostateczny jej kres. Stąd można albo przekroczyć próg wieczności, albo definitywnie porzucając dotychczasowe wartości, ostatecznie zerwać z przeszłością i zacząć zupełnie nowe życie po to, aby uwieńczyć je chwałą człowieka doskonałego. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram54 = {'title':'Poślubienie narzeczonej', \
'ctitle':'Kui mei', \
'picture':'''Piorun w jeziorze. Poślubienie młodej dziewczyny.
Ceremonia ślubna.
Wybraniec wie, że chwila może trwać wiecznie. ''', \
'judgment':'''Działanie prowadzi do nieszczęścia.
Nic nie jest korzystne. Złowróżbna.
Tak wybraniec rozumie chwilowe w świetle wiecznego końca. ''', \
'interpretation':'''	Heksagram opisuje niełatwe położenie osoby, która wchodzi w rolę podporządkowanego w obcym środowisku. Młoda dziewczyna wychodzi za mąż za starszego mężczyznę. Musi ona porzucić myśli o samodzielnym działaniu i realizowaniu własnych planów.
Ponieważ całkowicie zależy od swoich mocodawców, powinna zaakceptować swoją rolę i nie usiłować wpływać na bieg rzeczy, jeśli nie chce być przyczyną niesnasek i sprawić zawodu swoim zwierzchnikom. Jeszcze lepiej zrobi, gdy zapanuje nad swoimi emocjami i nie będzie wchodziła w nieodpowiedni związek. Wolne związki między ludźmi powinny respektować panujące stosunki. Wzajemna skłonność ma wielkie znaczenie jako zasada wszystkich związków świata.
Wśród ludzi wolne upodobanie jest podstawą związków: stosownie do niego zawiązują się i rozpadają. Kto nie potrafi okiełznać swoich namiętności, staje się ich więźniem i pozwala, aby fałsz zajął miejsce prawdy. Nie należy poszukiwać prawdy, opierając się o fałsz.
Kto pojmie istotę emocji, nie da się im zniewolić i pozostanie ich panem, dzięki czemu osiąga korzyści. Nie ty rządzisz w tym układzie. Niestety, mimo że jesteś szczery i prawy i wywiązujesz się ze swoich obowiązków doskonale, nie przyniesie ci to żadnych korzyści. Druga strona traktuje cię instrumentalnie.''', \
'1a':'''Odprawia konkubinę. Dziewczyna nie wychodzi za mąż i powraca do swoich sióstr. Kulawy, który może chodzić; działania przynoszą powodzenie. ''', \
'1b':'''Działanie bez powodzenia, ale jest dokąd wrócić. Tym razem ktoś nie okazał się odpowiedni, ale dalej ma szanse. Trzymając się swoich zasad, natrafi na właściwy los. ''', \
'2a':'''Poślubia jednooką. Nie przynosi korzyści. Wytrwałość samotnego człowieka sprzyja. ''', \
'2b':'''Łączysz się z kimś, kim się rozczarowujesz. Masz możliwość zorientować się w niekorzystnej sytuacji. Decydujesz, że nie był to dobry pomysł. Skoro tak, odłącz się i pozostań sam. Samotnik zyska, jeśli nie będzie zmieniał trybu życia. Potraktuj to jako nauczkę i wystrzegaj się podobnych znajomości w przyszłości. ''', \
'3a':'''◆ Poślubia pannę z oczekiwaniami. Zostaje konkubiną. ''', \
'3b':'''Wygórowane oczekiwania, samowolne, nie liczące się z dobrymi radami postępowanie prowadzi do upokorzenia i cierpienia. Można osiągnąć swój cel, aby niechcący stać się jego niewolnikiem. Dziewczyna, chcąc koniecznie wyjść za mąż, poniża się i zostaje niewolnicą. Idąc za dziewiątką na drugim miejscu, znajduje schronienie jako konkubina. ''', \
'4a':'''Panna młoda nie działa pochopnie. Zwleka, czekając na właściwą partię. Ceremonia ślubna zostaje przesunięta. ''', \
'4b':'''Nie nadszedł jeszcze odpowiedni czas na działanie, brakuje właściwych sprzymierzeńców. Jest przygotowany i zna swoją wartość, jednak powstrzymuje się. Zwłoka na przemyślenie i rozeznanie się w swoich uczuciach jest korzystna. Pomimo że, zdawałoby się, wszelkie szanse na możliwą do przyjęcia propozycję minęły, jednak ma rację, tak postępując. Wytrwałość zostanie nagrodzona. ''', \
'5a':'''* Cesarz wydaje za mąż młodszą córkę. Ubiór księżniczki nie dorównuje swoją wspaniałością strojom jej dworki: Dzienny księżyc jest po pełni. Powodzenie. ''', \
'5b':'''Wstępując w związek z kimś niższego stanu, należy powściągać dumę i nie nadużywać przynależnych z tytułu tradycji i hierarchii przywilejów. Wstępując w związek z kimś wyższego stanu, należy być świadomym swej pozycji i trzymać nadmierną dumę w ryzach, okazując prędzej zbytnią pokorę niż nadmierną wyniosłość. Równowaga w takim związku jest delikatna, dlatego należy zważać, aby nie zakłóciły jej błahostki. Zachowując dystans do swoich ról, można osiągnąć powodzenie. ''', \
'6a':'''◆ Panna młoda niesie koszyk, lecz nie ma w nim owoców. Pan młody poświęca owcę, lecz krew nie płynie. Nic nie jest korzystne. Nieszczęście. ''', \
'6b':'''Oparty na fałszywych związkach mariaż stał się nie do zniesienia.
Gdy opadły złudzenia, pozostał tylko egoizm. Na nim nie można oprzeć żadnego pozytywnego związku. Taka sytuacja nie rokuje żadnych widoków na wspólną, szczęśliwą przyszłość. Żadna ofiara jej nie poprawi. Nie ma na to rady. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram55 = {'title':'Obfitość', \
'ctitle':'Feng', \
'picture':'''Piorun nad ogniem. Zaćmienie. Słońce w południe przysłaniane burzowymi chmurami. Wielkość i pełnia jasności. Obfitość. ''', \
'judgment':'''Majątek w tarapatach. Piorun i błysk nadchodzą razem. Tak wybraniec wydaje w procesach sprawiedliwe wyroki i egzekwuje kary.
Powodzenie. Król osiąga to. Niech nie będzie smutny.
Jest bogaty jak słońce w południe. ''', \
'interpretation':'''	Kto zwycięży strach, opanuje jasność i poskromi uzyskaną moc, będzie mógł napić się z rogu obfitości, osiągając wielkość i sławę. Pozwala na to wewnętrzna wolność, wielkość i moc ducha. Gdy bardzo duże poczucie bezpieczeństwa połączone jest z bardzo dużą aktywnością, człowiek jest w stanie dokonać rzeczy wielkich. W takiej sytuacji łatwo jest dopiąć swojego celu i ziścić swe marzenia. Jednak nie każdemu to się udaje. Tylko człowiek wewnętrznie wolny od trosk i zmartwień wie, jak przyjąć czas pełni. Trzeba wykorzystać korzystny czas na gromadzenie i pomnażanie bogactwa, gdyż taki stan nie może utrzymać się długo. Skoro jest apogeum, nieuchronnie nastąpi schyłek. Nie należy się przejmować tym, że można to utracić. Teraz trzeba być jak słońce w południe w glorii swojej chwały. Nie bądź rozrzutny, nawet w czasie wielkiego powodzenia, kiedy okazji jest wiele. Wtedy powodzenie będzie trwało dłużej. Pieniądze wydawaj mądrze i nie chwal się swoim dostatkiem. Bogactwo lubi ciszę. Kiedy nadejdzie zmierzch, nie utraci swoich cennych wartości, kto się do nich nadmiernie nie przywiązuje. Zwróć uwagę, jak korupcja i sprzedajność zaćmiewa szczerość i uczciwość.
Wstrząs i przestrach stanowią konieczne warunki burzy oczyszczającej atmosferę, czyli procesu karnego, jeśli do takiego dojdzie.''', \
'1a':'''Spotyka kogoś bardzo podobnego do siebie. Los ich sobie przeznaczył. Pozostają razem przez dziesięć dni. Nie ma błędu. Gdy pójdzie dalej, potwierdzi słuszność swojej drogi i znajdzie wywyższenie. ''', \
'1b':'''Trafia na przeznaczonego sobie władcę. Te dwie osoby posiadają wewnętrzną moc i jasność spojrzenia. Powinny zjednoczyć się wokół wspólnego celu i podjąć jego realizację. Na pewno się im powiedzie. Dlatego należy wyruszyć i odszukać go, jeżeli jest na wysokiej pozycji. Jednak nie powinny być ze sobą dłużej, niż wymaga tego czas na wykonanie zadania. ''', \
'2a':'''Zaćmienie jest tak wielkie, że w południe widać Wielki Wóz. Idąc naprzód, dostaje podejrzaną chorobę.
Oto powrót, jakby coś ciekło. ''', \
'2b':'''Ciemne siły przesłoniły jasne. Podążając tą drogą, można się spodziewać nieprzyjemnych spraw. Lepiej zawrócić z tej drogi. ''', \
'3a':'''Zaćmienie jest tak wielkie, że w południe widać gwiazdy. Po ciemku łamie prawe ramię. Nie ma winy. ''', \
'3b':'''Ciemne siły przesłoniły jasne tak skutecznie, że nic już prawie nie widać.
Władca otoczony jest przez niegodziwców, którzy odsunęli od niego lojalnych i uczciwych. Zupełnie stracił kontrolę nad sytuacją. Nie ma tam miejsca dla człowieka zacnego. Nic już nie może uczynić, by zmienić fatalną sytuację. To nie jego wina. Prawa ręka władcy powinna się wycofać. ''', \
'4a':'''Zaćmienie jest tak wielkie, że w południe widać Wielki Wóz. Spotyka kogoś bardzo podobnego do siebie.
Działając razem, osiągną powodzenie. ''', \
'4b':'''Ciemne siły przesłoniły jasne, dalej sprawują kontrolę, ale przyćmiona jasność wydobywa się spod ich wpływu. Władca natrafia na kogoś godnego zaufania i zacnego. Wspólnie z nim działając, może otworzyć sobie drogę do sukcesu. ''', \
'5a':'''* Oto przychodzi pomyślny wzór. W swoim kręgu gromadzi wyśmienitych ludzi. Dobrobyt i sława są blisko. ''', \
'5b':'''Wzorcowa sytuacja. Kompletuje znakomity zespół. Konsultuje swoje działanie i kieruje się dobrymi radami znamienitych doradców. To gwarantuje, że można sięgnąć po róg obfitości. Na pewno będzie się można z niego napić. ''', \
'6a':'''Mieszka w domu pełnym obfitości, w którym się ukrywa. Wpatruje się w drzwi, których nie otwiera. Patrzy w głąb domu i nikogo nie dostrzega przez trzy lata. Złowróżbna. ''', \
'6b':'''Dom nie jest domem, ale schronem; ludzie nie są ludźmi, ale złoczyńcami czyhającymi na jego mienie. Blask materii zaciemnił wnętrze człowieka. Chciwość, zachłanność i przywiązanie do bogactw uczyniło z niego niewolnika. Strach i obawa przed ich utratą powodują, że nie może się z nich cieszyć, ba, nawet ich nie widzi. Oślepił go złudny blask mamony. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram56 = {'title':'Podróżnik', \
'ctitle':'Liu', \
'picture':'''Ogień na górze. Podróż. Wędrowanie. Lekcja życia.
Wybraniec wymierza kary z wyrozumiałością i ostrożnością. Wygasza waśnie, by nie marnować czasu w sądzie. ''', \
'judgment':'''Który jest w drodze i stara się znaleźć miejsce dla siebie. Powodzenie poprzez drobne działania. Wytrwaj w małych osiągnięciach. Trzymaj się swojej ścieżki. ''', \
'interpretation':'''	Podróżnik z natury swojego Tao przebywa w danym miejscu tylko przez jakiś czas. Trudno mu zapuścić korzenie, gdyż szybko nasyca się sytuacją i pragnie nowych doznań. Jego wędrowanie od doświadczenia do doświadczenia, przenoszenie się z miejsca na miejsce czy od oświecenia do oświecenia wynika ze strachu przed stabilizacją. Podróżnik doświadcza stabilizacji jako zagrożenia jego wolności i dlatego nie pozwala sobie, by dana sytuacja pochłonęła go na dłużej. Taka postawa nie pozwala mu na zahartowanie ducha w walce z przeciwnościami losu. On po prostu unika przeciwności, ciągle zmieniając miejsce pobytu. W ten sposób nigdy nie znajdzie swojej przystani, bo zawsze będzie uciekał, łudząc się, że za następnym zakrętem drogi skończą się jego poszukiwania. Jego dusza potrzebuje nowych doświadczeń, jak drzewo powietrza i wody, inaczej usycha. Lotny duch wędrowca w poszukiwaniu energii utrzymującej jego istnienie żywi się każdym nowym doświadczeniem, które daje mu radość i chwilowe spełnienie. Wędrowiec musi zawsze zachowywać rezerwę w swoich kontaktach, by nie dopuścić do zagrożenia własnej osoby. Jeżeli takie życie mu odpowiada, nie ma w tym nic złego. Jeżeli ma już dość tułaczki i chciałby coś zmienić w swoim życiu, powinien hartować swoją silną wolę, zaczynając od małych rzeczy. W ten sposób stanie się dzielnym człowiekiem.
Czasem wędrowiec musi podróżować w trudnym terenie, lecz jeśli będzie szczery, uczciwy i zdecydowany, jego życie nabierze sensu, a jego droga przez życie będzie znacznie łatwiejsza. Tak wyrabia się dzielność - w uczeniu się życia. Ponieważ jest podróżnikiem, nie chce w swojej wędrówce marnować czasu na spory sądowe, gdyż to zatrzymuje go w danym miejscu na dłużej, niżby sobie życzył. Dlatego szukając sprawiedliwości, powinien być roztropny i ostrożny w wymierzaniu kary swoim winowajcom.''', \
'1a':'''Podróżnik jest zdezorientowany na swojej drodze i jeśli skupia uwagę na błahostkach, sprowadza nieszczęście. ''', \
'1b':'''Kto ma zmącone widzenie świata, przypomina wędrowca, który nie wie, gdzie się zatrzymać. Jego pogmatwane drogi nie pozwalają mu dostrzec położenia innych ludzi. Lekko traktuje sprawy, które dla innych są poważne. Sytuacja przypomina bajkę o żabach Krasińskiego: „Wy się bawicie, nam chodzi o życie”. Myśli, że popisując się, spotka się z lepszym przyjęciem. Nie ma racji. Beztroska i prostacka postawa wywoła wrogość i sprowokuje niepowodzenie.
Podróżnik powinien być skromny i stwarzać wrażenie bezbronnego.
Wtedy może liczyć na zainteresowanie i poparcie otoczenia. ''', \
'2a':'''Podróżnik przybył do miasta. Ma swój dobytek ze sobą. Zdobywa oddanie i zaufanie młodego sługi. ''', \
'2b':'''Dotarł do właściwego miejsca we właściwym czasie. Jego wewnętrzne światło i silna wiara w siebie zwróci na niego uwagę i przyciągnie do niego ludzi, zyskując mu uznanie i przychylność. ''', \
'3a':'''Podróżnik podpalił dom. Opuścił go młody sługa.
Determinacja na ścieżce stwarza zagrożenie. ''', \
'3b':'''Silny, ale samowolny podróżnik powoduje dezorganizację, mieszając się w cudze sprawy. Traci miejsce oparcia i wsparcie przychylnych ludzi. Powodem jest jego zaangażowanie uczuciowe, chwilowa utrata kontroli nad właściwym kierunkiem drogi. Jego działania spotykają się z dezaprobatą, ludzie patrzą na niego nieufnie. Jeśli pozostanie na swojej ścieżce, nie uniknie zagrożenia stwarzanego przez dotkniętych domowników. ''', \
'4a':'''Podróżnik osiedla się i zapuszcza korzenie. Osiąga powodzenie materialne, lecz jego serce się nie raduje. ''', \
'4b':'''Postąpił sprzecznie ze swoją naturą wędrowca, znajdując spokojną przystań na uboczu. Nie mając nic innego do roboty i znajdując się w sprzyjających okolicznościach, udaje mu się wzbogacić. Mimo że z pozoru niczego mu nie brakuje, odczuwa niepokój i czuje się nieszczęśliwy. Gdy przyjdzie czas, że będzie musiał bronić zdobytego bogactwa, lepiej niech je porzuci i wróci na swoją drogę, gdzie będzie mógł wykorzystać swoje prawdziwe skarby. ''', \
'5a':'''Podróżnik upolował bażanta pierwszą strzałą.
Zyskuje nagrodę i sławę. ''', \
'5b':'''Inteligentny podróżnik, który wie, dokąd dąży, potrafi nawet przebywając z dala od stron rodzinnych, sprytnie wkraść się w łaski władcy, zdobywając prędko pole do popisu i uzyskując zaszczyty. ''', \
'6a':'''Podróżnik podpala gniazdo ptaka. Najpierw się raduje, potem lamentuje i rozpacza. Lekkomyślnie traci swoją krowę. Złowróżbna. ''', \
'6b':'''Beztroska spowodowała, że podpalił własny dom. Zarazem utracił dobytek, schronienie i źródło pożywienia. W ogniu spłonęły najcenniejsze wartości. Nadużył swojej pozycji, mniemając, że jest już niewzruszenie pewna i że nic mu nie zagraża. Miast pozostać skromnym i opanowanym, podjął się roli nieomylnego arbitra, tracąc szacunek i prestiż. Przecenił swoje siły. Teraz pozostał mu tylko żal i zgrzytanie zębów. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram57 = {'title':'Wiatr', \
'ctitle':'Sun', \
'picture':'''Wiatr gna wiatr. Podmuch.
Przenikliwość i łagodność.
Wybraniec kontynuuje swoje dzieło, jego wola przenika świat. ''', \
'judgment':'''Małe przynosi korzyść. Korzystne jest wykonać jakiś ruch. Sprzyjającym jest widzieć wielkiego człowieka. ''', \
'interpretation':'''	Ażeby odnieść sukces, należy najpierw przygotować teren pod działanie. Trzeba, by idee działań przeniknęły wpierw do umysłów i serc ludzi. Dlatego zanim podejmie się znaczącą aktywność, należy nieustannie na nich oddziaływać, przekazując im założenia i cele działań.
Dzięki małym krokom można uzyskać wpływ na bieg rzeczy. Czas jest tutaj narzędziem do osiągania wielkiego wpływu. Nie można oddziaływać bezpośrednio na sytuację, gdyż wywoła to lęk i opór nieuświadomionych i będzie tylko niepotrzebną stratą energii. Należy wpływać na sytuację siłą swojej osobowości, nie pozwalając uzależnić się od sytuacji próbami realizacji swoich kaprysów i oczekiwań. Zamiast wpłynąć na sytuację, staną się one jej składnikiem, nie pozwalając na znalezienie właściwego rozwiązania problemu. Kto jest silny, będzie posłuszny tej radzie albo zwróci się o pomoc do mądrego człowieka.''', \
'1a':'''◆ Przychodzi i odchodzi jak lekki powiew zefirku. Bądź jak wojownik i nie zbaczaj ze swej ścieżki. ''', \
'1b':'''Twoja naturalna łagodność rodzi wahania, które prowadzą do wewnętrznej rozterki. Jeśli chcesz pójść naprzód, musisz porzucić niezliczone obawy pojawiające się w twojej świadomości i niepewność, że nie podołasz. Powinieneś przyjąć postawę wojownika i być jak on niezłomnym i stanowczym. Musisz zdyscyplinować swoje wnętrze. Twoja sprawa będzie się rozwijać pomyślnie, jeżeli wykażesz determinację. ''', \
'2a':'''Wiatr przenika pod łóżko. Niezbędna jest wielka liczba kapłanów i magów. Powodzenie. Nie ma winy. ''', \
'2b':'''Niewidzialne, ciemne siły wywołują zamieszanie w psychice. Rodzą napięcia wewnętrzne i konflikty. Ich destrukcyjne działanie jest trudne do zlikwidowania. Konieczna jest pomoc pośredników, którzy obeznani są z podstępnymi siłami ciemności. Muszą oni przeniknąć i rozpoznać te siły i zlikwidować ich negatywny wpływ. ''', \
'3a':'''Nadmierne przenikanie. Upokorzenie. ''', \
'3b':'''Rozważanie problemu pod każdym kątem i z każdej strony wywołuje tysięczne wątpliwości i rodzi niepotrzebne skrupuły. Trzeba uciąć zbędne dywagacje, podejmując nieodwołalną decyzję. ''', \
'4a':'''◆ Znika poczucie winy. Trofeum łowcy daje trojaką korzyść. ''', \
'4b':'''Tak. Ma. Posiadł je. Posiadasz przymioty ducha, zasoby materialne i energię ciała, zrównoważyłeś swoje emocje. Zajmując eksponowaną pozycję, wykorzystujesz swoje cenne zasoby do realizacji wielkich celów. ''', \
'5a':'''* Pomyślna dzięki wytrwałości. Żal mija. Nic, co by było niesprzyjającym. Nie widać początku, ale będzie koniec. Rozważ zmiany trzy dni przed. Trzy dni po rozważ je jeszcze raz. Fortunna. ''', \
'5b':'''Władca heksagramu, który jest źródłem wpływania poprzez rozkazy, pracuje nad całym społeczeństwem. Aby wydawać rozkazy, trzeba najpierw usunąć zły początek, a dopiero potem osiągnąć dobry koniec. Należy zreformować i skorygować zły początek. Dokładnie przemyśl swoją sytuację i zastanów się nad zmianą. Być może nie od razu rozwój sytuacji będzie korzystny, ale nie znaczy to, że popełniłeś błąd. Przeanalizuj swoje zamiary ponownie i zacznij jeszcze raz. Znajdziesz właściwy kierunek. W ten sposób ruszysz z miejsca i trafisz na właściwą drogę. Zmiana jest na jesieni. Trzy dni przed jeszcze jest lato. Trzy dni po nastaje zima, koniec roku.
I ty możesz osiągnąć koniec. ''', \
'6a':'''Wiatr wieje pod łóżkiem coraz słabiej. (On) traci swe majętności i oręż. Złowróżbna, jeżeli nie zejdziesz ze swej ścieżki. ''', \
'6b':'''Nie masz sił na działanie, choć wiesz, co się święci. Przejrzałeś podstępne knowania antagonistów, choć nie dysponujesz odpowiednimi środkami, by z nimi walczyć. Zdając sobie sprawę z nierówności sił, powinieneś poniechać prób wpływu na sytuację i odpuścić. W przeciwnym razie grozi ci porażka. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram58 = {'title':'Przyjemność', \
'ctitle':'Tui', \
'picture':'''Jezioro w górze, jezioro w dole.
Uciecha i rozrywka. Uzurpacja.
Wybraniec łączy się z przyjaciółmi dla wspólnych rozmów i praktyk; choć rozmawiają swobodnie, ich porozumienie jest głębokie. ''', \
'judgment':'''Fortunna, jeżeli pozostaniesz na swojej ścieżce. ''', \
'interpretation':'''	Dobrze jest cieszyć się i radować. Radosny śmiech wpływa pozytywnie na organizm, dzięki czemu polepsza się zdrowie człowieka.
Należy jednak wiedzieć, że prawdziwa radość pochodzi z wnętrza człowieka, a nie jest wynikiem konsumpcji świata zewnętrznego.
Autentycznej radości sprzyjają szczerość intencji, dobre czyny, właściwe poczucie sprawiedliwości, pomaganie innym i wierność wyznawanym zasadom. Dają one mądrość, którą można dzielić się z innymi. Gdy radość wynika z zachłanności na przyjemności płynące z zewnątrz, jest uzurpacją i kończy się smutkiem i melancholią.''', \
'1a':'''Przyjemność wewnętrznej harmonii. Obiecująca. ''', \
'1b':'''Kto osiągnął wewnętrzny spokój, uwalniając się od pragnień i pożądań, może korzystać z dobrodziejstw autentycznej przyjemności.
Ogarnia go radość i potrafi cieszyć się wszystkim, co go spotyka.
Jest pogodny i uśmiechnięty. ''', \
'2a':'''* Przyjemność szczerości. Zachęcająca. Poczucie winy znika. ''', \
'2b':'''Szczera rozmowa po nieporozumieniu i sporach może wszystko naprawić. Wtedy przykre wydarzenia z przeszłości pójdą w niepamięć. ''', \
'3a':'''◆ Uleganie przyjemności. Nadchodząca uzurpacja. Złowróżbna. ''', \
'3b':'''Będąc wewnętrznie pustym, lepiej nie ulegać próżnej pokusie, bo można się zagubić. Unikaj pustych gestów. Choć może to dać zadowolenie innym, przynosi nieszczęście. ''', \
'4a':'''Rozważanie przyjemności. Przejściowa choroba sprzyja pomyślności. Ostrożność uwalnia od błędu. Samozadowolenie prowadzi do nieszczęścia. ''', \
'4b':'''Zastanawiając się, jaką przyjemność wybrać, popada w rozterkę.
Wszystkie wydają mu się jednakowo przyjemne. Jednak niech wie, że niektóre są zwodnicze w swojej naturze. Dokonując wyboru, powinien poniechać przyjemności zmysłowych. Wtedy będzie mógł doświadczyć przyjemności prawdziwej, płynącej ze spokoju wewnętrznego. ''', \
'5a':'''Błędne zaufanie w przyjemności. Strzeż się. ''', \
'5b':'''Nadmierne zadowolenie z siebie, wywołane przez przyjemność płynącą ze złego źródła. Szczerość, szczodrość i ufność, którą okazuje, sprawiają, że staje się łakomym kąskiem i ofiarą dla nikczemników.
Niebezpieczeństwo. Zagraża klęska. Choć doświadcza przyjemności, obcując z nimi, nie może nasiąknąć złem i dać się przez nie pochłonąć. Powinien taktownie wycofać się z potencjalnie groźnej sytuacji. Nie ufaj przewrotnemu człowiekowi, który chce ci zaszkodzić. To wilk w owczej skórze. Nie igraj z nim. Taka brawura jest zbędna i niebezpieczna. ''', \
'6a':'''Zatracenie w przyjemności. Ponętna. ''', \
'6b':'''Cień człowieka uzurpuje sobie prawo do rządzenia nim. Jego życiem rządzi zasada przyjemności. Kto jest słaby i próżny, goni za pustą przyjemnością. Ulega złudnemu powabowi zewnętrznego świata zmysłów. Doznania zmysłowe stają się dla niego jedynym celem życia Prowadzi to do przytępienia wrażliwości na dobro i zło, a radość czerpana z przeżywania przyjemności zatraca się. To nie jest prawdziwa przyjemność. Autentyczna przyjemność wypływa z wnętrza człowieka. Rozkosz, rozkosz, przekształcona w upadłe libido. Spójrz na obraz Salvadora Dali „Widmo libido”. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram59 = {'title':'Rozpraszanie', \
'ctitle':'Huan', \
'picture':'''Wiatr wieje nad rzeką. Woda paruje jak mgiełka.
Rozpraszanie.
Starożytni królowie składali ofiary Bogu i wznosili świątynie. ''', \
'judgment':'''Powodzenie. Nie schodź ze swojej ścieżki.
Król udaje się do świątyni przodków. Korzystne jest przekroczyć wielką wodę. Korzystne jest wytrwać. ''', \
'interpretation':'''	Kto ma moc i dobro w sercu, nie zmarnuje swych wysiłków.
Choćby oddał najwięcej z tego, co ma, i tak mu nie zabraknie. Gdy król podąża do świątyni, jednoczy wokół siebie naród i odwraca zły los. Dzięki zjednoczeniu wokół najwyższych celów można połączyć to, co rozdzielone egoizmem poszczególnych jednostek, i wspólnie dokonać wielkich czynów. Aby przezwyciężyć egoizm rozdzielający ludzi, oprócz siły religii potrzebne jest również współdziałanie w wielkich wspólnych przedsięwzięciach, które przed wolą ludzi stawiają wielki cel; wspólne skupienie na tym celu rozprasza wszystko, co oddziela, podobnie jak podczas przeprawy przez wielka rzekę wszyscy w łodzi zjednoczyć się muszą we wspólnej pracy i wysiłku.
Ale tylko ktoś sam wolny od wszelkich egoistycznych, niskich motywów, niezmienny w swej prawości, zdolny jest do rozproszenia twardości egoizmu. Mistyczny lęk wobec wieczności i intuicyjne poczucie jednego stwórcy wszystkich istot - to siły, które wyzwalają spod władzy egoizmu, a wspólnota zrodzona podczas adoracji jednoczy ludzkie serca.
	Akcja tego heksagramu polega na wzajemnych stosunkach i oddziaływaniu linii na drugim, czwartym i piątym miejscu.''', \
'1a':'''Gdy chroni konia, przyjdzie mu z pomocą. Pomyślna. ''', \
'1b':'''Dobrze jest zachować roztropność i pomyśleć o przyszłości. Gdy pojawi się możliwość wpływu na bieg rzeczy, trzeba być na nie przygotowanym i mieć możliwość działania. Takie przygotowanie nie rozproszy sytuacji. W razie czego nie wahaj się i działaj zdecydowanie. ''', \
'2a':'''◆ Sytuacja ulega rozproszeniu. Śpieszy, by schronić się u protektorów. Znika poczucie winy. ''', \
'2b':'''Gdy traci się kontrolę nad sytuacją, o czym świadczy uczucie zmieszania i wyobcowania, które odczuwasz, należy niezwłocznie poszukać poparcia u ludzi ci przychylnych. Nie można dopuścić, aby nieufność przekształciła się w złość, złość w hipokryzję, a hipokryzja w odrazę do świata i ludzi. ''', \
'3a':'''Rozprasza się sam. Nie ma poczucia winy. ''', \
'3b':'''Kto zrezygnuje z siebie, pozbywszy się egoistycznego poczucia własnej ważności, uzyskuje moc, dostęp do boskiej intencji. Zachowując przy tym nieskazitelność, wtapia się w nurt naturalnych przemian we wszechświecie i synchronizuje z jedynym istniejącym rytmem, zgodnie z którym działa i nie ma dla niego przeszkód nie do pokonania. (Jednak biorąc pod uwagę sposoby istnienia najbardziej i najmniej czujących istot, trzeba przyznać, że niezajmowanie się sobą jest zdecydowanie jednym z najdziwniejszych sposobów). ''', \
'4a':'''◆ Rozprasza się od swej gromady. Błyskotliwe!
Rozproszone zaczyna się gromadzić. Prostak tego nie pojmie. Najwyższa pomyślność. ''', \
'4b':'''Wokół zgromadziło się zbyt wiele osób i trudno ocenić ich prawdziwe intencje. Nie wiadomo, kto się podporządkuje, a kto czyha na potknięcie. W takim przypadku najlepiej zerwać kontakty ze wszystkimi i poczekać. Pomedytuj, pomódl się i zaapeluj o wsparcie. Komu naprawdę zależy, mimo wszystko odpowie na twoje wołanie, powróci i pozostanie przy tobie. W ten sposób odróżnisz swoich prawdziwych sprzymierzeńców. Inni, okazując swoje zdumienie, a czasem i wzgardę, obrażą się i odejdą. Nie martw się tym. Pozostałeś z autentycznymi przyjaciółmi. ''', \
'5a':'''* Rozpraszanie winy. Z czoła mówcy płynie pot.
Król rozdaje nagromadzone zboże. Wina znika. ''', \
'5b':'''Poprzednie działania nagromadziły wiele bogactw, ale też wiele związanych z tym negatywnych energii powodujących zagrożenia, których można się obawiać. Dobrze jest w takiej chwili mieć pomysł, wokół którego można zgromadzić ludzi i pozytywną energię, równocześnie pozbywając się złej. Kto wie, kiedy brać, a kiedy dawać, poznał tajniki rozpraszania. Kto jest mądry, chętnie pozbędzie się skąpstwa, aby doświadczyć szczodrości. Podobnie pozbywając się choroby, która wychodzi z ciała wraz z potem, odzyskuje się zdrowie. Tylko ludzie wielcy mogą dostrzec pozytywne skutki rozpraszania. ''', \
'6a':'''Rozprasza swoją krew. Oddala się ostrożnie. Nie pomyli się. ''', \
'6b':'''To, co miał najcenniejszego do ofiarowania, już oddał. Teraz jest czas, aby usunąć się ostrożnie, zostawiając sprawy ich własnemu biegowi. To jest zwycięstwo. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram60 = {'title':'Ograniczenie', \
'ctitle':'Czie', \
'picture':'''Rzeka nad jeziorem. Ograniczenie i kontrolowanie.
Na wymiar.
Wybraniec ustala prawidła systemu. Rozważa samą zasadę.
Sprawdza naturę liczby i miary. Koryguje zachowanie. ''', \
'judgment':'''Który wyznacza wymiar, dokonuje koniecznego ograniczenia. ''', \
'interpretation':'''	Sam tworzysz wymiar swojego istnienia. Wolność, którą posiadasz, trzeba jednak ograniczyć. Naprawdę będziesz wolny wtedy, gdy poznasz i zrozumiesz swoje osobiste ograniczenia. Musisz też poznać prawidła systemu, w którym przyszło ci żyć. Gdy będziesz się do nich stosował, ograniczając swoją wolność osobistą, dopiero wtedy uzyskasz dostęp do prawdziwej wolności działania. Nie należy też przesadzać z narzucanymi ograniczeniami. Dobrze jest rozważyć dwie skrajności: absolutnej wolności i totalnego skrępowania oraz znaleźć złoty środek. Zważ, że skrajne ograniczenia wywołują bunt, smutek i żal, zwłaszcza gdy trwają zbyt długo, a zupełny ich brak jest podcinaniem gałęzi, na której się siedzi. Tylko mądre ograniczenia pozwolą osiągnąć prawdziwą wolność i pełnię możliwości.
	Ograniczenie w sprawach ekonomicznych dotyczy kontrolowania wydatków, aby właściwie zarządzać finansami. Czas zacisnąć pasa oszczędność to droga wyjścia z kryzysu. Jednak nie należy z oszczędnością przesadzać - drastyczne cięcia mogą zahamować rozwój. Gdy zbiorą się nadwyżki, można sobie od czasu do czasu pofolgować.''', \
'1a':'''Nie opuszcza domu. Nie zbłądzi. ''', \
'1b':'''Nie podejmuj działań. Poczekaj w swoim wewnętrznym świecie, póki nie ukaże się wolna droga. Ograniczenia, które cię dotyczą, są zbyt duże. W ten sposób niepotrzebnie nie stracisz sił. ''', \
'2a':'''Nie opuszcza domu. Złowróżbna. ''', \
'2b':'''Teraz nie możesz czekać! Musisz zareagować i działać szybko. Porzuć wahania i wątpliwości. Nie bój się opuścić swojego miejsca.
Właśnie pojawia się wyjątkowa okazja, twój „centymetr sześcienny szczęścia”. Nie przegap go. ''', \
'3a':'''Jeżeli nie narzuci sobie ograniczeń, będzie rozpaczać. Żal będzie mógł mieć tylko do siebie. ''', \
'3b':'''Brak równowagi wewnętrznej powoduje, że popada w przesadę.
Ekscentryczne uciechy i rozkosze, nadmierna swoboda, uleganie pogoni za doznaniami zmysłowymi prowadzą do nieszczęścia. Nie wiń za to świata, w którym żyjesz i w którym dostrzegasz niemoralne zachowania innych ludzi. Musisz skorzystać z wolności wyboru i ograniczyć się w rozpuście. Wiedz, że bez samoograniczenia zamiast szczęścia przyjdzie lament. Wolność absolutna, która ci się marzy, podcina gałąź, na której sam siedzisz. Zważ na to. ''', \
'4a':'''Realistyczne ograniczenie. Prawidłowe. ''', \
'4b':'''Ograniczenia muszą pasować do sytuacji. Nazbyt srogie rygory, tak jak i zbytnia pobłażliwość przynoszą niepotrzebne cierpienia.
I jedne i drugie nie mogą hamować naturalnego działania i rozwoju. Inaczej życie będzie albo ciągłym zmaganiem, albo huśtawką emocjonalną. ''', \
'5a':'''* Satysfakcjonujące ograniczenie. Ruch do przodu przydaje honoru. ''', \
'5b':'''Ograniczenia muszą być nakładane na innych odpowiednio do wymogów, jakie stawiają okoliczności. Trzeba uważać, aby nie deptać ich wolności i aby dotyczyły wszystkich we właściwym stopniu.
Dobrze, gdy władca sam da przykład i narzuci rygory najpierw sobie. W ten sposób uzyska ich zgodę na restrykcje, a jego pozycja i szacunek wzrosną. ''', \
'6a':'''Przesadne restrykcje nie mogą trwać zbyt długo.
Trudno je wytrzymać. Poczucie winy w końcu znika. ''', \
'6b':'''Wszystko ma swoje granice, także rygory. Zbyt surowe, trwające ponad miarę ograniczenia powodują cierpienie i niezasłużone męczarnie. Z tego powodu można odczuwać poczucie winy. Czasem jednak takie srogie obostrzenia są konieczne i trzeba się do nich uciec, gdyż służą sprawie. Dlatego poczucie winy znika. Należy jednak uważać, by nie przeciągać struny. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram61 = {'title':'Wewnętrzna prawda', \
'ctitle':'Czong fu', \
'picture':'''Wiatr wieje nad jeziorem. Prawda w nim.
Wiarygodność i zaufanie.
Wybraniec uważnie rozpatruje sprawy sądowe i wstrzymuje egzekucje wyroków. ''', \
'judgment':'''Świnie i ryby. Proste ofiary. Powodzenie.
Korzystna jest niezłomność na ścieżce. Korzystne będzie przekroczyć wielką wodę. ''', \
'interpretation':'''	Wewnętrzna prawda określa stan umysłu będący odzwierciedleniem kontaktu człowieka z rzeczywistością. Jego umysł, a więc rejestr rzeczy, którego wyrazem są myśli, słowa i prezentowane zachowania, jest konstruktem opartym na doświadczeniu człowieka związanym z jego drogą życia. Można powiedzieć, że jest on identyczny z jego przekonaniami. Znaczy to, że człowiek nie posiada przekonań - przekonania są tożsame z nim samym. Przenikliwość umysłu posiadającego wewnętrzną prawdę, która w istocie jest prawdą samą w sobie, pozwala dostrzec uwarunkowania każdego człowieka uwikłanego w problemy swojej osobowości i wczuć się w jego sytuację, dostrzegając zarazem boski czynnik w każdym.
Kto umie dostrzec uwarunkowania swoich adwersarzy, wie, że nie należy osądzać ich pochopnie, kierując się emocjami, ale trzeba starać się dotrzeć do ich wnętrza. Nie jest to prosta sprawa, gdyż ludzie, z którymi ma do czynienia, podobnie jak świnie i ryby, niepodatni są na wpływy zewnętrzne. Tylko dysponując wielką mocą wewnętrznej prawdy, można wpłynąć na tych ludzi. Kto to rozumie, może podjąć się realizacji nawet bardzo skomplikowanych przedsięwzięć. Kto posiada wewnętrzną prawdę, ten ma wiarę pozwalającą podjąć dalekosiężne działania, nie zważając na okoliczności. Musi przy tym zachować wiarygodność i poprzez szczerość zdobyć przyjaźń i zaufanie partnera w działaniach. Wzajemne zaufanie i szczerość pomiędzy wspólnikami czy partnerami dopóki istnieje, sprzyja mierzeniu się z wielkimi planami.''', \
'1a':'''Zapobiegliwość przynosi sukces. Jeżeli coś jeszcze pozostaje, omeny nie dają wytchnienia. ''', \
'1b':'''Gdy posiada się prawdę wewnątrz siebie, posiada się zrozumienie.
Jeszcze nie do końca posiadłeś wewnętrzną prawdę. Spokój ducha jest zakłócany przez niejasne sytuacje, w które dajesz się wciągać. Zmowy, intrygi, podstępne knowania i machinacje ściągają cię z właściwej drogi. Za każdym razem kiedy chcesz iść w złą stronę, sygnalizują to omeny, które pojawiają się jak znaki ostrzegawcze.
Lepiej więc zapobiegać niebezpiecznym sytuacjom, nie dając się w nie wciągać. ''', \
'2a':'''Żuraw nawołuje w szuwarach. Młode mu odpowiadają. „Mam tutaj smaczne kąski”. „Zjem je razem z tobą”. ''', \
'2b':'''Wołania żurawia zachęcają, choć on sam ukryty jest w cieniu. Nawołuje do wspólnoty w przyjemności. Linia mówi o związku w obrębie tej samej płci, niekoniecznie seksualnym. Wewnętrzna prawda może, ale nie musi oznaczać, że ktoś ma inklinacje homoseksualne. ''', \
'3a':'''◆ Spotyka towarzysza. Raz uderza w bęben, to znów przestaje. Raz płacze, to znów śpiewa. ''', \
'3b':'''Jesteś w związku, od którego się uzależniłeś. Twoje zaangażowanie emocjonalne połączone z wewnętrzną słabością powoduje, że odgrywasz rolę marionetki, robiąc to, co chce twój partner. Masz wewnętrzne opory przeciwko takiemu związkowi, ale nie masz siły go zerwać. Przyciąganie i odpychanie, rozstania i powroty wywołują stałą huśtawkę emocjonalną, od ekstazy po depresję i na odwrót.
Powoduje to, że wpadasz w złość i udrękę. To, co wydaje ci się romantyczną miłością, wcale nią nie jest. Ulegasz złudzeniu i niepotrzebnie trwasz w tym związku, chyba że lubisz te krańcowe stany i takie życie ci odpowiada - wtedy nie możesz żalić się na swój los. ''', \
'4a':'''◆ Księżyc jest prawie pełny. Koń z zaprzęgu odbiega. Nie zrobisz błędu. ''', \
'4b':'''Towarzysz nagle opuścił ciebie. Nie ponosisz za to odpowiedzialności, to nie twoja wina. Nie możesz nic na to poradzić. Ale nie martw się. Nie ma tego złego, co by na dobre nie wyszło. Poszukaj przyjaciół wyżej postawionych i zwróć się do nich. Tak jak księżyc, który zwraca się do słońca. Być może nie będzie to łatwe i nie nastąpi prędko, ale zachowując pokorę i cierpliwie szukając, natrafisz w końcu na właściwych ludzi. ''', \
'5a':'''* Wewnętrzna prawda w nim. Łączy się z innymi. Nie ma błędu. ''', \
'5b':'''Tak! Ma Ją! Posiadł wewnętrzną prawdę. Ona należy do niego, tak jak związany jest z nią. Wewnętrzna prawda oznacza zrozumienie.
Siła jego prawdy, jej trwałość i wypływająca z nich wiara w siebie przyciągają do niego i łączą różnych ludzi, którzy stają się jego zwolennikami i zaczynają wyznawać jego idee. Ponieważ są oni zasadniczo różni, a jedynym spoiwem jest on sam, gdy wycofa się z tej sytuacji, może doprowadzić do wielkiej awantury. Jednak nie ma w tym jego winy. To nie on ponosi odpowiedzialność za skrywane ludzkie egoizmy, które dochodzą do głosu w takiej sytuacji. ''', \
'6a':'''Kogut pieje do nieba. Choćby był oddany sprawie, poniesie fiasko. ''', \
'6b':'''Prawda wypowiadanych słów, oparta na intelektualnej analizie i niepoparta doświadczeniem, ma tylko pozory prawdy. Nie można uzyskać prawdy jedynie na drodze poznania rozumowego. Niech wiedzą o tym wszyscy filozofowie. Zazwyczaj prowadzi to do jałowych spekulacji, a często na manowce poznania. Kiedy filozof tylko rozmyśla, pozostawiając swoje prawdy dla siebie, nie ma w tym nic złego. Zło pojawia się, gdy pragnie narzucić swoją wizję innym.
Prowadzi to do nieszczęścia, choćby nie wiadomo jak był przekonany o słuszności swoich idei. Takie wołanie nie zostanie usłyszane w niebie, bo mimo że zawiera w sobie wewnętrzną prawdę, nie zawiera prawdy samej w sobie. Dotyczy to też mówców, którym zależy jedynie na wywołaniu u słuchaczy przekonań, a więc pozorów prawdy, a nie biorą pod uwagą prawdy jako takiej. Niech zważą na to adwokaci i sędziowie. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram62 = {'title':'Mały sprawdzian', \
'ctitle':'Siao kuo', \
'picture':'''Piorun nad górą. Przeważanie małego.
Nadmiar w małym.
Wybraniec kontroluje swoje zachowanie. Kiedy trzeba być .skromnym, zachowuje prostotę; gdy traci, smuci się; kiedy wydaje pieniądze, jest oszczędny. ''', \
'judgment':'''Małe powodzenie. Korzystne jest być stanowczym.
Pozostań na swojej ścieżce. Można realizować małe cele. Nie wolno podejmować wielkich przedsięwzięć.
Gdy ptak obniża lot, śpiewa najweselej; kiedy próbuje się wzbić, ma poważne trudności. Dobrze jest pozostać na dole. ''', \
'interpretation':'''	Póki co, nie należy się odrywać od ziemi. Pozycja, do której aspiruje, przerasta jego aktualne możliwości. Nie dojrzał jeszcze do tego stanowiska. Ponieważ sprawa opiera się na zaufaniu ludzi, trzeba jeszcze wielu mniejszych sprawdzianów, aby nabrać doświadczenia w danej dziedzinie i zdobyć zaufanie ludu. Potrzebne są najpierw małe zwycięstwa, aby móc przejść do spraw wielkiej wagi. Kto nie ma dość sił, by realizować wielkie przedsięwzięcia, nie powinien nadużywać swojego powodzenia i powinien pozostać na małym, rozwijając je stopniowo. Nie wolno zachłysnąć się dotychczasowym powodzeniem. Zachowując swoje cele, należy pielęgnować małe, gdyż ono może się rozwijać. Należy wyjaśnić wszystkie zawiłości i dopracować szczegóły. Oszczędność sprzyja realizacji celów. Należy uważać, by nie stracić gruntu pod nogami.''', \
'1a':'''Wzlatujący ptak spada na ziemię. Złowróżbna. ''', \
'1b':'''Młody, słaby i nieopierzony ptak nie powinien opuszczać gniazda.
Najlepiej będzie, gdy pozostanie w swoim gnieździe, dopóki nie dorośnie i nie okrzepnie. ''', \
'2a':'''* Kobieta nie dochodzi do ojca, a spotyka się z matką. Mężczyzna nie dochodzi do księcia, a spotyka się z dworzaninem. Nie ma winy. ''', \
'2b':'''Nie zawsze trzeba trzymać się utartych schematów. Niekiedy lepiej jest zaprzestać dążenia wzwyż, choć tak nakazuje rutyna. Czasem trzeba poprzestać na mniejszym, zadowalając się skromniejszym stanowiskiem, aby móc się wykazać swoją przydatnością. ''', \
'3a':'''Uważaj na swoje tyły. Jeśli nie zachowasz należytej ostrożności i nie będziesz zapobiegliwy, stamtąd przyjdzie cios. Złowróżbna. ''', \
'3b':'''Nie możesz być zbytnio pobłażliwy, kiedy ktoś knuje za twoimi plecami. Jeżeli nie potrafisz profilaktycznie zapobiec zakusom na twoją pozycję, powinieneś uprzedzić uderzenie. Jeśli będziesz nazbyt zadzierał nosa i pozostaniesz zadufany we własne siły, wierząc w swą moc, zginiesz nawet od niezbyt silnego ciosu. W rzeczywistości, choć zajmujesz eksponowane miejsce, sam jesteś słaby. Nie daj się zaskoczyć. ''', \
'4a':'''Bez winy. Nie trwaj przy tym. Niebezpieczeństwo, gdy pójdzie naprzód. Bądź ostrożny. Nie działaj. ''', \
'4b':'''Odwrotność poprzedniej linii. Mocny człowiek zajmuje drugorzędną pozycję. W takim przypadku nie należy okazywać swojej siły. Należy zachować dystans do swojej roli i zbytnio się z nią nie identyfikować. Pozostając ostrożnym, należy cierpliwie czekać, dopóki nie nadejdą sprzyjające warunki. ''', \
'5a':'''* Gęste chmury nadciągają z zachodu, ale deszcz nie spada. Książę strzela i zabiera skórę do jaskini. ''', \
'5b':'''Należy cierpliwie czekać i być gotowym na właściwy moment. Sukcesu można spodziewać się lada chwila. Jeśli już odniesiesz sukces, nie chwal się tym. ''', \
'6a':'''Ptak wzlatuje za wysoko. Przekracza swoje granice, prowokując autodestrukcję. Złowróżbna. ''', \
'6b':'''Kto zajmuje pozycję, która mu nie przynależy i próbuje wykorzystać ją do swoich celów, prowokuje porażkę i może zostać skarcony przez los. Nie można przekraczać swojej miary. Kiedy brakuje sił i doświadczenia, sprawy łatwo mogą wymknąć się spod kontroli i spowodować upadek. Zważ na los Ikara. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram63 = {'title':'Spełnienie', \
'ctitle':'Ci czi', \
'picture':'''Rzeka nad ogniem. Woda gasi ogień. Spełnienie.
Już osiągnięte.
Wybraniec jest świadomy zagrożeń i zabezpiecza się przed złym posunięciem. ''', \
'judgment':'''Powodzenie w małych sprawach. Trzymaj się swojej ścieżki. Początek udany, na końcu zamęt. ''', \
'interpretation':'''	Dokonuje się przemiana. Wypełnia się czara powodzenia. Następuje właśnie moment spełnienia w życiu. Przewidywane niebezpieczeństwo wynika z ideału sytuacji, jaka nastąpiła. Wydaje się, że wszystko idzie gładko i panuje pełny ład, ale właśnie teraz trzeba być szczególnie ostrożnym i przezornym, aby nie dopuścić do roztrwonienia sukcesu. Należy uprzedzić zagrożenie wynikające z nieuchronnej zmiany i dezintegracji, jaką ta zmiana powoduje. Należy rozpoznać niebezpieczeństwa i zażegnać je dzięki zawczasu podjętym działaniom. Będąc świadomym niebezpieczeństwa rozpadu, należy usilnie starać się utrzymać osiągniętą pozycję, nie pozwalając sobie na odpoczynek i niedbalstwo. Nie można pozwolić, by woda z czary powodzenia przelała się i zagasiła wewnętrzny ogień, będący źródłem sukcesu. Czas jest tu elementem sprzyjającym; im dłużej utrzyma się pozycję, tym trwalszy będzie osiągnięty sukces.
Dobrze jest ustalić nowe cele i zacząć je realizować.''', \
'1a':'''Zatrzymuje powóz. Lis moczy ogon. Nie pomylisz się. ''', \
'1b':'''Sukces osiągnięty. Moment po spełnieniu. Nawet gdy inni uważają, że można jeszcze z tej sytuacji wyciągnąć jakieś korzyści, ty nie daj się ponieść ich nastrojowi i powstrzymaj dalsze działania. Los może się nagle odwrócić i zamienić sukces w niepowodzenie. ''', \
'2a':'''* Kobieta traci zasłony w swoim oknie. Nie należy ich szukać. Odnajdą się po siedmiu dniach. ''', \
'2b':'''Nagle traci ochronę swoich zwierzchności. Może się tak zdarzyć, gdy realizacja jakiegoś projektu dobiegnie końca. Nie należy z tego powodu popadać w panikę i dać się ponieść impulsom, by ją jak najszybciej odzyskać. Lepiej poczekać cierpliwie, nie zmieniając swojej pozycji, dopóki opiekuńcze skrzydła same nie wezmą cię pod siebie. ''', \
'3a':'''Starożytny cesarz podbił ziemie barbarzyńców i podporządkował je po trzech latach. Nie należy angażować prostaków. ''', \
'3b':'''Czegoś, co zostało osiągnięte wielkim trudem i nakładem sił, nie można zostawić w rękach ludzi odpowiednio nieprzygotowanych, gdyż swoją niekompetencją zmarnują ten wielki wysiłek. Co innego potrafią żołnierze, czego innego wymaga się od zarządców. ''', \
'4a':'''Eleganckie kreacje i wytworne ubiory idą w strzępy, by zatkać nieszczelność łodzi. Zachowaj czujność przez cały czas. ''', \
'4b':'''Trzy lata zmagań z przeciwnikami okazały się bardzo wyczerpujące dla prostych ludzi. Stracili oni zaufanie do swych przewodników.
I ty nie bądź zbyt ufny. Gdy przedsięwzięcie jest już bliskie finału, trzeba być uważnym, by niepozorne rysy na burcie statku sukcesu nie przekształciły się w szczeliny. Gdy tak się stanie, trzeba zareagować, aby zapobiec większemu nieszczęściu. Nie czas żałować róż, gdy płonie las. Gdy zagrożone jest istnienie, nie można oglądać się na konwenanse. Coś, co w normalnych warunkach byłoby stratą, w tych szczególnych zapobiega nieszczęściu. Lepiej zawczasu zapobiec fiasku, wtedy, gdy jeszcze wszystko można uratować. ''', \
'5a':'''* Sąsiad ze wschodu ofiarował wołu, ale nie dorównał drobnej ofierze sąsiada z zachodu. Szczerość będzie doceniona bardziej. ''', \
'5b':'''Najmniejsza ofiara, ale ofiarowana szczerze, ma większą wartość aniżeli talar podarowany w sytuacji braku szczerości albo gdy komuś zbywa bogactwa. Gdy uczciwość i szczerość goszczą w sercu, zwiastują sukces. Pomimo trudności finansowych daj z siebie wszystko, czym dysponujesz, żeby dopiąć swego. Niebiosa pomagają tym, którzy pomagają sami sobie. ''', \
'6a':'''Wpadł do wody i zanurzył się po same uszy. Niebezpieczeństwo. ''', \
'6b':'''Ktoś jest w położeniu lisa, który idąc przez zamarzniętą rzekę, wpada z głową pod lód. To jest bardzo trudna sytuacja, właściwie już fiasko działań. Można się jeszcze jakoś wyratować z tej sytuacji, ale niebezpieczeństwo jest wielkie. ''', \
'all1':''' ''', \
'all2':''' '''}

hexagram64 = {'title':'Przed spełnieniem', \
'ctitle':'Wei czi', \
'picture':'''Ogień nad rzeką. Słońce nad chmurami.
Przed spełnieniem. Jeszcze nie osiągnięte.
Wybraniec patrzy na rzeczy i widzi je, jakimi są, określa dla nich właściwe położenie. ''', \
'judgment':'''Właśnie przekracza. Powodzenie.
Jeżeli młody lis, gdy postawi już łapę na drugim brzegu rzeki, zmoczy ogon, wszystko zaprzepaści. ''', \
'interpretation':'''	Cel nie został jeszcze osiągnięty. Stan tuż przed przejściem.
Właśnie następuje ostatni etap przedsięwzięcia. Teraz jednak trzeba najbardziej uważać. Wydaje się, że panuje pełny zamęt, że nic nie jest na swoim miejscu. Jednak należy dokładnie przyjrzeć się sprawom, nie popadając w przesadny pesymizm. Dostrzec wtedy można, że są szanse wyjścia z obecnej, trudnej sytuacji, a sukces możliwy do osiągnięcia. Do celu właściwie jest niedaleko. Gdy panuje pełny nieład, każda zmiana prowadzi ku lepszemu. Teraz może już być tylko lepiej. Trzeba powoli poukładać sprawy, zachowując nadzwyczajną ostrożność. Ale uważaj, ostatni etap jest najważniejszy. Jeżeli pójdziesz ten ostatni odcinek zbyt odważnie, nie zachowawszy czujności do końca - przegrasz. Może cię zgubić twoja pewność siebie, wynikająca stąd, że do tej pory wszystko się udawało. Najpierw trzeba zbadać naturę rzeczy, ułożyć je na właściwe miejsca. Potem nastąpi spełnienie. Zachowaj się do końca jak doświadczony lis przechodzący zamarzniętą rzekę - wytrwaj przy swoim, a nastąpi spełnienie. Nie bądź jak młody lisek, który nie podjął działania, kiedy miał na to czas, gdyż w takim razie wpadniesz w kłopoty i twój plan się nie powiedzie. Ty nie możesz popełnić ponownie tego błędu.
	Heksagram ostrzega, że historia porażki może się powtórzyć.''', \
'1a':'''Lis moczy ogon. Bo nie może wziąć pod uwagę końca. Jego wina. ''', \
'1b':'''W czasie zamętu istnieje pokusa, aby wyrwać się do przodu i przyspieszyć konkretne działanie. Ale nie zna konsekwencji tych działań. Powinien się powstrzymać i przemyśleć swoje położenie, sprowadzając problemy do prawdziwych rozmiarów. Inaczej spotka go niesławna porażka. ''', \
'2a':'''Zatrzymuje powóz. Obiecująca. ''', \
'2b':'''Wciąż nie nadszedł właściwy moment, by rozpocząć przedsięwzięcia. Trzeba przyhamować, pozostając ciągle gotowym do podjęcia działań. Tak jak pozostaje się w samochodzie z włączonym silnikiem, aby w każdej chwili móc odjechać. ''', \
'3a':'''Przed spełnieniem. Jeszcze nie osiągnięte. Dobrze jest przekroczyć wielką wodę. ''', \
'3b':'''Wreszcie nadszedł czas na działanie. Ale nie działaj - zebrane siły są bowiem niewystarczające. Nie rokuje to powodzenia ruchu naprzód. W takiej. sytuacji trzeba być elastycznym, aby jak najszybciej stworzyć nowe okoliczności i zmodyfikować swoją aktywność. W tym celu należy zerwać niektóre nieefektywne związki i przemeblować elementy sytuacji tak, aby zmienić układ sił na bardziej korzystny. ''', \
'4a':'''Niezłomność sprzyja szczęściu. Do ataku! Po trzech latach czeka go wielka nagroda. Znika poczucie winy. ''', \
'4b':'''Naprzód! Teraz nastał właściwy czas na działanie. Musisz podjąć zdecydowane kroki. W tej chwili nie możesz się bać ani wahać. Posiadasz dość siły osobistej, a twoje wewnętrzne zasady są trwałe i jasne. Doprowadź swoje dzieło do końca, ufaj w zwycięstwo. Nagroda, która cię czeka, będzie warta siebie. ''', \
'5a':'''* Jasność i moc w nim. Nie ma poczucia winy.
Trzymaj się swojej ścieżki. Powodzenie. ''', \
'5b':'''Moc jest z tobą, wiedza jest w tobie. Dopiąłeś wielkiego celu. Ciemne moce zostały pokonane. Zwycięstwo. Teraz możesz zbierać owoce swojego trudu. ''', \
'6a':'''Celebracja triumfu, uczta zwycięstwa. Powodzenie, jeżeli lis nie wpadnie po uszy do wody. ''', \
'6b':'''Nadeszły nowe, wspaniałe czasy. Wielki sukces powinien być odpowiednio uczczony w gronie zaufanych przyjaciół. Odtąd trzeba dbać o osiągnięty dobrobyt, by nie zaprzepaścić trudów i efektów zwycięstwa. Wybraniec wie, jak tego dokonać. Ale jest też taka możliwość, że po osiągniętym sukcesie dalej zostaną popełnione grube błędy i poniesione straty. Na to trzeba uważać. ''', \
'all1':''' ''', \
'all2':''' '''}

terms = {'title':'Słowniczek terminów i symboli', \
'bez winy':'znaczy, że brak jest wyrzutów sumienia, gdyż nie popełniono błędów. Również, że można naprawić chwilowe odstępstwo z właściwej drogi i skorygować swoją pozycję.', \
'biały':'kolor niewinności, prostoty. Wyraża umiarkowanie i czyste intencje.', \
'błąd':'niewłaściwe posunięcie. Nie od razu powoduje kłopoty. Dlatego można i należy go jak najszybciej naprawić.', \
'czas obiektywny heksagramu':'czas właściwy określonym porom roku. Gdy wylosowany z tym tekstem heksagram zgodny jest z czasem jego losowania, znaczy to, że chwila jest odpowiednia, harmonizuje z naturalnym biegiem rzeczy.', \
'deszcz':'oczyszczenie, uwolnienie od złej energii, ulga dla świadomości', \
'determinacja':'stałe dążenie, wytrwałość, stanowczość podążania daną ścieżką.', \
'dziesięć dni lub lat':'okres nieokreślony, ale bardzo długi. Musi bowiem minąć pełny cykl kosmiczny. Czasem literalnie oznacza taki przeciąg czasu.', \
'doświadczony człowiek':'synonim mądrego umysłu.', \
'fortunna':'działania zmierzają w dobrym kierunku.', \
'klacz':'symbol pierwiastka żeńskiego. Symbolizuje poddanie, uległość, wytrwałość.', \
'koń':'pozytywny pierwiastek męski.', \
'korzystny':'obiecujący, udany. Właściwe działania podejmowane we właściwym czasie, zgodne z ładem wszechrzeczy. Prowadzi do wewnętrznej harmonii i szczęścia.', \
'krowa':'pozytywny pierwiastek żeński.', \
'księżyc':'pierwiastek żeński w swym tajemniczym aspekcie.', \
'mądry umysł':'doświadczony człowiek, ten który posiadł prawdziwą mądrość i może służyć radą. Zazwyczaj w bliższym lub dalszym otoczeniu każdego znajduje się taki ktoś. Również sam I Cing.', \
'nieskazitelny':'człowiek dążący do wolności, zachowujący cnoty i unikający odstępstw od właściwego postępowania.', \
'nieszczęście':'pojawia się, gdy zamierzenia są złe, a czyny i uporczywe działania niezgodne z ładem nieba.', \
'niezłomność':'trwałość w dążeniu lub wierność swoim przekonaniom, też trzymanie się swojej ścieżki.', \
'obiecująca':'należy się spodziewać pozytywnych rezultatów.', \
'poczucie winy':'wyrzuty sumienia; pojawia się na skutek świadomych działań, nie jest wynikiem zrządzenia losu. Gdy pojawia się w wyroczni, znaczy, że człowiek zszedł ze ścieżki i powinien zastanowić się nad sobą, póki to odstępstwo nie jest jeszcze zbyt duże. Ostrzega przed kontynuowaniem dążeń w tym kierunku. Skłania do „żalu za grzechy”, który powinien wpłynąć na porzucenie niewłaściwej drogi.', \
'południe':'ziemia do uprawy, bezpieczna ale wymagająca trudu.', \
'południowy zachód':'sprzyjający osiągnięciom kierunek podążania.', \
'powodzenie':'synonim sukcesu.', \
'północ':'ziemia, gdzie czyhają niebezpieczeństwa.', \
'północny wschód':'kierunek wiodący na manowce.', \
'prostak':'człowiek małoduszny, posiadający zawężone horyzonty, pionek życiowy i głupiec.', \
'przekroczyć wielką wodę':'trudne, ryzykowne, ale właściwe przedsięwzięcie, dające prognozę sukcesu podejmowanych działań. Tekst pojawia się, gdy człowiek dysponuje odpowiednimi walorami wewnętrznymi i siłą osobistą.', \
'rabuś':'nikczemnik, łotr, zły człowiek. Intencje jego są nieczyste. Symbol ekspansywnego, agresywnego pierwiastka.', \
'siedem dni lub lat':'okres, który obejmuje pełny cykl sześcioelementowej zmiany. Zmiana może dotyczyć miesięcy lub lat. Czasem oznacza literalnie siedem lat lub dni.', \
'siła osobista':'wynikająca z odwagi, jasnego osądu i wewnętrznej mocy, pojawia się na skutek odpowiednio długiego przebywania na właściwej ścieżce. Jest to skumulowana pozytywna energia, której można użyć w dobrym celu. Nie należy jej mylić z siłą fizyczną.', \
'smok':'symbol męskiej siły yang, w jej twórczym aspekcie. starożytni królowie - wielcy władcy starożytności stanowiący wzór do naśladowania.', \
'sukces':'zamierzenia będą udane, plany się powiodą, cel zostanie osiągnięty.', \
'szczęście':'synonim powodzenia i sukcesu. Wyraża dobry koniec zamyślonych zamiarów, które zgodne są z ładem wszechrzeczy. upokorzenie - pomniejszenie, nieprzyjemne uczucie pojawiające się, gdy sprawy zabrną za daleko na złej drodze. Dotyczy tych, którzy in tencjonalnie albo lekceważąco brną w złym kierunku i nie chcą zawrócić ze złej drogi.', \
'ścieżka':'droga prowadząca do wolności, ale wąska. Taka, o której wspomina Chrystus, gdy mówi: Szeroka jest brama i przestronna droga, która wiedzie na zatracenie [do piekła], a ciasna jest brama i wąska droga wiodąca do żywota (do nieba). Ścieżka, ponieważ jest wąska, wymaga ostrożności i skupienia w podążaniu nią.', \
'trzy dni lub lata':'okres nieokreślony, ale stosunkowo krótki. Czasem literalnie oznacza taki przeciąg czasu.', \
'wielki człowiek':'człowiek, który jest w harmonii z niebem, nosi Prawdę w sobie. Też sam I Cing.', \
'wina':'pojawia się na skutek uporczywego, niezważającego na ostrzeżenia postępowania.', \
'wschód':'ziemia nieprzyjazna, ziemia wrogów.', \
'wybraniec':'być może jeden z owych stu czterdziestu czterech tysięcy, o których wspomina Biblia. W każdym razie człowiek, który odważył się podjąć odpowiedzialność za swój los i chce prowadzić świadome i szczęśliwe życie.', \
'wytrwałość':'stałe dążenie, synonim determinacji.', \
'zachód':'ziemia przyjazna, ziemia przodków.', \
'zacny człowiek':'człowiek szlachetny, posiadający szerokie horyzonty, pełen cnót i zalet osobistych, których używa w zbożnym celu.', \
'złoty':'kolor złotego środka, bardzo pozytywny. Wyraża doskonałość, prawdę i wewnętrzny ład.', \
'złowróżbna':'pojawia się, gdy sprawy zmierzają w zdecydowanie złym kierunku.', \
'znakomite posunięcie':'ruch w bardzo dobrym kierunku, przyniesie powodzenie.', \
'żal':'skrucha, wyraz bliskoznaczny z wyrzutami sumienia, pojawia się, by ostrzec przed zejściem ze ścieżki.', \
'żółty':'kolor bardzo pozytywny, barwa harmonii, spokoju, umiarkowania. Wyraża jasność i piękno.'}


# other important dictionaries

maindict = {"777777":1, "888888":2, "788878":3, "878887":4, "777878":5, \
"878777":6, "878888":7, "888878":8, "777877":9, "778777":10, "777888":11, \
"888777":12, "787777":13, "777787":14, "887888":15, "888788":16, "788778":17, \
"877887":18, "778888":19, "888877":20, "788787":21, "787887":22, "888887":23, \
"788888":24, "788777":25, "777887":26, "788887":27, "877778":28, "878878":29, \
"787787":30, "887778":31, "877788":32, "887777":33, "777788":34, "888787":35, \
"787888":36, "787877":37, "778787":38, "887878":39, "878788":40, "778887":41, \
"788877":42, "777778":43, "877777":44, "888778":45, "877888":46, "878778":47, \
"877878":48, "787778":49, "877787":50, "788788":51, "887887":52, "887877":53, \
"778788":54, "787788":55, "887787":56, "877877":57, "778778":58, "878877":59, \
"778878":60, "778877":61, "887788":62, "787878":63, "878787":64}

names = {1:"Niebo", 2:"Ziemia", 3:"Rosnąca udręka", \
4:"Młodzieńcza niewiedza", 5:"Oczekiwanie na wyjście", \
6:"Konflikt", 7:"Wojsko", 8:"Związek", 9:"Małe Ograniczające", \
10:"Stąpanie", 11:"Pokój", 12:"Separacja", \
13:"Wspólnota w otwartej przestrzeni", 14:"Wielka nagroda", \
15:"Umiarkowanie", 16:"Entuzjazm", 17:"Naśladowanie", \
18:"Naprawianie zniszczeń", 19:"Przybywanie", 20:"Kontemplacja", \
21:"Przegryzanie", 22:"Piękno", 23:"Rozpad", 24:"Punkt zwrotny", \
25:"Zaskoczenie", 26:"Wielkie magazynowanie", 27:"Usta", \
28:"Wielki sprawdzian", 29:"Topiel", 30:"Ogień", 31:"Wpływ", \
32:"Trwanie", 33:"Odwrót jako władanie", 34:"Wielka potęga", \
35:"Postęp", 36:"Zmrok", 37:"Ród", 38:"Opozycja", 39:"Przeszkoda", \
40:"Uwolnienie", 41:"Umniejszenie", 42:"Powiększenie", 43:"Przełom", \
44:"Spotkanie", 45:"Zgromadzenie", 46:"Dojrzewanie, drzewo", \
47:"Okowy", 48:"Studnia", 49:"Rewolucja, przewrót", \
50:"Naczynie ofiarne", 51:"Piorun", 52:"Góra", 53:"Stopniowy postęp", \
54:"Poślubienie narzeczonej", 55:"Obfitość", 56:"Podróżnik", \
57:"Wiatr", 58:"Przyjemność", 59:"Rozpraszanie", 60:"Ograniczenie", \
61:"Wewnętrzna prawda", 62:"Mały sprawdzian", 63:"Spełnienie", \
64:"Przed spełnieniem"}

hexagrams = {1:"䷀", 2:"䷁", 3:"䷂", 4:"䷃", 5:"䷄", 6:"䷅", 7:"䷆", 8:"䷇", \
9:"䷈", 10:"䷉", 11:"䷊", 12:"䷋", 13:"䷌", 14:"䷍", 15:"䷎", 16:"䷏", \
17:"䷐", 18:"䷑", 19:"䷒", 20:"䷓", 21:"䷔", 22:"䷕", 23:"䷖", 24:"䷗", \
25:"䷘", 26:"䷙", 27:"䷚", 28:"䷛", 29:"䷜", 30:"䷝", 31:"䷞", 32:"䷟", \
33:"䷠", 34:"䷡", 35:"䷢", 36:"䷣", 37:"䷤", 38:"䷥", 39:"䷦", 40:"䷧", \
41:"䷨", 42:"䷩", 43:"䷪", 44:"䷫", 45:"䷬", 46:"䷭", 47:"䷮", 48:"䷯", \
49:"䷰", 50:"䷱", 51:"䷲", 52:"䷳", 53:"䷴", 54:"䷵", 55:"䷶", 56:"䷷", \
57:"䷸", 58:"䷹", 59:"䷺", 60:"䷻", 61:"䷼", 62:"䷽", 63:"䷾", 64:"䷿"}

chnames = {1:"乾", 2:"坤", 3:"屯", 4:"蒙", 5:"需", 6:"訟", 7:"師", 8:"比", \
9:"小畜", 10:"履", 11:"泰", 12:"否", 13:"同人", 14:"大有", 15:"謙", 16:"豫", \
17:"隨", 18:"蠱", 19:"臨", 20:"觀", 21:"噬嗑", 22:"賁", 23:"剝", 24:"復", \
25:"無妄", 26:"大畜", 27:"頤", 28:"大過", 29:"坎", 30:"離", 31:"咸", 32:"恆", \
33:"遯", 34:"大壯", 35:"晉", 36:"明夷", 37:"家人", 38:"睽", 39:"蹇", 40:"解", \
41:"損", 42:"益", 43:"夬", 44:"姤", 45:"萃", 46:"升", 47:"困", 48:"井", \
49:"革", 50:"鼎", 51:"震", 52:"艮", 53:"漸", 54:"歸妹", 55:"豐", 56:"旅", \
57:"巽", 58:"兌", 59:"渙", 60:"節", 61:"中孚", 62:"小過", 63:"既濟", 64:"未濟"}

trigrams = {"777":"☰ Niebo", "778":"☱ Jezioro", "787":"☲ Ogień", "788":"☳ Błyskawica", \
            "877":"☴ Wind", "878":"☵ Rzeka", "887":"☶ Góra", "888":"☷ Ziemia"}

cyfry = {1:"pierwsza", 2:"druga", 3:"trzecia", 4:"czwarta", 5:"piąta", 6:"szósta"}
cyfry2 = {1:"pierwszej", 2:"drugiej", 3:"trzeciej", 4:"czwartej", 5:"piątej", 6:"szóstej"}

linijki = {"6":"▄▄▄▄▄▄   ▄▄▄▄▄▄", "7":"▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄", \
"8":"▄▄▄▄▄▄   ▄▄▄▄▄▄", "9":"▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄"}

# the pictures (base64)
backgrpic = "iVBORw0KGgoAAAANSUhEUgAAAk4AAAFyAQMAAAA5x8f9AAAABlBMVEX///8rGgoxImm6AAAAAXRS\
TlMAQObYZgAAFxNJREFUeF6VnD/O5biRwEnIsJLGMHUwaF1hQgcN6ypzBIcdNCwaDhz6CD7Kylhg\
HfoKGswFuHBgLsylFlL9F0l9swpm+n1P/D0WWSxWFUtyzs3nWZ1bzvNwzk1ncXDBN9FN5/Vf58+z\
uOtDcveH0zkXrib6mi7UBTyAuyPoxmfnNkTd3xjU9ES5G+WBEe7Wgir3n6D1xZ2h9Xqj3BYfqHCh\
3Eqo84Fy0GyBbwA13U1cMBwen/mMIKD0eoIuLgU+3J8WkH+rbsYuJc3ayi0nSKsl3G7UXPDDWd0N\
AHwAxlQ1aslXV1fHcsgU3rdnHAc1JVN2oQJK/ugPNyW37u6TIzkSf3ce7nfcWjr8o3O/JVWYz6z4\
bndbkvlUqrUebttZXO7wBv2vqHwsRIVhZGmNHLvDnnzhKaFpXFF96I+kKdQcGmSjdfHuyH53uAIq\
AyoBiroRroYem0+J5JDhOhO0xg7D3wzq3FmgCwXoqcB3h0aBqlScEpiAw6Ayo/YLhRq63w2qQsG6\
ufEbtJpu/Ayo+YS2gEoXCscQJYwNClYgoOBu7PyFSnb577Qcg0Y5QuE4JERVWLWmW4F+b7fSinJU\
QMH4kGE4I+m5dMufOIWRpHULodAIkOayjVkQjEPEWr3dyBUsCXWxWewLSHF3el8RHHk4QdaAcyrS\
OoMKBUYEOrzfDU9RpltsaIZm1VeR1i1VoaYLTqru40Yo+LMHi4/kc3dfnfsG6xd0RaPc77WNmU6+\
cCgjqE+6DFXY0ezJJpJdc3kYn1OuxCY43KjlcFP0IDgu+q+uvb7AiDivUJU3OHej1ktkLyZq4S7O\
UU8jrs1ZSLzbJVSi9QT1hdb7BcBlEJKW7gAJNwGJjcEluuFYHtza42Jeq0YVUK2zj3LLheJlCkrA\
iu9WUnnq9jRCoUmhXb5y6wm5GxtT8hValDQ94/X1cf8eoA7hbqTz2KCV8IDbYGEh6gJia0FpYzqT\
jZFL1l3BDX+DNc4d2d3UoqjbDQqt/nIAFIQqiErCVSi39VAOlQamC/XAa9QMqKBRYYzyCewpzfmW\
yc5fdBgZRpGy+RblEzAySOh8dDNZ1IP0Z4ffomstbv5zi5pgumh/vDfSGwWtYZ3l2+NKygAGwyGb\
c6gZqm4uMiS7TxvdeEZfWcLcWTg0X2RxvnezLJEz8vIobtHO0w8NCpdcpOk6rNO8RjYjsIiyMjQW\
RD5vJk+93CiQcHHukxNUuu+MY9QJRow06gQdgC5d0qyMqqgdLHxzRfRVwFSBekODNdsGEdztMWp3\
AeW8UeVCkbJbo3R8hDrYYQAD77jBBo2VhO8ocnsKBAOILnBvsWMbvUL5FlWMe4WbWybH5yHAqlzp\
Hkr8GDR6K6P+bgWAIGCIqrhrn4Q6qEHvVkGFs72os4fENGRv2luX4w3l0Y+p1JziqamjODOjlg7q\
T0V1K0CD2J1uE4VuHdTP4scAMw9/uALlGKH+dWb0Y1DCOlYdEBy0rn9Bq0Rb3I4WqUUlR1bXD1CH\
LHrPElZCtT7UMUYVtaFsrGKxQVG4knl6u3esiAocT6VL2L63EgnVX4g3QMdTNbSoDCgwJ8NuAQqN\
/EiCDDpSX1Dp9mOc7OiDexPFwGGIqsrHH6NkReSli/lPsybAyA9RpJ1rF7VvtlvLGYeoHW4YXcfM\
N0lw4dwYNY9RbrMZgLO/mGUcXmYvnCYS/Q4W8xi1jFEe77LX1lcG/6LqGYxneqLW/r0TpAVGOjU1\
KH90URXyV0MF3bX/K77YNkBBlD+UMDxR09mfJ85jDC7JDanY46fBug/oHo0Xc4Myl/WMdv11DY8R\
8KJXr6qzQ/Jh1m2fA7/GN02wTtYZg0YtTyvq/h+oFEzTZ7d+GSrdOlgElQ3K6Of7WLWKkJrV+kT5\
Fx1sFnjXs/DpXcJ2C9ybhV8RJfFNH1WevxLNH/4s3ZpY0mmAmh/DbAc20sD/CvyBt8Eq4ehkYgQV\
FCq/o2ooRsJiJYieUBAUv6Ku/Wh+oLyahFVZ7WM8VrABWgnBdgtqUqjyEUpLiO2CsaI7oeq7lTkf\
NiY/UeFjlGktqGJQSczVxKjwilqHKDFX8N2HqGUgYPosecoAqLFp+AfYb4uaGbUmQBUK2i3qLxoV\
H6jkfmNQlVFwWGLjb29QVx7vh0UHiRoFqgBmYWlQxQi7X8t0WxVq211QqIIoia02NRqTRrlz98pl\
3N1WRd5Evn1xqePHHMBl1BIJRScJcdWoA9I/tROw/5dzy88azL2kzGBmEf77kgJQuBR/p1FzdNMf\
bcrSOmfq+ptCZZBOyVBDMrNgUcWidhGQjEYSVAnVqNluVkJ9oALuqYUcGq1LeYHWg+3rgfJI+ORO\
yguowVlt62qtRnSrRnGuWU5//1fmaD1P09o6fccD7C1qakdytjGt+fQILJ1GzU9UfqjSbN08gwp4\
Jnrf2KJOizJW1KAcXnwGNllT8DiFaPJ2a4Pyd4YtPgOJeIGrRVnNElJlVKbxDxrlNmv+ok9mCP5m\
UHKiviLVOrLq+vsZfRk6Jxr16yZU2p+6cSVtP0DNBLUSJutQxc+X/R+gcoP6kQVo/dZ4f3xFwb61\
03axaZS3qHCe//wYlWHQldphoYRFja6khr0Cygy1Hbr9LaJP6pj03JHpTGPf3+XHGbwZUHBUvA3W\
HDl97yj3jVFJoRKjxKqU9QPUJ0cLrDZTqFHLAGXLFUg/ESUW2JqrPBgvhaqCMkHuMxIZoXaFYtdv\
tQvaRiIhDVBFUPDPB+qwi3DanR+hVNgM47ZYRyg7MxwzJvw+GPjfot5njareoqo1/++B5ZmNTNpO\
FHDMpxEqac50DesotExfsGjlF6Hm5PzhtroNsxtn/KUoOrLsozC26mF+eqBwAxst2BtV+qi4ipKi\
KqTxWCRCrT3U/ECtZxmj6hvqGpZoUK/DGvH0aennySxqA2d1PFjg+Q1Ol9wDVUYziB3KXXXP3zu3\
WNRIANmtU1fd02ar6G5IeV8ZW3+KDzTIHqXkyoiXfHq4mvRQhes5jBe5vUiocjrWO4pSZMiFNl/H\
qDzKC/8Rv5sASWV+J+tge8UBiqozZr1NR3fu3SlML5nyOnGxDEr62d0RXw5dBZXqqlbwWR/nYQXI\
dInbR00koW973KA2jCd+bkHkS6QuavdP1Fne8r5cuDf1jkcBMSHKv3pjzrkh6nATCcZjkIcoDDJT\
t9+ZzVVgVH1FzYxqJQysc6Cf5Kr/daDoFNW3EvJCDoDCrna1IYHl6J/LUjDCVXMTe1TzADUPz5gw\
GDkc1s1STFu7IlDdaddgpUfGd8G8WfEjTyzEQZa5AkrsAk5GcS/eE0i4KEqQc2mxCzgZqTOwplLQ\
n7P1wYy5Egm7EhTrtf7OWSezNVczJ6zHXopUDItOqeRPoY1HAuRx5YDnzLvEK/rYFpUroCz+FXUa\
VKV1IgM0UVcjo1oBpWLYbo+MkgqkTYIkexlUMajMlbMTV1CdIuHWqqitx9PaIFqw0UmRlDG32pAN\
Kjmv0nJsW6SyCCWsXT9fUOS2FR+5omk+dVnqgpYPLfxwDj0l3ovWyorbO6FOsMqAH0q4ooQZPx0u\
O4d57YlRXJo3XNAi4ZK4CBel9wcWVU40SqlZhbuolkg4Jfy0kyvkK6XaAYV/D00iq5qzunLnz640\
+br7s7DzAv9esI7rRk3GLEwsIX+H1MscklZNYDgpgLtLdM1gsatrE9aHFMhNciIQMbi5UMCxg/UX\
lNdKCKjM+k8PzXxzMwRwBUC/0YN18fXiYXlxU1Z+THXu08WZDs64rk7nfzMXia9SnZO4kD08/JhQ\
4Su8VwXgcaXlG4BHqkWzHrS54roPLpuXs+oK5T3GdHlC4c4pqJOr0GkM4LwPm242xohSYeVV9Io9\
P1QAdwAqYeMqpcS2JKgIihRL7o9cOOUxyQ/k54EHMBh1M2TH2iWAy+w0L5wNs45X5vGgk8oFUB6+\
ZVkOx5rCPbCJnip7+gyoqYpeF9RBPGCYybBW0aLVGnoOB3aXnPuD2J+C93tEsX8kFvtZ9XRwaTB2\
ycOiKHA/rASylPTUhccjPSsh1X9FNlegMjhfkex9wKHO/fgoSk5oi2yuQAUKrTJ/akvpc/90NamH\
DJw1V1Qxcfs7esH+0K9bLYQ6pALMzeDJFu7IJ6ckpGOwtbsrSihTAIU1uighgHY3GV92Huz7J5mr\
yItpKaYjPgGYrEQjIQfwT3MVnS881HCLqW+trYSZUEVQK/TuCw11dtrVOkiK0Iy7DWWioGTO5dhD\
PMBOHbqzoUzUgTNLCEwAF7y/ncJIKBgLaq4dC3lSzivU0XdsJj6eo+ZuUhJGx8Xq4h/91HNsZHTX\
is0rnzh7RC03chIz2AbmhRQZd2Sa67mKhPoBLPaP/j6Kj3BBImqBLCx3UVALG91/jNytFai/ubC3\
egb26aT6BYwuDu5/jKI6Vfk45cvoLLzU16LLJF6qFfEribpglASFA3izv3Mu7PhpnOYVJ26G1UMo\
tnXgH7HRHeeyZlXmkhFlry27BW9Gf2Fo/VRBSYua4u1qSQFGK6F+2lOU8WhR4GqRwYn9wbILl0KI\
2aLC7f5uZwZU7mfsol64YmMUil0tNjjVbW+oYM3VYlH8bA0a/9czIG9R3qDWszrt1PxPF6UL+rVZ\
+eIOk0reGRU+PIqYAEUj8itXDCp9jJIGW6VBA6U+BcUp//TLUIEsTgUnQzosrtbxhqqih0hdK2TC\
VIexdAVQfoRSYnwBczUXmHxRFFBuLm9dX1HStcP5Ak/ndqJjQIW33LQ9TvotHJTwOIojciJ4cO3J\
oEhPs5OfYX/hs4D7h1MWlel0wyqdWGzn5hEKhkR+nlBW6cRiH0MJfz6zRe2EaiSMMJpD1D/NJK5U\
qldsdOyVxY6MGi9peSCbqtLsHBZAHdMYVd1zTC7I3JdwgeqW0bUb1In74NmVcIWq2Y8PPQOQJ879\
iYSM4utdQk+J9/ysvw+2OvhdQtFkfJLYoNwQNc62gSCY1dxNvXX8AAX9MBJWxCKKPwFxfP0J+tHq\
NZks+REgjq9o7fKkBF5OIbGv+oZarAXcRMKJUOx6vUu4Tx0JDwiRqkb5gvwxCj0iq1qQqPtekfjT\
Gyp0VAsi3/YK1iP6V3N606qWk8cWs0HZOsCsuBhw24EHFHv1GrU8LJ/6gK0ExXm1wNHUbmxjbOov\
jeWzKE+oBKhsUGmyS25tJXRawkyupAhK01cNqrrQFBNUs1lkCVeDWYn0MJhI6C3KbQblHqhklO7f\
ZyOhRoWHH5sEtVjD0VxGQjiLsV4IRluI2l9QhzMosMDq+hFG+ANUAQn1JMycTTJSCiqqPza67jaN\
2p1PDWqWJyHUHw0KzmkEVbhL825YqJsG5QwKjNupUShBsF1bMwsaYk/CZPUTsiKHdpIp7JuT+MxH\
K2Fb+FIvFDCC1uvC5SRb0THP49DboH4A39OEzCYECEk2DCuh9XElToAMj6AOmoopudW+cqKtjlaZ\
6oqoJKjCU/EjnQu1ElobIygAcwueCtvfdVhQWQ3qVKiDErnWE1nsxtCWUXVQBVAZUIVRYwl3Nwuq\
WhRm/D2hAD6cw8zvgAoaJfj9BRVbCTPnIulCPGti7qNaCRPeVXi5mVOV8IKaH/qfJIuTLYokTF3U\
0+5EXq4XCodr06+LEnVvUY9N1V+oT1jxeEieQvzcHuovd8huUIW9FJ8otUMx6USauLdPr1zmZ0pL\
J1RdEmRxUE3xrzSaHdRlfuZqUQlQ9m0xIYpy4yeLKi6U1s11ZrlVjEefOUV/PHrl+q9aIUVFshyB\
6JdH2WHfe15uRtEa1IpN0epZVFEo3sZolHYREGTaEs6hTk/yBWBBLYAiyIKoxLZUPQ6WLWq3qMMz\
iqNdOfo/KUmo0pPDLeeAAF7WyAYoyuUc5vUWyY7OblG87LlmNCkUSXjoFy0OniE72DQtKD6h2PdY\
zGlKsB5IW0AK7eDjBaGqe5JwR5QJAZ6nFJELkjb8+ES5TVCDh0pEwiRBV0KVOp2gFnFLz1EexYjk\
PKkwozy/M41HIL2gTgcifYcqE6XqnkUDlJO69PeczIK7dpaqexGtqsD644zFQp6XoEA0f7hZn628\
Ziw4zF6ll7zx3OfR31RgvY1JqlZmkoH/ypnX6Yz3wcyvQcL3i3Z2E8/jqU6FlYRe2yuGReJVIagp\
X6IF5bWt7yCpGjq0o8H1SoFc1fouYUEUQVaDIvN90Cbr31BSmiYndxJjJkBV3ka2F9mgMEKSMRZV\
ybbA/18lzOxqc4Ft0j76jihQqtc5TFzHtVCBbWrSpFSQ9y5hQl9YJNwOjcJZo1Xz/i4TjpY2vFdQ\
G81ERdTrHB405RdSLN8nhXIbokhdxii37TbPhyhOZSy8jfAc9kZs/wM4PCzhrnJVgUTLxmv7V1/A\
uO1U8ECWT1CevIlkvLZh1jBJrYVI+IX6WaCmC+R9n0NHo7Nl2lQBxVH9sjt/6Pyrb4+Kyejv2AHZ\
VMFq0rliZq8Nv/7cRRV/cg5AS/gNp3GVM9Q1Uilp6KMm2q7YtRBUuEdpo26TTzNApQsFPouJ1oqD\
MiG/u43cgEISzuPXCWUpwloJJTkfsf04LwPrsBNKysYzC7jRKt7Ja5tftvp4oZKptci8cG6Gl25n\
1NIByhpRE2J5foSmGK8tuy4Kq8vEiE4GdVpUwv9uwwzyoU3MZiobD1P5ltEqr8M3uezafQyC4sZJ\
UMsIJeea7Fz52wnSeWkaTKn+W/qKxdnwoGslpNaNbT/q8uBxVJQAUKDKiMraAuNgAirAVPQlDLDu\
tfu4FrVvBH6kYffpTpr7V/fxD2REGSX2iZ/x2H2B6r9tezkP33ZWLcf1e3YElvMe10/jM6aINo72\
Z0ZJZgCVo/LWvfRRCTsgi0dSarIFQWHjrL6w109sNSfQVoPKOiaYCrxwVGq27LWv9LMTG1F+d7Gv\
OCZyuC2nDD0TYx7ImgyK7NMBKPLaBiinUUlykGBdtISB4vfBC+AkagyAYl+r3HSVGQjste09VEZz\
yyhebx5Qu5tVaiIJKvTUYNMo8bW+XXSQkMPKKgJalEgWecORs6RP5MashOJ5ia2KMiPKutdGdOFs\
bBSvbfQkDPsKVC/6VXwtrmK1qACoMCjFkzcGbg6M6PeyAG09HtX8+v55enWct2cjGmUBzlJEpypz\
tm4FyWd6D0NkX2uVnRH7wWdZS289A14eKl+jl0I/XQdOUXS9I8LsWgmzRl1zJYnUFbQSJaQoutwH\
H72nPndF8qhULExWElLj4oKUUIdTwZxG8V6+A6qovf8HiJuXDFsm1sHVpV+3M3FiOasEeTBPrE0J\
ojK0g19nQR0WlSxKEiecfv09VJqxHeyVXt2QKigPKB3fL5THjGIHV3lNlEax05IUCj1ie9pBiiGo\
v6oMOhv1VaNkDvWjD0Wi101SmMWiTjSVugZSTjWpHq+ioIlQ/0b7IyiQEFEzoVZBnVFQGywDTo2y\
hOKnsbtPqIlQcDcJuHFQIfW0eEmwqz0Z/n0ODQKhmGwnx/hpiJoJtTAKMwNZfpjUTDwgkaTKw+/f\
REsKoRIuTlnoKJdZhzbN90WVanA/cMdJylvyWv0OewqcOFwTyVU/Inj1MtJr1urHF1tDk7SAxrIc\
AUULPbDxaiXclc/nDFd79TJ2KEboSJh1AZD43TLSfm/6MUedInzMg1mec2zG8jtjyuYDyM3ioeyC\
vb6ahOISdUFMKOaHZGQ5mDTXSRICKuMcyp7clM8JKj9QhzapaxUJUdfWRkJO/RdnNiTKnxTe2zyT\
F1idBjUZVDIoI+FG5NO+O0OrkEbpkZ84BM9sB4OgUEJBSXHajTp3g8rKqwdZCEWP7dppp4G8mvDI\
syseFCo1B98P1IIBD0Tt7jEhk32WbraoxaDEiJ7J2bkFCQ3Ki7i1LbVxGyHT/wEovKD22egl0wAA\
AABJRU5ErkJggg=="

picture = "iVBORw0KGgoAAAANSUhEUgAAAFkAAABZAQMAAABvxRrsAAAABlBMVEX////86U+Aw01uAAAAAXRS\
TlMAQObYZgAAAUdJREFUeF6l0z9uMyEQBfCHKGgi0bqIzBVSpvjkvdJXprAMR0NKkWvMESgpEJPF\
y59RZKfJVPtr3qx23uKYf1ijOCw4pgnNnAY8M+cFchNbgU0TQcDtoIewPxEfwsTnKAJfVYCrDQtF\
IgpE/A36NziBs8An8wIz4wloW4i4LAScJV4lXiTWmChgG04DBOja4XbMt9uiZea4Tj+b0B7J514c\
TgRX7tD5DQn2iDP0jgzDfecHysCGq6owx9YrakNpUFlVvSM3aNJlwgaTTO64wJJJMKnhP1y01NCz\
3Q46cIOLs2QFWxhQCR4DhlAxemWDKoA7cIHOE7nt6FdVsa1pgeNbCfgAeHRULKgi0JJRO2wSaPvU\
QEtVpYMB6CLCTB5hApZwgk3rl4PruAEmejqQ7o2LsyyqY9w4LHiGQBXYioBLEiQhwnp7vwG+L8P1\
TYei+wAAAABJRU5ErkJggg=="

icon = "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQAQMAAAAlPW0iAAAABlBMVEX////86U+Aw01uAAAAAXRS\
TlMAQObYZgAAAEJJREFUeF4NxKERgDAMQNGvEhmLybEGdzWMEtkJ6roBAzFEh4hEcR2gAszDEgu0\
og/ym8iJLfaXNugXxZENvzkmxAcQCguO+Wn1uwAAAABJRU5ErkJggg=="

exiticon = "iVBORw0KGgoAAAANSUhEUgAAAAwAAAAMBAMAAACkW0HUAAAAGFBMVEUAAAD86U/86U/86U/86U/8\
6U/86U/86U/xtMgFAAAAB3RSTlMAA6WZswiKqdOGQQAAAElJREFUeF4NyLENgCAUQMFHTKwJugAV\
NdWfwNi6giuAyVtfyjt8YRdnJqTZNwenM7xIt34PiwtwaIUUOjLF0RbDWpysSU3scPgDKm4TBCRU\
f8AAAAAASUVORK5CYII="

onlineicon = "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAABBVBMVEUAAAD86U/86U/86U/86U/8\
6U/86U/86U/86U/86U/86U/86U/86U/86U/86U/86U/86U/86U/86U/86U/86U/86U/86U/86U/8\
6U/86U/86U/86U/86U/86U/86U/86U/86U/86U/86U/86U/86U/86U/86U/86U/86U/86U/86U/8\
6U/86U/86U/86U/86U/86U/86U/86U/86U/86U/86U/86U/86U/86U/86U/86U/86U/86U/86U/8\
6U/86U/86U/86U/86U/86U/86U/86U/86U/86U/86U/86U/86U/86U/86U/86U/86U/86U/86U/8\
6U/86U/86U/86U/86U/86U/SUDeMAAAAVnRSTlMATO+BOu4//conKu1RAfz+tiXOEwhK8FAEFVMW\
zD6KGH4U8gqvuH8JZSGEF5pLyfQsAoi5lfFHbEhFHVIvcQ2wbYKsfGEbQ3ZUN6gwnWq6GvjeBehf\
B1onITgAAAC0SURBVHhebcjFmsJAFAXh01EsIQkwE9ydcXd3t/P+j8L9OrCb2tWPf5uaKbtTa1WX\
/2hQl80lX/HZO0kP6xf0tTQNTtqFLu6sBu2ygMmdUujNYK2pPgcCEUdjb5fIhPsHXBfY4ObWNomS\
ciyuCOxl4ysKHKqjYw3B6RklnCvHYUqgeEkNsXq55o3AbT4B3D/QLkBC2hXD0zPdVehe+fZOuDQW\
//H59V0MEJllJGV+foE/LJoDTewfHyWlj2kAAAAASUVORK5CYII="

# actually not used...
picture_black = "iVBORw0KGgoAAAANSUhEUgAAAFkAAABZAQMAAABvxRrsAAAABlBMVEX///8AAABVwtN+AAAAA\
XRSTlMAQObYZgAAAUdJREFUeF6l0z9uMyEQBfCHKGgi0bqIzBVSpvjkvdJXprAMR0NKkWvMESgpEJPFy59RZK\
fJVPtr3qx23uKYf1ijOCw4pgnNnAY8M+cFchNbgU0TQcDtoIewPxEfwsTnKAJfVYCrDQtFIgpE/A36NziBs8A\
n8wIz4wloW4i4LAScJV4lXiTWmChgG04DBOja4XbMt9uiZea4Tj+b0B7J514cTgRX7tD5DQn2iDP0jgzDfecH\
ysCGq6owx9YrakNpUFlVvSM3aNJlwgaTTO64wJJJMKnhP1y01NCz3Q46cIOLs2QFWxhQCR4DhlAxemWDKoA7cI\
HOE7nt6FdVsa1pgeNbCfgAeHRULKgi0JJRO2wSaPvUQEtVpYMB6CLCTB5hApZwgk3rl4PruAEmejqQ7o2Lsyyq\
Y9w4LHiGQBXYioBLEiQhwnp7vwG+L8P1TYei+wAAAABJRU5ErkJggg=="

# the values...
rzut = 1
hexa = ''
linie = ''
after = ''
temp = ''


# info pages in main window (info1 - info7)
def info7():
    B_more.place_forget()
    B_less.configure(command=lambda: info6())
    L_info.configure(text=info_7)
def info6():
    B_more.configure(command=lambda: info7())
    B_less.configure(command=lambda: info5())
    L_info.configure(text=info_6)
def info5():
    B_more.configure(command=lambda: info6())
    B_less.configure(command=lambda: info4())
    L_info.configure(text=info_5)
    B_qaz.place_forget()
    B_wiki.place_forget()
    B_taraka.place_forget()
    B_ichingpl.place_forget()
def info4():
    B_less.configure(command=lambda: info3())
    B_more.configure(command=lambda: info5())
    L_info.configure(text=info_4)
    B_qaz.place(x=7, y=334)
    B_wiki.place(x=126, y=334)
    B_taraka.place(x=238, y=334)
    B_ichingpl.place(x=347, y=334)
def info3():
    B_more.configure(command=lambda: info4())
    B_less.configure(command=lambda: info2())
    L_info.configure(text=info_3)
    B_qaz.place_forget()
    B_wiki.place_forget()
    B_taraka.place_forget()
    B_ichingpl.place_forget()
def info2():
    B_more.configure(command=lambda: info3())
    B_less.configure(command=lambda: info1())
    B_less.place(x=7, y=365)
    B_more.place(x=94, y=365)
    L_info.configure(text=info_2)
def info1():
    picture.place_forget()
    B_less.place_forget()
    L_info.configure(text=info_1)
    L_info.place(x=15, y=0)
    B_more.configure(command=lambda: info2())
    B_more.place(x=94, y=365)
    window.title("I Ching. O Księdze Przemian i tym programie")
    B_info.place_forget()
    B_last.place(x=260, y=365)
    B_ichi.place(x=400, y=365)
    B_exit.place(x=538, y=365)
    window.unbind('<Return>')
    window.unbind('6')
    window.unbind('7')
    window.unbind('8')
    window.unbind('9')
    B_6.place_forget()
    B_7.place_forget()
    B_8.place_forget()
    B_9.place_forget()
    B_random.place_forget()
    T_hex1.delete('1.0', END)
    T_hex2.delete('1.0', END)
    L_title.place_forget()
    L_left.place_forget()
    L_right.place_forget()
    B_online.place_forget()
    B_interpr.place_forget()
    T_hex1.place_forget()
    T_hex2.place_forget()


# shows intro, resets all values, and creates interface for entering numbers
def intro():
    # reseting 
    global rzut
    rzut = 1
    global temp
    temp = ""
    # the interface
    window.title("Księga Przemian - I Ching")
    # reseting interface
    T_hex1.delete('1.0', END)
    T_hex2.delete('1.0', END)
    T_hex1.place_forget()
    T_hex2.place_forget()
    B_less.place_forget()
    B_more.place_forget()
    L_info.place_forget()
    L_right.place_forget()
    B_online.place_forget()
    B_interpr.place_forget()
    B_ichi.place_forget()
    B_online.place_forget()
    B_interpr.place_forget()
    if len(linie) != 6:
        B_last.place_forget()
    else:
        B_last.place(x=73, y=365)
    # configuring and placing elements   
    L_title.configure(text="Księga Przemian - I Ching")
    L_title.place(x=74, y=33) 
    picture.place(x=525, y=25)
    L_left.configure(text="Skup się głęboko na swoim pytaniu...\n\
...w pełnym skupieniu, bez pośpiechu — wciśnij sześciokrotnie „losuj”...\n\
...albo też użyj monet, czy gałązek krwawnika i przyciśnij odpowiedni guzik.")
    L_left.place(x=10, y=145)
    B_info.place(x=7, y=365)
    B_6.place(x=175, y=305)
    B_7.place(x=225, y=305)
    B_8.place(x=275, y=305)
    B_9.place(x=325, y=305)
    B_random.place(x=375, y=305)
    # …and binding keybord strokes
    window.bind('<Return>', lambda e: clicked("rand"))
    window.bind('6', lambda e: clicked("6"))
    window.bind('7', lambda e: clicked("7"))
    window.bind('8', lambda e: clicked("8"))
    window.bind('9', lambda e: clicked("9"))


# child window with interpretations
def interprtWindow():
    win = Toplevel()
    win.geometry('1220x710')
    win.configure(background=bg)
    ourhex = eval('hexagram' + str(maindict[hexa]))
    afterhex = eval('hexagram' + str(maindict[after]))
    # interface elements
    T_hex = Text(win, font=("Terminal", 10), bg=bg, fg="#FCE94F", \
          relief="flat", highlightthickness=0, width='16', height='7', bd='0')
    T_hex.tag_config('red', foreground="#FF0D00")
    T_hex.place(x=1070, y=20)    
    L_title = Label(win, font=("Cookie", 38), fg="#FCE94F", bg=bg, wraplength="1200",
                  justify="left")
    L_title.place(x=50, y=12)
    L_ctitle = Label(win, font=("Cookie", 32), fg="#FCE94F", bg=bg, wraplength="1200",
                  justify="left")
    L_ctitle.place(x=160, y=80)    
    T_int = Text(win, font=("Ubuntu", 14), bg=bg, fg="#80B0FF", \
          relief="flat", highlightthickness=0, wrap="word", width='110', bd='0')    
    T_int.tag_config("bold", font=("Ubuntu", 14, "bold"))
    T_int.place(x=5, y=135)    
    B_close = Button(win, text="Zamknij", bg=bg, activebackground=abg, fg=fg, compound="right", \
                image = ico, command=lambda: win.destroy())
    B_close.place(x=1110, y=675) 
    B_after = Button(win, bg=bg, activebackground=abg, fg=fg, compound="right", \
                image = ico)
    B_dict = Button(win, text="Słowniczek", bg=bg, activebackground=abg, fg=fg, compound="right", \
                image = ico, command=lambda: dictionary())    
    picture = Label(win, image=img, bg=bg)  
    picture.place(x=770, y=30)

    #   ↓
    def beforeChange():
        win.title(hexagrams[maindict[hexa]] + ' ' + names[maindict[hexa]] + '  –  Interpretacja')
        T_hex.delete('1.0', END)
        T_int.delete('1.0', END)
        # showing hexagram BEFORE change
        for x in range(5, -1, -1):
            if linie[x] != hexa[x]:
                T_hex.insert(END, linijki[hexa[x]] + "\n", 'red')
            else:
                T_hex.insert(END, linijki[hexa[x]] + "\n")
        # main iterpretations
        L_title.configure(text=str(maindict[hexa])+'. '+ourhex['title'])
        L_ctitle.configure(text=chnames[maindict[hexa]]+'   '+ourhex['ctitle'])
        T_int.insert(END, 'Obraz:\n')
        T_int.insert(END, ourhex['picture'] + '\n\n', 'bold')
        T_int.insert(END, 'Osąd:\n')
        T_int.insert(END, ourhex['judgment'] + '\n\n', 'bold')
        T_int.insert(END, 'Interpretacja:\n')
        T_int.insert(END, ourhex['interpretation'])
        # the changing lines
        for x in range(0, 6):
            if linie[x] != hexa[x]:
                T_int.insert(END, '\n\n' + str(x + 1) + '. ' + ourhex[str(x + 1) + 'a'], "bold")
                T_int.insert(END, '\n' + ourhex[str(x + 1) + 'b'])
        # special case: 1st or 2nd hexagram with all lines changing
        if linie == '999999' or linie == '666666':
            T_int.insert(END, '\n\n' + ourhex['all1'], 'bold')
            T_int.insert(END, '\n' + ourhex['all2'])
        # the button for other page
        B_after.configure(text="Po przemianie", command=lambda: afterChange())
        # shows only if needed
        if linie != hexa:
            B_after.place(x=970, y=675)
        B_dict.place(x=848, y=675)

    #   ↓
    def afterChange():
        win.title(hexagrams[maindict[after]] + ' ' + names[maindict[after]] + '  –  (po przemianie)')
        T_hex.delete('1.0', END)
        T_int.delete('1.0', END)
        # showing hexagram AFTER change
        for x in range(5, -1, -1):
            T_hex.insert(END, linijki[after[x]] + "\n")
        # iterpretations after change
        L_title.configure(text=str(maindict[after])+'. '+afterhex['title'])
        L_ctitle.configure(text=chnames[maindict[after]]+'   '+afterhex['ctitle'])
        T_int.insert(END, 'Obraz:\n')
        T_int.insert(END, afterhex['picture'] + '\n\n', 'bold')
        T_int.insert(END, 'Osąd:\n')
        T_int.insert(END, afterhex['judgment'] + '\n\n', 'bold')
        T_int.insert(END, 'Interpretacja:\n')
        T_int.insert(END, afterhex['interpretation'])
        # the button for other page 
        B_after.configure(text="Przed przemianą", command=lambda: beforeChange())
        B_after.place(x=954, y=675)
        B_dict.place(x=832, y=675)

    # first showing interpretation
    # before the change
    beforeChange()


# the window with the terms used by I Ching
def dictionary():
    dictwin = Toplevel()
    dictwin.geometry('1220x710')
    dictwin.configure(background=bg)
    dictwin.title(terms['title'])
    T_dict = Text(dictwin, font=("Ubuntu", 14), bg=bg, fg=fg, \
          relief="flat", highlightthickness=0, wrap="word", width='110', height='32', bd='0')
    T_dict.tag_config('key', foreground="#F57900")
    T_dict.place(x=5, y=5)
    for a in terms.keys():
        if a == 'title':
            continue
        T_dict.insert(END, a + '\t\t\t', 'key')
        T_dict.insert(END, terms[a] + '\n\n')
    B_close = Button(dictwin, text="Zamknij", bg=bg, activebackground=abg, fg=fg, compound="right", \
                image = ico, command=lambda: dictwin.destroy())
    B_close.place(x=1110, y=675) 

    
# how to deal with the online buttons
def callback(url):
    webbrowser.open(url)


# show result im main window
def showit():
    global linie
    global hexa
    global after
    #first calculate other hexagrams if not calculated
    if len(hexa) != 6 and len(after) != 6:
        for x in range(0, 6):
            if linie[x] == '6':
                hexa += '8'
                after += '7'
            elif linie[x] ==  '7':
                hexa += '7'
                after += '7'
            elif linie[x] == '8':
                hexa += '8'
                after += '8'
            elif linie[x] == '9':
                hexa += '7'
                after += '8'

    B_info.place(x=7, y=365)
    window.unbind('<Return>')
    window.unbind('6')
    window.unbind('7')
    window.unbind('8')
    window.unbind('9')
    B_less.place_forget()
    B_more.place_forget()
    B_last.place_forget()
    B_6.place_forget()
    B_7.place_forget()
    B_8.place_forget()
    B_9.place_forget()
    B_random.place_forget()
    hexagram = maindict[hexa]
    hexafter = maindict[after]
    window.title(hexagrams[hexagram] + ' ' + names[hexagram])
    L_info.place_forget()
    L_title.configure(text="Księga Przemian - I Ching", font=("Cookie", 34), fg="#FF0D00")
    L_title.place(x=125, y=5)
    L_left.configure(text="Odpowiedź „Księgi Przemian” to: " + hexagrams[hexagram] + " " \
                     + chnames[hexagram] + "\n" + str(hexagram) + ". „" + names[hexagram], \
                     font=("Cookie", 18), fg="#80B0FF", justify="left")
    L_left.place(x=10, y=80)               
    L_right.configure(text=hexagrams[hexafter] + " " + chnames[hexafter] + \
                      " Heksagram po przemianie:" + "\n" + str(hexafter) + ". „" + names[hexafter])
    L_right.place(x=350, y=80)
    picture.place(x=525, y=0)

    # showing the hexagrams
    T_hex1.delete('1.0', END)
    T_hex1.place(x=70, y=147)
    T_hex1.configure(width="28")
    for x in range(5, -1, -1):
        if linie[x] != hexa[x]:
            if x > 0:
                T_hex1.insert(END, linijki[linie[x]], "red")
                T_hex1.insert(END, "   " + str(cyfry[x + 1]) + " linia zmienna\n", "chng")
            else:
                T_hex1.insert(END, linijki[linie[x]], "red")
                T_hex1.insert(END, "   " + str(cyfry[x + 1]) + " linia zmienna", "chng")
        else:
            if x > 0:
                T_hex1.insert(END, linijki[linie[x]] + "\n", "norm")
            else:
                T_hex1.insert(END, linijki[linie[x]], "norm")    
    T_hex2.place(x=400, y=147)
    for x in range(5, -1, -1):
        if x > 0:
            T_hex2.insert(END, linijki[after[x]] + "\n")
        else:
            T_hex2.insert(END, linijki[after[x]])

    B_ichi.place(x=160, y=365)
    B_interpr.place(x=405, y=365)
    B_online.place(x=298, y=365)
    window.bind('<Return>', lambda e: interprtWindow())


# let's deal with the user input :)
def clicked(linia):
    B_less.place_forget()
    B_more.place_forget()
    global linie
    global rzut
    global hexa
    global after
    global temp
    if rzut < 7:
        if linia == "rand":
            # jeśli użytkownik nie podał liczby - w linii poniżej 3 wirtualne monety :)
            linia = str(random.randint(2,3) + random.randint(2,3) + random.randint(2,3))
        elif linia == "10":
            linia = ''
        temp += linia
        L_left.configure(text=(int(linia), "na", cyfry2[rzut], "linii."), font=("Cookie", 30))
        L_left.place(x=195, y=170)
        rzut += 1
        T_hex1.place(x=15, y=140)
        T_hex1.configure(height="7", width="16")
        # building the hexagram
        if linia in ('6', '9'):
            T_hex1.insert('1.0', linijki[linia] + "\n", "red")
        else:
            T_hex1.insert('1.0', linijki[linia] + "\n", "norm")
    if rzut == 7:
        # we have new toss, so we reset the old one now
        hexa = ''
        after = ''
        linie = temp
        # and show it
        showit()


### configuring main window
window = Tk()
window.title("Księga Przemian - I Ching")
window.geometry('630x400')
window.configure(background=bg)

# ...and it’s elements
# pictures
img = PhotoImage(data=picture)
picture = Label(window, image=img, bg=bg)
ico = PhotoImage(data=icon)
window.iconphoto(False, ico)
extco = PhotoImage(data=exiticon)
backgr = PhotoImage(data=backgrpic)
onlico = PhotoImage(data=onlineicon)

#label widgets
L_title = Label(window, font=("Cookie", 40), bg=bg, fg="#FF0D00")
L_left = Label(window, font=("Cookie", 20), fg="#80B0FF", bg=bg, justify="center")
L_right = Label(window)
L_right = Label(window, text="", font=("Cookie", 18), fg="#80B0FF", bg=bg, justify="right")
L_info = Label(window, font=("Ubuntu", 14), fg="#FCE94F", bg=bg, wraplength="590",
               justify="left", image=backgr, compound="center")

#text widgets
T_hex1 = Text(window, font=("Monospace", 14), bg=bg, fg="#FCE94F", height="7", width="28", \
          relief="flat", highlightthickness=0)
T_hex1.tag_config("red", foreground="#FF0D00")
T_hex1.tag_config("chng", font=("Cookie", 14), foreground="#FF0D00", offset="-2", spacing3="-2")
T_hex1.tag_config("norm", spacing3="3")
T_hex2 = Text(window, font=("Monospace", 14), bg=bg, fg="#FCE94F", spacing3="3", height="6", \
          width="16", relief="flat", highlightthickness=0)

#keyboard bindings
window.bind('<F5>', lambda e: intro())
window.bind('<F1>', lambda e: info1())
window.bind('<Escape>', lambda e: window.destroy())

#buttons
B_interpr = Button(window, text='Interpretacja', bg=bg, activebackground=abg, fg="#ffffee", compound="right", \
                   image = ico, command=lambda: interprtWindow())
B_6 = Button(window, text="6", bg=bg, activebackground=abg, fg=fg, command=lambda: clicked("6"))
B_7 = Button(window, text="7", bg=bg, activebackground=abg, fg=fg, command=lambda: clicked("7"))
B_8 = Button(window, text="8", bg=bg, activebackground=abg, fg=fg, command=lambda: clicked("8"))
B_9 = Button(window, text="9", bg=bg, activebackground=abg, fg=fg, command=lambda: clicked("9"))
B_random = Button(window, text="losuj!", bg=bg, activebackground=abg, fg=fg, command=lambda: clicked("rand"))
B_ichi = Button(window, text="Nowe pytanie", bg=bg, activebackground=abg, fg=fg, compound="right", \
                image = ico, command=lambda: intro())
B_exit = Button(window, text="Wyjdź", bg=bg, activebackground=abg, fg=fg, compound="right", \
                image = extco, command=lambda: window.destroy())
B_exit.place(x=538, y=365)
B_info = Button(window, text="O", bg=bg, activebackground=abg, fg=fg, compound="right", \
                image = ico, command=lambda: info1())
B_more = Button(window, text="Dalej", bg=bg, activebackground=abg, fg=fg, compound="right", \
                image = ico)
B_less = Button(window, text="Wróć", bg=bg, activebackground=abg, fg=fg, compound="left", \
                image = ico)
B_last = Button(window, text="Ostatni wynik", bg=bg, activebackground=abg, fg=fg, compound="left", \
                image = ico, command=lambda: showit())

#online buttons:
B_online = Button(window, text='iching.pl', bg=bg, activebackground=abg, fg=fg, compound="right", \
                  image = onlico, command=lambda: callback("http://www.iching.pl/iching.php?x=" + linie))
B_qaz = Button(window, text='pl.qaz.wiki', bg=bg, activebackground=abg, fg=fg, compound="right", image = onlico, command=lambda: callback("https://pl.qaz.wiki/wiki/I_Ching_divination"))
B_wiki = Button(window, text='wikipedia', bg=bg, activebackground=abg, fg=fg, compound="right", image = onlico, command=lambda: callback("https://pl.wikipedia.org/wiki/Yijing"))
B_taraka = Button(window, text='taraka.pl', bg=bg, activebackground=abg, fg=fg, compound="right", image = onlico, command=lambda: callback("http://www.taraka.pl/icing_mawangdui_00"))
B_ichingpl = Button(window, text='iching.pl', bg=bg, activebackground=abg, fg=fg, compound="right", image = onlico, command=lambda: callback("http://www.iching.pl"))


# first checking for arguments...
# we allow only 1 argument
if len(sys.argv) > 2:
    print('Za dużo argumentów na raz. Żegnam.')
    sys.exit()

# one argument? hmm. let's check what is it...
if len(sys.argv) == 2:
    #help?
    arg = sys.argv[1]
    if arg in ('-h', '--help', '-?', '/h', '/help', 'help', '/?', 'about',
               '-about', '--about', '/about', 'o', '-o', '--o', '/o'):
        info1()
    #version?
    elif arg in ('--version', '-version', 'version', '--wersja', '-wersja', 'wersja'):
        print(current_version)
        sys.exit()
    elif arg in maindict.keys():
        rzut = 7
        linie = str(arg)
        hexa = str(arg)
        after = str(arg)
        clicked('10')
    else:
        #numbers?
        try:
            int(arg)
        except:
            print("Nie zrozumiałem o co ci chodzi")
            sys.exit()
        else:
            #hexsagram number?
            if 0 < int(arg) < 65:
                tmp = list(maindict.keys())[list(maindict.values()).index(int(arg))]
                if maindict[tmp] == int(arg):
                    linie = tmp
                    showit()
                else:
                    print("jakiś błąd")
                    sys.exit()
            #toss result (six numbers of 6-9)?
            elif len(arg) == 6 and not any((c in ('0', '1', '2', '3', '4', '5') for c in arg)):
                linie = arg
                showit()
            else:
                print("Nie zrozumiałem o co ci chodzi")
                sys.exit()  


# no extra argument?
if len(sys.argv) == 1:
    # so let's go! :)
    intro()

window.mainloop()
