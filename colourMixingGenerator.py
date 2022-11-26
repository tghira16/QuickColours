import math
salmon = '#FA8072'
teal = '#008080'
aquamarine = '#7FFFD4'
pine = '#01796f'
maroon = '#c32148'
coral = '#FF7F50'
royal = '#4169E1'
silver = '#C0C0C0'
spring = '#89DA59'
stone = '#336B87'
seafoam = '#C4DFE6'
crimson = '#8D230F'
olive = '#8EBA43'



colours = [salmon, teal, aquamarine,pine, maroon,coral, royal,silver, spring, stone, seafoam, crimson, olive]

def vec2hex(x):
    h = "#"
    for i in x:
        if i > 255 or i < 0:
            print("Invalid: values must be positive and less than 256", i)
            return None
        elif i < 16:
            h += "0" + str(hex(int(round(i))))[-1:]
        else:
            h += str(hex(int((round(i)))))[-2:]
    return h


def hex2vec(h):
    h1, h2, h3, = int(h[1:3], 16), int(h[3:5], 16), int(h[5:], 16)
    return [h1, h2, h3]



def norm(x):
    t = 0
    for v in x:
        t += v ** 2
    return t ** (0.5)

def vec2normvec(x):
    n = norm(x)
    new = []
    for v in x:
        new.append(round(v/n,2))
    return new


def generate_html(hex):
    htmlcode = f'<tr>\n<td class="cbox" bgcolor="{hex}"> <td>'
    htmlcode += '<td class="cbox"> </td>\n'
    htmlcode += f'<td>{hex}</td>\n'
    vec = hex2vec(hex)
    nvec = vec2normvec(vec)
    htmlcode += f'<td>{vec}</td>\n'
    htmlcode += f'<td>{nvec}</td>\n'
    htmlcode += r'</tr>'
    return htmlcode



with open('gen_html_cols.txt', 'w') as f:
    for c in colours:
        f.write(generate_html(c))
