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


# Part 21 NAND gate
data = read_data('./data/part_21_NAND.txt', 2)
find_points(data)
plt.plot(data[0], data[1])
plt.title('NAND Gate Voltage Transfer Curve')
plt.xlabel('$v_{in}$ (V)')
plt.ylabel('$v_{out}$ (V)')
plt.grid()
#plt.legend(bbox_to_anchor=(1.01 , 0.6), loc='upper left', borderaxespad=0.2)
plt.savefig("./figures/part_21_NAND.png", bbox_inches='tight')
plt.close()


# Part 21 NOR gate
data = read_data('./data/part_21_NOR.txt', 2)
find_points(data)
plt.title('NOR Gate Voltage Transfer Curve')
plt.xlabel('$v_{in}$ (V)')
plt.ylabel('$v_{out}$ (V)')
plt.grid()
plt.plot(data[0], data[1])
plt.savefig("./figures/part_21_NOR.png", bbox_inches="tight")
plt.close()


# Part 22 NAND Gate A in
data = read_data('./data/part_22_NAND_A.txt', 3)
plt.plot(data[0]/1E-6, data[1], label='$v_{in}$')
plt.plot(data[0]/1E-6, data[2], label='$v_{out}$')
plt.title('Dynamic NAND gate response with variable $A$ input')
plt.xlabel('$t$ ($\mu$s)')
plt.ylabel('Voltage (V)')
plt.grid()
plt.legend(bbox_to_anchor=(1.01, 0.6), loc='upper left', borderaxespad=0.2)
plt.savefig('./figures/part_22_NAND_A.png', bbox_inches='tight')
plt.close()


# Part 22 NAND Gate B in
data = read_data('./data/part_22_NAND_B.txt', 3)
plt.plot(data[0]/1E-6, data[1], label='$v_{in}$')
plt.plot(data[0]/1E-6, data[2], label='$v_{out}$')
plt.title('Dynamic NAND gate response with variable $B$ input')
plt.xlabel('$t$ ($\mu$s)')
plt.ylabel('Voltage (V)')
plt.grid()
plt.legend(bbox_to_anchor=(1.01, 0.6), loc='upper left', borderaxespad=0.2)
plt.savefig('./figures/part_22_NAND_B.png', bbox_inches='tight')
plt.close()


# Part 22 NAND Gate AB in
data = read_data('./data/part_22_NAND_AB.txt', 3)
plt.plot(data[0]/1E-6, data[1], label='$v_{in}$')
plt.plot(data[0]/1E-6, data[2], label='$v_{out}$')
plt.title('Dynamic NAND gate response with common input')
plt.xlabel('$t$ ($\mu$s)')
plt.ylabel('Voltage (V)')
plt.grid()
plt.legend(bbox_to_anchor=(1.01, 0.6), loc='upper left', borderaxespad=0.2)
plt.savefig('./figures/part_22_NAND_AB.png', bbox_inches='tight')
plt.close()


# Part 22 NOR Gate A in
data = read_data('./data/part_22_NOR_A.txt', 3)
plt.plot(data[0]/1E-6, data[1], label='$v_{in}$')
plt.plot(data[0]/1E-6, data[2], label='$v_{out}$')
plt.title('Dynamic NOR gate response with variable $A$ input')
plt.xlabel('$t$ ($\mu$s)')
plt.ylabel('Voltage (V)')
plt.grid()
plt.legend(bbox_to_anchor=(1.01, 0.6), loc='upper left', borderaxespad=0.2)
plt.savefig('./figures/part_22_NOR_A.png', bbox_inches='tight')
plt.close()


# Part 22 NOR Gate B in
data = read_data('./data/part_22_NOR_B.txt', 3)
plt.plot(data[0]/1E-6, data[1], label='$v_{in}$')
plt.plot(data[0]/1E-6, data[2], label='$v_{out}$')
plt.title('Dynamic NOR gate response with variable $B$ input')
plt.xlabel('$t$ ($\mu$s)')
plt.ylabel('Voltage (V)')
plt.grid()
plt.legend(bbox_to_anchor=(1.01, 0.6), loc='upper left', borderaxespad=0.2)
plt.savefig('./figures/part_22_NOR_B.png', bbox_inches='tight')
plt.close()


# Part 22 NOR Gate AB in
data = read_data('./data/part_22_NOR_AB.txt', 3)
plt.plot(data[0]/1E-6, data[1], label='$v_{in}$')
plt.plot(data[0]/1E-6, data[2], label='$v_{out}$')
plt.title('Dynamic NOR gate response with common input')
plt.xlabel('$t$ ($\mu$s)')
plt.ylabel('Voltage (V)')
plt.grid()
plt.legend(bbox_to_anchor=(1.01, 0.6), loc='upper left', borderaxespad=0.2)
plt.savefig('./figures/part_22_NOR_AB.png', bbox_inches='tight')
plt.close()


# Part 23
data = read_data('./data/part_23.txt', 6)
plt.plot(data[0]/1E-6 + 20, data[1], label='$v_{out}$')
plt.plot(data[0]/1E-6 + 20, data[2], label='$v_a$')
plt.plot(data[0]/1E-6 + 20, data[3], label='$v_b$')
plt.plot(data[0]/1E-6 + 20, data[4], label='$v_c$')
plt.plot(data[0]/1E-6 + 20, data[5], label='$v_d$')
plt.grid()
plt.title('CMOS Ring Oscillator Output Waveform')
plt.xlabel('$t$ ($\mu$s)')
plt.ylabel('Voltage (V)')
plt.legend(bbox_to_anchor=(1.01, 0.6), loc='upper left', borderaxespad=0.2)
plt.savefig('./figures/part_23.png', bbox_inches='tight')
plt.close()


plt.plot(data[0]/1E-6 + 20, data[1], label='$v_{out}$')
plt.plot(data[0]/1E-6 + 20, data[2], label='$v_a$')
plt.grid()
plt.title('CMOS Ring Oscillator Output Waveform')
plt.xlabel('$t$ ($\mu$s)')
plt.ylabel('Voltage (V)')
plt.legend(bbox_to_anchor=(1.01, 0.6), loc='upper left', borderaxespad=0.2)
plt.savefig('./figures/part_23_reduced.png', bbox_inches='tight')
plt.close()

