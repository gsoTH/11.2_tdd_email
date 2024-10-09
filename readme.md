# Email Validierung 
 Einer Ihrer Kollegen hat eine Python-Funktion `is_valid_email(email:str)` zur Überprüfung von Email-Adressen am GSO geplant. In einem ersten Schritt sollen die Klassenverteiler getestet werden. Jede Emailadresse beginnt mit dem Usernamen (z.B.: "FI123") und endet mit der Domain. Für den Usernamen existieren folgende Anforderungen:
 - Kürzel besteht aus bestimmten Kombinationen mit zwei oder drei Buchstaben (z.B. "FI" für Fachinformatiker)
 - Wenn das Kützel aus zwei Buchstaben besteht, müssen drei Ziffern folgen
 - wenn das Kürzel aus drei Buchstaben besteht, müssen zwei Ziffern folgen
 - Die erste Ziffer ist die letzte Stelle des Jahres der Einschulung (FI**1**23) wurde z.B. im Jahr 202**1** eingeschult)
 - Die letzte Ziffer bzw. die letzten zwei Ziffern sind die Nummer der Klasse. Diese beginnt mit 1 bzw. 01


 Positiv- und Negativbeispiele sind in Unittests definiert: [test_input_validation.py](./test_input_validation.py).


## Ziele :dart:
**Primär:**
- Clean Code, TDD: Die Begriffe [Clean-Code](https://www.ionos.de/digitalguide/websites/web-entwicklung/was-ist-clean-code/) bzw. Code-Smell und Refactoring sind verinnerlicht. Für Clean-Code können mindestens DRY, KISS und YAGNI erläutert werden. Der Zusammenhang zwischen Unit-Tests und Refactoring kann erläutert werden.
- [Parametrisierten Tests](https://docs.pytest.org/en/7.3.x/how-to/parametrize.html#pytest-mark-parametrize) können eingesetzt werden.

**Sekundär:**
- Die Funktion soll alle Testfälle korrekt verarbeiten.
- Es sollen eine weitere Funktion `is_valid_password` (inkl. Testfällen entstehen), die überprüft, ob ein übergebenes Passwort den [Anforderungen des BSI](https://www.bsi.bund.de/DE/Themen/Verbraucherinnen-und-Verbraucher/Informationen-und-Empfehlungen/Cyber-Sicherheitsempfehlungen/Accountschutz/Sichere-Passwoerter-erstellen/sichere-passwoerter-erstellen_node.html) entspricht.

## Aufgabenstellung
1. Informieren Sie sich über Clean Code und TDD. Fügen Sie Ihre Notizen in beliebiger Dateiform (.md ist natürlich am coolsten) in dieses Repository ein.
2. Implementieren Sie nach Test-Driven-Developement so lange, bis alle Testfälle grün sind. Betreiben Sie regelmäßig Refactoring! Überarbeiten Sie Ihren Code vor jedem Commit so, dass die Funktionalität erhalten bleibt, aber der Code ~~besser~~ ~~lesbarer~~ frei von Code-Smells ist. Meine Empfehlung: nach jedem erfolgreich implementierten Testfall einen Commit anlegen.

## Nützliche Links
- [Parametrisierte Tests mit Pytest](https://docs.pytest.org/en/7.3.x/how-to/parametrize.html#pytest-mark-parametrize)
- [Docstrings in Python](https://www.programiz.com/python-programming/docstrings)
- [Artikel zu Clean-Code](https://www.ionos.de/digitalguide/websites/web-entwicklung/was-ist-clean-code/), zuletzt abgerufen im September 2023
- [Katalog Code-Smells](https://luzkan.github.io/smells/)
- [Katalog Refactoring](https://refactoring.com/catalog/)

### weniger nützliche Links
- Sollten Sie sich in  für Emails interessieren, empfehle ich dieses [Video zum Thema ](https://www.youtube.com/watch?v=mrGfahzt-4Q), das Sie sich gerne in Ihrer Freizeit ansehen dürfen.
- Ebenfalls für die Freizieit: [Password Game](https://neal.fun/password-game/)
- ["Mutter aller Email-Regex"](https://www.ex-parrot.com/pdw/Mail-RFC822-Address.html)

