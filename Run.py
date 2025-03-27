try:
    import requests, secrets, time, random, pytz, os, sys
    from requests_toolbelt.multipart.encoder import MultipartEncoder
    from fake_useragent import UserAgent
    from rich.panel import Panel
    from rich import print as Print
    from rich.console import Console
    from requests.exceptions import RequestException
except ModuleNotFoundError:
    print("Please install the required modules by running: pip install -r requirements.txt")
    exit()

def Banner() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    Print(
        Panel(r"""[bold red]    _______ _ _    ____                  _  __   __
   |__   __(_) |  |  _ \                | | \ \ / /
      | |   _| | _| |_) | ___   ___  ___| |_ \ V / 
      | |  | | |/ /  _ < / _ \ / _ \/ __| __| > <  
      | |  | |   <| |_) | (_) | (_) \__ \ |_ / . \ 
      [bold white]|_|  |_|_|\_\____/ \___/ \___/|___/\__/_/ \_\
             [underline red]𝚃𝚒𝚔𝚝𝚘𝚔 𝙵𝚛𝚎𝚎 𝚅𝚒𝚎𝚠𝚜 - 𝚋𝚢 𝚁𝚘𝚣𝚑𝚊𝚔""", style="bold bright_yellow", width=59
        )
    )
    return None

def Delay(wait: int) -> None:
    for i in range(wait, 0, -1):
        Print(f"[bold bright_yellow]   ──>[bold white] TUNGGU[bold green] {i}[bold white] DETIK...         ", end="\r")
        time.sleep(1)
    return None
    
def Submit(session: requests.Session, cookies_string: str, video_urls: str) -> bool:
    boundary = "----WebKitFormBoundary" + secrets.token_hex(8)
    session.headers.update(
        {
            "Content-Type": f"multipart/form-data; boundary={boundary}",
            "Referer": "https://myinstafollow.com/free-tiktok-views/",
            "Sec-Fetch-Site": "same-origin",
            "Cookie": f"{cookies_string}",
            "Sec-Fetch-Mode": "cors",
            "Accept": "*/*",
            "Sec-Fetch-Dest": "empty",
            "Origin": "https://myinstafollow.com",
            "Content-Length": "0"
        }
    )

    multipart_data = MultipartEncoder(
        fields={
            "postlink": f"{video_urls}",
            "service": "6397",
            "tiktokviewsQuantity": "100",
            "extended_user_agent": f"""Browser CodeName: Mozilla | 
                Browser Name: Netscape | 
                Browser Version: {session.headers['User-Agent'].replace('Mozilla/', '')} | 
                Cookies Enabled: true | 
                Platform: {Operating_System(session.headers['User-Agent'])} | 
                User-agent header: {session.headers['User-Agent']} | 
                Language: en-US | 
                Screen Resolution: {random.choice(['1280x720', '1920x1080', '1366x768', '1600x900', '2560x1440', '3840x2160', '1024x768', '1440x900'])} | 
                Color Depth: 24 | 
                Browser Window Size: {random.choice([1280, 1366, 1440, 1600, 1920])}x{random.randint(500, 900)} | 
                Time Zone: {random.choice(pytz.all_timezones)} | 
                Languages: en-US, en | 
                Hardware Concurrency: {random.choice([2, 4, 6, 8, 12, 16, 32])} | 
                Device Memory: {random.choice([2, 4, 8, 16, 32, 64])} GB | 
                Touch Support: false | 
                JavaScript Enabled: true"""
        },
        boundary=boundary
    )
    response = session.post('https://myinstafollow.com/themes/vision/part/free-tiktok-views/submitForm.php', data=multipart_data, verify=True)
    if '"status":"error"' in response.text:
        remainingTime = response.json().get("remainingTime", 0)

        hours, remainder = divmod(remainingTime, 3600)
        minutes, seconds = divmod(remainder, 60)

        Print(f"[bold bright_yellow]   ──>[bold yellow] REMAINING TIME: {hours}H {minutes}M {seconds}S     ", end="\r")
        time.sleep(4.5)
        Delay(wait=int(remainingTime))
        return True
    elif '"status":"success"' in response.text:
        Print(
            Panel(f"""[bold white]Status: [bold green]Successfully...
[bold white]Link: [bold red]{video_urls}
[bold white]Views:[bold green] +100""", style="bold bright_yellow", width=59, title="[bold bright_yellow]>> [Success] <<")
        )
        time.sleep(5.0)
        return True
    else:
        Print(f"[bold bright_yellow]   ──>[bold red] FAILED TO SUBMIT VIEWS!     ", end="\r")
        time.sleep(4.5)
        return False

def Discover(session: requests.Session, user_agent: str) -> str:
    session.headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "en-US,en;q=0.9",
        "Sec-Fetch-Dest": "document",
        "Host": "myinstafollow.com",
        "Sec-Fetch-Site": "none",
        "Connection": "keep-alive",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Mode": "navigate",
        "User-Agent": f"{user_agent}",
        "Upgrade-Insecure-Requests": "1",
        "Accept-Encoding": "gzip, deflate"
    }
    response = session.get('https://myinstafollow.com/free-tiktok-views/', allow_redirects=True, verify=True)
    cookies_string = "".join([f"{key}={value};" for key, value in session.cookies.get_dict().items()])
    return cookies_string

def Operating_System(user_agent: str) -> str:
    platform_map = {
        "Windows": "Win32",
        "Mac OS X": "Darwin",
        "iPhone": "IOS",
        "iPad": "IOS",
        "Android": "Android",
        "Linux": "Linux"
    }
    platform = next((v for k, v in platform_map.items() if k in user_agent), "Unknown")
    return platform

def Feature() -> None:
    Banner()
    Print(Panel("[bold white]Silakan Masukkan Link Postingan Tiktok, Pastikan Akun Tidak Dalam Keadaan Private. Contohnya:[bold red] https://ww\nw.tiktok.com/@rozhak.sch.id/video/7311522299532840198[bold white]", style="bold bright_yellow", width=59, title="[bold bright_yellow]>> [Tiktok Link] <<", subtitle="[bold bright_yellow]╭──────", subtitle_align="left"))
    video_urls = Console().input("[bold bright_yellow]   ╰─> ")
    if 'tiktok.com' in video_urls:
        Print(Panel("[bold white]Anda Bisa Menggunakan CTRL + C Jika Stuck Dan Gunakan CTRL + Z Untuk Berhenti!", style="bold bright_yellow", width=59, title="[bold bright_yellow]>> [Notes] <<"))
        while True:
            try:
                session = requests.Session()
                cookies_string = Discover(session, UserAgent().random)
                Delay(wait=90)
                Submit(session, cookies_string, video_urls)
            except RequestException:
                Print(f"[bold bright_yellow]   ──>[bold red] FAILED TO CONNECT TO THE SERVER!     ", end="\r")
                time.sleep(10.0)
                continue
            except KeyboardInterrupt:
                Print(f"                                    ", end="\r")
                time.sleep(2.0)
                continue
    else:
        Print(Panel("[bold red]Maaf, Sepertinya Tautan Video Tiktok Yang Anda Masukkan Salah. Silakan Coba Lagi!", style="bold bright_yellow", width=59, title="[bold bright_yellow]>> [Incorrect Link] <<"))
        sys.exit()

if __name__ == '__main__':
    try:
        os.system('git pull')
        Feature()
    except Exception as e:
        Print(Panel(f"[bold red]{str(e).title()}!", style="bold bright_yellow", width=59, title="[bold bright_yellow]>> [Error] <<"))
    except KeyboardInterrupt:
        sys.exit()