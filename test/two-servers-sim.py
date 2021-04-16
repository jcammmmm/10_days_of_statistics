from numpy.random import exponential as geo
from numpy.random import randint as ran
import sys

def main():
    print("???????????")
    print("?COMO USAR?")
    print("???????????")
    print("py two-servers-sim.py <u1> <u2> <numero_de_simulaciones>")
    print("py two-servers-sim.py 19 34 2_000_000")
    print()

    u1 = 5
    u2 = 9
    scenes = 20000
    if len(sys.argv) == 4:
        u1 = int(sys.argv[1])
        u2 = int(sys.argv[2])
        scenes = int(sys.argv[3])


    print("#########################################################################")
    print("#### PARAMETROS u1= {} y u2= {} fijos con escenas= {} constantes".format(u1, u2, scenes))
    print("#########################################################################")
    print()
    sim_ev_a(scenes, u1, u2)
    sim_ev_b(scenes, u1, u2)
    
"""
EVENTO A
A se encuentra aun en servicio cuando me paso a hacer fila para
ser atendido por s2

scenes: cantidad de situaciones que describe el problema --(A, B en s2
        haciendo fila, y M con s1 libre)
u1, u2: las tasas a las cuales atienden s1 y s2 respectivamente (beta), por
        ejemplo
        beta                     lambda
        3.0 personas por hora :: cada 1/3.0 horas se atiende a alguien 
        2.3 personas por hora :: cada 1/2.3 horas se atiende a alguien 
        1.8 personas por hora :: cada 1/1.8 horas se atiende a alguien 
"""
def sim_ev_a(scenes, u1, u2):
    ev_a_count = 0
    for _ in range(scenes):
        """
        A tiene que durar en s2 siendo atendido lo que me demoro haciendo fila,
        para podermelo encontrar.
        La exponencial de numpy tiene como parametro lambda = 1/beta = 1/u1
        """
        m_time = geo(1/u1) # mi tiempo en s1 (= de s1 a s2)
        a_time = geo(1/u2) # tiempo de A en s2
        if m_time < a_time:
            ev_a_count += 1
    
    print("EVENTO A:")
    print("A se encuentra aun en servicio cuando me paso a hacer fila para ser atendido por s2")
    print("escenas\t: {}".format(scenes))
    print("u1\t: {}".format(u1))
    print("u2\t: {}".format(u2))
    print("simulacion \t: {}".format(ev_a_count/scenes))
    print("teorico \t: {}".format(u1/(u1 + u2)))
    print(" * teorico = u1/(u1 + u2)")
    print()

        
"""
EVENTO B
B se encuentra aun en el sistema cuando me paso a hacer fila para
ser atendido por s2

scenes: cantidad de situaciones que describe el problema --(A, B en s2
        haciendo fila, y M con s1 libre)
u1, u2: las tasas a las cuales atienden s1 y s2 respectivamente (beta), por
        ejemplo
        beta                     lambda
        3.0 personas por hora :: cada 1/3.0 horas se atiende a alguien 
        2.3 personas por hora :: cada 1/2.3 horas se atiende a alguien 
        1.8 personas por hora :: cada 1/1.8 horas se atiende a alguien 
"""
def sim_ev_b(scenes, u1, u2):
    ev_b_count = 0
    for _ in range(scenes):
        """
        Para esta simulacion se tienen en cuenta los eventos en los que B ya no esta el sistema,
        cuando yo pase a hacer fila a s2.
        Esto sucede cuando A ha sido atendido y B ha sido atendido. De esta manera en la simulacion
        se cuentan aquellos casos en los que mi tiempo (m_time) es superior a los tiempos de A y B
        siendo atendidos (a_time y b_time respectivamente).
        """
        m_time = geo(1/u1) # mi tiempo en s1 (= de s1 a s2)
        a_time = geo(1/u2) # tiempo de A en s2 (atendido)
        b_time = geo(1/u2) # tiempo de B en s2 
        """
        A no esta en el sistema cuando yo llego
        y
        B no esta en el sistema cuando yo llego
        """
        if  m_time > a_time + b_time:
            ev_b_count += 1
    
    print("EVENTO B:")
    print("B se encuentra aun en el sistema cuando me paso a hacer fila para ser atendido por s2")
    print("escenas\t: {}".format(scenes))
    print("u1\t: {}".format(u1))
    print("u2\t: {}".format(u2))
    print("simulacion \t: {}".format(1 - ev_b_count/scenes))
    a = (1 - ((u2/(u1 + u2))**2))
    b = (u1/(u1 + u2))*(1 + (u2/(u1 + u2)))
    print("teorico \t: {}".format(a))
    print(" * teorico 1 - (u2/(u1 + u2)))**2")
    print()

if __name__ == "__main__":
    main()