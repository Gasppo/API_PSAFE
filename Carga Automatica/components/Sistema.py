class Sistema:
   def __init__(self, AssetName, IP, Plataforma,Ambiente):
       self.IP = IP
       self.AssetName = AssetName
       self.Plataforma = Plataforma
       self.DNS = AssetName+".rio.ar.bsch"
       self.Cuentas = []
       self.AssetID = 0
       self.ManagedSystemID = 0
       self.Ambiente = Ambiente
   def agregar_cuenta(self, Acc):
       self.Cuentas.append(Acc)
   def set_AssetID(self, ID):
       self.AssetID = ID
   def set_ManagedSystemID(self, ID):
       self.ManagedSystemID = ID