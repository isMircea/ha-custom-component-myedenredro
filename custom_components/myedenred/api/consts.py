DEFAULT_COUNTRY = "RO"

COUNTRIES = [
    { "value": DEFAULT_COUNTRY, "label": "Romania" }
]

API_LOGIN_URL = {
    "RO": "https://myedenred.ro/edenred-customer/api/authenticate/default"
}

API_LIST_URL = {
    "RO": "https://myedenred.ro/edenred-customer/api/protected/card/list"
}

API_ACCOUNTMOVEMENT_URL = {
    "RO": "https://myedenred.ro/edenred-customer/api/protected/card/{}/accountmovement"
}
