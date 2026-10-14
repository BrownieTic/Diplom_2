class Url:
    MAIN_PAGE_URL = 'https://stellarburgers.education-services.ru/'

class API:
    creating_user_api = f'{Url.MAIN_PAGE_URL}api/auth/register'
    delete_iser_api = f'{Url.MAIN_PAGE_URL}api/auth/user'