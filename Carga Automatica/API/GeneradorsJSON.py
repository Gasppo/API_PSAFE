
import json
from .PostDatas import datos_post_asset, datos_post_asset_database, datos_post_managedSystem #pylint: disable=E0402

#Create system asset data for console
def Datos_Asset(Sistema):
    JSON_Asset = datos_post_asset
    JSON_Asset['IPAddress'] = Sistema.IP
    JSON_Asset['AssetName'] = Sistema.AssetName
    JSON_Asset['DnsName'] = Sistema.DNS
    Datos = json.dumps(JSON_Asset)
    return Datos

#Create DB asset data for console
def Datos_DB(Base):
    JSON_DB = datos_post_asset_database
    JSON_DB['PlatformID'] = Base.tipo[0]
    JSON_DB['InstanceName'] = Base.InstanceName
    JSON_DB['Port'] = Base.port
    if ( Base.InstanceName.upper() == 'MSSQLSERVER' and Base.tipo[0] == 11):
        JSON_DB['IsDefaultInstance'] = 'true'
    Datos = json.dumps(JSON_DB)
    return Datos

#Create Managed System asset data for console
def Datos_MSYS(tupla):
    JSON_MSYS = datos_post_managedSystem
    JSON_MSYS['PlatformID'] = tupla[0]
    JSON_MSYS['FunctionalAccountID'] = tupla[1]
    JSON_MSYS['PasswordRuleID'] = tupla[2]
    if tupla[0] == 2:
        JSON_MSYS['LoginAccountID'] = tupla[1]
    Datos = json.dumps(JSON_MSYS)
    return Datos

#Create Managed Account data for console
def Datos_MACC(Cuenta,tupla):
    JSON_MACC = {
        'AccountName':Cuenta.AccName,
        'Description':Cuenta.Desc,
        'PasswordRuleID':tupla[2],
        'ReleaseDuration':480,
        'MaxReleaseDuration':1440
    }
    if Cuenta.AccName.lower() == "root":
        JSON_MACC['LoginAccountFlag'] = "True"
    if Cuenta.Pass.lower() == "auto":
        JSON_MACC['AutoManagementFlag'] = "True"
        JSON_MACC['CheckPasswordFlag'] = "True"
        JSON_MACC['ChangePasswordAfterAnyReleaseFlag'] = "True"
        JSON_MACC['ResetPasswordOnMismatchFlag'] = "True"
    else:
        JSON_MACC['AutoManagementFlag'] = "False"
        JSON_MACC['Password'] = Cuenta.Pass
    Datos = json.dumps(JSON_MACC)
    return Datos