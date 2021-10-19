from pypresence import Presence

import time

client_id = "895902436802306058"

RPC = Presence(client_id=client_id)
RPC.connect()

RPC.update(state="Editing: modmail.py", details="Workspace: Wissen", large_image="python-logo-4k-i6-2932x2932",
           small_image="untitled_design_2_1_", start=time.time(), buttons=[{"label": "My Instagram", "url": "https://www.instagram.com/__the.asynchronus__/"}, {"label": "Get Rich with Dank Memer HERE!!", "url": "https://discord.gg/uqgxaUebwh"}])

while 1:
    time.sleep(1)
