class taxi():
    def __init__(self,emri,mbiemri,nrtaxi,kompania="urban"):
        self.emri=emri
        self.mbiemri=mbiemri
        self.nrtaxi=nrtaxi
        self.kompania=kompania

    def get_kompania(self):#kompania readonly
        return self.kompania
    def paraqit(self):
        print(self.emri)
        print(self.mbiemri)
        print(self.nrtaxi)
        print(self.kompania)

t=taxi("arlind","krasniqi",1)
t1=taxi("albin","krasniqi",2)
t.paraqit()
print("-----------------")
t1.paraqit()





