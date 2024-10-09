import pytest   #benötigt für Parametrisierung
from input_validation import is_valid_email

@pytest.mark.parametrize("email", [
    ("IAF01@gso.schule.koeln")
,   ("IAF99@gso.schule.koeln")
,   ("IAH01@gso.schule.koeln")
,   ("IAH99@gso.schule.koeln")
,   ("FI001@gso.schule.koeln")
,   ("FI999@gso.schule.koeln")
,   ("BFG01@gso.schule.koeln")
,   ("BFG99@gso.schule.koeln")
,   ("BFT01@gso.schule.koeln")
,   ("BFT99@gso.schule.koeln")
])
def test_is_valid_email__gueltige_Adressen(email):
    # arrange
    email_adress_to_be_tested = email
    
    # act
    response = is_valid_email(email_adress_to_be_tested)
    
    # assert
    assert response is True


@pytest.mark.parametrize("email", [
    ("IAF01gso.schule.koeln")   # Fehlendes @-Zeichen
,   ("IAF01@gso.schule")        # Falsche Top-Level-Domain
,   ("IAF01@schule.koeln@schule.koeln")  # Mehrfache Domain
,   ("BFT999@gso.schule.koeln") # Zu lange Klassennummer
,   ("FI99@gso.schule.koeln")   # FI-Klassen benötigen eine Dreistellige Ziffer
,   ("FI100@gso.schule.koeln")  # Klassennummer muss mindestens mit 1 beginnen
,   ("IAH00@gso.schule.koeln")  # Klassennummer muss mindestens mit 1 beginnen
,   ("IAF10@gso.schule.koeln")  # Klassennummer muss mindestens mit 1 beginnen
,   ("BFG90@gso.schule.koeln")  # Klassennummer muss mindestens mit 1 beginnen
,   ("ABC11@gso.schule.koeln")  # Kürzel ist sinnlos
])
def test_is_valid_email__ungueltige_Adressen(email):
    # arrange
    email_adress_to_be_tested = email
    
    # act
    response = is_valid_email(email_adress_to_be_tested)
    
    # assert
    assert response is False