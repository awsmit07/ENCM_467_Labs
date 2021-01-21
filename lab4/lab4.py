#!/usr/bin/env python3

from matplotlib import pyplot as plt
import numpy as np

plt.rcdefaults()
plt.figure(dpi=300)
plt.rc('text', usetex=True)
plt.rc('font', family='serif')


def read_data(path, n_cols):
    cols = [np.array([])] * n_cols
    with open(path) as _file:
        _file.readline()
        for line in _file:
            if line == '\n':
                continue
            tmp = line.split('\t')
            for i, col in enumerate(cols):
                cols[i] = np.append(col, np.float(float(tmp[i])))
    return cols


def find_points(data):
    v_in = data[0]
    v_out = data[1]
    dv_out= np.diff(v_out)/(v_in[1] - v_in[0])

    min_dif = np.abs(v_in - v_out)
    index = np.where(np.isclose(min_dif, np.min(min_dif)))
    v_inv = index
    v_ol = v_out[-1]
    v_oh = v_out[0]
    v_il = 0
    v_ih = -1
    set_ih = False

    for i, dv in enumerate(dv_out):
        if not set_ih and dv >= -1:
            v_il = i
        elif not set_ih:
            set_ih = True
        if dv <= -1 and set_ih:
            v_ih = i
    v_il += 1
    v_ih += 1
    print('Vinv: ', v_out[v_inv])
    print('Vol:', v_ol)
    print('Voh', v_oh)
    print('Vil', v_in[v_il])
    print('Vih', v_in[v_ih])
    print('NML', v_in[v_il] - v_ol)
    print('NMH', v_oh - v_in[v_ih])
    return v_inv, v_il, v_ih

# Graph Timing Diagram
data = read_data('./data/timings.txt', 8)
headings = ['', '$A_1$', '$A_0$', '$B_1$', '$B_0$', '$C_O$', '$Q_1$', '$Q_0$']
time = data[0]/1E-3
for i in range(1, 8):
    plt.plot(time, data[i] + (35 - 5*i - 1*i), f'C{i}', label=headings[i])

plt.legend(bbox_to_anchor=(1.01 , 0.6), loc='upper left', borderaxespad=0.2)
plt.ylabel('Logic Levels')
plt.yticks([10.5], '')
plt.xlabel('time (ms)')
plt.xticks([i/10 for i in range(0, 81, 5)],
           [str(i/10) if i % 20 == 0 else '' for i in range(0, 81, 5)])
plt.grid()
plt.title('Timing Diagram of the 2 bit full adder')
plt.savefig('./figures/timing.png', bbox_inches='tight')
plt.close()



plt.rcdefaults()
plt.figure(dpi=300)
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
# Graph propagation delay
time = data[0]/1E-6
plt.plot(time[377:544], data[3][377:544], label='$B_1$')
plt.plot(time[377:544], data[6][377:544], label='$Q_1$')
plt.xlabel('time ($\mu$s)')
plt.ylabel('Voltage (V)')
plt.grid()
plt.xlim([1990, 2010])
plt.legend(bbox_to_anchor=(1.01 , 0.6), loc='upper left', borderaxespad=0.2)
plt.title('Transition of $Q_1$ due to a change in $B_1$')
plt.savefig('./figures/delays.png', bbox_inches='tight')
plt.close()

