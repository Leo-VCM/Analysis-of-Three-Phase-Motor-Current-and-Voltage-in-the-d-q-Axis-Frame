import numpy as np
import matplotlib.pyplot as plt

# 生成角度數據
theta_fine = np.linspace(0, 2 * np.pi, 1000)  

# 生成三相電流和電壓
I_a_fine = 5 * np.cos(theta_fine)                
I_b_fine = 5 * np.cos(theta_fine - 2*np.pi/3)     
I_c_fine = 5 * np.cos(theta_fine + 2*np.pi/3)     

V_a_fine = 12 * np.cos(theta_fine)               
V_b_fine = 12 * np.cos(theta_fine - 2*np.pi/3)    
V_c_fine = 12 * np.cos(theta_fine + 2*np.pi/3)    

# d-q 軸變換
I_d_fine = (2/3) * (I_a_fine * np.cos(0) + I_b_fine * np.cos(2*np.pi/3) + I_c_fine * np.cos(-2*np.pi/3))
I_q_fine = (2/3) * (-I_a_fine * np.sin(0) - I_b_fine * np.sin(2*np.pi/3) - I_c_fine * np.sin(-2*np.pi/3))

V_d_fine = (2/3) * (V_a_fine * np.cos(0) + V_b_fine * np.cos(2*np.pi/3) + V_c_fine * np.cos(-2*np.pi/3))
V_q_fine = (2/3) * (-V_a_fine * np.sin(0) - V_b_fine * np.sin(2*np.pi/3) - V_c_fine * np.sin(-2*np.pi/3))

# 繪製三相電流波形
plt.figure(figsize=(10, 6))
plt.plot(theta_fine, I_a_fine, label="I_a (A)")
plt.plot(theta_fine, I_b_fine, label="I_b (A)")
plt.plot(theta_fine, I_c_fine, label="I_c (A)")
plt.xlabel("Theta (radians)")
plt.ylabel("Current (A)")
plt.title("Three-Phase Currents")
plt.legend()
plt.grid()

# 繪製 d-q 軸電流波形
plt.figure(figsize=(10, 6))
plt.plot(theta_fine, I_d_fine, label="I_d (A)", linestyle="--")
plt.plot(theta_fine, I_q_fine, label="I_q (A)", linestyle="--")
plt.xlabel("Theta (radians)")
plt.ylabel("Current (A)")
plt.title("D-Q Axis Currents")
plt.legend()
plt.grid()

# 繪製三相電壓波形
plt.figure(figsize=(10, 6))
plt.plot(theta_fine, V_a_fine, label="V_a (V)")
plt.plot(theta_fine, V_b_fine, label="V_b (V)")
plt.plot(theta_fine, V_c_fine, label="V_c (V)")
plt.xlabel("Theta (radians)")
plt.ylabel("Voltage (V)")
plt.title("Three-Phase Voltages")
plt.legend()
plt.grid()

# 繪製 d-q 軸電壓波形
plt.figure(figsize=(10, 6))
plt.plot(theta_fine, V_d_fine, label="V_d (V)", linestyle="--")
plt.plot(theta_fine, V_q_fine, label="V_q (V)", linestyle="--")
plt.xlabel("Theta (radians)")
plt.ylabel("Voltage (V)")
plt.title("D-Q Axis Voltages")
plt.legend()
plt.grid()

plt.show()
