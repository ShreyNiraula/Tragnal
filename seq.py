import time
seq = {
    'p1': {
        't1': [1, 0, 0, 0, 20],
        't2': [0, 0, 1, 1, 90],
        't3': [0, 0, 1, 0, 20],
    },

    'p2': {
        't1': [0, 0, 1, 0, 70],
        't2': [0, 0, 1, 0, 70],
        't3': [1, 0, 0, 0, 70],
    },

    'p3': {
        't1': [1, 0, 0, 0, 60],
        't2': [1, 0, 0, 0, 40],
        't3': [1, 0, 1, 1, 60],
    }
}

phase = {}
phase_number = None

def rashikSide():
    init_time = int(round(time.time()))
    while True:
        global phase, phase_number
        tym = int(round(time.time())) - init_time

        if (tym < 20):
            # print('Phase 1\t' + str(phase) )
            print('u finally here at tym 20 zone')
            seq['p1']['t1'][4] = 20 - tym
            seq['p1']['t2'][4] = 90 - tym
            seq['p1']['t3'][4] = 20 - tym
            phase = seq['p1']
            phase_number = 1

        elif (tym >= 20 and tym < 90):
            # print('Phase 2\t' + str(phase))
            seq['p2']['t1'][4] = 70 - (tym - 20)
            seq['p2']['t2'][4] = 70 - (tym - 20)
            seq['p2']['t3'][4] = 70 - (tym - 20)
            phase = seq['p2']
            phase_number = 2

        elif (tym >= 90 and tym < 130):
            # print('Phase 3\t' + str(phase))
            seq['p3']['t1'][4] = 60 - (tym - 90)
            seq['p3']['t2'][4] = 40 - (tym - 90)
            seq['p3']['t3'][4] = 60 - (tym - 90)
            phase = seq['p3']
            phase_number = 3

        elif (tym >= 130):
            init_time = int(round(time.time()))

        time.sleep(0.25)




