<img src="https://cdn-icons-png.freepik.com/512/743/743007.png" width="100" />

Shopping with Pytest
======
Shopping automation

Project Dependencies
---------------------

- *`pytest`*
- *`pyyaml`*
- *`selenium==4.13.00`*
- *`Faker`*
  
Coverage
---------

  - Sign up
  - Women Category Shopping
  - Men Category Shopping
  - Kids Category Shopping
  - Checkout
  - Payment

Pre-requisites
--------------

1. Python 3 (Make sure python is added to your system PATH)
2. Python Extension (VSCode)
3. pip
4. virtualenv
------------------------------------------------
Setting up first run on your local machine
------------------------------------------

1. Clone this project on your local machine

   ```
   https://github.com/markuusche/shopping-pytest
   ```

3. Open a terminal inside your local clone of the repository.

4. Using python's virtualenv, create a virtual environment inside the project. <br>
   Install:
   ```
   pip install virtualenv
   ```
   Create a virtual environment:
   ```
   virtualenv venv
   ```

   where venv is the name of the virtual environment you are creating.
   It is also recommended to use __venv__ as the name of your virtual environment
   cause this is the recognized file exception on our ``.gitignore``

6. Activate the virtualenv you just created.
   
   * Windows CMD
      ```bash
      venv\Scripts\activate
      ```
   * Windows Git Bash
      ```bash
      source venv/scripts/activate
      ```
   * Windows Powershell
      ```bash
      venv\Scripts\activate.ps1
      ```
   * MacOS/Linux
      ```bash
     source venv/bin/activate
      ```

7. Install the project dependencies.
    ```bash
     pip install -r requirements.txt
    ```

Thats it! You have setup your local environment to run test for this project.


Run the script:

```
pytest -v -rA
```

</br>

