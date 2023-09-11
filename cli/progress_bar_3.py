import time
import progressbar


max_value = 200

widgets = [
    progressbar.Timer(format=' [elapsed time: %s]'),
    progressbar.Bar('*'),
    progressbar.Counter(format=' %d of '+str(max_value)),
    progressbar.ETA(format=' (Remaining: %s)'),
]

bar = progressbar.ProgressBar(maxval=max_value, widgets=widgets).start()

for i in range(max_value):
    time.sleep(0.1)
    bar.update(i)
