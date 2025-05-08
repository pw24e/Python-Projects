# Digital Passport

A Python library that implements a fully-featured “digital passport” class according to the UN’s new specification. Passports are Python objects with the same fields and behaviors as a real-world passport, plus digital conveniences like JSON export/load and visit-tracking.

## Features

- **`Passport` class**  
  - Public instance variables: `first_name`, `last_name`, `dob` (as `datetime.date`), `country`, `exp_date` (as `datetime.date`)  
  - Auto-incrementing `passport_number` (starting at 0)  
  - Methods to:
    - Check validity (`is_valid`)
    - Verify identity data (`check_data`)
    - Generate human-readable summary (`summary`)
    - Stamp entries to countries (`stamp`)
    - List visited countries (`countries_visited`)
    - Count visits per country (`times_visited`, raises `CountryNotVisitedError` if none)
    - Compute “sum of squared visits” score (`sum_square_visits`)
    - Export to JSON file (`export`) & load back (`load`)

- **`BritishPassport` subclass**  
  - Defaults `country` to  
    "The United Kingdom of Great Britain and Northern Ireland"  
  - Otherwise identical interface to `Passport`

- **Error handling**  
  - `CountryNotVisitedError` for unvisited-country lookups

- **Code quality**  
  - Follows PEP-8 (checked by flake8)  
  - Docstrings compliant with PEP-257  
  - Long lines allowed up to 200 characters  


## Disclaimer

This project was developed as a homework assignment for a University of Liverpool class. Do not redistribute or represent as original work.

© 2024 Prathusha Y Wijesinghe
