import math
import argparse

parser = argparse.ArgumentParser(description='welcome')
parser.add_argument('-a','--radius',type=int,help='num1')
parser.add_argument('-b', '--height',type=int, help='num2')
args = parser.parse_args()

def v_calc(radius, height):
    return (math.pi)*(radius**2)*(height)
if __name__ == "__main__":
    print(v_calc(args.radius,args.height))