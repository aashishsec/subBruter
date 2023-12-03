import requests,colorama,random,argparse,concurrent.futures

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

def banner():



    print(f'''{bold}{random_color}


░██████╗██╗░░░██╗██████╗░██████╗░██████╗░██╗░░░██╗████████╗███████╗███████╗░█████╗░██████╗░░█████╗░███████╗██████╗░
██╔════╝██║░░░██║██╔══██╗██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
╚█████╗░██║░░░██║██████╦╝██████╦╝██████╔╝██║░░░██║░░░██║░░░█████╗░░█████╗░░██║░░██║██████╔╝██║░░╚═╝█████╗░░██████╔╝
░╚═══██╗██║░░░██║██╔══██╗██╔══██╗██╔══██╗██║░░░██║░░░██║░░░██╔══╝░░██╔══╝░░██║░░██║██╔══██╗██║░░██╗██╔══╝░░██╔══██╗
██████╔╝╚██████╔╝██████╦╝██████╦╝██║░░██║╚██████╔╝░░░██║░░░███████╗██║░░░░░╚█████╔╝██║░░██║╚█████╔╝███████╗██║░░██║
╚═════╝░░╚═════╝░╚═════╝░╚═════╝░╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░╚════╝░╚══════╝╚═╝░░╚═╝
      
        Author   : Aashish💕💕  
                                              
        Github   : https://github.com/aashish36
                    
      ''')
    print("-" * 80)

    print(f"{bold}{random_color}subBruteForcer starting at {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

    print("-" * 80)

    print(f"{bold}{random_color}[*] URL".ljust(20, " "), ":", Domain)

    print(f"{bold}{random_color}[*] Wordlist".ljust(20, " "), ":",wordlist)

    print(f"{bold}{random_color}[*] Threads".ljust(20, " "), ":", threads)

    print("-" * 80)


parser=argparse.ArgumentParser(description=f"{bold}{random_color} subBruteForcer is a tool designed to efficiently probe for alive subdomains from a provided wordlist list.")

parser.add_argument('-d','--Domain',metavar='list',type=str,required=True,help=f"[{bold}{random_color}INFO]: {bold}{random_color}domain.")

parser.add_argument('-w','--wordlist',metavar='list',type=str,required=True,help=f"[{bold}{random_color}INFO]: {bold}{random_color}List of wordlist.")

parser.add_argument('-o','--output',metavar='output',type=str,default="subBruteForcer.txt",required=False,help=f"[{bold}{random_color}INFO]: {bold}{random_color}File to save our output.")

parser.add_argument("-t", "--threads", help=f"[{bold}INFO{random_color}]: {random_color}{random_color}Threading level to make fast process.", type=int, default=100)

args=parser.parse_args()

Domain=args.Domain

output=args.output

threads=args.threads

wordlist=args.wordlist

global_output=[]


def subBrute(domain,word):

    global global_output

    try:

            if domain[0:5]=="https" or domain[0:7]=="http://":
                        
                  url=f"{word}.{domain}"

            else:
              
                  url="https://{}.{}".format(word,domain)

            request=requests.get(url,timeout=10)

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

                global_output.append(f"(Status: {statusCode}) --[Size: {len(request.content)}]---> {[path]}\n")
                
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

    word=[]
    
    try:
        with open(wordlist,"r") as p:
       
           paths=p.read().splitlines()
        
           for p in paths:
          
               word.append(p)

        threading(Domain,word)

        saveOutput(output) 
           
    except KeyboardInterrupt as e:
        
        print(f"[{blue}INFO{random_color}]: dirbrute says exit!")
        
        exit()

    except Exception as e:
        
        pass 

if __name__ == "__main__":

    main(wordlist)