# Phonebook Django webapp
## About

Following features have been implemented at the moment:

- Create(add) contact
- Search by name
- Search by phone
- A contact could have many phones attached to it
- Delete contacts
- Contacts are stored in sqlite DB via Django ORM

## Plan to follow
====================

[Install and initialize empty project Video How To(RUS)](https://youtu.be/LuqGny28YEw)
1. Create git rep
1. Create venv
1. Start project

===================

[Create app and models Video How To(RUS)](https://youtu.be/c9unEJWRuMA)
1. Create app `phonebook`
1. Create `Models`

=====================

[HomePageVIew and Template Video How To(RUS)](https://youtu.be/qHHsyj754D0)
1. Create `HomePageVIew`
1. Create `home.html` template
1. Add path to `HomePageVIew`
1. Add bootstrap (CDN)

=======================

1. Add navbar (add navbar-expand-lg class)
1. Add `home` navbar item
1. Add `Add` and `All` navbar items
1. Add `CreatePersoneForm` and `AddPhoneFormView`. Add path to `AddPhoneFormView`
1. Add `django-crispy-forms`
1. Add Html form, submit button
1. Redefine `get_success_url` of `AddPhoneFormView` for adding phones
1. Redefine `get_context_data` of `HomePageView` for filtering
1. add card for rearch result in `home.html` template. Add `search_message` and all results
1. add `all_phones_to_string` to `Persone` Model. Add result table to `home.html`
1. add `DeletePhoneView` and functional

1. add search forms to `home.html`

## Install 

1. clone project and cd to project dir
1. create venv and activate it
    ```zsh
    #linux/mac
    python3 -m venv env
    source ./env/bin/activate
    ```
    ```bash
    #win cmd
    python -m venv env
    .\env\Scripts\activate
    ```
1. Install dependensies:
    ```zsh
    pip install -r requirements.txt
    ```

## Run it

1. cd to `src` directory
1. run
    ```zsh
    #linux/mac
    python3 manage.py runserver
    ```
    ```bash
    #win cmd
    python manage.py runserver
    ```

## Video explanation[RUS]

coming soon..
[How to... (RUS)](https://www.youtube.com/watch?v=PxT8c7qP-o0&list=PLIMYb25g876h9hdwBa6asZfABu4vbLGNM)
## Previous step
- [Crossplatform Kivy Phonebook app](https://youtu.be/PxT8c7qP-o0)
## Next steps

- Create the same app as web-app usind Django + Django REST Framework + VUE
