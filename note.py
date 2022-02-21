class Note:

    def __init__(self, issuer):
        self.issuer = issuer
        self.spv_jurisdiction = None
        self.investor_type = None
        self.investor_jurisdiction = None
        self.valid_jurisdictions = ["UK", "EU", "Both", "None"]

    def inv_applicable_rules(self):
        if self.investor_type == "institutional":
            if self.investor_jurisdiction == "Both":
                return "Both"
            elif self.investor_jurisdiction == "UK":
                return "UK"
            elif self.investor_jurisdiction == "EU":
                return "EU"
            else:
                return "None"
        else:
            return "N/A"

    def set_spv_jurisdiction(self, answer):
        if answer in self.valid_jurisdictions:
            self.spv_jurisdiction = answer

    def set_investor_jurisdiction(self, answer):
        if answer in self.valid_jurisdictions:
            self.investor_jurisdiction = answer





issuer = input("what is the issuer name? ")
note = Note(issuer)
note.investor_type = input ("Specify institutional or not institution: ")
note.investor_jurisdiction = input("what is the jurisdiction of the investor? ")
print(note.inv_applicable_rules())

