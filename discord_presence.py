import pypresence, psutil, time

client_id = '960217211631468575'  
boottime = time.time()
RPC = pypresence.Presence(client_id)
RPC.connect()

while True:
    cpuusage = round(psutil.cpu_percent(),1)
    ramusage = round(psutil.virtual_memory()[2],1)
    if cpuusage > 75.0 or ramusage > 85.0: pcstatus = "ITS BURNING"; icon = "fire_ico"
    elif cpuusage > 55.0 or ramusage > 65.0: pcstatus = "Its warming"; icon = "ok_ico"
    elif cpuusage > 35.0 or ramusage > 45.0: pcstatus = "Its oke"; icon = "ok_ico"
    elif cpuusage > 25.0 or ramusage > 35.0: pcstatus = "Its cold"; icon = "ice_ico"
    else: pcstatus = "Its ok i think (i cant tell)"; icon = "pc"
    pcdetails = f"CPU: {cpuusage}% RAM {round(psutil.virtual_memory().percent,1)}%"
    RPC.update(
        state = pcstatus,
        details = pcdetails,
        large_image = "pc",
        large_text = "ash ketchum's pc",
        small_image = icon,
        small_text = f"My PC Status: {pcstatus}",

        buttons = [
            {"label": "join my server", "url": "http://gg.gg/serverforprogramers"},
        ],
        start=boottime
    )
    time.sleep(15)