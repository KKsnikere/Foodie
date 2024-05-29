# Web aplikācijas Foodie apraksts un instrukcija

## Projekta mērķis

Šī web aplikācija ir izstrādāta, lai palīdzētu lietotājiem sekot līdzi savam kaloriju patēriņam. Lietotāji varēs ievadīt un pārvaldīt ēdienus, ko viņi patērē, un saņemt informāciju par to uzturvērtību. Aplikācija piedāvā lietotājam draudzīgu interfeisu un uzticamu datu bāzes pārvaldību.

## Tehnoloģijas

Projekta izstrādē tiek izmantotas sekojošas tehnoloģijas:

### 1. Python

Python ir augsta līmeņa, interpretēta programmēšanas valoda, kas ir zināma ar savu vienkāršību un lasāmību. Python piedāvā plašu bibliotēku un ietvaru klāstu, kas palīdz ātri un efektīvi izstrādāt web aplikācijas.

### 2. Django

Django ir Python web ietvars, kas veicina ātru izstrādi un tīru, pragmatisku dizainu. Django nodrošina daudzas funkcijas, piemēram, autentifikāciju, datu pārvaldību, veidņu dzinēju, un citas, kas ievērojami samazina izstrādes laiku.

#### Galvenās Django iespējas:

- **ORM (Object-Relational Mapping)**: Ļauj izstrādātājiem mijiedarboties ar datu bāzēm, izmantojot Python kodu, nevis SQL.
- **Admin Interface**: Automātiski ģenerēts administrēšanas interfeiss, kas ļauj viegli pārvaldīt aplikācijas datus.
- **Security**: Iebūvēti aizsardzības mehānismi pret biežākajiem web uzbrukumiem, piemēram, CSRF un XSS.

### 3. PostgreSQL

PostgreSQL ir spēcīga, atvērtā koda relāciju datu bāzes sistēma, kas pazīstama ar savu uzticamību un izpildījumu. Tā nodrošina plašu datu tipu un funkcionalitātes atbalstu, kas ir noderīgi sarežģītu lietojumprogrammu izstrādē.

#### Galvenās PostgreSQL iespējas:

- **ACID Atbalsts**: Nodrošina transakciju uzticamību un datu integritāti.
- **Paplašināmība**: Atbalsta pielāgotas funkcijas, datu tipus, operatorus un indeksus.
- **SQL Standartu Atbilstība**: Atbalsta plašu SQL standartu kopumu, kas padara datu pārvaldību efektīvu un elastīgu.

## Projekta struktūra

Aplikācija sastāv no vairākām galvenajām komponentēm:

- **Lietotāja interfeiss**: Izveidots, izmantojot Django veidnes, HTML un CSS, lai nodrošinātu lietotājiem draudzīgu un intuitīvu pieredzi.
- **Datubāze**: PostgreSQL tiek izmantota, lai glabātu lietotāju datus, ēdienu informāciju un kaloriju ierakstus.
- **Backend**: Django nodrošina datu apstrādi, validāciju, autentifikāciju un citus backend pakalpojumus.

## Secinājums

Šī kaloriju saskaitīšanas web aplikācija ir izstrādāta, izmantojot mūsdienīgas un uzticamas tehnoloģijas, kas nodrošina stabilitāti, drošību un lietotājam draudzīgu pieredzi. Python, Django un PostgreSQL kombinācija ļauj veidot spēcīgu un efektīvu aplikāciju, kas spēj apmierināt lietotāju vajadzības.

#  Instrukcija

## 1. Python Instalēšana

1. Lejupielādējiet un instalējiet Python no [python.org](https://www.python.org/downloads/).
2. Instalācijas laikā atzīmējiet "Add Python to PATH" un nospiediet "Install Now".
3. Pārbaudiet instalāciju:

   python --version

## 2. Virtuālās vides izveidošana

1. Atveriet komandrindu.
2. Navigējiet uz direktoriju, kur vēlaties izveidot projektu.
3. Izveidojiet virtuālo vidi:

  python -m venv myenv
  myenv\Scripts\activate

## 3. Django instalēšana
   pip install django
   django-admin startproject myproject
   cd myproject

## 4. Servera palaišana

  python manage.py runserver
  Atveriet http://127.0.0.1:8000/ savā pārlūkprogrammā.

Šīs instrukcijas palīdzēs jums ātri un vienkārši palaist Django projektu.





<img src="https://github.com/KKsnikere/healthAppFoodie/blob/main/Screenshot2.png" />
<img src="https://github.com/KKsnikere/healthAppFoodie/blob/main/Screenshot1.png" />

