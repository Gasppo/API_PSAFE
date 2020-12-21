#!/usr/bin/scl enable rh-python36 -- python
#
# PSAFE account, system and database registration
#
# Usage: psafe.py filename.csv ORACLE/MONGODB/MYSQL/POSTGRESQL/MSSQL/SRV
#
# CSV file format for registering assets into PSAFE Console
#
#
# For loading server assets
# { hostname (short), ip, platform, environment, user accounts }
#
# For loading database assets
# { DB/CDB/PDB name, port, hostname (short), user accounts }
#
#
# Platform: Windows, Linux
# Environment: Produccion, Desarrollo
#
#
# (C) 2020 Federico Trasande, IBM Argentina SRL

import requests
import json
import sys
import argparse
import math
import configparser
import datetime
import os
import getpass
import logging
from API.API_GENERAL import BeyondTrustAPI
from API.GeneradorsJSON import Datos_DB


#Componentes
from components.Base import Base
from components.Sistema import Sistema
from components.Cuenta import Cuenta
from components.CuentasPermitidas import Accounts, AccountsDefaultCDB, AccountsDefaultMONGO, AccountsDefaultMSSQL, AccountsDefaultMYSQL, AccountsDefaultPDB, AccountsDefaultPOSTGRES
from components.DatosAPI import PSAFE_HOST, PSAFE_KEY, PSAFE_USER, PSAFE_PASS, PSAFE_WORKGROUP
from components.PlatformInfo import *


API = BeyondTrustAPI(PSAFE_KEY, PSAFE_USER, PSAFE_PASS, PSAFE_HOST)


#Inicio de sesion de API
def signin(API):
    Respuesta = API.signin()
    logging.info("Iniciando conexion con la API...\n    URI:        %s" % (Respuesta.url))
    if Respuesta.ok:
        logging.info("Conexion exitosa con la API!")
        return True
    logging.error("No se pudo establecer conexion\nStatus Code: %d" % (Respuesta.status_code))
    return False


#Cierre de session de API
def signout(API):
    Respuesta = API.singout()
    logging.info("Terminando conexion con la API...\n    URI:        %s" % (Respuesta.url))
    if Respuesta.ok:
        logging.info("Desconexion exitosa con la API!")
        return True
    logging.error("*** Error en la desconexion\nStatus Code: %d" % (Respuesta.status_code))
    return False

#Get Managed System ID from asset name
def get_AssetID(API,AssetName):
    Respuesta = API.get_assetByName(PSAFE_WORKGROUP, AssetName) 
    if Respuesta.status_code != 200:
        logging.error("*** Error en la busqueda de datos\nStatus Code: %d" % (Respuesta.status_code))
        return -1
    AssetInfo = json.loads(Respuesta.text)
    logging.info("AssetID encontrada! AssetID: %d" % (AssetInfo['AssetID']))
    return AssetInfo['AssetID']

#Get Managed System info
def get_msysID(API,Sistema):
    Respuesta = API.get_managedSystems()
    Listado_Completo = json.loads(Respuesta.text)
    for Elemento in Listado_Completo:
        if(Elemento['SystemName'] == Sistema.AssetName):
            return(Elemento['ManagedSystemID'])
    logging.error("*** Error en la busqueda de datos de Managed System\nStatus Code: %d" % (Respuesta.status_code))
    return -1

#Get DB System info
def get_msysID_DB(API,Database):
    Respuesta = API.get_managedSystems()
    Listado_Completo = json.loads(Respuesta.text)
    for Elemento in Listado_Completo:
        if(Elemento['DatabaseID'] == Database.DatabaseID):
            return(Elemento['ManagedSystemID'])
    logging.error("*** Error en la busqueda de datos de Managed System\nStatus Code: %d" % (Respuesta.status_code))
    return -1

#Get DB ID from asset name
def get_DatabaseID(session,InstanceName):
    Respuesta = session.get(base + '/Databases')
    Lista_DBs = json.loads(Respuesta.text)
    for Instance in Lista_DBs:
        if Instance['InstanceName'] == InstanceName:
            return Instance['DatabaseID']
    return -1

#Get DB ID from asset name 
def get_DatabaseID_fromAssetID(session,InstanceName, AssetID):
    Respuesta = session.get(base +'/Assets/'+str(AssetID)+'/Databases')
    Lista_DBs = json.loads(Respuesta.text)
    for Instance in Lista_DBs:
        if Instance['InstanceName'] == InstanceName:
            return Instance['DatabaseID']
    return -1

#Create System asset
def post_asset(session,Sistema):
    datos = Datos_Asset(Sistema)
    Respuesta = session.post(base + '/Workgroups/'+PSAFE_WORKGROUP+'/Assets',data=datos,headers=datype)
    #print("Status Code post_DB: %d" % Respuesta.status_code )
    if Respuesta.status_code < 300:
        Diccionario = json.loads(Respuesta.text)
        Sistema.set_AssetID(Diccionario['AssetID'])
        return Respuesta
    else:
        print("Error loading asset: %s\nMessage: %s" % (Sistema.AssetName,Respuesta.text))
        return -1

#Create DB Asset
def post_DB(session,Base):
    datos = Datos_DB(Base)
    print("\nAsset Id: "+str(Base.AssetID)+"\n")
    Respuesta = session.post(base + '/Assets/'+str(Base.AssetID)+'/Databases',data=datos,headers=datype)
    #print("Status Code post_DB: %d" % Respuesta.status_code )
    if Respuesta.status_code < 300:
        Diccionario = json.loads(Respuesta.text)
        Base.set_DatabaseID(Diccionario['DatabaseID'])
        return Respuesta    
    else:
        print("Error registering DB: %s\nMessage: %s" % (Base.InstanceName,Respuesta.text))
        return -1

#Assign environment attribute to asset
def post_attributes_ambiente(session,Sistema):
    if Sistema.Ambiente == "Produccion":
        amb = str(Prod)
    elif Sistema.Ambiente == "Desarrollo":
        amb = str(Desa)
    else:
        return -1
    Respuesta = session.post(base + '/Assets/'+str(Sistema.AssetID)+'/Attributes/'+amb)
    return Respuesta

#Assign OS attribute to asset
def post_attributes_os(session,Sistema):
    Respuesta = session.post(base + '/Assets/'+str(Sistema.AssetID)+'/Attributes/'+str(Sistema.Plataforma[3]))
    return Respuesta

#Create Managed System asset
def post_ManagedSystem_Asset(session,type,Sistema):
    datos = Datos_MSYS(type)
    Respuesta = session.post(base + '/Assets/'+str(Sistema.AssetID)+'/ManagedSystems',data=datos,headers=datype)
    if Respuesta.status_code == 201:
        Diccionario = json.loads(Respuesta.text)
        Sistema.set_ManagedSystemID(Diccionario['ManagedSystemID'])
        return Respuesta
    else:
        if "ManagedSystemID" in Respuesta.text:
            print("*** Registering Managed System anyway ***")
            Diccionario = json.loads(Respuesta.text)
            Sistema.set_ManagedSystemID(Diccionario['ManagedSystemID'])
            return Respuesta
        else:
            print("Error creating MSYS for %s\nMessage: %s" % (Sistema.AssetName,Respuesta.text))
            return -1

#Create DB Managed System asset
def post_ManagedSystem_DB(session,type,Base):
    datos = Datos_MSYS(type)
    print("\nDB Id: "+str(Base.DatabaseID)+"\n")
    Respuesta = session.post(base + '/Databases/'+str(Base.DatabaseID)+'/ManagedSystems',data=datos,headers=datype)
    if Respuesta.status_code == 201:
        Diccionario = json.loads(Respuesta.text)
        Base.set_ManagedSystemID(Diccionario['ManagedSystemID'])
        return Respuesta
    else:
        if "ManagedSystemID" in Respuesta.text:
            print("*** Registering Managed System anyway ***")
            Diccionario = json.loads(Respuesta.text)
            Base.set_ManagedSystemID(Diccionario['ManagedSystemID'])
            return Respuesta
        else:
            print("Error creating Managed System for %s\nMessage: %s" % (Base.InstanceName,Respuesta.text))
            return -1            

#Create accounts for Managed System asset
def post_ManagedAccount(session,type,Sistema,Cuenta):
    url_account = base+"/ManagedSystems/"+str(Sistema.ManagedSystemID)+"/ManagedAccounts"
    datos = Datos_MACC(Cuenta,type)
    Respuesta = session.post(url_account, data = datos,headers=datype)
    if "already exists" in Respuesta.text:
        print("Account '"+Cuenta.AccName+"' exists")
        return -1
    else:
        print("Account '"+Cuenta.AccName+"' added")
        return Respuesta


def Crear_DB(API, Info, dbPlatform):
    Cuentas = []
    passtype = "auto"

    if dbPlatform == "ORACLE" and "cdb" in Info[0].lower():
        Type = ORACLE_CDB
        Cuentas = AccountsDefaultCDB
    elif dbPlatform == "ORACLE" and "cdb" not in Info[0].lower():
        Type = ORACLE_PDB
        Cuentas = AccountsDefaultPDB
    elif dbPlatform == "MONGODB":
        Type = MONGO_DB
        Cuentas = AccountsDefaultMONGO
        passtype = "temporal"
    elif dbPlatform == "MYSQL":
        Type = MYSQL_DB
        Cuentas = AccountsDefaultMYSQL
    elif dbPlatform == "MSSQL":
        Type = MSSQL_DB
        Cuentas = AccountsDefaultMSSQL
    elif dbPlatform == "POSTGRESQL":
        Type = POSTGRES
        Cuentas = AccountsDefaultPOSTGRES

    Database = Base(Info[0],Info[1],Type)
    for Account in Cuentas:
        Database.agregar_cuenta(Account)
    # Add application user accounts specified in csv file
    for Account in Info[3:]:
        Database.agregar_cuenta(Cuenta(Account,passtype,"Cuenta de aplicacion "+str(Account)+"\nGRPIBMIMPLEMID"))
    AssetID = get_AssetID(API,Info[2])
    Database.set_assetID(AssetID)
    return Database

