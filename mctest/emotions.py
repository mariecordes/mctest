def make_heart():
    print('   xx   xx   ')
    print(' xxxxx xxxxx ')
    print('xxxxxxxxxxxxx')
    print('  xxxxxxxxx  ')
    print('    xxxxx    ')
    print('      x      ')

def make_heart2(x):
    layer1 = '   xx   xx   '
    layer2 = ' xxxxx xxxxx '
    layer3 = 'xxxxxxxxxxxxx'
    layer4 = '  xxxxxxxxx  '
    layer5 = '    xxxxx    '
    layer6 = '      x      '

    layer_list = [layer1, layer2, layer3, layer4, layer5, layer6]

    return layer_list[x]
