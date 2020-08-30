import numpy as np
import datetime
import time

def getqData(Week, hrTime):
    #defines time in hour
    t = np.array([8, 10, 12, 14, 16, 18, 20])
    #collected data(flow of each road) for a week
    qData = {

        'Sunday' : {
            #qx = [qx at 08,qx at 10,qx at 12,qx at 14,qx at 16,qx at 18,qx at 20]
            'q0' : np.array([700, 700, 700, 700, 700, 700, 700]),
            'q1' : np.array([300, 300, 300, 300, 300, 300, 300,]),
            'q2' : np.array([700, 700, 700, 700, 700, 700, 700]),
            'q3' : np.array([200, 200, 200, 200, 200, 200, 200]),
            'q4' : np.array([200, 200, 200, 200, 200, 200, 200]),
            'q5' : np.array([100, 100, 100, 100, 100, 100, 100]),
        },

        'Monday' : {
            #qx = [qx at 08,qx at 10,qx at 12,qx at 14,qx at 16,qx at 18,qx at 20]
            'q0' : np.array([700, 700, 700, 700, 700, 700, 700]),
            'q1' : np.array([300, 300, 300, 300, 300, 300, 300,]),
            'q2' : np.array([700, 700, 700, 700, 700, 700, 700]),
            'q3' : np.array([200, 200, 200, 200, 200, 200, 200]),
            'q4' : np.array([200, 200, 200, 200, 200, 200, 200]),
            'q5' : np.array([100, 100, 100, 100, 100, 100, 100]),
        },

        'Tuesday' : {
            #qx = [qx at 08,qx at 10,qx at 12,qx at 14,qx at 16,qx at 18,qx at 20]
            'q0' : np.array([700, 700, 700, 700, 700, 700, 700]),
            'q1' : np.array([300, 300, 300, 300, 300, 300, 300,]),
            'q2' : np.array([700, 700, 700, 700, 700, 700, 700]),
            'q3' : np.array([200, 200, 200, 200, 200, 200, 200]),
            'q4' : np.array([200, 200, 200, 200, 200, 200, 200]),
            'q5' : np.array([100, 100, 100, 100, 100, 100, 100]),
        },

        'Wednesday' : {
            #qx = [qx at 08,qx at 10,qx at 12,qx at 14,qx at 16,qx at 18,qx at 20]
            'q0' : np.array([700, 700, 700, 700, 700, 700, 700]),
            'q1' : np.array([300, 300, 300, 300, 300, 300, 300,]),
            'q2' : np.array([700, 700, 700, 700, 700, 700, 700]),
            'q3' : np.array([200, 200, 200, 200, 200, 200, 200]),
            'q4' : np.array([200, 200, 200, 200, 200, 200, 200]),
            'q5' : np.array([100, 100, 100, 100, 100, 100, 100]),
        },

        'Thursday' : {
            #qx = [qx at 08,qx at 10,qx at 12,qx at 14,qx at 16,qx at 18,qx at 20]
            'q0' : np.array([700, 700, 700, 700, 700, 700, 700]),
            'q1' : np.array([300, 300, 300, 300, 300, 300, 300,]),
            'q2' : np.array([700, 700, 700, 700, 700, 700, 700]),
            'q3' : np.array([200, 200, 200, 200, 200, 200, 200]),
            'q4' : np.array([200, 200, 200, 200, 200, 200, 200]),
            'q5' : np.array([100, 100, 100, 100, 100, 100, 100]),
        },

        'Friday' : {
            #qx = [qx at 08,qx at 10,qx at 12,qx at 14,qx at 16,qx at 18,qx at 20]
            'q0' : np.array([700, 700, 700, 700, 700, 700, 700]),
            'q1' : np.array([300, 300, 300, 300, 300, 300, 300,]),
            'q2' : np.array([700, 700, 700, 700, 700, 700, 700]),
            'q3' : np.array([200, 200, 200, 200, 200, 200, 200]),
            'q4' : np.array([200, 200, 200, 200, 200, 200, 200]),
            'q5' : np.array([100, 100, 100, 100, 100, 100, 100]),
        },

        'Saturday' : {
            #qx = [qx at 08,qx at 10,qx at 12,qx at 14,qx at 16,qx at 18,qx at 20]
            'q0' : np.array([700, 700, 700, 700, 700, 700, 700]),
            'q1' : np.array([300, 300, 300, 300, 300, 300, 300,]),
            'q2' : np.array([700, 700, 700, 700, 700, 700, 700]),
            'q3' : np.array([200, 200, 200, 200, 200, 200, 200]),
            'q4' : np.array([200, 200, 200, 200, 200, 200, 200]),
            'q5' : np.array([100, 100, 100, 100, 100, 100, 100]),
        }
    }

    #initilize an array to hold return values
    q = np.array([])
    for i in range(6):
        tmpStr = 'q' + str(i)
        q = np.append(q, np.interp(hrTime, t, qData[Week][tmpStr]))

    return q

def getPhaseTime(Weekday, timeHour):

    #number of phase
    p = 3

    #How long is all redtime
    allRedTime = 6

    #traffic flow
    # q = np.array([700,300,700,200,200,100])
    q = getqData(str(Weekday), int(timeHour))
    print(q)

    # #saturation headway
    # h = np.array([1.9,1.8,1.6,1.8,2.0,1.5])

    # yellowTime = tReaction + (V_85)/(2*a + 19.5*g)
    yellowTime = np.array([3, 3, 3])



    #calculation of saturation flow(s)  = 1/h
    # s = 3600/h
    #override with standard value of s for given width of the lane
    s = np.array([2250, 2250, 2250, 2250, 1850, 1850])
    # s = np.array([2250, 2250, 2250, 2250, 2250, 2250])

    #saturated flow/volume
    sPhase = np.array([[s[2],s[3],s[5]],[s[0],s[1],s[2]],[s[1],s[4],s[5]]])
    #s = [[phase1], [phase2], [phase3]]

    #flow ratio (q/s)
    y  = q/s
    yPhase = np.array([[y[2],y[3],y[5]],[y[0],y[1],y[2]],[y[1],y[4],y[5]]])

    #All lost Time(L)
    #L = yellowTime*p + allRedTime
    L = np.sum(yellowTime) + allRedTime


    #critical flow(cfY)
    cfY = np.array([np.max(yPhase[0]), np.max(yPhase[1]), np.max(yPhase[2])])


    # Optimum cycle time(C) = (1.5L + 5)/(1 - sum(y))
    C = (1.5*L + 5)/(1 - np.sum(cfY))

    greenTime = ((C - L)/np.sum(cfY))*cfY

    # print(C)
    # print(greenTime)
    # print(yellowTime)
    # print(C - greenTime-yellowTime - 6)

    #create a dictnary to return for the function
    cycle = {
        'greenTime': np.around(greenTime).astype(int),
        'yellowTime': np.around(yellowTime).astype(int),
        'redTime': (np.around(C) - np.around(greenTime) - np.around(yellowTime) - np.around(allRedTime)).astype(int),
        'allRedTime': int(round(allRedTime)),
        'cycleTime': int(round(C))
    }

    return cycle

def getCycle():
     x = datetime.datetime.now()
     cycle = getPhaseTime(x.strftime("%A"), (x.strftime("%H")))
     return cycle

def getTrafficLight(cycle, tym):
    tym = int(tym)
    ##it converts the phase time to traffic time

    #effective phase time = greenTime + yellowTime
    phaseTime = cycle['greenTime'] + cycle['yellowTime']

    #find which phase is the system right now using tym or is it in allredtime
    if tym >= 0 and tym <= phaseTime[0]:
        #system is iin index 0 or phase 1
        #hence update which phase
        phaseNum = 1

        #for traffic light 1 (red)
        t1 = [1,0,0,0, int(phaseTime[0] - tym)] #RYGStime

        #for traffic 2 (green&Side or side)
        if tym < cycle['greenTime'][0]:
            #t2 must be green & side
            t2 = [0,0,1,1, int(cycle['greenTime'][0] - tym)] #RYGStime
        else:
            ### t2 is Side and not yellow
            t2 = [0,0,0,1, int(phaseTime[0] + phaseTime[1] - tym)]

        #for traffic 3 (green or yellow)
        if tym < cycle['greenTime'][0]:
            #t3 must be green
            t3 = [0,0,0,1, int(phaseTime[0] - tym)] #RYGStime
        else:
            #t3 is yellow
            t3 = [0,1,0,0, int(phaseTime[0] - tym)]

    elif tym > phaseTime[0] and tym <= (phaseTime[0] + phaseTime[1]):
        #system is iin index 1 or phase 2
        #hence update which phase
        phaseNum = 2

        #for traffic light 1 (green&side or side)
        if tym < (phaseTime[0] + cycle['greenTime'][1]):
            #t1 is green&Side
            t1 = [0,0,1,1, int(phaseTime[0] + cycle['greenTime'][1] - tym)] #RYGStime
        else:
            #t1 is side
            t1 = [0,0,0,1, int(phaseTime[0] + phaseTime[1] + phaseTime[2] - tym)]

        #for traffic 2 (Side or yellow)
        if tym < (phaseTime[0] + cycle['greenTime'][1]):
            #t2 is Side
            t2 = [0,0,0,1, int(phaseTime[0] + phaseTime[1] - tym)] #RYGStime
        else:
            #t2 is yellow
            t2 = [0,1,0,0, int(phaseTime[0] + phaseTime[1] - tym)]

        #for traffic 3 (red)
        t3 = [1,0,0,0, int(phaseTime[0] + phaseTime[1] - tym)]

    elif tym > (phaseTime[0] + phaseTime[1]) and tym <= (phaseTime[0] + phaseTime[1] + phaseTime[2]):
        #system is iin index 2 or phase 3
        #hence update which phase
        phaseNum = 3

        #for traffic light 1 (side or yellow)
        if tym < (phaseTime[0] + phaseTime[1] + cycle['greenTime'][2]):
            #t1 is Side
            t1 = [0,0,0,1, int(phaseTime[0] + phaseTime[1] + phaseTime[2] - tym)] #RYGStime
        else:
            #t1 is yellow
            t1 = [0,1,0,0,  int(phaseTime[0] + phaseTime[1] + phaseTime[2] - tym)]

        #for traffic 2 (red)
        t2 = [1,0,0,0,  int(phaseTime[0] + phaseTime[1] + phaseTime[2] - tym)]

        #for traffic 3 (greeen&side or yellow)
        if tym < (phaseTime[0] + phaseTime[1] + cycle['greenTime'][2]):
            #t3 is green&side
            t3 = [0,0,1,1,  int(phaseTime[0] + phaseTime[1] + phaseTime[2] - tym)] #RYGStime
        else:
            #t3 is yellow
            t3 = [0,1,0,0,  int(phaseTime[0] + phaseTime[1] + phaseTime[2] - tym)]

    else:
        #hence update which phase
        phaseNum = 0
        #system is in allRedtime
        t1 = [1,0,0,0, int(cycle['allRedTime'] + phaseTime[0] + phaseTime[1] + phaseTime[2] - tym)]
        t2 = [1,0,0,0, int(cycle['allRedTime'] + phaseTime[0] + phaseTime[1] + phaseTime[2] - tym)]
        t3 = [1,0,0,0, int(cycle['allRedTime'] + phaseTime[0] + phaseTime[1] + phaseTime[2] - tym)]

    #return a dict containing traffic signals
    signal = {  #RYGStime
        't1' : t1,
        't2' : t2,
        't3': t3
    }

    return signal, phaseNum


# #test getTrafficLight(cycle, tym)
# tC = getCycle()
# t = 0
# x = getTrafficLight(tC, t)
# print(x)

traffic_phase_state_K = 1
isPhaseRessetted_K = None

phase = {}
phase_number = None
def koteshworSeqGenerationFunction():
    global phase,phase_number, isPhaseRessetted_K, traffic_phase_state_K
    init_time = int(time.time())
    tym = 0

    #get all the phase values initially
    cycle = getCycle()

    while True:

        #update tym as time passes
        if( int(round(time.time())) - init_time >= 1):
            tym+=1
            init_time = int(round(time.time()))

        #get phaseTime
        phaseTime = cycle['greenTime'] + cycle['yellowTime']

        #next phase button is presses
        if(isPhaseRessetted_K):
            tym = 0
            init_time = int(round(time.time()))

            if(traffic_phase_state_K==1):
                tym = phaseTime[0]

            if(traffic_phase_state_K == 2):
                tym = phaseTime[0] + phaseTime[1]

            if (traffic_phase_state_K == 3):
                tym = 0

            isPhaseRessetted_K = False


        #get all the traffic signals of the traffic lights
        phase, phase_number = getTrafficLight(cycle, tym)

        # print(str(type(phase['t1'][4])))

        #take a nap
        time.sleep(0.2)
        #reset tym if tym>= C

        if tym >= cycle['cycleTime']:
            tym = 0
            #get all cycle again for new time(hour) and day of the week
            cycle = getCycle()


# if __name__ == "__main__":
#     koteshworSeqGenerationFunction()