# dev_ops_lato_2025
## ZADANIE 7 GIT actions - unit testy, automatyzacja 

Cel laboratoriów. 
Celem laboratoriów jest zapoznanie się z narzędziem git actions i zbudowanie własnego flow https://codefresh.io/learn/github-actions/github-actions-workflows-basics-examples-and-a-quick-tutorial/



### 1 Zaktualizować repo w kilku krokach 
- 1.1 Zaktualizować wszystkie metadane projektu 
```bash
git fetch --all
```

- 1.2 Przełączyć się na branch main 
```bash
git checkout main
```

- 1.3 Pobrać zmiany w kodzie 
```bash
git pull 
```

## UWAGA DALSZE KROKI PROSZĘ ROBIĆ NA SWOIM REPO


### 2 Stworzyć własne repo w oparciu o env_00000
- 2.1 Skopiować zawartość do nowego folderu o nazwie env_nrIndeksu
- 2.2 Na własnym repo dodać branch roboczy 


### 3 Przerobić skrypt yml 
- W folderze .github/workflows zedytować skrypt yml (ten z folderu z labem) tak aby test uruchamiał się tylko na NASZYM  ROBOCZYM branchu i żadnym  innym. 

- Zrobić commita i wysłać do swojego brancha UPEWNIĆ SIĘ PRZED WYSŁANIEM, ŻE PRACUJEMY NA ROBOCZYM BRANCHU
- Zobaczyć czy test wykonał się pozytywnie 

### 4 Przerobić kod na swój 

-  w pythonie dodać kilka nowych funkcji, które korzystają z innej biblioteki np. pandas. Aktualne testy i testy do nowych funkcji tak stworzyć by można było uruchomić je oddzielnie -> jedna komenda jeden test 

- Za pomocą dokumentacji i stron pomocniczych wykonać następujący workflow :
    - Stworzyć równolegle 4 joby, które testują każdą z funkcji z osobna 
    - Stworzyć job new_test, gdzie będą uruchomione nowo dodane testy po tym jak zakończą się 4 poprzednie (słowo klucz needs)
  


### 7 Sprawozdanie 

- 7.1 Sprawozdanie ma być dokumentacją pracy tj opisem wykonanych kroków wraz z zdjęciami i opisem wykorzystywanych metod. Ma ona pozwolić na odtworzenie zadania z wykorzystaniem instrukcji ze sprawozdania 
- 7.2 Ma być ono zapisane za pomocą markdowna w nowo stworzonym  folderze. 
- 7.3 Sprawozdanie jak i plik yml i folder z kodem dodać na branchu grupowym i otworzyć PR 


### Zaliczenie laboratoriów 
- Sprawozdanie w docelowej lokalizacji 
- Gotowe do oddania praca i sprawozdanie w postaci commita na branchu z zadaniem  
- Wszelkie edycje skryptów testowych i automatyzujących workflow jest zabronione (czyli plików nie wymienionych w instrukcji)
- Pushe mają być wykonywane WYŁĄCZNIE Z NASZYCH KONT GITHUB 


### Tematy dodatkowe 
- Po co są używane stage 
- Jak można zmniejszyć liczbę własnoręcznie pisanych kroków w jobie (opisać przykładową procedurę z marketu np do tworzenia środowiska pod dockera)
- Co to są artefakty w pipelinie i do czego służą
- Jakie są inne narzędzia do wykonywania pipelinów testowych (podać co najmniej 3 z czego min 1 ma być open source)
- Do czego w pipelinie może służyć sonar qube


