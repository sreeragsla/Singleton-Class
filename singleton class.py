def singleton(args):
    L=[]
    def inner():
        if not L:
            mco=args()
            L.append(mco)
            
        return L[0]
    return inner

@singleton

class Multiplex:
    def __init__(self):
        self.tickets=300

    def booking(self,nt):
        if nt<=self.tickets:
            self.tickets-=nt
            print('Tickets Booked Successfully')
            print('Available Tickets - ',self.tickets)
        else:
            print('Tickets Not Available')
            print('Available Tickets - ',self.tickets)

srg,sla=Multiplex(),Multiplex()
srg.booking(256)
sla.booking(52)
            
