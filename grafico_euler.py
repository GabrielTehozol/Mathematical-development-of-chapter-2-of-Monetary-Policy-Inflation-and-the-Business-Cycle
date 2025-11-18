import numpy as np
import matplotlib.pyplot as plt

beta = 0.99
sigma = 2.0

gc = np.linspace(0.9, 1.1, 200)      # crecimiento del consumo
gz = np.linspace(0.95, 1.05, 200)    # crecimiento de Z
pi = np.linspace(0.0, 0.08, 200)     # inflación esperada

# Valores base para los otros componentes
gz_base = 1.0
pi_base = 0.02
gc_base = 1.0

# 1) Q_t vs g_c
Q_gc = beta * gc**(-sigma) * gz_base * 1/(1+pi_base)

plt.figure(figsize=(5,3.5))
plt.plot(gc, Q_gc, linewidth=2)
plt.xlabel(r"$\frac{C_{t+1}}{C_t}$")
plt.ylabel(r"$Q_t$")
plt.title(r"Efecto del consumo en $Q_t$")
plt.tight_layout()
plt.savefig("ecu8_Q_vs_gc.png", dpi=300)
plt.close()

# 2) Q_t vs g_z
Q_gz = beta * gc_base**(-sigma) * gz * 1/(1+pi_base)

plt.figure(figsize=(5,3.5))
plt.plot(gz, Q_gz, linewidth=2)
plt.xlabel(r"$\frac{Z_{t+1}}{Z_t}$")
plt.ylabel(r"$Q_t$")
plt.title(r"Efecto de preferencias en $Q_t$")
plt.tight_layout()
plt.savefig("ecu8_Q_vs_gz.png", dpi=300)
plt.close()

# 3) Q_t vs inflación esperada
Q_pi = beta * gc_base**(-sigma) * gz_base * 1/(1+pi)

plt.figure(figsize=(5,3.5))
plt.plot(pi, Q_pi, linewidth=2)
plt.xlabel(r"$\pi_{t+1}^e$")
plt.ylabel(r"$Q_t$")
plt.title(r"Efecto de la inflación en $Q_t$")
plt.tight_layout()
plt.savefig("ecu8_Q_vs_pi.png", dpi=300)
plt.close()

# ============================
# Parámetros base
# ============================
sigma = 1.0   # curvatura de utilidad del consumo
phi_base = 0.6  # phi "intermedio" para el primer gráfico

# Rango de empleo (en log): n_t
n = np.linspace(-0.3, 0.5, 200)


# ===================================================
# 1) Gráfico: salario real vs empleo (c_t fijo)
# ===================================================

c0 = 0.0  # log de consumo "normal"
wmp = sigma * c0 + phi_base * n   # w_t - p_t = sigma c_t + phi n_t

plt.figure(figsize=(6, 4))
plt.plot(n, wmp, linewidth=2)

# Ejes al estilo "económico"
plt.axhline(0, linewidth=0.8)
plt.axvline(0, linewidth=0.8)

plt.xlabel(r"$n_t \equiv \log N_t$")
plt.ylabel(r"$w_t - p_t \equiv \log\left(\frac{W_t}{P_t}\right)$")
plt.title("Oferta de trabajo competitiva (c$_t$ fijo)")

# Anotaciones didácticas
plt.text(0.05, sigma * c0 + phi_base * 0.05,
         r"Mayor empleo $n_t$",
         ha="left", va="bottom")
plt.text(-0.25, sigma * c0 + phi_base * (-0.25),
         r"Menor empleo $n_t$",
         ha="left", va="top")

plt.tight_layout()
plt.savefig("ls_n_vs_w.png", dpi=300)
plt.savefig("ls_n_vs_w.pdf")
plt.close()


# ===================================================
# 2) Gráfico: desplazamiento por cambios en c_t
# ===================================================

c_low = -0.1   # consumo bajo (log)
c_high = 0.1   # consumo alto (log)

wmp_low = sigma * c_low + phi_base * n
wmp_high = sigma * c_high + phi_base * n

plt.figure(figsize=(6, 4))
plt.plot(n, wmp_low, linestyle="--", linewidth=2, label=r"$c_t^{\text{bajo}}$")
plt.plot(n, wmp_high, linestyle="-", linewidth=2, label=r"$c_t^{\text{alto}}$")

plt.axhline(0, linewidth=0.8)
plt.axvline(0, linewidth=0.8)

plt.xlabel(r"$n_t \equiv \log N_t$")
plt.ylabel(r"$w_t - p_t$")
plt.title("Desplazamiento por mayor consumo $c_t$")

plt.legend()

# Flecha y texto para explicar el desplazamiento
y_mid = sigma * c_low + phi_base * 0.2
plt.annotate("Aumento de $c_t$\n(desplazamiento hacia arriba)",
             xy=(0.2, sigma * c_low + phi_base * 0.2),
             xytext=(0.25, y_mid + 0.1),
             arrowprops=dict(arrowstyle="->"),
             ha="left", va="center")

plt.tight_layout()
plt.savefig("ls_shift_c.png", dpi=300)
plt.savefig("ls_shift_c.pdf")
plt.close()


# ===================================================
# 3) Gráfico: distintas pendientes según phi
# ===================================================

phi_low = 0.3
phi_high = 1.2
c_ref = 0.0  # mismo consumo de referencia

wmp_phi_low = sigma * c_ref + phi_low * n
wmp_phi_high = sigma * c_ref + phi_high * n

plt.figure(figsize=(6, 4))
plt.plot(n, wmp_phi_low, linestyle="--", linewidth=2,
         label=r"$\phi$ baja (oferta elástica)")
plt.plot(n, wmp_phi_high, linestyle="-", linewidth=2,
         label=r"$\phi$ alta (oferta inelástica)")

plt.axhline(0, linewidth=0.8)
plt.axvline(0, linewidth=0.8)

plt.xlabel(r"$n_t \equiv \log N_t$")
plt.ylabel(r"$w_t - p_t$")
plt.title("Distintas pendientes de la oferta de trabajo según $\phi$")

plt.legend()

plt.tight_layout()
plt.savefig("ls_phi_pendiente.png", dpi=300)
plt.savefig("ls_phi_pendiente.pdf")
plt.close()