import io
import sys


def count(layer, num):
    return len([x for x in layer if x == num])


def sol1(data):
    size = 25 * 6
    layers = [data[i * size:i * size + size] for i in range(int(len(data) / size))]
    min_layer_idx, min_layer_zeros = 0, float('inf')
    for i, layer in enumerate(layers):
        layer_zeros = count(layer, 0)
        if layer_zeros < min_layer_zeros:
            min_layer_idx = i
            min_layer_zeros = layer_zeros

    min_layer_ones = count(layers[min_layer_idx], 1)
    min_layer_twos = count(layers[min_layer_idx], 2)
    return min_layer_ones * min_layer_twos


def sol2(data):
    w, h = 25, 6
    size = w * h
    layers = [data[i * size:i * size + size] for i in range(int(len(data) / size))]
    pixel_symbol = {0: ' ', 1: '*'}
    out = io.StringIO()
    for ih in range(h):
        for iw in range(w):
            pos = iw + ih * w
            pixel = next(
                l[pos]
                for l in layers
                if l[pos] in {0, 1})
            print(pixel_symbol[pixel], end='', file=out)
        print('', file=out)
    return out.getvalue()


def main():
    data = sys.stdin.readline().strip()
    data = list(map(int, data))
    print(sol1(data))
    print(sol2(data))


main()
