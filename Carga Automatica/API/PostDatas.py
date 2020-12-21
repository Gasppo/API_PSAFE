datos_post_asset = {
'IPAddress': "" ,
'AssetName': "",  #String
'DnsName': "",  #String
'DomainName': "",  #String
'MacAddress': "",  #String
'AssetType': "",  #String
'OperatingSystem': "" #string
}

datos_post_attributeTypes = {
'Name': "", #string
}

datos_post_attributes = {
'ParentAttributeID' : 0, # can be null
'ShortName' : "",  #String
'LongName' : "",  #String
'Description' : "",  #String
'Value0' : 0 # can be null
}

datos_post_asset_database = {
'PlatformID' : 0,
'InstanceName' : "",  #String
'IsDefaultInstance' : "", #bool
'Port' : 0,
'Version' : "" #string
}

datos_post_userGroupsLOCAL = {
'groupType': "", #string = "BeyondInsight",
'groupName': "",  #String
'description': "",  #String
'isActive': "", #bool
'Permissions': [ { 'PermissionID': 0, 'AccessLevelID': 0 }, ... ],
'SmartRuleAccess': [ { 'SmartRuleID': 0, 'AccessLevelID': 0 } ],
'ApplicationRegistrationIDs': [ 0 ]
}

datos_post_userGroupsAD = {
'groupType': "", #string = "ActiveDirectory",
'groupName': "",  #String
'forestName': "",  #String
'domainName': "",  #String
'description': "",  #String
'bindUser': "",  #String
'bindPassword': "",  #String
'useSSL': "", #bool
'isActive': "", #bool
'Permissions': [ { 'PermissionID': 0, 'AccessLevelID': 0 }, ... ],
'SmartRuleAccess': [ { 'SmartRuleID': 0, 'AccessLevelID': 0 }, ... ],
'ApplicationRegistrationIDs': [ 0 ]
}

datos_post_userGroupsPermissions = [
{
'PermissionID' : 0,
'AccessLevelID' : 0
},
{}
]

datos_post_userGroupsSmartRuleAccess = {
'AccessLevelID': 0
}

datos_post_userLOCAL = {
'UserType': "", #string = "BeyondInsight",
'UserName': "",  #String
'FirstName': "",  #String
'LastName': "",  #String
'EmailAddress': "",  #String
'Password': "", #string
}

datos_post_userAD = {
'UserType': "", #string = "ActiveDirectory",
'UserName': "",  #String
'ForestName': "",  #String
'DomainName': "",  #String
'BindUser': "",  #String
'BindPassword': "",  #String
'UseSSL': "" #bool
}

datos_post_managedSystem = {
'PlatformID': 0,
'ContactEmail': "", #String
'Description': "", #String
'Port': 0, # can be null
'Timeout': "",
'SshKeyEnforcementMode': 0, # can be null
'PasswordRuleID': 0,
'DSSKeyRuleID': 0, # can be null
'LoginAccountID': 0, # can be null
'ReleaseDuration': 480,
'MaxReleaseDuration': 1440,
'ISAReleaseDuration': 0,
'AutoManagementFlag': "", #bool
'FunctionalAccountID': 0, # can be null
'ElevationCommand': "", #String # can be null
'CheckPasswordFlag': "", #bool
'ChangePasswordAfterAnyReleaseFlag': "", #bool
'ResetPasswordOnMismatchFlag': "", #bool
'ChangeFrequencyType': "", #String
'ChangeFrequencyDays': 0,
'ChangeTime': "" #String
}

datos_post_managedSystem_DB = {
'ContactEmail': "", #String
'Description': "", #String
'Timeout': "",
'PasswordRuleID': 0,
'ReleaseDuration': 0,
'MaxReleaseDuration': 0,
'ISAReleaseDuration': 0,
'AutoManagementFlag': "", #bool
'FunctionalAccountID': 0, # can be null
'CheckPasswordFlag': "", #bool
'ChangePasswordAfterAnyReleaseFlag': "", #bool
'ResetPasswordOnMismatchFlag': "", #bool
'ChangeFrequencyType': "", #String
'ChangeFrequencyDays': 0,
'ChangeTime': "" #String
}

datos_post_managedAccountToSystem = {
'AccountName': "", #String
'Password': "", #String
'PrivateKey': "", #String
'Passphrase': "", #String
'PasswordFallbackFlag': "", #bool
'LoginAccountFlag': "", #bool
'Description': "", #String
'PasswordRuleID': 0,
'ApiEnabled': "", #bool
'ReleaseNotificationEmail': "", #String
'ChangeServicesFlag': "", #bool
'RestartServicesFlag': "", #bool
'ChangeTasksFlag': "", #bool
'ReleaseDuration': 0,
'MaxReleaseDuration': 0,
'ISAReleaseDuration': 0,
'MaxConcurrentRequests': 0,
'AutoManagementFlag': "", #bool
'DSSAutoManagementFlag': "", #bool
'CheckPasswordFlag': "", #bool
'ResetPasswordOnMismatchFlag': "", #bool
'ChangePasswordAfterAnyReleaseFlag': "", #bool
'ChangeFrequencyType': "", #String
'ChangeFrequencyDays': 0,
'ChangeTime': "", #String
'NextChangeDate': ""
}

datos_requests = {
'SystemID': 0,
'AccountID': 0,
'DurationMinutes': 0,
'Reason': "", #String
'TicketNumber': "" #String
"""
'AccessType': "", #String
'ApplicationID': 0, # can be null
'AccessPolicyScheduleID': 0, # can be null
'ConflictOption': "", #String
'TicketSystemID': 0,
'RotateOnCheckin': "" #bool
"""
}

datos_post_quickrule = {
'AccountIDs': [0],
'Title': "",
'Category': "",
'Description': ""
}