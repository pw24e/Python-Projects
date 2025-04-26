from datetime import date
from datetime import datetime

class Passport:

    """Class to represent a passport."""

    passport_count = 0  #defining the class variable

    def __init__(self, first_name, last_name, dob, country, exp_date):
        """initialize passport details """
        self.first_name = first_name
        self.last_name = last_name
        self.dob = datetime.strptime(dob, "%Y-%m-%d").date()
        self.country = country
        self.exp_date = datetime.strptime(exp_date, "%Y-%m-%d").date()
        self.stamps ={}  #to track countries visited and their countries
        self.passport_id = Passport.passport_count
        Passport.passport_count += 1
    def summary(self):
        """Provide a summary of passport details and validity."""
        validity = "It is valid" if self.is_valid() else "It is invalid"
        return (f"This passport belongs to {self.first_name} {self.last_name}, born on {self.dob} "
            f"in {self.country}. {validity}")
    def is_valid(self):
        """Check if passport is valid based on expiration date."""
        return self.exp_date > date.today()
    def check_data(self, first_name, last_name, dob, country):
        """Verify passport details match the given information."""
        return (self.first_name == first_name and
                self.last_name == last_name and
                self.dob == dob and
                self.country == country and
                self.is_valid())
    def stamp(self, country_name):
        """Stamp the passport with a visit to a new country."""
        if country_name == self.country:
            return
        if country_name in self.stamps:
            self.stamps[country_name]+= 1
        else:
            self.stamps[country_name]= 1
    def countries_visited(self):
        """Return a list of countries visited."""
        return list(self.stamps.keys())
    def times_visited(self, country_name):
        """Return the number of times a country was visited."""
        return self.stamps.get(country_name, 0)
    def sum_square_visits(self):
        """Return the sum of the squares of visit counts."""
        return sum(count**2 for count in self.stamps.values())
    def passport_number(self):
        """Return the passport's unique ID number."""
        return self.passport_id
# if __name__ == "__main__":
#     alan = Passport(
#         "Alan",
#         "Turing",
#         "1912-06-23",
#         "The United Kingdom",
#         "2024-06-07"
#     )
#     print("Alan is valid", alan.is_valid())
#     # should output: False
#     print(alan.summary())
#     # should output: This passport belongs to Alan Turing, born on 1912-06-23 in The United Kingdom. It is invalid.
#     codegrade = Passport(
#         "Code",
#         "Grade",
#         "2017-07-21",
#         "The Netherlands",
#         "2999-12-31"
#     )
#     print(codegrade.check_data("Code", "Grade", "2017-07-21", "The Netherlands"))
#     # should output: True
