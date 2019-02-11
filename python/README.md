In [29]: import random
In [30]: z = random.sample(range(0,100000), 100)

In [31]: a = [(z[i], i) for i in range(len(z))]

In [32]: %timeit a.sort(key=lambda service_name: service_name[0])
13.5 µs ± 72.3 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

In [34]: a = [(z[i], i) for i in range(len(z))]

In [35]: %timeit sorted(a)
23.4 µs ± 851 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)


Generating python files from proto:
protoc --proto_path=$PWD --python_out=$PWD/../python_proto $PWD/file_name.proto
