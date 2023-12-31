# subBruter - Active Subdomain Enumeration Tool

[Tool Link](https://github.com/aashishsec/subBruter/)

- subBruter is a Python-based tool designed to efficiently probe for alive subdomains using a provided wordlist.
  
- It utilizes multithreading to accelerate the brute-force process, making it faster and more efficient.
  
- The tool supports customizable options such as the target domain, wordlist, output file, and the number of threads.
  
-  Works in all platforms.

## Features

- Multithreading: Utilizes the concurrent.futures module to perform subdomain brute-forcing concurrently, enhancing speed.
  
- Customizable: Allows users to specify the target domain, wordlist, output file, and the number of threads via command line arguments.
  
- User-Agent Rotation: Randomly selects a user-agent from a predefined list to simulate different browsers.

## Installation

- Clone the repository to your local machine.
  
- Install the required dependencies using pip


```bash

git clone https://github.com/aashish36/subBruter.git

cd subBruter

pip install -r requirements.txt

```

## Usage

- The output contains status codes and content length.

- This python code will save the results of the analysis to a file named 'subBruteForcer.txt'.

- Run the script using the following command: 

``` bash

usage: subBruter.py [-h] -d list -w list [-o output] [-t THREADS]

subBruter is a tool designed to efficiently probe for alive subdomains from a provided wordlist.

options:
  -h, --help            show this help message and exit.
  -d list, --Domain list
                        [INFO]: Domain to brute force.
  -w list, --wordlist list
                        [INFO]: List of wordlist.
  -o output, --output output
                        [INFO]: File to save our output.
  -t THREADS, --threads THREADS
                        [INFO]: Threading level to make fast process.

```

## Tool 

![image](https://github.com/aashishsec/subBruter/assets/65489287/63118583-d112-45ee-82c5-5b7cfd837a69)


## Tool Output

``` bash


░██████╗██╗░░░██╗██████╗░██████╗░██████╗░██╗░░░██╗████████╗███████╗██████╗░
██╔════╝██║░░░██║██╔══██╗██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔════╝██╔══██╗
╚█████╗░██║░░░██║██████╦╝██████╦╝██████╔╝██║░░░██║░░░██║░░░█████╗░░██████╔╝
░╚═══██╗██║░░░██║██╔══██╗██╔══██╗██╔══██╗██║░░░██║░░░██║░░░██╔══╝░░██╔══██╗
██████╔╝╚██████╔╝██████╦╝██████╦╝██║░░██║╚██████╔╝░░░██║░░░███████╗██║░░██║
╚═════╝░░╚═════╝░╚═════╝░╚═════╝░╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
      
        Author   : Aashish💕💕  

        Github   : https://github.com/aashish36

      
--------------------------------------------------------------------------------
subBruteForcer starting at 05/12/2023 12:21:03
--------------------------------------------------------------------------------
[*] URL     : youtube.com
[*] Threads : 500
[*] Wordlist : subdomains.txt
[*] No.of Words : 100000
--------------------------------------------------------------------------------
(Status: 200) --[Size: 782223]---> https://www.youtube.com
(Status: 200) --[Size: 749932]---> https://m.youtube.com
(Status: 200) --[Size: 2015]---> https://music.youtube.com
(Status: 200) --[Size: 893087]---> https://fr.youtube.com
(Status: 200) --[Size: 889382]---> https://jp.youtube.com
(Status: 200) --[Size: 758703]---> https://it.youtube.com
(Status: 200) --[Size: 20681]---> https://research.youtube.com
(Status: 200) --[Size: 856183]---> https://mx.youtube.com
(Status: 200) --[Size: 824934]---> https://es.youtube.com
(Status: 200) --[Size: 849827]---> https://in.youtube.com
(Status: 200) --[Size: 907432]---> https://tw.youtube.com
(Status: 200) --[Size: 2001748]---> https://news.youtube.com
(Status: 200) --[Size: 777311]---> https://de.youtube.com
(Status: 200) --[Size: 869605]---> https://nl.youtube.com
(Status: 200) --[Size: 890197]---> https://br.youtube.com
(Status: 200) --[Size: 392887]---> https://ru.youtube.com
(Status: 200) --[Size: 851164]---> https://cz.youtube.com
(Status: 200) --[Size: 850716]---> https://no.youtube.com
(Status: 200) --[Size: 780929]---> https://pl.youtube.com
(Status: 200) --[Size: 786364]---> https://kr.youtube.com
(Status: 200) --[Size: 594421]---> https://cms.youtube.com
(Status: 200) --[Size: 889905]---> https://za.youtube.com
(Status: 200) --[Size: 116654]---> https://kids.youtube.com
(Status: 200) --[Size: 890067]---> https://nz.youtube.com
(Status: 200) --[Size: 847181]---> https://il.youtube.com
(Status: 200) --[Size: 902184]---> https://hu.youtube.com
(Status: 200) --[Size: 428429]---> https://se.youtube.com
(Status: 200) --[Size: 793155]---> https://ie.youtube.com
(Status: 200) --[Size: 778306]---> https://uk.youtube.com
(Status: 200) --[Size: 774764]---> https://au.youtube.com
(Status: 200) --[Size: 1596]---> https://parents.youtube.com
(Status: 200) --[Size: 282163]---> https://director.youtube.com
(Status: 200) --[Size: 6752078]---> https://vr.youtube.com
(Status: 200) --[Size: 498230]---> https://gaming.youtube.com
(Status: 200) --[Size: 22197]---> https://charts.youtube.com
(Status: 200) --[Size: 438785]---> https://shows.youtube.com
(Status: 200) --[Size: 58590]---> https://artists.youtube.com
(Status: 200) --[Size: 1596]---> https://families.youtube.com

```

## Contributing

- Contributions are welcome!
  
- If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.
  
![image](https://github.com/aashish36/JSScanner/assets/65489287/70f7e3a8-e95f-429b-9433-89087daad721)
