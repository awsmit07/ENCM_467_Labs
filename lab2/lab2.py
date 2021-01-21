#!/usr/bin/env python3

from matplotlib import pyplot as plt
import numpy as np

plt.rcdefaults()
plt.figure(dpi=200)
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
    print(v_out[v_inv], v_ol, v_oh, v_in[v_il], v_in[v_ih])
    return v_inv, v_il, v_ih


# Graph for part 2a Saturation
data = read_data('data/part2a_sat.txt', 2)
plt.plot(data[0], data[1], label='$V_{out}$')
v_inv, v_il, v_ih = find_points(data)
plt.plot((0, 5), (0, 5), '--C1')
plt.plot(data[0][v_inv], data[1][v_inv], 'oC1', label='$V_{INV}$')
plt.plot((data[0][v_il] - 0.2, data[0][v_il] + 0.2),
         (data[1][v_il] + 0.2, data[1][v_il] - 0.2), '--C2')

plt.plot((data[0][v_ih] - 0.2, data[0][v_ih] + 0.2),
         (data[1][v_ih] + 0.2, data[1][v_ih] - 0.2), '--C2')
plt.plot((data[0][v_il], data[0][v_il]), (0, 5), '--C3', label='$V_{IL}$')
plt.plot((data[0][v_ih], data[0][v_ih]), (0, 5), '--C4', label='$V_{IH}$')
plt.plot((0, 5), (data[1][-1], data[1][-1]), '--C5', label='$V_{OL}$')
plt.plot((0, 5), (data[1][0], data[1][0]), '--C6', label='$V_{OH}$')

plt.title('Voltage transfer characteristics for Linearly Loaded\ninverter'
         ' in saturation')
plt.xlabel('$V_{in}$ (V)')
plt.ylabel('$V_{out}$ (V)')
plt.grid()
plt.legend(bbox_to_anchor=(1.01 , 0.6), loc='upper left', borderaxespad=0.2)
plt.savefig("./figures/part_2a_sat.png", bbox_inches='tight')
plt.close()


# Graph for part 2a Triode
data = read_data('data/part2a_tri.txt', 2)
plt.plot(data[0], data[1])
find_points(data)
plt.title('Voltage transfer characteristics for Linearly Loaded\ninverter'
         ' in triode')
plt.xlabel('$V_{in}$ (V)')
plt.ylabel('$V_{out}$ (V)')
plt.grid()
plt.savefig("./figures/part_2a_tri.png", bbox_inches='tight')
plt.close()


# Graph for part 2b CMOS inverter
data = read_data('data/part2b.txt', 2)
plt.plot(data[0], data[1], label='$V_{out}$')
v_inv, v_il, v_ih = find_points(data)
plt.plot((0, 5), (0, 5), '--C1')
plt.plot(data[0][v_inv], data[1][v_inv], 'oC1', label='$V_{INV}$')
plt.plot((data[0][v_il] - 0.5, data[0][v_il] + 0.5),
         (data[1][v_il] + 0.5, data[1][v_il] - 0.5), '--C2')

plt.plot((data[0][v_ih] - 0.5, data[0][v_ih] + 0.5),
         (data[1][v_ih] + 0.5, data[1][v_ih] - 0.5), '--C2')
plt.plot((data[0][v_il], data[0][v_il]), (0, 5), '--C3', label='$V_{IL}$')
plt.plot((data[0][v_ih], data[0][v_ih]), (0, 5), '--C4', label='$V_{IH}$')
plt.plot((0, 5), (data[1][-1], data[1][-1]), '--C5', label='$V_{OL}$')
plt.plot((0, 5), (data[1][0], data[1][0]), '--C6', label='$V_{OH}$')

plt.title('Voltage transfer characteristics for a CMOS inverter.')
plt.xlabel('$V_{in}$ (V)')
plt.ylabel('$V_{out}$ (V)')
plt.grid()
plt.legend(bbox_to_anchor=(1.01 , 0.6), loc='upper left', borderaxespad=0.2)
plt.savefig("./figures/part_2b.png", bbox_inches='tight')
plt.close()


# Graph for part 3a
data = read_data('data/part3a.txt', 3)
plt.plot(data[0][:460], data[1][:460], label='$v_{in}$')
plt.plot(data[0][:460], data[2][:460], label='$v_{out}$')
plt.title('Transient Response for a resistively loaded inverter.')
plt.plot((10.5E-3, 10.5E-3+0.695822E-3), (2.5, 2.5), '--o', label='$t_{PHL}$')
plt.plot((0.0106056, 0.0128063), (4.5, 4.5), '--o', label='$t_{rise}$')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.grid()
plt.legend(bbox_to_anchor=(1.01 , 0.6), loc='upper left', borderaxespad=0.2)
plt.savefig("./figures/part_3a.png", bbox_inches='tight')
plt.close()


# Graph for part 3b
data = read_data('data/part3b.txt', 3)
plt.plot(data[0][:300], data[1][:300], label='$v_{in}$')
plt.plot(data[0][:300], data[2][:300], label='$v_{out}$')
plt.title('Transient Response for a CMOS inverter.')
plt.legend(bbox_to_anchor=(1.01 , 0.6), loc='upper left', borderaxespad=0.2)
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.grid()
plt.savefig("./figures/part_3b.png", bbox_inches='tight')
plt.close()


