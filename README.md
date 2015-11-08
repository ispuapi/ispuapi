# ispuapi

ISPUAPI (ISPU+API)
Appliaction Programming Interface
for PM10 data retreival on current location in Indonesia.
it is defaultly retreive PM10 data for Pekanbaru.
data retreival for other locations is still under development
some functions still buggy or the data is not entirely valid except
for Pekanbaru.

# howto

how to using ispuapi

```
>> import ispuapi.ispuapi
>> pku = ispuapi.aqi('pku')
>> import matplotlib.pyplot as plt # modul plotting
>> plt.xlabel('Waktu')
>> plt.ylabel('Tingkat PM10')
>> plt.plot(pku)
>> plt.show()
```
![hasil plotting](/img/img.png)


# license

MIT

# author

Vicky Vernando Dasta
