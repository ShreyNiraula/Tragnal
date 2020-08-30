# Tragnal
Webapp to simulate the traffic synchronization (6th sem project)


## How to operate:
- first git clone 
- cd to tragnal

### Within tragnal
- pip install -r requirements.txt (pip3 install for linux)


## How to run flask app

### 1. For Linux
- cd to tragnal, if not
- open terminal and type below two commands:
``` export FLASK_APP=tragnal2.py ```
``` flask run ```


### Login
- flask asks to login
- for now just access by email=`sss@sss.com` and password=`sss` (already registered user)



## Features in Webapp

### Junctions
- shows the three junctions: Koteshwor, Jadibuti and Lokanthali
- Click on each to visit their respective page

### Home 
- simple short description of project

### Profile
- profile info of authenticated user 
- **currently not implemented**

### Developer Teams
- Short information of our team members with their photos

### Logput
- click to logout


## More on Junctions
### Features

#### Map and Counter
- in either of junctions:Koteshwor, Jadibuti, Lokanthali; you can view the map and counter
- counter functionality works when combined with the hardware that generates the sequence pattern.
- also works with generated sequence with threading functionality

#### LiveStream
- livestream feature is possible when flask app gets the frames from IPcamera
- (not visible when visiting site only)

#### Graphs
- graphs that show the **Traffic Volume Chart in a Day** and **Traffic Volume Chart during a week**



## Some Pictures




