# PSAFE Server information
PSAFE_HOST = ""
PSAFE_KEY = ""
PSAFE_USER = ""
PSAFE_PASS = ""


PSAFE_WORKGROUP = "1"
auth_head='PS-Auth key=%s; runas=%s; pwd=[%s];' % (PSAFE_KEY, PSAFE_USER, PSAFE_PASS)
base='https://%s/BeyondTrust/api/public/v3' % (PSAFE_HOST)
header = {'Authorization': auth_head}
datype={'Content-type':'application/json'}