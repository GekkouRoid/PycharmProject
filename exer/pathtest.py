from pathlib import Path

p = Path()

for file in p.glob('*.*'):
    print(file)
    if str(file) == 'youare.png':
        print('True')
        break

