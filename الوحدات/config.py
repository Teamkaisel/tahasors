import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

API_ID  =  int ( getenv ( "API_ID" ، "17382799" ))
API_HASH   =   getenv ( "API_HASH"  ،  "70184773d578115dfefdc4a9e8a8bcf4" )
BOT_TOKEN  =  getenv ( "BOT_TOKEN" ، "" )
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION  =  getenv ( "STRING_SESSION" ، "AgBEA3LBDM24fNTLcNhb23EPITQC9Q9na7kGF3FmTUQGS0cAO6l5byANkJsnWiqT_S46FONT71w46R4q2t4UTy74yZbyu5GvqzkaiuXoJ-KTZXDeKusVd31R-qsJxUuusZKVMxKjtPHHINOmU_6Rr_XcS8H3t4kzkONuWS6LUztvje_h2xx2odX-vytHcJyVKI9dwiXxb0032JoynNXSU4m1w81BQC7-Y3jTEEFn_ZWGX6Tj56wwgZEthbxe9YXgO8YlFslQ9ZwuA-G5pMiN9Nx-gzUig2kpvhCSaupw1tVk-edrTb9bNSKh_nmevQ1nQKZ39pIdFapdmBHRtLziF4KjAAAAAUogW0cA" )
COMMAND_PREFIXES  =  list ( getenv ( "COMMAND_PREFIXES" ، "/!." ). split ())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
