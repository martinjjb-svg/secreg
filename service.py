

class Notes:
    """
    A representation of an issue. Attributes: issuer, spv, investors
    """

    def __init__(self, issuer, spv, investors, retention):
        self.issuer = issuer
        self.spv = spv
        self.investors = investors
        self.retention = retention
        self.jurisdiction = ["EU", "UK", "both"]
        self.retention_method = ["a", "b", "c", "d", "e"]

    @classmethod
    def get_user_input(self):
        while 1:
            try:
                issuer = input('Enter issuer name: ')
                spv = input('Enter spv jurisdiction: ')
                investors = input('Enter investor jurisdiction: ')
                retention = input('Enter appropriate letter from following list: \n'
                                  'a for Nominal Value of each tranche sold \n'
                                  'b for  Revolving - nominal value of each of securitised exposure \n'
                                  'c for Random selection - nominal value of each of securitised exposure \n'
                                  'd for First loss tranche - nominal value of each of securitised exposure \n'
                                  'e for First loss exposure - every securitised exposure in securitisation: ')
                return self(issuer, spv, investors, retention)
            except:
                print('Invalid input!')
                continue

    def apply_jurisdiction(self):
        if self.spv == self.jurisdiction[0] and self.investors == self.jurisdiction[0]:
            return "EU applies"
        elif self.spv == self.jurisdiction[1] and self.investors == self.jurisdiction[1]:
            return "UK applies"
        elif self.spv == self.jurisdiction[2]:
            return "EU and UK securitisation regs apply"
        else:
            return "other"


    def apply_retention_method(self):
        if self.retention == self.retention_method[0]:
            return "Vertical slice applies"
        elif self.retention == self.retention_method[1]:
            return "revolving applies"
        elif self.retention == self.retention_method[2]:
            return "random selection applies"
        elif self.retention == self.retention_method[3]:
            return "First loss tranche applies"
        elif self.retention == self.retention_method[4]:
            return "First loss exposure applies"
        else:
            return "other"


# creating an issue object and returning name and applicable jurisdictions
i1 = Notes.get_user_input()
i1.amount = "£10 million"
print(i1.apply_jurisdiction())
print(i1.issuer, i1.apply_jurisdiction(), i1.amount)
print(i1.apply_retention_method())
