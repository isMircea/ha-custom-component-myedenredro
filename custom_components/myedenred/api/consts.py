DEFAULT_COUNTRY = "RO"

COUNTRIES = [
    { "value": DEFAULT_COUNTRY, "label": "Romania" }
]

API_LOGIN_URL = {
    "RO": "https://sso.eu.edenred.io/web/session/step/password?returnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fresponse_type%3Dcode%26client_id%3D1ea2d5a62e8347adb53f83fc7f3227db%26scope%3Dopenid%2520edg-xp-appcontainer-sa-api%26redirect_uri%3Dhttps%253A%252F%252Fuser.myedenred.ro%252Flogin%26acr_values%3Dtenant%253Aro-ben%26ui_locales%3Dro%26code_challenge%3D3doz2VXczEMNL3E5y0Lv9p-RS-vIK8C0lgU8C0moSjE%26code_challenge_method%3DS256"
}

API_LIST_URL = {
    "RO": "https://myedenred.ro/edenred-customer/api/protected/card/list"
}

API_ACCOUNTMOVEMENT_URL = {
    "RO": "https://myedenred.ro/edenred-customer/api/protected/card/{}/accountmovement"
}
