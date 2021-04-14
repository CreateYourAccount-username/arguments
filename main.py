# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# Part 1: Greet Template


def greet(name, template='Hello, <name>!'):
    template = template.replace('<name>', name)
    return template


# Part 2: Force


def force(mass, body='earth'):
    # define dict with gravity values per body, rounded to 1 decimal
    gravity_dict = {'sun': 274.0,
                    'jupiter': 25.0,
                    'neptune': 11.2,
                    'saturn': 10.4,
                    'earth': 9.8,
                    'uranus': 8.9,
                    'venus': 8.9,
                    'mars': 3.7,
                    'mercury': 3.7,
                    'moon': 1.6,
                    'pluto': 0.6}
    # formula: force = mass * gravity
    gravity = gravity_dict[body]  # lookup gravity value from dictionary
    force = mass * gravity
    return force


# Part 3: Gravity


def pull(m1, m2, d):
    # do calculation
    G = 6.674 * 10 ** -11  # Gravitational constant
    pull = G * (m1 * m2 / d ** 2)
    # return result
    return pull
