import requests,colorama,random,argparse,concurrent.futures,httpx

from datetime import datetime

from colorama import Fore, Back, Style

colorama.init(autoreset=True)

green = Fore.GREEN

magenta = Fore.MAGENTA

cyan = Fore.CYAN

mixed = Fore.RED + Fore.BLUE

red = Fore.RED

blue = Fore.BLUE

yellow = Fore.YELLOW

white = Fore.WHITE

reset = Style.RESET_ALL

colors = [magenta,cyan,mixed,red,blue,yellow, white]

random_color = random.choice(colors)

bold = Style.BRIGHT

USER_AGENT  = [
        
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",

    "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",

    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",

    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",

    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",

    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/99.0.1150.36",

    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",

    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",

    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0",

     ]
     
random_user_agent = random.choice(USER_AGENT)

header={"User-Agent": random_user_agent}

def banner():

    print(f'''{bold}{random_color}


░██████╗██╗░░░██╗██████╗░██████╗░██████╗░██╗░░░██╗████████╗███████╗██████╗░
██╔════╝██║░░░██║██╔══██╗██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔════╝██╔══██╗
╚█████╗░██║░░░██║██████╦╝██████╦╝██████╔╝██║░░░██║░░░██║░░░█████╗░░██████╔╝
░╚═══██╗██║░░░██║██╔══██╗██╔══██╗██╔══██╗██║░░░██║░░░██║░░░██╔══╝░░██╔══██╗
██████╔╝╚██████╔╝██████╦╝██████╦╝██║░░██║╚██████╔╝░░░██║░░░███████╗██║░░██║
╚═════╝░░╚═════╝░╚═════╝░╚═════╝░╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
      
        Author   : Aashish💕💕  
                                              
        Github   : https://github.com/aashish36
                    
      ''')
    print("-" * 80)

    print(f"{bold}{random_color}subBruteForcer starting at {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

    print("-" * 80)

    print(f"{bold}{random_color}[*] URL".ljust(20, " "), ":", Domain)

    print(f"{bold}{random_color}[*] Threads".ljust(20, " "), ":", threads)

    print(f"{bold}{random_color}[*] Wordlist".ljust(20, " "), ":",wordlist)



parser=argparse.ArgumentParser(description=f"{bold}{random_color} subBruteForcer is a tool designed to efficiently probe for alive subdomains from a provided wordlist.")

parser.add_argument('-d','--Domain',metavar='list',type=str,required=True,help=f"[{bold}{random_color}INFO]: {bold}{random_color}Domain to brute force.")

parser.add_argument('-w','--wordlist',metavar='wordlist',help=f"[{bold}{random_color}INFO]: {bold}{random_color}List of wordlist.",default="subdomains.txt")

parser.add_argument('-o','--output',metavar='output',type=str,default="subBruteForcer.txt",required=False,help=f"[{bold}{random_color}INFO]: {bold}{random_color}File to save our output.")

parser.add_argument("-t", "--threads", help=f"[{bold}INFO{random_color}]: {random_color}{random_color}Threading level to make fast process.", type=int, default=500)

args=parser.parse_args()

Domain=args.Domain

output=args.output

threads=args.threads

wordlist=args.wordlist

global_output=[]

global_words=[]

def subBrute(domain,word):

    global global_output

    if domain[0:5]=="https" or domain[0:7]=="http://":
                        
            url=f"{word}.{domain}"

    else:
              
            url="https://{}.{}".format(word,domain)

    try:
            with httpx.Client(verify=False,timeout=10,follow_redirects=True,headers=header) as client:

                   request=client.get(url)

            statusCode=request.status_code

            content_length = request.headers.get('Content-Length')

            if statusCode== 200:

               if content_length is not None:
                   
                   print(f"{green}(Status: {statusCode}) --[Size: {content_length}]---> {url}")

                   global_output.append(f"(Status: {statusCode}) --[Size: {content_length}]---> {url}\n")

               else:
                   
                   print(f"{green}(Status: {statusCode}) --[Size: {len(request.content)}]---> {url}")

                   global_output.append(f"(Status: {statusCode}) --[Size: {len(request.content)}]---> {url}\n")

            elif statusCode==404 or statusCode==429:
                 
                 pass
            
            else:
               
                print(f"{random_color}(Status: {statusCode}) --[Size: {len(request.content)}]---> {url}")

                global_output.append(f"(Status: {statusCode}) --[Size: {len(request.content)}]---> {[url]}\n")
                
    except KeyboardInterrupt as e:
        
            print(f"[{blue}INFO{random_color}]: subBruteForcer says BYE!")
        
            exit()
                
    except Exception as e:
        
           pass

def saveOutput(output):

    with open(output, 'w') as file:
        
        file.writelines(global_output)


def threading(Domain,paths):
    
    try:

        with concurrent.futures.ThreadPoolExecutor(max_workers=threads*2) as executor:
            
           futures = [executor.submit(subBrute, Domain,path) for path in paths]
           
        concurrent.futures.wait(futures)
           
    except KeyboardInterrupt as e:
        
        print(f"[{bold}INFO{random_color}]: subBruteForcer says exit!")
        
        exit()

    except Exception as e:
        
        pass 


def main(wordlist):
        
    banner()

    global global_words

    try:
        
        with open(wordlist,"r") as p:
       
           paths=p.read().splitlines()
        
           for p in paths:
          
               global_words.append(p)

        print(f"{bold}{random_color}[*] No.of Words".ljust(20, " "), ":", len(global_words))

        print("-" * 80)

        threading(Domain,global_words)

        saveOutput(output)

           
    except KeyboardInterrupt as e:
        
        print(f"[{blue}INFO{random_color}]: dirbrute says exit!")
        
        exit()

    except Exception as e:
        
        pass 

if __name__ == "__main__":

    main(wordlist)
