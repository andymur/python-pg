#!/usr/bin/python3


if __name__ == "__main__":
    diap = 15
    res = []
    for a in range(1, diap + 1):
        for b in range(1, diap + 1):
            kl = a**3 + b**3
            #print("a: {0}, b: {1}, kl: {2}".format(a, b, kl))
            for c in range(1, diap + 1):
                dcube = (kl - c**3)
                if dcube > 0:
                    d = round(dcube**(1./3.))
                else:
                    continue
                kr = c**3+d**3
                if a != b and a != c and a != d and b != c and b != d and c != d and kl == kr:
                    res.append((a,b,c,d,kl,kr))
    print(res)
