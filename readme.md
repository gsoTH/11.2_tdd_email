# Email Validierung 
 Einer Ihrer Kollegen hat eine Python-Funktion `is_valid_email(email:str)` zur Überprüfung von Email-Adressen geschrieben. Die Funktion nutzt Regular Expressions (kurz RegEx), um Muster in String zu finden. RegEx sind ein mächtiges Werkzeug, können aber nur schwer gewartet werden sie werden schnell zu [code-smells "stinkendem Code"](https://luzkan.github.io/smells/complicated-regex-expression).

 Immerhin hat Ihr Kollege daran gedacht, einige Testfälle zu definieren, um die Fähigkeiten seiner Funktion zu überprüfen.


## Ziele :dart:
Primär:
- Die Funktion soll "möglichst viele" [gültige und ungültige Email-Adressen](https://www.tumblr.com/codefool/15288874550/list-of-valid-and-invalid-email-addresses) korrekt erkennen.

Sekundär:
- Es soll eine weitere Funktion `describe_email_error` entstehen, die Informationen zum Fehler in einer E-Mail-Adresse ausgibt.

## Aufgabenstellung
**Wiederholen** Sie die folgenden Arbeitsschritte so lange, bis die Ziele möglichst erreicht sind.
 1. Betreiben Sie Refactoring! Überarbeiten Sie die Funktion `is_valid_email(email:str)` so, dass die Funktionalität erhalten bleibt, aber der Code ~~besser~~ lesbarer wird.
 2. Erweitern Sie die Testfälle in `test_email_validation.py` um eine gültige oder ungültige E-Mail-Adresse.
 3. Erweitern Sie die Funktion `is_valid_email(email:str)` so, dass der neue Testfall erfolgreich ist.

## Nützliche Links
- [Beispiele für gültige und ungültige Email-Adressen](https://www.tumblr.com/codefool/1528.8874550/list-of-valid-and-invalid-email-addresses)
- [Parametrisierte Tests mit Pytest](https://docs.pytest.org/en/7.3.x/how-to/parametrize.html#pytest-mark-parametrize)
- [Docstrings in Python](https://www.programiz.com/python-programming/docstrings)
- Sollten Sie sich in Ihrer Freizeit für Emails interessieren, empfehle ich dieses [Video zum Thema ](https://www.youtube.com/watch?v=mrGfahzt-4Q)

