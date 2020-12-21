import requests
import json
import sys
import os
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class BeyondTrustAPI:

    def __init__(self, Key, User, Password, IP):
        self.Key = Key
        self.IP = IP
        self.User = User
        self.Password = '['+Password+']'
        self.auth_head='PS-Auth key=%s; runas=%s; pwd=%s;' % (self.Key, self.User, self.Password)
        self.base='https://%s/BeyondTrust/api/public/v3' % (IP)
        self.header = {'Authorization': self.auth_head}
        self.datype={'Content-type':'application/json'}
        self.session = requests.Session()
        self.session.headers.update(self.header)

    #OPERACIONES BASICAS
    def signin(self):
        print("Signing in...")
        signin_url = self.base+'/Auth/SignAppin'
        return self.session.post(signin_url ,verify=False)

    def signout(self):
        print("Signing out...")
        signout_url = self.base+'/Auth/Signout'
        return self.session.post(signout_url ,verify=False)

    #ASSETS
    def get_assets(self, WorkgroupID):
        return self.session.get(self.base+'/Workgroups/'+str(WorkgroupID)+'/Assets')

    def get_asset(self, AssetID):
        return self.session.get(self.base+'/'+str(AssetID))

    def get_assetByName(self, WorkgroupID, AssetName):
        return self.session.get(self.base+'/Workgroups/'+str(WorkgroupID)+'/Assets?name='+AssetName)

    def post_asset(self, WorkgroupID, datos):
        return self.session.post(self.base+'/'+str(WorkgroupID)+'/Assets', data = datos, headers = self.datype)

    #ATTRIBUTES & ATTRIBUTE TYPES
    def get_attributeTypes(self):
        return self.session.get(self.base+'/AttributeTypes')

    def get_attribute(self, attributeTypeID):
        return self.session.get(self.base+'/AttributeTypes/'+str(attributeTypeID)+'/Attributes')

    def post_attributeTypes(self, datos):
        return self.session.post(self.base+'/AttributeTypes', data = datos, headers = self.datype)

    def post_attributes(self, datos, attributeTypeID):
        return self.session.post(self.base+'/AttributeTypes/'+str(attributeTypeID)+'/Attributes', data = datos, headers = self.datype)

    #DATABASES
    def get_databases(self):
        return self.session.get(self.base+'/Databases')

    def get_asset_databases(self, AssetID):
        return self.session.get(self.base+'/Assets/'+str(AssetID)+'/Databases')

    def post_asset_database(self, AssetID, datos):
        return self.session.post(self.base+'/Assets/'+str(AssetID)+'/Databases', data = datos, headers = self.datype)
    
    #PERMISIONS AND ACCESS LEVELS
    def get_permissions(self):
        return self.session.get(self.base+'/Permissions')

    def get_accessLevels(self):
        return self.session.get(self.base+'/AccessLevels') 

    #USER GROUPS
    def get_userGroups(self):
        return self.session.get(self.base+'/UserGroups')

    def get_userGroupByName(self, name):
        return self.session.get(self.base+'/UserGroups?name='+name)

    def get_userGroupByID(self, GroupId):
        return self.session.get(self.base+'/UserGroups/'+str(GroupId))

    def post_userGroups(self, datos):
        return self.session.post(self.base+'/UserGroups', data = datos, headers = self.datype)
    
    def post_userGroupsPermissions(self,datos, GroupID):
        return self.session.post(self.base+'/UserGroups/'+str(GroupID)+'/Permissions', data = datos, headers = self.datype)

    def post_userGroupSmartRuleAccess(self, datos, GroupId, SmartRuleId):
        return self.session.post(self.base+'/UserGroups/'+str(GroupId)+'/SmartRules/'+str(SmartRuleId)+'/AccessLevels', data = datos, headers = self.datype)

    #USERS
    def get_users(self):
        return self.session.get(self.base+'/Users')

    def get_userByID(self, UserId):
        return self.session.get(self.base+'/Users'+str(UserId))

    def get_usersByGroupID(self, GroupId):
        return self.session.get(self.base+'/UserGroups/'+str(GroupId)+'/Users')

    def get_groupsByUserID(self, UserId):
        return self.session.get(self.base+'/Users/'+str(UserId)+'/UserGroups')

    def post_existingUserToGroup(self, UserId, GroupId):
        return self.session.post(self.base+'/Users/'+str(UserId)+'/UserGroups/'+str(GroupId))

    def post_user(self, datos, GroupId):
        return self.session.post(self.base+'/UserGroups/'+str(GroupId)+'/Users', data = datos, headers = self.datype)

    #SMART RULES
    def get_smartRules(self):
        return self.session.get(self.base+'/SmartRules')

    def get_smartRuleByName(self, name):
        return self.session.get(self.base+'/SmartRules?title='+name)

    def get_smartRuleByID(self, SmartRuleId):
        return self.session.get(self.base+'/SmartRules/'+str(SmartRuleId))

    #MANAGED SYSTEMS
    def get_managedSystems(self):
        return self.session.get(self.base+'/ManagedSystems')

    def get_managedSystemsByID(self, ManagedSystemId):
        return self.session.get(self.base+'/ManagedSystems/'+str(ManagedSystemId))

    def get_managedSystemByAssetID(self, AssetId):
        return self.session.get(self.base+'/Assets/'+str(AssetId)+'/ManagedSystems')

    def get_managedSystemByDatabaseID(self, DatabaseId):
        return self.session.get(self.base+'/Databases/'+str(DatabaseId)+'/ManagedSystems')

    def get_managedSystemByName(self, Name):
        ManagedSystems = json.loads(self.get_managedSystems().text)
        for System in ManagedSystems:
            if System['SystemName'].lower() == Name.lower():
                return System

    def post_managedSystemByAssetID(self, AssetId, datos):
        return self.session.post(self.base+'/Assets/'+str(AssetId)+'/ManagedSystems', data = datos, headers = self.datype)

    def post_managedSystemByDatabaseID(self, DatabaseId, datos):
        return self.session.post(self.base+'/Databases/'+str(DatabaseId)+'/ManagedSystems', data = datos, headers = self.datype)

    def delete_managedSystem(self, ManagedSystemID):
        return self.session.delete(self.base+'/ManagedSystems/'+str(ManagedSystemID))

    #MANAGED ACCOUNTS
    def get_managedAccounts(self):
        return self.session.get(self.base+'/ManagedAccounts')

    def get_managedAccountsByID(self, ManagedAccountId):
        return self.session.get(self.base+'/ManagedAccounts/'+str(ManagedAccountId))

    def get_managedAccountBySystemID(self, ManagedSystemId):
        return self.session.get(self.base+"/ManagedSystems/"+str(ManagedSystemId)+'/ManagedAccounts')

    def get_managedAccountsBySystemAndAccountName(self, SystemName, AccountName):
        return self.session.get(self.base+'/ManagedAccounts?systemName='+SystemName+'&accountName='+AccountName)

    def post_managedAccountToSystem(self, SystemId, datos):
        return self.session.post(self.base+'/ManagedSystems/'+str(SystemId)+'/ManagedAccounts', data = datos, headers = self.datype) 
    def put_managedAccountCreds(self, ManagedAccountID, Password, Cambiar_Sistema = False):
        atributos = {
           "Password" : Password,
           "UpdateSystem" : Cambiar_Sistema
            }
        datos = json.dumps(atributos)
        return self.session.put(self.base+'/ManagedAccounts/'+str(ManagedAccountID)+'/Credentials', data = datos, headers = self.datype)

    #REQUESTS
    def get_requests(self):
        return self.session.get(self.base+'/Requests')
    
    def post_requests(self, datos):
        return self.session.post(self.base+'/Requests', data = datos, headers = self.datype) 
    
    def put_requests_checkin(self, RequestID):
        return self.session.put(self.base+'/Requests/'+str(RequestID)+'/Checkin', data = "{}", headers = self.datype)
    
    def get_credentials(self, RequestID):
        return self.session.get(self.base+'/Credentials/'+str(RequestID))

    #WORKGROUPS
    def get_workgroups(self):
        return self.session.get(self.base+'/Workgroups')

    def get_workgroupByName(self, WorkgroupName):
        return self.session.get(self.base+'/Workgroups?name='+ WorkgroupName)
    
    #FUNCTIONAL ACCOUNTS
    def get_functionalAccounts(self):
        return self.session.get(self.base+'/FunctionalAccounts')

    #APPLICATGIONS
    def get_applications(self):
        return self.session.get(self.base+'/Applications')

    def post_managedAccountApplication(self, accountID, applicationID):
        return self.session.post(self.base+'/ManagedAccounts/'+str(accountID)+'/Applications/'+str(applicationID))




