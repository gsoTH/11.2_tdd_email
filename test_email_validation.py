import pytest
from email_validation import is_valid_email

@pytest.mark.parametrize("email", [
    ("test@email.com")
,   ("t.est@email.com")
,   ("test@em.ail.com")
])
def test_is_valid_email__gueltige_Adressen(email):
    assert is_valid_email(email) == True


@pytest.mark.parametrize("email", [
    ("testemail.com")   # Fehlendes @-Zeichen
,   ("test@email")      # Fehlende Top-Level-Domain
])
def test_is_valid_email__ungueltige_Adressen(email):
    assert is_valid_email(email) == False


## Zukunftsmusik
# @pytest.mark.parametrize("email, expected_output", [
#     ("testemail.com","Fehlendes @-Zeichen")
# ])
# def test_describe_email_error__Fehler_wird_ausgegeben(email, expected_output):
#     assert describe_email_error(email) == expected_output