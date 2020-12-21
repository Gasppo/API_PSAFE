from .Cuenta import Cuenta #pylint: disable=E0402

Accounts = [
   Cuenta("epayo","auto","Administrador Windows\nGRPIBMINTELAD"),
   Cuenta("root","auto","Cuenta root\nGRPIBMADMUX"),
   Cuenta("srvctena","auto","Cuenta srvctena\nGRPSEGINFUXORA"),
   Cuenta("grid","auto","Cuenta grid\nGRPIBMTECNOBDORA"),
   Cuenta("oracle","auto","Cuenta oracle\nGRPIBMTECNOBDORA"),
   Cuenta("mysql","auto","Cuenta MySQL\nGRPIBMTECNOBDORA"),
   Cuenta("postgres","auto","Cuenta PostgreSQL\nGRPIBMTECNOBDORA"),
   Cuenta("mongod","auto","Cuenta MongoDB\nGRPIBMTECNOBDORA"),
   Cuenta("ctmagent","auto","Cuenta ctmagent\nGRPIBMIMPLEMID\nGRPPRBTYSWAP\nGRPPRBCCB"),
   Cuenta("snowunix","auto","Cuenta snowunix\nGRPSEGINFUXORA"),
   Cuenta("ndm","auto","Cuenta ndm\nGRPIBMIMPLEMID\nGRPIBMSSOBAS")
]

AccountsDefaultMSSQL = [
    Cuenta("sa","1qaz2WSX","Cuenta MSSQL\nGRPIBMADMSQL")
]

AccountsDefaultCDB = [
    Cuenta("SYS","Yue_as4_sa9_xXc","Cuenta SYS\nGRPIBMTECNOBDORA"),
    Cuenta("C##GRAFANA","Pa55_x_Grafa","GRPIBMTECNOBDORA"),
    Cuenta("SYSTEM","auto","Cuenta SYSTEM\nGRPIBMTECNOBDORA")
]

AccountsDefaultPDB = [
    Cuenta("A299943","auto","GRPSEGINFUXORA"),
    Cuenta("A109024","auto","GRPSEGINFUXORA"),
    Cuenta("A308476","auto","GRPSEGINFUXORA"),
]

AccountsDefaultMONGO = [
    Cuenta("A299943","temporal","GRPSEGINFUXORA"),
    Cuenta("A109024","temporal","GRPSEGINFUXORA"),
    Cuenta("A308476","temporal","GRPSEGINFUXORA"),
    Cuenta("C##SISERV","temporal","GRPSEGINFUXORA"),
    Cuenta("C##SRVCPBPS","temporal","GRPSEGINFUXORA")
]

AccountsDefaultMYSQL = [
    Cuenta("A299943","auto","GRPSEGINFUXORA"),
    Cuenta("A109024","auto","GRPSEGINFUXORA"),
    Cuenta("A308476","auto","GRPSEGINFUXORA"),
    Cuenta("C##SISERV","auto","GRPSEGINFUXORA"),
    Cuenta("C##SRVCPBPS","auto","GRPSEGINFUXORA")
]

AccountsDefaultPOSTGRES = [
    Cuenta("A299943","auto","GRPSEGINFUXORA"),
    Cuenta("A109024","auto","GRPSEGINFUXORA"),
    Cuenta("A308476","auto","GRPSEGINFUXORA"),
    Cuenta("C##SISERV","auto","GRPSEGINFUXORA"),
    Cuenta("C##SRVCPBPS","auto","GRPSEGINFUXORA")
]