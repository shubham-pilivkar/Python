class ReservationForm:
    type = "RailWay Form"
    def information(self):
        print(f"The Name of Applicant: {self.name}")
        print(f"The Date Of Reversion: {self.date}")
        print(f"The Name of Railway: {self.railName}")

applicant = ReservationForm()
applicant.name = "Shubham"
applicant.date = "22 Nov"
applicant.railName = "Rajdhani Express"
applicant.information()