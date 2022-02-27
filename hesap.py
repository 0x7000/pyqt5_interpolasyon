from scipy.interpolate import interp1d


def intp(arg: str, x: list, y: list, q: float):
    x1 = []
    y1 = []
    for xx in x:
        x1. append(int(xx))
    for yy in y:
        y1.append(int(yy))
    try:
        if len(x1) != len(y1):
            raise Exception("Diziler eşit değil.")
        else:
            if arg == "x":
                inp = interp1d(x1, y1, fill_value="extrapolate", kind="linear")
            else:
                inp = interp1d(y1, x1, fill_value="extrapolate", kind="linear")
            sonuc = inp(q)
            return sonuc
    except Exception as e:
        return str(e)
