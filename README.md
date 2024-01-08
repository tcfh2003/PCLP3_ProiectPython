# PCLP3_ProiectPython

Main project is in the Proiect_MicroPython folder on the MicroPython_DemoVersion branch.
Documentation and use instructions are in that folder in PCLP3-Proiect_Beliciu_Andrei_Fratu_Halunga_Theodor.docx





### Basic Operating Instructions without images (in romanian)

1.	Se descarcă și instalează Python3
2.	Se descarcă și se rulează uPyCraft (în repozitorul de pe GitHub /Proiect_MicroPython/uPyCraft_V1.1.exe)
3.	Se descarcă fișierul Firmware binar pentru ESP32 (în repozitorul GitHub /Proiect_MicroPython/ESP32_GENERIC-IDF3-20210202-v1.14.bin)
4.	Se conectează ESP32 la calculator și se determină portul COM la care este conectat (în Windows, în Device Manager > Ports(COM & LPT))
5.	În uPyCraft, se selectează portul găsit în meniul de sus, Tools > Serial > COM…
6.	Se selectează placa ESP32 în meniul Tools > board > esp32
7.	Se instalează bootloader-ul de MicroPython pe ESP32 folosind meniul Tools > BurnFirmware, și selectând în fereastra nou apărută placa esp32, adresa de scriere (0x1000), ștergerea memoriei flash setată ”yes”, portul COM al plăcii folosit anterior, iar în secțiunea Firmware Choose se folosește opțiunea Users și se caută fișierul Firmware binar descărcat anterior
8.	Se realizează pe o placă de test montajul de mai jos. Modulul de buzzer pasiv MH-FMD se alimentează la 5V și la masă, iar portul de I/O se conectează la portul 25 al ESP32. Portul 35 al ESP32 se conectează printr-un rezistor de pull-down la masă și la buton, care se mai leagă la portul de 3,3V al ESP32.
9.	Se inițializează conexiunea cu ESP32 apăsând pe butonul Connect din meniul din dreapta în uPyCraft
10.	Se deschide în uPyCraft fișierul din repozitor /Proiect_MicroPython/Python_Scripts/sample_period.py, apoi se apasă butonul din meniul din dreapta în uPyCraft DownloadAndRun
11.	Se determină cu ajutorul unui osciloscop perioada de eșantionare. În cazul nostru, perioada de eșantionare a fost de 44us
12.	Se rulează programul din repozitor /Proiect_MicroPython/Python_Scripts/ signal_list_generator/main.py și se copiază listele afișate în variabilele din /Proiect_MicroPython/Python_Scripts/multiple_signals.py. Conțiuntul acestui se deschide în uPyCraft, se salvează și se apasă butonul DownloadAndRun