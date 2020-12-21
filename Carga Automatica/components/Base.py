class Base:
   def __init__(self, InstanceName, port, tipo):
       self.InstanceName = InstanceName
       self.DatabaseID = 0
       self.AssetID = 0
       self.ManagedSystemID = 0
       self.tipo = tipo
       self.port = port
       self.Cuentas = []
   def agregar_cuenta(self, Acc):
       self.Cuentas.append(Acc)
   def set_assetID(self,ID):
       self.AssetID = ID
   def set_DatabaseID(self, ID):
       self.DatabaseID = ID
   def set_ManagedSystemID(self, ID):
       self.ManagedSystemID = ID